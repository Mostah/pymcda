import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/../")
import csv
import datetime
import random
import time
from itertools import product
from pymcda.learning.lp_avfsort import LpAVFSort
from pymcda.types import CriterionValue, CriteriaValues
from pymcda.types import Alternatives, Criteria, PerformanceTable
from pymcda.types import AlternativesAssignments, Categories
from pymcda.generate import generate_alternatives
from pymcda.generate import generate_categories_profiles
from pymcda.generate import generate_random_profiles
from pymcda.generate import generate_random_criteria_weights
from pymcda.pt_sorted import SortedPerformanceTable
from pymcda.utils import compute_ca
from pymcda.uta import AVFSort
from test_utils import test_result, test_results

class dataset(object):

    def __init__(self, name):
        self.name = name

    def is_complete(self):
        for obj in self.__dict__:
            if obj is None:
                return False
        return True

def load_mcda_data(csvfile, obj, *field):
    csvfile.seek(0)
    csvreader = csv.reader(csvfile, delimiter = ";")
    try:
        obj = obj().from_csv(csvreader, *field)
    except:
        print("Cannot get %s" % obj())
        return None

    return obj

def load_data(filepath):
    try:
        csvfile = open(filepath, 'rb')
        csvreader = csv.reader(csvfile, delimiter = ";")
    except:
        print("Cannot open file '%s'" % filepath)
        return None

    data = dataset(os.path.basename(filepath))
    data.a = load_mcda_data(csvfile, Alternatives, "pt")
    data.c = load_mcda_data(csvfile, Criteria, "criterion")
    data.pt = load_mcda_data(csvfile, PerformanceTable, "pt",
                             ["c%d" % i
                              for i in range(1, len(data.c) + 1)])
    data.pt.round()
    data.aa = load_mcda_data(csvfile, AlternativesAssignments,
                             "pt", "assignment")
    data.cats = load_mcda_data(csvfile, Categories, "category",
                               None, "rank")

    if data.is_complete() is False:
        return None

    return data

def run_test(seed, data, pclearning, nseg):
    random.seed(seed)

    # Separate learning data and test data
    pt_learning, pt_test = data.pt.split(2, [pclearning, 100 - pclearning])
    aa_learning = data.aa.get_subset(pt_learning.keys())
    aa_test = data.aa.get_subset(pt_test.keys())

    worst = data.pt.get_worst(data.c)
    best = data.pt.get_best(data.c)

    # Run the linear program
    t1 = time.time()

    css = CriteriaValues([])
    for c in data.c:
        cs = CriterionValue(c.id, nseg)
        css.append(cs)

    lp = LpAVFSort(css, data.cats, worst, best)
    obj, cvs, cfs, catv = lp.solve(aa_learning, pt_learning)

    t_total = time.time() - t1

    model = AVFSort(c, cvs, cfs, catv)

    # CA learning set
    aa_learning2 = model.get_assignments(pt_learning)
    ca_learning = compute_ca(aa_learning, aa_learning2)

    # Compute CA of test setting
    if len(aa_test) > 0:
        aa_test2 = model.get_assignments(pt_test)
        ca_test = compute_ca(aa_test, aa_test2)
    else:
        ca_test = 0

    # Compute CA of whole set
    aa2 = model.get_assignments(data.pt)
    ca = compute_ca(data.aa, aa2)

    t = test_result("%s-%d-%d" % (data.name, seed, pclearning))
    t['seed'] = seed
    t['na'] = len(data.a)
    t['nc'] = len(data.c)
    t['ncat'] = len(data.cats)
    t['ns'] = nseg
    t['pclearning'] = pclearning
    t['na_learning'] = len(aa_learning)
    t['na_test'] = len(aa_test)
    t['obj'] = obj
    t['ca_learning'] = ca_learning
    t['ca_test'] = ca_test
    t['ca_all'] = ca
    t['t_total'] = t_total

    return t

def run_tests(nseeds, data, pclearning, nseg, filename):
    # Create the CSV writer
    f = open(filename, 'wb')
    writer = csv.writer(f)

    # Write the test options
    writer.writerow(['data', data.name])
    writer.writerow(['ns', nseg])
    writer.writerow(['pclearning', pclearning])

    # Create a test_results instance
    results = test_results()

    # Initialize the seeds
    seeds = range(nseeds)

    # Run the algorithm
    initialized = False
    for _nseg, _pclearning, seed in product(nseg, pclearning, seeds):
        t1 = time.time()
        t = run_test(seed, data, _pclearning, _nseg)
        t2 = time.time()

        if initialized is False:
            fields = ['seed', 'na', 'nc', 'ncat', 'ns', 'pclearning',
                      'na_learning', 'na_test', 'obj', 'ca_learning',
                      'ca_test', 'ca_all', 't_total']
            writer.writerow(fields)
            initialized = True

        t.tocsv(writer, fields)
        f.flush()
        print("%s (%5f seconds)" % (t, t2 - t1))

        results.append(t)

    # Perform a summary
    writer.writerow(['', ''])

    t = results.summary(['na', 'nc', 'ncat', 'ns', 'pclearning',
                         'na_learning', 'na_test'],
                        ['obj', 'ca_learning', 'ca_test', 'ca_all',
                         't_total'])
    t.tocsv(writer)

if __name__ == "__main__":
    from optparse import OptionParser
    from test_utils import read_single_integer, read_multiple_integer
    from test_utils import read_csv_filename

    parser = OptionParser(usage = "python %s [options]" % sys.argv[0])
    parser.add_option("-i", "--csvfile", action = "store", type="string",
                      dest = "csvfile",
                      help = "csv file with data")
    parser.add_option("-p", "--pclearning", action = "store", type="string",
                      dest = "pclearning",
                      help = "Percentage of data to use in learning set")
    parser.add_option("-k", "--ns", action = "store", type="string",
                      dest = "ns",
                      help = "number of segments")
    parser.add_option("-s", "--nseeds", action = "store", type="string",
                      dest = "nseeds",
                      help = "number of seeds")
    parser.add_option("-f", "--filename", action = "store", type="string",
                      dest = "filename",
                      help = "filename to save csv output")
    (options, args) = parser.parse_args()

    while not options.csvfile:
        options.csvfile = raw_input("CSV file containing data ? ")
    data = load_data(options.csvfile)
    if data is None:
        exit(1)

    options.pclearning = read_multiple_integer(options.pclearning,
                                               "Percentage of data to " \
                                               "use in the learning set")
    options.ns = read_multiple_integer(options.ns, "Number of function " \
                                       "segments")
    options.nseeds = read_single_integer(options.nseeds, "Number of seeds")

    dt = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    default_filename = "data/test_lp_avfsort-%s-%s.csv" \
                       % (data.name, dt)
    options.filename = read_csv_filename(options.filename, default_filename)

    run_tests(options.nseeds, data, options.pclearning, options.ns,
              options.filename)

    print("Results saved in '%s'" % options.filename)
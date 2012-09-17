from __future__ import division
import csv
import datetime
import sys
sys.path.insert(0, "..")
import time
import random
from itertools import product

from mcda.types import alternatives_affectations, performance_table
from mcda.electre_tri import electre_tri
from inference.meta_electre_tri_global2 import meta_electre_tri_global
from tools.utils import compute_ac
from tools.sorted import sorted_performance_table
from tools.generate_random import generate_random_alternatives
from tools.generate_random import generate_random_criteria
from tools.generate_random import generate_random_criteria_values
from tools.generate_random import generate_random_performance_table
from tools.generate_random import generate_random_categories
from tools.generate_random import generate_random_profiles
from tools.generate_random import generate_random_categories_profiles
from tools.utils import normalize_criteria_weights
from tools.utils import add_errors_in_affectations
from test_utils import test_result, test_results

def test_meta_electre_tri_global(seed, na, nc, ncat, na_gen, pcerrors,
                                 max_oloops, nmodels, max_loops):

    # Generate an ELECTRE TRI model and assignment examples
    a = generate_random_alternatives(na)
    c = generate_random_criteria(nc)
    cv = generate_random_criteria_values(c, seed)
    normalize_criteria_weights(cv)
    pt = generate_random_performance_table(a, c)

    cat = generate_random_categories(ncat)
    cps = generate_random_categories_profiles(cat)
    b = cps.get_ordered_profiles()
    bpt = generate_random_profiles(b, c)

    lbda = random.uniform(0.5, 1)

    model = electre_tri(c, cv, bpt, lbda, cps)
    aa = model.pessimist(pt)

    # Add errors in assignment examples
    aa_err = aa.copy()
    aa_erroned = add_errors_in_affectations(aa_err, cat.get_ids(),
                                            pcerrors)

    # Sort the performance table
    pt_sorted = sorted_performance_table(pt)

    t1 = time.time()

    # Initialize nmodels meta instances
    metas = []
    for i in range(nmodels):
        meta = meta_electre_tri_global(a, c, cps, pt, cat, aa_err)
        metas.append(meta)

    # Perform at max oloops on the set of metas
    ca_iter = [ 1 ] * (max_oloops + 1)
    nloops = 0
    for i in range(0, max_oloops):
        models_ca = {}
        for meta in metas:
            m, ca = meta.optimize(max_loops)
            models_ca[m] = ca

            if ca == 1:
                break

        models_ca = sorted(models_ca.iteritems(),
                           key = lambda (k,v): (v,k),
                           reverse = True)

        nloops += 1
        ca_best = models_ca[0][1]

        ca_iter.append(ca_best)

        if ca_best == 1:
            break

        for j in range(int(nmodels / 2), nmodels):
            metas[j] = meta_electre_tri_global(a, c, cps, pt, cat,
                                               aa_err)

    t_total = time.time() - t1

    model2 = models_ca[0][0]

    # Determine the number of erroned alternatives badly assigned
    aa2 = model2.pessimist(pt)

    ok_erroned = 0
    for alt in a:
        if aa(alt.id) == aa2(alt.id) and alt.id in aa_erroned:
            ok_erroned += 1

    total = len(a)
    ca_erroned = ok_erroned / total

    # Generate alternatives for the generalization
    a_gen = generate_random_alternatives(na_gen)
    pt_gen = generate_random_performance_table(a_gen, c)
    aa_gen = model.pessimist(pt_gen)
    aa_gen2 = model2.pessimist(pt_gen)
    ca_gen = compute_ac(aa_gen, aa_gen2)

    # Save all infos in test_result class
    t = test_result("%s-%d-%d-%d-%d-%g-%d" % (seed, na, nc, ncat, na_gen,
                    pcerrors, max_loops))

    # Input params
    t['seed'] = seed
    t['na'] = na
    t['nc'] = nc
    t['ncat'] = ncat
    t['na_gen'] = na_gen
    t['pcerrors'] = pcerrors
    t['max_loops'] = max_loops
    t['nmodels'] = nmodels
    t['max_oloops'] = max_oloops

    # Ouput params
    t['ca_best'] = ca_best
    t['ca_erroned'] = ca_erroned
    t['ca_gen'] = ca_gen
    t['nloops'] = nloops
    t['t_total'] = t_total

    t['ca_iter'] = ca_iter

    return t

def run_tests(na, nc, ncat, na_gen, pcerrors, nseeds, max_loops, nmodels,
              max_oloops, filename):
    # Create the CSV writer
    writer = csv.writer(open(filename, 'wb'))

    # Write the test options
    writer.writerow(['na', na])
    writer.writerow(['nc', nc])
    writer.writerow(['ncat', ncat])
    writer.writerow(['na_gen', na_gen])
    writer.writerow(['pcerrors', pcerrors])
    writer.writerow(['nseeds', nseeds])
    writer.writerow(['max_loops', max_loops])
    writer.writerow(['nmodels', nmodels])
    writer.writerow(['max_oloops', max_oloops])
    writer.writerow(['', ''])

    # Create a test_results instance
    results = test_results()

    # Initialize the seeds
    seeds = range(nseeds)

    # Run the algorithm
    initialized = False
    for _na, _nc, _ncat, _na_gen, _pcerrors, _max_oloops, _nmodels, \
        _max_loops, seed \
        in product(na, nc, ncat, na_gen, pcerrors, max_oloops, nmodels,
                   max_loops, seeds):

        t1 = time.time()
        t = test_meta_electre_tri_global(seed, _na, _nc, _ncat, _na_gen,
                                         _pcerrors, _max_oloops, _nmodels,
                                         _max_loops)
        t2 = time.time()

        if initialized is False:
            fields = ['seed', 'na', 'nc', 'ncat', 'na_gen', 'pcerrors',
                      'max_oloops', 'nmodels', 'max_loops', 'ca_best',
                      'ca_erroned', 'nloops', 't_total']
            writer.writerow(fields)
            initialized = True

        t.tocsv(writer, fields)
        print("%s (%5f seconds)" % (t, t2 - t1))

        results.append(t)

    # Perform a summary
    writer.writerow(['', ''])

    t = results.summary(['na', 'nc', 'ncat', 'na_gen', 'pcerrors',
                         'max_oloops', 'nmodels', 'max_loops'],
                         ['ca_best', 'ca_erroned', 'nloops', 't_total'])
    t.tocsv(writer)

    # Summary by columns
    writer.writerow(['', ''])

    t = results.summary_columns(['na', 'nc', 'ncat', 'na_gen', 'pcerrors',
                                 'max_oloops', 'nmodels', 'max_loops'],
                                ['ca_iter'], 'seed')
    t.tocsv(writer)

if __name__ == "__main__":
    from optparse import OptionParser

    parser = OptionParser(usage = "python %s [options]" % sys.argv[0])
    parser.add_option("-n", "--na", action = "store", type="string",
                      dest = "na",
                      help = "number of assignment examples")
    parser.add_option("-c", "--nc", action = "store", type="string",
                      dest = "nc",
                      help = "number of criteria")
    parser.add_option("-t", "--ncat", action = "store", type="string",
                      dest = "ncat",
                      help = "number of categories")
    parser.add_option("-g", "--na_gen", action = "store", type="string",
                      dest = "na_gen",
                      help = "number of generalization alternatives")
    parser.add_option("-e", "--errors", action = "store", type="string",
                      dest = "pcerrors",
                      help = "ratio of errors in the learning set")
    parser.add_option("-s", "--nseeds", action = "store", type="string",
                      dest = "nseeds",
                      help = "number of seeds")
    parser.add_option("-l", "--max-loops", action = "store", type="string",
                      dest = "max_loops",
                      help = "max number of loops for the metaheuristic " \
                             "used to find the profiles")
    parser.add_option("-m", "--nmodels", action = "store", type="string",
                      dest = "nmodels",
                      help = "Size of the population (of models)")
    parser.add_option("-o", "--max_oloops", action = "store", type="string",
                      dest = "max_oloops",
                      help = "Max number of loops of the whole "
                             "metaheuristic")
    parser.add_option("-f", "--filename", action = "store", type="string",
                      dest = "filename",
                      help = "filename to save csv output")

    (options, args) = parser.parse_args()

    while not options.na:
        options.na = raw_input("Number of assignment examples ? ")
    options.na = options.na.split(",")
    options.na = [ int(x) for x in options.na ]

    while not options.nc:
        options.nc = raw_input("Number of criteria ? ")
    options.nc = options.nc.split(",")
    options.nc = [ int(x) for x in options.nc ]

    while not options.ncat:
        options.ncat = raw_input("Number of categories ? ")
    options.ncat = options.ncat.split(",")
    options.ncat = [ int(x) for x in options.ncat ]

    while not options.na_gen:
        options.na_gen = raw_input("Number of generalization " \
                                   "alternatives ? ")
    options.na_gen = options.na_gen.split(",")
    options.na_gen = [ int(x) for x in options.na_gen ]

    while not options.pcerrors:
        options.pcerrors = raw_input("Ratio of errors ? ")
    options.pcerrors = options.pcerrors.split(",")
    options.pcerrors = [ float(x) for x in options.pcerrors ]

    while not options.max_loops:
        options.max_loops = raw_input("Max number of loops for profiles' " \
                                      "metaheuristic ? ")
    options.max_loops = options.max_loops.split(",")
    options.max_loops = [ int(x) for x in options.max_loops ]

    while not options.nmodels:
        options.nmodels = raw_input("Population size (models) ? ")
    options.nmodels = options.nmodels.split(",")
    options.nmodels = [ int(x) for x in options.nmodels ]

    while not options.max_oloops:
        options.max_oloops = raw_input("Max number of loops for the " \
                                       "whole metaheuristic ? ")
    options.max_oloops = options.max_oloops.split(",")
    options.max_oloops = [ int(x) for x in options.max_oloops ]

    while not options.nseeds:
        options.nseeds = raw_input("Number of seeds ? ")
    options.nseeds = int(options.nseeds)

    while not options.filename:
        dt = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        default_filename = "test_meta_electre_tri_global-%s.csv" % dt
        options.filename = raw_input("File to save CSV data [%s] ? " \
                                     % default_filename)
        if not options.filename:
            options.filename = default_filename

    if options.filename[-4:] != ".csv":
        options.filename += ".csv"

    run_tests(options.na, options.nc, options.ncat, options.na_gen,
              options.pcerrors, options.nseeds, options.max_loops,
              options.nmodels, options.max_oloops, options.filename)
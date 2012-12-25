from __future__ import division
import sys
sys.path.insert(0, "..")
from itertools import product
import math
import random

def get_wrong_assignments(aa, aa_learned):
    l = list()
    for a in aa:
        aid = a.alternative_id
        if aa(aid) != aa_learned(aid):
            l.append(aid)
    return l

def compute_fitness(aa, aa_learned):
    ok = total = 0
    for a in aa:
        aid = a.alternative_id
        if aa(aid) == aa_learned(aid):
            ok += 1
        total += 1
    return ok/total

class meta_electre_tri_profiles():

    def __init__(self, model, pt_sorted, cat, aa_ori):
        self.na = len(aa_ori)
        self.nc = len(model.criteria)
        self.model = model
        self.nprofiles = len(model.profiles)
        self.pt_sorted = pt_sorted
        self.aa_ori = aa_ori
        self.cat = self.categories_rank(cat)
        self.cat_ranked = self.rank_categories(cat)
        self.aa_by_cat = self.sort_alternative_by_category(aa_ori)
        self.b0 = pt_sorted.get_worst_ap()
        self.bp = pt_sorted.get_best_ap()
        self.build_concordance_table(aa, self.model.bpt)

    def categories_rank(self, cat):
        return { c.id: c.rank for c in cat }

    def rank_categories(self, cat):
        c_rank = { c.id: c.rank for c in cat }
        return sorted([ cat for (cat, rank) in c_rank.items() ])

    def sort_alternative_by_category(self, aa):
        aa_by_cat = {}
        for a in aa:
            aid = a.alternative_id
            cat = self.cat[a.category_id]
            if cat in aa_by_cat:
                aa_by_cat[cat].append(aid)
            else:
                aa_by_cat[cat] = [ aid ]
        return aa_by_cat

    def compute_above_histogram(self, aa, cid, profile, above,
                                cat_b, cat_a, ct, f):
        w = self.model.cv[cid].value
        lbda = self.model.lbda

        h_above = {}
        num = total = 0
        alts, perfs = self.pt_sorted.get_middle(cid,
                                                profile.performances[cid],
                                                above.performances[cid],
                                                True, False)

        for i, a in enumerate(alts):
            conc = ct[a]
            diff = conc - w
            if self.aa_ori(a) == cat_a:
                if aa(a) == cat_a and diff < lbda:
                        # --
                        total += 5
                elif aa(a) == cat_b and diff < lbda:
                        # -
                        total += 1
            elif self.aa_ori(a) == cat_b and aa(a) == cat_a:
                if diff >= lbda:
                    # +
                    num += 0.75
                    total += 1
                    h_above[perfs[i] + 0.00001] = num / total
                else:
                    # ++
                    num += 1
                    total += 1
                    h_above[perfs[i] + 0.00001] = num / total
            elif self.cat[self.aa_ori(a)] < self.cat[cat_b]:
                num += 0.5
                total += 1
                h_above[perfs[i] + 0.00001] = num / total
#                print self.cat[cat_a]

        return h_above

    def compute_below_histogram(self, aa, cid, profile, below,
                                cat_b, cat_a, ct, f):
        w = self.model.cv[cid].value
        lbda = self.model.lbda

        h_below = {}
        num = total = 0
        alts, perfs = self.pt_sorted.get_middle(cid,
                                                below.performances[cid],
                                                profile.performances[cid],
                                                False, True)
        alts.reverse()
        perfs.reverse()
        for i, a in enumerate(alts):
            conc = ct[a]
            diff = conc + w
            if self.aa_ori(a) == cat_a and aa(a) == cat_b:
                if diff >= lbda:
                    # ++
                    num += 1
                    total += 1
                    h_below[perfs[i] - 0.00001] = num / total
                else:
                    # +
                    num += 0.75
                    total += 1
                    h_below[perfs[i] - 0.00001] = num / total
            elif self.aa_ori(a) == cat_b:
                if aa(a) == cat_b and diff >= lbda:
                    # --
                    total += 5
                elif aa(a) == cat_a and diff >= lbda:
                    # -
                    total += 1
            elif self.cat[self.aa_ori(a)] > self.cat[cat_a]:
                num += 0.5
                total += 1
                h_below[perfs[i] - 0.00001] = num / total

        return h_below

    def histogram_get_max(self, h, current):
        key = None
        val = 0
        diff = 0
        for k, v in h.items():
            if v >= val:
                tmp = abs(current - k)
                if tmp >= diff:
                    key = k
                    val = v
                    diff = tmp
        return key

    def print_histo(self, h):
        val = h.keys()
        val.sort()
        for i in val:
            print i,':', h[i]

    def build_concordance_table(self, aa, profiles):
        self.ct = { profile.alternative_id: dict() for profile in profiles }
        for a, profile in product(aa, profiles):
            ap = self.pt_sorted[a.alternative_id]
            conc = self.model.concordance(ap, profile)
            self.ct[profile.alternative_id][a.alternative_id] = conc

    def update_concordance_table(self, profile, cid, old, new):
        if old > new:
            down = True
            w = self.model.cv[cid].value
        else:
            down = False
            w = -self.model.cv[cid].value

        alts, perfs = self.pt_sorted.get_middle(cid, old, new,
                                                False, down)

        for a in alts:
            self.ct[profile][a] += w

    def compute_histograms(self, aa, f, profile, below, above, cat_b, cat_a):
        criteria = self.model.criteria
        p_perfs = profile.performances

        moved = False
        max_val = 0

        cids = self.model.criteria.keys()
        random.shuffle(cids)

        for cid in cids:
            ct = self.ct[profile.alternative_id]

            h_below = self.compute_below_histogram(aa, cid, profile,
                                                   below, cat_b,
                                                   cat_a, ct, f)
            h_above = self.compute_above_histogram(aa, cid, profile,
                                                   above, cat_b,
                                                   cat_a, ct, f)
            h = h_below
            h.update(h_above)

            if not h:
                continue

#            self.print_histo(h)
            i = self.histogram_get_max(h, p_perfs[cid])
#            print 'move', cid, i, h[i]

            r = random.uniform(0, 1)

            if r <= h[i]:
                self.update_concordance_table(profile.alternative_id, cid,
                                              p_perfs[cid], i)
                p_perfs[cid] = i
                moved = True
            elif moved is False and h[i] > max_val:
                max_val = h[i]
                max_cid = cid
                max_move = i

        if moved is False and max_val > 0:
            p_perfs[max_cid] = max_move

    def get_below_and_above_profiles(self, i):
        profiles = self.model.profiles
        bpt = self.model.bpt

        if i == 0:
            below = self.b0
        else:
            below = bpt[profiles[i-1]]

        if i == self.nprofiles-1:
            above = self.bp
        else:
            above = bpt[profiles[i+1]]

        return below, above

    def optimize(self, aa, f):
        profiles = self.model.profiles
        for i, profile in enumerate(profiles):
            pperfs = self.model.bpt[profile]
            below, above = self.get_below_and_above_profiles(i)
            cat_b, cat_a = self.cat_ranked[i], self.cat_ranked[i+1]
            self.compute_histograms(aa, f, pperfs, below, above, cat_b, cat_a)

if __name__ == "__main__":
    from tools.generate_random import generate_random_alternatives
    from tools.generate_random import generate_random_criteria
    from tools.generate_random import generate_random_criteria_values
    from tools.generate_random import generate_random_performance_table
    from tools.generate_random import generate_random_categories
    from tools.generate_random import generate_random_profiles
    from tools.generate_random import generate_random_categories_profiles
    from tools.utils import normalize_criteria_weights
    from tools.utils import display_affectations_and_pt
    from tools.sorted import sorted_performance_table
    from mcda.electre_tri import electre_tri_bm
    from ui.graphic import display_electre_tri_models

    a = generate_random_alternatives(1000)

    c = generate_random_criteria(10)
    cv = generate_random_criteria_values(c, 1)
    normalize_criteria_weights(cv)
    pt = generate_random_performance_table(a, c)

    cat = generate_random_categories(3)
    cps = generate_random_categories_profiles(cat)
    b = cps.get_ordered_profiles()
    bpt = generate_random_profiles(b, c)

#    lbda = 0.75
    lbda = random.uniform(0.5, 1)

    model = electre_tri_bm(c, cv, bpt, lbda, cps)
    aa = model.pessimist(pt)

    print('Original model')
    print('==============')
    cids = c.keys()
    bpt.display(criterion_ids=cids)
    cv.display(criterion_ids=cids)
    print("lambda: %.7s" % lbda)

    bpt2 = generate_random_profiles(b, c, 0123)
    model2 = electre_tri_bm(c, cv, bpt2, lbda, cps)
    print('Original random profiles')
    print('========================')
    bpt2.display(criterion_ids=cids)

    pt_sorted = sorted_performance_table(pt)
    meta = meta_electre_tri_profiles(model2, pt_sorted, cat, aa)

    for i in range(1, 501):
        aa2 = model2.pessimist(pt)

        f = compute_fitness(aa, aa2)
        print('%d: fitness: %g' % (i, f))
        bpt2.display(criterion_ids=cids)
        if f == 1:
            break

        meta.optimize(aa2, f)

    print('Learned model')
    print('=============')
    print("Number of iterations: %d" % i)
    bpt2.display(criterion_ids=cids)
    cv.display(criterion_ids=cids)
    print("lambda: %.7s" % lbda)

    total = len(a)
    nok = 0
    anok = []
    for alt in a:
        if aa(alt.id) != aa2(alt.id):
            anok.append(alt)
            nok += 1

    print("Good affectations: %3g %%" % (float(total-nok)/total*100))
    print("Bad affectations : %3g %%" % (float(nok)/total*100))

    if len(anok) > 0:
        print("Alternatives wrongly assigned:")
        display_affectations_and_pt(anok, c, [aa, aa2], [pt])

#    display_electre_tri_models([model, model2], [pt, pt])
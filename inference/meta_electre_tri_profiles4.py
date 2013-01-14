from __future__ import division
import sys
sys.path.insert(0, "..")
from itertools import product
import math
import random
from mcda.types import alternative_assignment, alternatives_assignments

class meta_electre_tri_profiles4():

    def __init__(self, model, pt_sorted, aa_ori):
        self.na = len(aa_ori)
        self.nc = len(model.criteria)
        self.model = model
        self.nprofiles = len(model.profiles)
        self.pt_sorted = pt_sorted
        self.aa_ori = aa_ori
        self.cat = self.categories_rank(self.model.categories)
        self.cat_ranked = self.model.categories
        self.aa_by_cat = self.sort_alternative_by_category(aa_ori)
        self.b0 = pt_sorted.get_worst_ap()
        self.bp = pt_sorted.get_best_ap()
        self.build_concordance_table()
        self.build_assignments_table()

    def categories_rank(self, cat):
        return { cat: i + 1 for i, cat in enumerate(self.model.categories) }

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

    def compute_above_histogram(self, cid, profile, above,
                                cat_b, cat_a, ct):
        w = self.model.cv[cid].value
        lbda = self.model.lbda

        h_above = {}
        num = total = 0
        alts, perfs = self.pt_sorted.get_middle(cid,
                                                profile.performances[cid],
                                                above.performances[cid],
                                                True, True)

        for i, a in enumerate(alts):
            conc = ct[a]
            diff = conc - w
            if self.aa_ori(a) == cat_a:
                if self.aa(a) == cat_a and diff < lbda:
                        # --
                        total += 5
                elif self.aa(a) == cat_b:
                        # -
                        total += 1
            elif self.aa_ori(a) == cat_b and self.aa(a) == cat_a:
                if diff >= lbda:
                    # +
                    num += 0.5
                    total += 1
                    h_above[perfs[i] + 0.00001] = num / total
                else:
                    # ++
                    num += 2
                    total += 1
                    h_above[perfs[i] + 0.00001] = num / total
            elif self.aa_ori(a) != self.aa(a) and \
                 self.cat[self.aa_ori(a)] < self.cat[cat_a]:
                num += 0.1
                total += 1
                h_above[perfs[i] + 0.00001] = num / total

        return h_above

    def compute_below_histogram(self, cid, profile, below,
                                cat_b, cat_a, ct):
        w = self.model.cv[cid].value
        lbda = self.model.lbda

        h_below = {}
        num = total = 0
        alts, perfs = self.pt_sorted.get_middle(cid,
                                                below.performances[cid],
                                                profile.performances[cid],
                                                True, True)
        alts.reverse()
        perfs.reverse()
        for i, a in enumerate(alts):
            conc = ct[a]
            diff = conc + w
            if self.aa_ori(a) == cat_a and self.aa(a) == cat_b:
                if diff >= lbda:
                    # ++
                    num += 2
                    total += 1
                    h_below[perfs[i]] = num / total
                else:
                    # +
                    num += 0.5
                    total += 1
                    h_below[perfs[i]] = num / total
            elif self.aa_ori(a) == cat_b:
                if self.aa(a) == cat_b and diff >= lbda:
                    # --
                    total += 5
                elif self.aa(a) == cat_a:
                    # -
                    total += 1
            elif self.aa_ori(a) != self.aa(a) and \
                 self.cat[self.aa_ori(a)] > self.cat[cat_b]:
                num += 0.1
                total += 1
                h_below[perfs[i]] = num / total

        return h_below

    def histogram_choose(self, h, current):
        key = random.choice(h.keys())
        val = h[key]
        diff = abs(current - key)
        for k, v in h.items():
            if v >= val:
                tmp = abs(current - k)
                if tmp > diff:
                    key = k
                    val = v
                    diff = tmp
        return key

    def get_alternative_assignment(self, aid):
        for profile in reversed(self.model.profiles):
            if self.ct[profile][aid] >= self.model.lbda:
                return self.model.categories_profiles[profile].value.upper

        return self.model.categories_profiles[profile].value.lower

    def build_assignments_table(self):
        self.good = 0
        self.aa = alternatives_assignments()
        for aa in self.aa_ori.values():
            aid = aa.alternative_id
            cat = self.get_alternative_assignment(aid)
            self.aa.append(alternative_assignment(aid, cat))

            cat_ori = aa.category_id
            if cat == cat_ori:
                self.good += 1

    def build_concordance_table(self):
        self.ct = { bp.alternative_id: dict() for bp in self.model.bpt }
        for aid, bp in product(self.aa_ori.keys(), self.model.bpt):
            ap = self.pt_sorted[aid]
            conc = self.model.concordance(ap, bp)
            self.ct[bp.alternative_id][aid] = conc

    def rebuild_tables(self):
        self.build_concordance_table()
        self.build_assignments_table()

    def update_tables(self, profile, cid, old, new):
        if old > new:
            down, up = True, False
            w = self.model.cv[cid].value
        else:
            down, up = False, True
            w = -self.model.cv[cid].value

        alts, perfs = self.pt_sorted.get_middle(cid, old, new,
                                                up, down)

        for a in alts:
            self.ct[profile][a] += w
            old_cat = self.aa[a].category_id
            new_cat = self.get_alternative_assignment(a)
            ori_cat = self.aa_ori[a].category_id

            if old_cat == new_cat:
                continue
            elif old_cat == ori_cat:
                self.good -= 1
            elif new_cat == ori_cat:
                self.good += 1

            self.aa[a].category_id = new_cat

    def optimize_profile(self, profile, below, above, cat_b, cat_a):
        criteria = self.model.criteria
        p_perfs = profile.performances

        moved = False
        max_val = 0

        cids = self.model.criteria.keys()
        random.shuffle(cids)

        for cid in cids:
            ct = self.ct[profile.alternative_id]

            h_below = self.compute_below_histogram(cid, profile,
                                                   below, cat_b,
                                                   cat_a, ct)
            h_above = self.compute_above_histogram(cid, profile,
                                                   above, cat_b,
                                                   cat_a, ct)
            h = h_below
            h.update(h_above)

            if not h:
                continue

            i = self.histogram_choose(h, p_perfs[cid])

            r = random.uniform(0, 1)

            if r <= h[i]:
                self.update_tables(profile.alternative_id, cid,
                                   p_perfs[cid], i)
                p_perfs[cid] = i
                moved = True
            elif moved is False and h[i] > max_val:
                max_val = h[i]
                max_cid = cid
                max_move = i

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

    def optimize(self):
        profiles = self.model.profiles
        for i, profile in enumerate(profiles):
            pperfs = self.model.bpt[profile]
            below, above = self.get_below_and_above_profiles(i)
            cat_b, cat_a = self.cat_ranked[i], self.cat_ranked[i+1]
            self.optimize_profile(pperfs, below, above, cat_b, cat_a)

        return self.good / self.na

if __name__ == "__main__":
    from tools.generate_random import generate_random_electre_tri_bm_model
    from tools.generate_random import generate_random_alternatives
    from tools.generate_random import generate_random_performance_table
    from tools.generate_random import generate_random_profiles
    from tools.utils import normalize_criteria_weights
    from tools.utils import display_assignments_and_pt
    from tools.utils import get_number_of_possible_coallitions
    from tools.sorted import sorted_performance_table
    from mcda.electre_tri import electre_tri_bm
    from mcda.types import alternative_performances
    from mcda.types import performance_table
    from ui.graphic import display_electre_tri_models

    # Generate a random ELECTRE TRI BM model
    model = generate_random_electre_tri_bm_model(10, 4, 123)
    worst = alternative_performances("worst",
                                     {c.id: 0 for c in model.criteria})
    best = alternative_performances("best",
                                    {c.id: 1 for c in model.criteria})

    # Generate a set of alternatives
    a = generate_random_alternatives(1000)
    pt = generate_random_performance_table(a, model.criteria)
    aa = model.pessimist(pt)

    print('Original model')
    print('==============')
    cids = model.criteria.keys()
    model.bpt.display(criterion_ids=cids)
    model.cv.display(criterion_ids=cids)
    print("lambda: %.7s" % model.lbda)
    print("number of possible coallitions: %d" %
          get_number_of_possible_coallitions(model.cv, model.lbda))

    model2 = model.copy()
    model2.bpt = generate_random_profiles(model.profiles, model.criteria)
    print('Original random profiles')
    print('========================')
    model.bpt.display(criterion_ids = cids)

    pt_sorted = sorted_performance_table(pt)
    meta = meta_electre_tri_profiles4(model2, pt_sorted, aa)

    for i in range(1, 1001):
        f = meta.good / meta.na
        print('%d: fitness: %g' % (i, f))
        model2.bpt.display(criterion_ids=cids)
        if f == 1:
            break

        f = meta.optimize()

    print('Learned model')
    print('=============')
    print("Number of iterations: %d" % i)
    model.bpt.display(criterion_ids = cids)
    model.cv.display(criterion_ids = cids)
    print("lambda: %.7s" % model.lbda)

    total = len(a)
    nok = 0
    anok = []
    for alt in a:
        if aa(alt.id) != meta.aa(alt.id):
            anok.append(alt)
            nok += 1

    print("Good affectations: %3g %%" % (float(total-nok)/total*100))
    print("Bad affectations : %3g %%" % (float(nok)/total*100))

    if len(anok) > 0:
        print("Alternatives wrongly assigned:")
        display_assignments_and_pt(anok, model.criteria, [aa, meta.aa],
                                    [pt])

    aps = [ pt["%s" % aid] for aid in anok ]
    display_electre_tri_models([model, model2],
                               [worst, worst], [best, best])

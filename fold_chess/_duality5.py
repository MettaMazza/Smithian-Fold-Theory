"""Move/un-move duality (Rung 3 gate 2) for KQKRR: predecessors5 and the
non-capture successors must be exact inverses on sampled legal states."""
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fold_chess5 import NSTATES5, decode5, is_legal5, successors5
from fold_solve5 import predecessors5

SEED = 20260612
if __name__ == "__main__":
    target = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
    rng = random.Random(SEED)
    checked = fb = bb = 0
    ex = []
    while checked < target:
        idx = rng.randrange(NSTATES5)
        wk, wq, r1, r2, bk, stm = decode5(idx)
        if not is_legal5(wk, wq, r1, r2, bk, stm):
            continue
        checked += 1
        for s in successors5(idx):
            if isinstance(s, tuple):
                continue
            if idx not in predecessors5(s):
                fb += 1
                if len(ex) < 8:
                    ex.append(("FWD", idx, s))
        for p in predecessors5(idx):
            succ = [s for s in successors5(p) if not isinstance(s, tuple)]
            if idx not in succ:
                bb += 1
                if len(ex) < 8:
                    ex.append(("BWD", idx, p))
    print("DUALITY checked=%d forward_breaks=%d backward_breaks=%d" % (checked, fb, bb))
    for e in ex:
        print("  ", e)
    print("DUALITY %s" % ("PASS" if fb == 0 and bb == 0 else "FAIL"))

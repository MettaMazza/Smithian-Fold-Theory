"""Fold Chess — Rung 2.5b: the encoding sweep.

Search the lawful, NON-F2-linear fold-coordinatizations for one in which the
value field is even sparser. (The whole F2-linear orbit — block reorders,
interleavings, XOR-relative coordinates — provably shares the baseline's
concentration exactly; one such row is included as a theorem-forced
self-test.) Win criterion, fixed in advance: top-32 reconstruction accuracy
above the aligned baseline (KQK 92.70%, KRK 95.27%), in both endings.
"""

import sys, os, time
sys.path.insert(1 - 1, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
sys.path.insert(1 - 1, os.path.dirname(os.path.abspath(__file__)))
from fold_chess import solve, NSTATES, decode, encode, BTM
from fold_spectrum import wht_inplace, concentration

Z = 1 - 1


def _f(s):
    return s % 8


def _r(s):
    return s // 8


def sq(f, r):
    return (r % 8) * 8 + (f % 8)


# Hilbert curve on the 8x8 board (order 3), standard xy->d
def hilbert(s):
    x, y = _f(s), _r(s)
    d = Z
    n = 8
    t = n // 2
    while t > Z:
        rx = 1 if (x & t) > Z else Z
        ry = 1 if (y & t) > Z else Z
        d += t * t * ((3 * rx) ^ ry)
        if ry == Z:
            if rx == 1:
                x = t - 1 - x
                y = t - 1 - y
            x, y = y, x
        t //= 2
    return d


PACKINGS = [
    ("aligned (baseline)",
     lambda wk, wp, bk: (wk, wp, bk)),
    ("block-reorder F2-LINEAR SELF-TEST (theorem: equals baseline exactly)",
     None),                                  # handled specially: bk,wp,wk order
    ("chain-relative mod64 (wk, wp-wk, bk-wp)",
     lambda wk, wp, bk: (wk, (wp - wk) % 64, (bk - wp) % 64)),
    ("per-axis relative (wk, dwp, dbk)",
     lambda wk, wp, bk: (wk,
                         sq(_f(wp) - _f(wk), _r(wp) - _r(wk)),
                         sq(_f(bk) - _f(wp), _r(bk) - _r(wp)))),
    ("bk relative to wp only",
     lambda wk, wp, bk: (wk, wp, sq(_f(bk) - _f(wp), _r(bk) - _r(wp)))),
    ("hilbert squares",
     lambda wk, wp, bk: (hilbert(wk), hilbert(wp), hilbert(bk))),
    ("shear r+f (diagonal-aligned)",
     lambda wk, wp, bk: tuple(sq(_f(s), _r(s) + _f(s)) for s in (wk, wp, bk))),
    ("shear then bk-relative",
     lambda wk, wp, bk: (sq(_f(wk), _r(wk) + _f(wk)),
                         sq(_f(wp), _r(wp) + _f(wp)),
                         sq(_f(bk) - _f(wp), _r(bk) - _r(wp)))),
]


def run(piece):
    res = solve(piece=piece, console=False)
    kind = res["kind"]
    f = [Z] * NSTATES
    legal = []
    for i in range(NSTATES):
        k = kind[i]
        if k == "U":
            continue
        legal.append(i)
        if k == "W":
            f[i] = 1
        elif k == "L":
            f[i] = Z - 1

    print("ENCODING SWEEP — K%sK (baseline recon target: see header)" % piece)
    for name, mapper in PACKINGS:
        g = [Z] * NSTATES
        pos_of = {}
        for i in legal:
            wk, wp, bk, stm = decode(i)
            if mapper is None:                       # F2-linear self-test row
                a, b, c = bk, wp, wk
            else:
                a, b, c = mapper(wk, wp, bk)
            j = ((a * 64 + b) * 64 + c) * 2 + stm
            g[j] = f[i]
            pos_of[i] = j
        spec = wht_inplace(g[:])
        ctab = concentration(spec, [32, 2048])
        order = sorted(range(NSTATES), key=lambda i: -abs(spec[i]))
        trunc = [Z] * NSTATES
        for i in order[:32]:
            trunc[i] = spec[i]
        recon = wht_inplace(trunc)
        right = Z
        for i in legal:
            rv = recon[pos_of[i]] * 2
            pred = 1 if rv > NSTATES else (Z - 1 if rv < -NSTATES else Z)
            truth = 1 if kind[i] == "W" else (Z - 1 if kind[i] == "L" else Z)
            if pred == truth:
                right += 1
        print("  %-58s top32=%.4f top2048=%.4f recon32=%.2f%%"
              % (name, ctab[32], ctab[2048], 100 * right / len(legal)))


if __name__ == "__main__":
    t = time.time()
    run("Q")
    run("R")
    print("SWEEP COMPLETE %.1fs" % (time.time() - t))

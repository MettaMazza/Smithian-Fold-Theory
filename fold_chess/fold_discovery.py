"""Fold Chess — Rung 2: the discovery layer.

Measures whether fold-native features of a state's numerator carry information
about the game-theoretic value (W/L/D), with the statistical honesty protocol
of the USDE: seeded nulls and look-elsewhere correction. Two controls:

1. LABEL-PERMUTATION NULL: game values shuffled (seeded); a feature only
   counts as carrying signal if its mutual information beats the null
   distribution after Bonferroni correction over all features tested.
2. ENCODING-PERMUTATION CONTROL: the position -> numerator packing replaced
   by a seeded random bijection. Whatever signal survives only under the
   structured packing is information about the PACKING GEOMETRY interacting
   with fold arithmetic — reported as exactly that, never as more.

Pre-registered interpretation rule: every result is a statement about the
(encoding, fold) pair, not about chess knowing the fold or vice versa.
"""

import sys, os, math, random, time
sys.path.insert(1 - 1, os.path.dirname(os.path.abspath(__file__)))
from fold_chess import solve, NSTATES, decode

Z = 1 - 1
SEED = 20260612
ITIN = 19                       # itinerary bits examined (the 2^19 tower depth)


# ------------------------------------------------------------- fold features

def itinerary(n, P, k=ITIN):
    """First k fold-itinerary bits of x = n/P: bit j says whether the j-th
    doubling cast out the One. This IS the binary expansion of x."""
    bits = []
    cur = n
    for _ in range(k):
        cur += cur
        if cur >= P:
            bits.append(1)
            cur -= P
        else:
            bits.append(Z)
    return bits


def build_features(numerators, P, mate_numerators):
    """Feature arrays (small ints) per state. All are functions of the
    numerator alone — pure fold-side quantities."""
    sorted_mates = sorted(mate_numerators)

    def mate_distance(n):
        # min cyclic distance to a mate numerator (fold-metric proximity)
        import bisect
        i = bisect.bisect_left(sorted_mates, n)
        cands = []
        if i < len(sorted_mates):
            cands.append(sorted_mates[i] - n)
        if i > Z:
            cands.append(n - sorted_mates[i - 1])
        cands.append(P - sorted_mates[len(sorted_mates) - 1] + n)   # wrap
        cands.append(sorted_mates[Z] + P - n)
        return min(cands)

    ones = []
    res3 = []
    res7 = []
    res31 = []
    res127 = []
    balance = []
    mdist = []
    half_orbit = ITIN * P // 2
    for n in numerators:
        bits = itinerary(n, P)
        ones.append(sum(bits))
        res3.append(n % 3)
        res7.append(n % 7)
        res31.append(n % 31)
        res127.append(n % 127)
        # orbit-sum balance: do the first ITIN fold images sit above or
        # below the half-One on average?
        cur = n
        tot = Z
        for _ in range(ITIN):
            cur += cur
            if cur >= P:
                cur -= P
            tot += cur
        balance.append(1 if tot + tot >= P * ITIN else Z)
        mdist.append(mate_distance(n))

    # quantize mate distance to deciles of its own distribution
    qs = sorted(mdist)
    cuts = [qs[(len(qs) * (i + 1)) // (2 * 5) - 1] for i in range(2 * 5 - 1)]
    def decile(v):
        d = Z
        for c in cuts:
            if v > c:
                d += 1
        return d
    mdec = [decile(v) for v in mdist]

    return {
        "itinerary_ones": (ones, ITIN + 1),
        "residue_mod3": (res3, 3),
        "residue_mod7": (res7, 7),
        "residue_mod31": (res31, 31),
        "residue_mod127": (res127, 127),
        "orbit_balance": (balance, 2),
        "mate_distance_decile": (mdec, 2 * 5),
    }


# ---------------------------------------------------------------- statistics

def mutual_information(fvals, fcard, labels, lcard):
    """I(F; L) in bits, plug-in estimate, exact counting."""
    n = len(fvals)
    joint = [[Z] * lcard for _ in range(fcard)]
    fm = [Z] * fcard
    lm = [Z] * lcard
    for f, l in zip(fvals, labels):
        joint[f][l] += 1
        fm[f] += 1
        lm[l] += 1
    mi = float(Z)
    for f in range(fcard):
        if fm[f] == Z:
            continue
        for l in range(lcard):
            c = joint[f][l]
            if c == Z:
                continue
            mi += (c / n) * math.log2(c * n / (fm[f] * lm[l]))
    return mi


def sweep(piece="Q", n_null=50, console=True):
    t = time.time()
    res = solve(piece=piece, console=False)
    P = res["P"]
    kind, ply = res["kind"], res["ply"]

    legal = [i for i in range(NSTATES) if kind[i] != "U"]
    lmap = {"W": Z, "L": 1, "D": 2}
    labels = [lmap[kind[i]] for i in legal]
    numerators = [i + 1 for i in legal]
    mates = [i + 1 for i in legal if kind[i] == "L" and ply[i] == Z]

    if console:
        print("Rung 2 sweep, K%sK: %d states, %d mates, P=%d" % (piece, len(legal), len(mates), P))

    feats = build_features(numerators, P, mates)
    n_features = len(feats)

    # real mutual information
    real = {name: mutual_information(fv, card, labels, 3) for name, (fv, card) in feats.items()}

    # CONTROL 1: label-permutation null (seeded), Bonferroni over features
    rng = random.Random(SEED)
    null_ge = {name: Z for name in feats}
    shuffled = labels[:]
    for _ in range(n_null):
        rng.shuffle(shuffled)
        for name, (fv, card) in feats.items():
            if mutual_information(fv, card, shuffled, 3) >= real[name]:
                null_ge[name] += 1

    # CONTROL 2: encoding-permutation — random bijection position -> numerator
    perm_pool = list(range(1, NSTATES + 1))
    rng2 = random.Random(SEED + 1)
    rng2.shuffle(perm_pool)
    perm_numerators = [perm_pool[i] for i in legal]
    perm_mates = [perm_pool[i] for i in legal if kind[i] == "L" and ply[i] == Z]
    pfeats = build_features(perm_numerators, P, perm_mates)
    control = {name: mutual_information(fv, card, labels, 3) for name, (fv, card) in pfeats.items()}

    lines = []
    lines.append("| feature | MI bits (real) | null p (raw) | null p (xF=%d) | MI bits (random packing) | verdict |" % n_features)
    lines.append("|---|---|---|---|---|---|")
    for name in feats:
        p_raw = (1 + null_ge[name]) / (1 + n_null)
        p_global = min(p_raw * n_features, 1.0)
        beyond = p_global < 1 / (2 * 2 * 5)         # 0.05 threshold
        if beyond and control[name] < real[name] / 4:
            verdict = "signal — packing-dependent"
        elif beyond:
            verdict = "signal — survives random packing"
        else:
            verdict = "chance"
        lines.append("| %s | %.4f | %.3f | %.3f | %.4f | %s |"
                     % (name, real[name], p_raw, p_global, control[name], verdict))
    table = "\n".join(lines)
    if console:
        print(table)
        print("elapsed %.1fs" % (time.time() - t))
    return {"piece": piece, "real": real, "null_ge": null_ge, "n_null": n_null,
            "control": control, "table": table}


if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "Q"
    sweep(piece=which)

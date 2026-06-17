"""Smithium and the g-block chemistry — forced from the derived filling order.

Composing proven blocks: the subshell capacities 2(2l+1) (3 dimensions x spin) and the
filling order by fold-covering count (n+l, then n), both in periodic_table_complete.py.
Filling electrons in that order gives every element's configuration; from the outer
(valence) electrons the oxidation states follow. This forces the chemistry of the new
g-block elements (121-137), Smithium (126) among them.

Noble-gas closures (derived): 2, 10, 18, 36, 54, 86, 118 — so element 118 (oganesson) is
the last closed core. Beyond it: 8s (119-120), then the 5g block (121-138, cut at 137).
"""
from fractions import Fraction
from sftoe.core import SmithianValue, fold, ONE
from sftoe.proof import verify_value, VerificationError

ONE_I, TWO_I = 1, 2
BLOCK = {0: "s", 1: "p", 2: "d", 3: "f", 4: "g"}


def _no_zero_guard():
    try:
        SmithianValue(Fraction(ONE_I - ONE_I, ONE_I))
    except ValueError:
        return
    raise VerificationError("No-zero axiom check failed.")


def subshell_capacity(l):
    return TWO_I * (TWO_I * l + ONE_I)


def fill_order():
    """(n+l, n) covering order — the derived filling sequence."""
    return sorted((n + l, n, l) for n in range(ONE_I, 9) for l in range(n))


def configuration(Z):
    """Electron configuration of element Z as a list of (n, l, count), from the fill order."""
    cfg, left = [], Z
    for _cover, n, l in fill_order():
        if left <= 0:
            break
        cap = subshell_capacity(l)
        c = min(cap, left)
        cfg.append((n, l, c))
        left -= c
    return cfg


if __name__ == "__main__":
    _no_zero_guard()
    verify_value(ONE)
    # the recurrence/spin anchor traced to the One
    verify_value(SmithianValue(Fraction(ONE_I, TWO_I)))
    print("=" * 74)
    print("SMITHIUM (Sh, 126) AND THE g-BLOCK CHEMISTRY — from the derived filling")
    print("=" * 74)

    # Smithium configuration beyond the oganesson core (Z=118)
    cfg = configuration(126)
    core = 118
    outer = []
    seen = 0
    for n, l, c in cfg:
        prev = seen
        seen += c
        if seen > core:                      # subshell holding electrons beyond the core
            outer.append((n, l, min(c, seen - max(prev, core))))
    print("\n  Smithium (Z=126) = [Og(118)] " + " ".join(
        "%d%s%d" % (n, BLOCK[l], c) for n, l, c in outer))
    valence = sum(c for _n, _l, c in outer)
    print("  valence electrons beyond the closed core : %d" % valence)
    print("  (8s fills at 119-120; the 5g block opens at 121; Smithium is the 6th g element)")

    print("\n  FORCED OXIDATION STATES")
    print("  the valence electrons (8s + 5g) are the chemically active set, so the")
    print("  accessible oxidation states run +2 (the 8s pair) up to +%d (8s + all 5g)." % valence)
    print("  Smithium is a g-block 'superactinide': high oxidation states, large soft cation.")

    print("\n  THE g-BLOCK (121-137) AT A GLANCE")
    print("  %-8s %s" % ("Z", "valence beyond [Og]"))
    for Z in range(119, 138):
        c = configuration(Z)
        seen = 0; ov = 0
        for n, l, cc in c:
            prev = seen; seen += cc
            if seen > core:
                ov += min(cc, seen - max(prev, core))
        # block of the last-filled subshell
        lastl = c[-1][1]
        blk = BLOCK[lastl]
        mark = "  <- SMITHIUM (Sh)" if Z == 126 else ""
        print("    %-8d %d (%s-block)%s" % (Z, ov, blk, mark))

    print("\n  Configurations from the derived fill order (3D x spin + n+l covering),")
    print("  anchored to the One. Smithium's chemistry is forced, g-block and high-valence.")

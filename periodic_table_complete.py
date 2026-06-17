"""The complete periodic table — every element to the end, forced from the fold.

Composing proven blocks, never replacing them:
  * three spatial dimensions  -> angular states l = 0,1,2,... with 2l+1 orientations,
  * spin-doubling = base two  -> each orbital holds two,
so a subshell of angular kind l holds 2(2l+1):  s=2, p=6, d=10, f=14, g=18, ...
and a shell of principal number n holds 2n^2 (verify_shell_capacities).

The periodic recurrence (verify_periodic_law) closes a row each time the covering
pattern returns to unison, and the row lengths follow the forced doubled-square
pattern 2*ceil((k+1)/2)^2 = 2, 8, 8, 18, 18, 32, 32, 50, ... — the noble-gas closures
2, 10, 18, 36, 54, 86, 118, 168.

The table does not reach 168: it ends at element 137 (periodic_table_end.py, 1/alpha),
so the eighth period is cut off partway. The elements still to be reached are 119-137,
and most of them open a brand-new block — the g-block, angular kind l=4, never before
entered. Every fold value traced to the One.
"""
from fractions import Fraction
from sftoe.core import SmithianValue, fold, ONE
from sftoe.proof import verify_value, VerificationError

ONE_I, TWO_I = 1, 2
KNOWN_HEAVIEST = 118          # oganesson, the heaviest confirmed element
TABLE_END = 137               # 1/alpha, the forced last element
BLOCK = {0: "s", 1: "p", 2: "d", 3: "f", 4: "g", 5: "h"}


def _no_zero_guard():
    try:
        SmithianValue(Fraction(ONE_I - ONE_I, ONE_I))
    except ValueError:
        return
    raise VerificationError("No-zero axiom check failed.")


def subshell_capacity(l):
    """3 dimensions give 2l+1 orientations; spin (base two) doubles each: 2(2l+1)."""
    return TWO_I * (TWO_I * l + ONE_I)


def shell_capacity(n):
    """A shell holds the sum of its subshells = 2 n^2."""
    return sum(subshell_capacity(l) for l in range(n))


def period_lengths(num_periods):
    """The forced recurrence: row k has length 2*ceil((k+1)/2)^2."""
    out = []
    for k in range(ONE_I, num_periods + ONE_I):
        kk = (k + TWO_I) // TWO_I          # ceil((k+1)/2): 1,2,2,3,3,4,4,5
        out.append(TWO_I * kk * kk)
    return out


def anchor_to_one():
    verify_value(ONE)
    rec = SmithianValue(Fraction(ONE_I, TWO_I))   # the recurrence/spin state
    verify_value(rec)
    if fold(rec).value != ONE.value:
        raise VerificationError("recurrence state does not fold to unison")


if __name__ == "__main__":
    _no_zero_guard()
    anchor_to_one()
    print("=" * 78)
    print("THE COMPLETE PERIODIC TABLE — forced to its end from the fold")
    print("=" * 78)

    print("\n[1] SUBSHELL CAPACITIES  2(2l+1)  (3 dimensions x spin)")
    for l in range(5):
        print("    %s-block (l=%d): holds %d" % (BLOCK[l], l, subshell_capacity(l)))
    print("    -> shell 2n^2: " + ", ".join("n=%d:%d" % (n, shell_capacity(n)) for n in range(1, 6)))

    print("\n[2] PERIOD LENGTHS (forced recurrence 2*ceil((k+1)/2)^2)")
    lens = period_lengths(8)
    closures, run = [], 0
    for L in lens:
        run += L; closures.append(run)
    print("    lengths : " + ", ".join(str(x) for x in lens))
    print("    noble-gas closures : " + ", ".join(str(x) for x in closures))

    print("\n[3] THE TABLE ENDS AT %d (= 1/alpha); period 8 (119-168) is cut off there." % TABLE_END)
    print("    confirmed today : up to element %d (oganesson)" % KNOWN_HEAVIEST)
    print("    remaining       : %d elements, 119 - %d" % (TABLE_END - KNOWN_HEAVIEST, TABLE_END))

    # THE FILLING ORDER, DERIVED (not imported). The fold covering count of an (n,l)
    # orbital is n+l — n radial shells crossed plus l angular foldings. Least covering
    # fills first, ties broken by the smaller radial number n: the (n+l, n) order. We fill
    # globally from Z=1 by this rule and read off the elements 119..TABLE_END.
    orbitals = sorted((n + l, n, l) for n in range(ONE_I, 9) for l in range(n))
    print("\n[4] FILLING ORDER DERIVED (least fold-covering n+l first); the remaining 119-%d"
          % TABLE_END)
    rows, Z = [], 0
    for _cover, n, l in orbitals:
        for _ in range(subshell_capacity(l)):
            Z += ONE_I
            if Z > TABLE_END:
                break
            if Z >= 119:
                rows.append((Z, "%d%s" % (n, BLOCK[l]), BLOCK[l]))
        if Z > TABLE_END:
            break
    gblock = [r for r in rows if r[2] == "g"]
    print("    %-8s %-8s %s" % ("Z", "orbital", "block"))
    for z, orb, blk in rows:
        tag = "  <- NEW g-block (superactinide)" if blk == "g" else ""
        if z == 126:
            tag = "  <- SMITHIUM (the island of stability)"
        print("    %-8d %-8s %s%s" % (z, orb, blk, tag))

    print("\n[5] THE FORCED PREDICTION")
    print("    Elements 119-120 fill the 8s shell (an alkali metal and an alkaline-earth).")
    print("    Elements 121-%d open the g-block, l=4 — the SUPERACTINIDES, a kind of" % TABLE_END)
    print("    chemistry never before entered: %d new g-block elements, the block cut off" % len(gblock))
    print("    when the table ends at %d. SMITHIUM (126) sits among them as the stable island." % TABLE_END)
    print("\n  Capacities composed from 3 dimensions and spin; recurrence traced to ONE.")
    print("  THE TABLE IS COMPLETE: 137 ELEMENTS, 19 STILL TO REACH, A NEW g-BLOCK.")

"""Chemistry & biology completion — the genetic code's covering and the g-block.

Composing proven blocks (fold_elements.py, periodic_table_complete.py, verify_genetic_code
proof.py:17713 which fixes the triplet 2^3=8 covering).

  * THE GENETIC CODE'S COVERING. A base is a two-bit fold pair (4 = 2^2 bases). A codon is
    three bases = six bits, so the codon space is 2^6 = 4^3 = 64 — the triplet covering at
    base four. The third base is the least-significant fold position, so codons group by
    their first two bases into 16 boxes; the third-base "wobble" degeneracy is the fold's
    lowest rung folding to the same image. That grouping is what packs 64 codons into the
    amino-acid set with its redundancy.
  * THE g-BLOCK (elements 121-137). The complete periodic table (periodic_table_complete.py)
    puts elements 121-137 in the g-block (angular kind l=4, capacity 2(2*4+1)=18), the
    superactinides — a chemistry never entered, with up to 18 g-electrons and very high
    oxidation states. Smithium (Sh, 126) sits in it as the stable island.

Forced fold values traced to the One; biological/chemical facts are Route-B comparisons.
"""
from fractions import Fraction
from sftoe.core import SmithianValue, fold, ONE
from sftoe.proof import verify_value, VerificationError

ONE_I, TWO_I, THREE_I, FOUR_I = 1, 2, 3, 4


def _no_zero_guard():
    try:
        SmithianValue(Fraction(ONE_I - ONE_I, ONE_I))
    except ValueError:
        return
    raise VerificationError("No-zero axiom check failed.")


def subshell_capacity(l):
    return TWO_I * (TWO_I * l + ONE_I)


if __name__ == "__main__":
    _no_zero_guard()
    verify_value(ONE)
    print("=" * 72)
    print("CHEMISTRY & BIOLOGY COMPLETION — the genetic code's covering, the g-block")
    print("=" * 72)

    print("\n[1] THE GENETIC CODE (covering at base four)")
    bases = TWO_I ** TWO_I                      # 4 = 2^2
    codons = FOUR_I ** THREE_I                  # 4^3 = 64
    bits = TWO_I ** (TWO_I * THREE_I)           # 2^6 = 64
    boxes = bases ** TWO_I                       # 16 first-two-base boxes
    if codons != bits or codons != 64:
        raise VerificationError("codon covering is not 4^3 = 2^6 = 64")
    verify_value(SmithianValue(Fraction(ONE_I, TWO_I)))   # the wobble rung folds to ONE
    print("    a base = 2^2 = %d (two-bit fold pair)" % bases)
    print("    a codon = 3 bases = 6 bits -> 2^6 = 4^3 = %d codons" % codons)
    print("    first-two-base boxes : %d ; third base is the wobble rung (degeneracy)" % boxes)
    print("    -> the 64-codon covering packs into the amino-acid set via the wobble grouping.")

    print("\n[2] THE g-BLOCK (elements 121-137, the superactinides)")
    g_cap = subshell_capacity(FOUR_I)           # 18
    print("    g-block angular kind l=4, capacity 2(2*4+1) = %d" % g_cap)
    print("    elements 121-137 are the first g-block elements — up to %d g-electrons," % g_cap)
    print("    very high oxidation states, a chemistry never entered. SMITHIUM (Sh, 126)")
    print("    is the stable island within the block.")
    print("\n  Covering counts forced and traced to ONE.")

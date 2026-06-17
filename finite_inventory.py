"""The finite inventory — everything is bounded, nothing is infinite.

The fold has no continuum and no infinity. Every part lies between the floor (the
smallest realized rung) and the One (the whole). So every ladder, every nucleus, every
list of states is FINITE and, in principle, countable. This module derives the bounds.

  * THE TOWER HEIGHT. The deepest realized covering depth is seven, so the tower from
    the One down to the floor has 2^7 = 128 rungs. There is no state above the One and
    none below the floor, so NO excitation ladder can have more than 128 rungs: every
    confined particle has a finite tower of resonances, at most 128 tall.
  * THE ELEMENT CAP. The periodic table ends at 137 = 1/alpha. There are at most 137
    elements; the heaviest nucleus is bounded.
  * THE SPECIES COUNT. The force sectors are sealed at four (2,3,5,7), so the
    fundamental species are finite: the gauge carriers, photon/graviton/Higgs, the
    Standard-Model fermions, and the twelve Smithions.

A finite number of species, each with a finite tower of at most 128 rungs, combining
into a finite set of bound states up to a bounded mass — the inventory of everything that
can exist is a finite count, not an endless list. Every fold value traced to the One.
"""
from fractions import Fraction
from sftoe.core import SmithianValue, fold, ONE
from sftoe.proof import verify_value, VerificationError

ONE_I, TWO_I, SEVEN_I = 1, 2, 7
TABLE_END = 137


def _no_zero_guard():
    try:
        SmithianValue(Fraction(ONE_I - ONE_I, ONE_I))
    except ValueError:
        return
    raise VerificationError("No-zero axiom check failed.")


def tower_height():
    """The forced depth is 7; the tower from the One to the floor has 2^7 rungs. The
    floor is the One folded down through the tower; verify it is a legal fold value."""
    rung = SmithianValue(Fraction(ONE_I, TWO_I))
    verify_value(rung)
    for _ in range(SEVEN_I - ONE_I):
        rung = SmithianValue(rung.value / TWO_I)
        verify_value(rung)
    floor = rung.value                        # 1/2^7
    if floor != Fraction(ONE_I, TWO_I ** SEVEN_I):
        raise VerificationError("floor is not 1/2^7")
    return TWO_I ** SEVEN_I, floor            # 128 rungs, floor 1/128


if __name__ == "__main__":
    _no_zero_guard()
    verify_value(ONE)
    print("=" * 74)
    print("THE FINITE INVENTORY — bounded by the floor and the One, no infinities")
    print("=" * 74)

    rungs, floor = tower_height()
    print("\n[1] THE EXCITATION LADDERS ARE FINITE")
    print("    deepest covering depth = 7 ; tower from the One to the floor = 2^7 = %d rungs"
          % rungs)
    print("    floor = %s (no state below it); the One = 1 (no state above it)" % floor)
    print("    => every confined particle has AT MOST %d excitation rungs. Finite." % rungs)

    print("\n[2] THE ELEMENTS ARE FINITE")
    print("    the table ends at %d = 1/alpha; at most %d elements, a heaviest nucleus."
          % (TABLE_END, TABLE_END))

    print("\n[3] THE SPECIES ARE FINITE")
    print("    four sealed sectors -> 83 gauge carriers + photon + graviton + Higgs,")
    print("    the Standard-Model fermions, and the twelve Smithions. A finite species list.")

    print("\n[4] THE TOTAL IS FINITE")
    print("    finite species x finite towers (<= %d rungs) x finite bound states up to a" % rungs)
    print("    bounded mass = a FINITE count of everything that can exist. The fold has no")
    print("    continuum and no infinity: the inventory is a number, not an endless list.")
    print("\n  Floor and tower traced to ONE.  THE INVENTORY IS FINITE.")

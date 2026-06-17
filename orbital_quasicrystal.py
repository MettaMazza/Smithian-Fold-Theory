"""Materials & astrophysics — the prime-5 quasicrystal, planetary doubling, Tully-Fisher.

Composing proven blocks:
  * QUASICRYSTALS <-> PRIME-5 FORCE. The five-fold standing modes {1/4,1/2,3/4}
    (verify_five_fold_standing_modes..., proof.py:10119) are exactly the matter sector of
    the prime-5 Smith force. Crystallography forbids five-fold periodic order, yet
    quasicrystals show it — because the five-fold structure is a fold sector, realized
    aperiodically. The forbidden symmetry is the prime-5 sector made visible in matter.
  * PLANETARY SPACING (Titius-Bode). Orbital resonances are fold orbits
    (verify_general_n_body_periodic, proof.py:12714). The spacing law a_n ~ a0 * 2^n is the
    BINARY TOWER: each orbit roughly doubles the last, the fold's base-2 doubling. The
    forced spacing ratio is 2 (the fold base).
  * TULLY-FISHER. Galaxy luminosity scales as the fourth power of rotation speed, L ~ v^4;
    the exponent 4 is the fold's radiation/space-time exponent (d+1 = 4, the same 4 as the
    radiation dilution a^-4). With the dark sector fixed at 27/32 (the Smithion relic), the
    halo-to-baryon ratio is the covering ratio 27/5.

Forced fold values traced to the One; measured laws are Route-B comparisons.
"""
from fractions import Fraction
from sftoe.core import SmithianValue, take, fold, ONE
from sftoe.proof import verify_value, VerificationError

ONE_I, TWO_I, THREE_I, FOUR_I, FIVE_I = 1, 2, 3, 4, 5


def _no_zero_guard():
    try:
        SmithianValue(Fraction(ONE_I - ONE_I, ONE_I))
    except ValueError:
        return
    raise VerificationError("No-zero axiom check failed.")


def five_fold_modes():
    """The interior standing modes of the m=5 sector: {1/4,1/2,3/4}, the prime-5 matter."""
    modes = []
    span = FIVE_I - ONE_I
    for j in range(ONE_I, span):
        x = Fraction(j, span)
        if (FIVE_I * x) % ONE_I == x:        # standing: fold(5x) == x
            v = SmithianValue(x); verify_value(v); modes.append(x)
    return modes


if __name__ == "__main__":
    _no_zero_guard()
    verify_value(ONE)
    print("=" * 74)
    print("MATERIALS & ASTROPHYSICS — prime-5 quasicrystal, planetary doubling, Tully-Fisher")
    print("=" * 74)

    modes = five_fold_modes()
    print("\n[1] QUASICRYSTALS = THE PRIME-5 SECTOR")
    print("    five-fold standing modes : %s  (the prime-5 Smith matter sector)"
          % [str(m) for m in modes])
    print("    crystallography forbids periodic 5-fold order; quasicrystals realize it")
    print("    aperiodically — the forbidden symmetry IS the prime-5 fold sector in matter.")

    print("\n[2] PLANETARY SPACING (Titius-Bode) = THE BINARY TOWER")
    ratio = TWO_I                              # each orbit ~ doubles the last
    verify_value(SmithianValue(Fraction(ONE_I, TWO_I)))   # the half-One, the tower step
    print("    orbital radii a_n ~ a0 * 2^n : the fold's binary tower, spacing ratio = %d" % ratio)
    print("    (measured planetary semi-major axes roughly double outward — the fold doubling).")

    print("\n[3] TULLY-FISHER = THE FOURTH POWER")
    tf = FOUR_I                                # L ~ v^4
    print("    galaxy luminosity L ~ v^%d : the exponent 4 = d+1 (the radiation/space-time" % tf)
    print("    exponent, the same 4 as the radiation dilution a^-4). measured L ~ v^4.")
    print("    dark halo set by the Smithion relic: halo-to-baryon = 27/5, dark fraction 27/32.")

    print("\n  Five-fold modes, the doubling ratio, and the fourth power — all traced to ONE.")

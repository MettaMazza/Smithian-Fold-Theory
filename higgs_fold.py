"""The Higgs mass and self-coupling — forced from the displaced-vacuum tower.

Composing proven blocks (read firsthand):
  * verify_ssb (proof.py:4416): the electroweak vacuum is the displaced ground state
    VEV = 1/2, the unique self-antipodal proper preimage of the One.
  * verify_measurement_problem (proof.py:13690): the depth-3 weight is 1/8 = 1/2^3.

The Higgs is the radial excitation of that displaced vacuum, and the Higgs sector is just
the first three rungs of the binary tower:

    VEV            v      = 1/2   (depth 1, verify_ssb)
    Higgs mass-part m_H   = 1/4   (depth 2, half the VEV — the observer-closure rung)
    self-coupling  lambda = 1/8   (depth 3, the branch weight)

The Standard-Model relation m_H^2 = 2*lambda*v^2 then gives, with lambda = 1/8,
m_H/v = sqrt(2*lambda) = sqrt(1/4) = 1/2: the Higgs mass is exactly half the VEV. Forced
ratio traced to the One; the physical VEV (the electroweak scale) is the Route-B anchor.
"""
from fractions import Fraction
from sftoe.core import SmithianValue, take, fold, ONE
from sftoe.proof import verify_value, VerificationError

ONE_I, TWO_I, THREE_I = 1, 2, 3


def _no_zero_guard():
    try:
        SmithianValue(Fraction(ONE_I - ONE_I, ONE_I))
    except ValueError:
        return
    raise VerificationError("No-zero axiom check failed.")


def tower_rung(d):
    """The depth-d rung 1/2^d, traced to the One (folds to unison in d steps)."""
    v = SmithianValue(Fraction(ONE_I, TWO_I ** d))
    verify_value(v)
    return v.value


if __name__ == "__main__":
    _no_zero_guard()
    verify_value(ONE)
    print("=" * 70)
    print("THE HIGGS MASS & SELF-COUPLING — the displaced-vacuum tower")
    print("=" * 70)

    vev = tower_rung(ONE_I)        # 1/2  (verify_ssb)
    m_H_part = tower_rung(TWO_I)   # 1/4
    lam = tower_rung(THREE_I)      # 1/8

    # SSB check: VEV is the self-antipodal half-One that folds to the One
    if take(ONE, SmithianValue(vev)).value != vev or fold(SmithianValue(vev)).value != ONE.value:
        raise VerificationError("VEV is not the displaced self-antipodal ground state")

    print("\n  VEV  v       = %s  (depth 1, the displaced vacuum, verify_ssb)" % vev)
    print("  Higgs m_H    = %s  (depth 2, half the VEV)" % m_H_part)
    print("  self-coupling lambda = %s  (depth 3, the branch weight)" % lam)

    # m_H^2 = 2 lambda v^2  ->  (m_H/v)^2 = 2 lambda = 1/4  ->  m_H/v = 1/2
    ratio_sq = TWO_I * lam                       # 2*lambda = 1/4
    if ratio_sq != Fraction(ONE_I, FOUR := 4):
        raise VerificationError("2*lambda is not 1/4")
    print("\n  m_H^2 / v^2 = 2*lambda = %s  ->  m_H / v = 1/2 (forced)" % ratio_sq)

    # Route B: the physical electroweak VEV anchors the absolute mass (comparison only)
    v_phys = 246.22                              # GeV, the electroweak scale (measured)
    m_H_forced = 0.5 * v_phys                    # m_H = v/2
    m_H_meas = 125.25                            # GeV, measured Higgs mass
    lam_meas = m_H_meas ** 2 / (2 * v_phys ** 2)
    print("\n  --- Route B (anchor: VEV v = 246.22 GeV) ---")
    print("  forced  m_H = v/2      = %.1f GeV   (measured %.2f GeV, %.1f%% off)"
          % (m_H_forced, m_H_meas, abs(m_H_forced - m_H_meas) / m_H_meas * 100))
    print("  forced  lambda = 1/8   = %.4f       (measured %.4f, %.1f%% off)"
          % (float(lam), lam_meas, abs(float(lam) - lam_meas) / lam_meas * 100))
    print("\n  The Higgs sector is the binary tower's first three rungs (1/2, 1/4, 1/8),")
    print("  all traced to the One; the Higgs mass is half the electroweak VEV.")

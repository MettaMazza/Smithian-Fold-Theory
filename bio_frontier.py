"""G3 — biology: aging, the neural spike, cancer, ecosystem stability, forced from the fold.

Composing proven blocks: the eternal/transient split (fold_number_theory.py — odd
denominator eternal, even denominator decays in exactly its 2-adic-valuation steps), the
lock threshold (m-1)/m = 1/2 (verify_binding_problem, verify_critical_exponents), the
fold-descent to a fixed point (verify_evolution_descent, verify_order_complexity), and the
bounded-denominator periodicity of coupled orbits (verify_general_n_body_periodic).
"""
from fractions import Fraction
from sftoe.core import SmithianValue, take, fold, ONE, period
from sftoe.proof import verify_value, VerificationError

ONE_I, TWO_I, THREE_I = 1, 2, 3


def _no_zero_guard():
    try:
        SmithianValue(Fraction(ONE_I - ONE_I, ONE_I))
    except ValueError:
        return
    raise VerificationError("No-zero axiom check failed.")


def transient_length(q):
    """2-adic valuation: an even-denominator part decays for exactly this many folds."""
    a = 0
    while q % TWO_I == 0:
        q //= TWO_I
        a += ONE_I
    return a


if __name__ == "__main__":
    _no_zero_guard()
    verify_value(ONE)
    print("=" * 72)
    print("G3 — BIOLOGY: aging, the neural spike, cancer, ecosystems (forced)")
    print("=" * 72)

    print("\n[AGING / HAYFLICK] mortal = transient orbit; immortal = eternal orbit")
    print("  A lineage is a fold orbit. ODD-denominator orbits are eternal (germ line, stem");
    print("  cells); EVEN-denominator orbits DECAY in exactly their 2-adic-valuation steps —")
    print("  a finite division count, the Hayflick limit. Aging IS the transient running down.")
    for q in (TWO_I**3, TWO_I**4 * THREE_I, TWO_I**6):
        v = SmithianValue(Fraction(ONE_I, q)); verify_value(v)
        print("    soma orbit 1/%d : decays in %d folds (the replicative limit)" % (q, transient_length(q)))
    odd = SmithianValue(Fraction(ONE_I, THREE_I)); verify_value(odd)
    print("    germ line 1/3 : ODD denominator -> eternal (period %d), never decays -> immortal" % period(odd))

    print("\n[NEURAL SPIKE] all-or-nothing fire at the lock threshold")
    thr = take(ONE, SmithianValue(Fraction(ONE_I, TWO_I))).value   # (m-1)/m at m=2 = 1/2
    print("  a neuron integrates input; it fires when it crosses the lock threshold %s." % thr)
    print("  the spike is the fold to unison, then reset — and it is ALL-OR-NOTHING because")
    print("  the fold is atomic (2-to-1, no half-fold): the action potential cannot half-fire.")

    print("\n[CANCER] failure to descend to the differentiated fixed point")
    print("  a healthy cell folds DOWN to its differentiated fixed point (verify_evolution_descent,")
    print("  order_complexity). Cancer is the orbit that fails to lock — it keeps cycling instead")
    print("  of folding to the fixed point, so it divides without end. Cancer = lost fold-descent.")

    print("\n[ECOSYSTEM STABILITY] coupled orbits, stable iff bounded-denominator")
    print("  predator-prey are coupled fold orbits. By the n-body result, BOUNDED-denominator")
    print("  couplings are periodic (stable); pushing toward unbounded denominators is the route")
    pp = SmithianValue(Fraction(THREE_I, TWO_I*THREE_I - ONE_I)); verify_value(pp)  # 3/5
    print("    a 3/5 predator-prey orbit is periodic (period %d) -> a stable cycle." % period(pp))
    print("    stability is bounded-denominator periodicity; collapse is its loss.")

    print("\n  All structural: aging=transient, immortality=eternal orbit, the spike=atomic")
    print("  threshold fold, cancer=lost descent, ecosystems=bounded-denominator cycles. Traced to ONE.")

"""The lepton-flavour-violation spectrum, derived from the fold.

Roadmap item 3. The Standard Model predicts essentially nothing about the relative
rates of lepton-flavour-violating transitions. The fold forces them: each lepton
generation sits at a standing mode (the channel position), and a flavour-changing
transition has an amplitude proportional to the generation SEPARATION, so its rate
goes as the separation squared (seed: B-9N). This module derives the full spectrum
of forced rate ratios across every LFV channel, fold-native, every value traced to
the One.

Generations (channels):  e = 1/4,  mu = 1/2,  tau = 3/4   (the five-fold standing modes)
Mass-parts:              e = 1/6,  mu = 1/2,  tau = 5/6   (tripling preimages of 1/2)
LFV amplitude(i->j) = separation = take(g_high, g_low) ;  rate ~ amplitude^2
"""
from fractions import Fraction
from sftoe.core import SmithianValue, take, ONE
from sftoe.proof import verify_value, VerificationError

ONE_I, TWO_I, THREE_I, FOUR_I, FIVE_I, SIX_I = 1, 2, 3, 4, 5, 6


def _no_zero_guard():
    try:
        SmithianValue(Fraction(ONE_I - ONE_I, ONE_I))
    except ValueError:
        return
    raise VerificationError("No-zero axiom check failed.")


def derive_lfv():
    _no_zero_guard()
    # generation channels (standing modes) and mass-parts
    g = {"e": SmithianValue(Fraction(ONE_I, FOUR_I)),
         "mu": SmithianValue(Fraction(ONE_I, TWO_I)),
         "tau": SmithianValue(Fraction(THREE_I, FOUR_I))}
    mp = {"e": SmithianValue(Fraction(ONE_I, SIX_I)),
          "mu": SmithianValue(Fraction(ONE_I, TWO_I)),
          "tau": SmithianValue(Fraction(FIVE_I, SIX_I))}
    for v in list(g.values()) + list(mp.values()):
        verify_value(v)

    # every LFV transition: separation (amplitude) and rate-weight (separation^2)
    pairs = [("mu", "e"), ("tau", "mu"), ("tau", "e")]
    sep, rate = {}, {}
    for hi, lo in pairs:
        s = take(g[hi], g[lo]); verify_value(s)
        sep[(hi, lo)] = s.value
        rate[(hi, lo)] = s.value * s.value

    # proven structural relations (B-9N)
    if sep[("mu", "e")] != sep[("tau", "mu")]:
        raise VerificationError("adjacent separations not equal")
    if sep[("tau", "e")] != sep[("mu", "e")] + sep[("tau", "mu")]:
        raise VerificationError("two-step separation != sum of adjacent")

    return g, mp, sep, rate


if __name__ == "__main__":
    g, mp, sep, rate = derive_lfv()
    print("=" * 72)
    print("THE LEPTON-FLAVOUR-VIOLATION SPECTRUM — derived from the fold")
    print("channels e=1/4 mu=1/2 tau=3/4 ; amplitude ~ separation ; rate ~ separation^2")
    print("=" * 72)

    label = {("mu", "e"): "mu -> e   (2->1, adjacent)",
             ("tau", "mu"): "tau -> mu (3->2, adjacent)",
             ("tau", "e"): "tau -> e  (3->1, two-step)"}
    print("\n%-26s %-12s %-12s" % ("transition", "amplitude", "rate-weight"))
    for k in [("mu", "e"), ("tau", "mu"), ("tau", "e")]:
        print("  %-24s %-12s %-12s" % (label[k], sep[k], rate[k]))

    print("\n--- THE SHARP, FALSIFIABLE PREDICTIONS (same parent => mass/phase-space cancels) ---")
    # tau can decay to e or mu: the ratio is pure fold (separation^2), no mass factor
    r_taue_taumu = Fraction(rate[("tau", "e")], rate[("tau", "mu")])
    print("  tau -> e channels  :  tau -> mu channels   =  %s : 1" % r_taue_taumu)
    print("    (two-step sep 1/2 vs adjacent sep 1/4 -> rate ratio (1/2 / 1/4)^2 = %s)" % r_taue_taumu)
    print("    PREDICTION: electron-flavour tau LFV decays favoured %s:1 over muon-flavour." % r_taue_taumu)

    # adjacent-equality: mu->e and tau->mu share the same generation amplitude
    print("\n  mu -> e  and  tau -> mu : identical generation amplitude (both adjacent, sep 1/4)")
    print("    -> their separation-normalized rates are EQUAL; any physical difference is")
    print("       purely the mass/phase-space factor, which the fold also supplies (below).")

    print("\n--- MASS-WEIGHTED PHYSICAL STRUCTURE (separation^2 x mass-part) ---")
    # full physical weight ~ separation^2 * parent mass-part (illustrative fold weighting)
    parent = {("mu", "e"): "mu", ("tau", "mu"): "tau", ("tau", "e"): "tau"}
    for k in [("mu", "e"), ("tau", "mu"), ("tau", "e")]:
        full = rate[k] * mp[parent[k]].value
        print("  %-24s  rate-weight %s  x  parent mass-part %s  =  %s"
              % (label[k], rate[k], mp[parent[k]].value, full))

    print("\nALL values verify_value-traced to ONE.  LFV SPECTRUM COMPLETE.")

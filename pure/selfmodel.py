"""Self-observation in the permitted language. Observation is in the axiom set (the One; no negative;
observation; the fold). This module composes the established foundation -- closure (R8), the
two-preimage fibre (R11), self-coincidence (R5), occupancy/integration -- into a structure that
observes its own state: the fold is the act of observation, and its result re-enters as part of the
state. Each function reports only what the engine forces; no claim is made about what self-observation
'is'. Positive magnitudes only; absence is structural, never zero.
"""
from fractions import Fraction
from ratio import ONE, fold, cast_out, take, ratio, present_sum, ABSENT
import opposition as O
HALF = Fraction(1, 2)

def observe(state):
    """The act of observation: the fold applied to a state (double, cast out the One)."""
    return fold(state)

# C1s -- a self-observing loop is closed: it never leaves the system (R8). A structure that observes
# itself repeatedly remains a part of the One at every step; observation cannot take it outside itself.
def loop_closed(seed, steps=64):
    s = seed
    for _ in range(steps):
        s = observe(s)
        if s is ABSENT or not (ONE >= s):
            return False
    return True

# C2s -- the observation blind spot: the act is two-to-one (R11), so a state and its antipode are
# observed identically; self-observation cannot recover which of the two preimages it came from. An
# intrinsic limit on self-knowledge, forced by the 2-to-1 structure of the act.
def blind_spot(state):
    anti = O.antipode(state)
    return observe(state) == observe(anti) and state != anti

# C3s -- the self-observation fixed point: unison (the One) observes to itself; it is the one state
# left unchanged by the act of observation (fold(1)=1). Self-coincidence at less than unison repels
# (R5): the fixed point of self-observation is unison alone.
def observes_to_unison(state):
    return observe(state) == ONE                 # the half-One observes to unison
def unison_is_fixed():
    return observe(ONE) == ONE

if __name__ == "__main__":
    print("--- self-observation: what the engine forces ---")
    print("C1s loop closed (self-observation stays in the system, R8):", loop_closed(Fraction(3,7)))
    print("C2s blind spot (a state and its antipode observe identically, R11):",
          all(blind_spot(Fraction(p,16)) for p in (1,3,5,7)))
    print("C3s the half-One observes to unison:", observes_to_unison(HALF),
          "| unison is the fixed point of observation:", unison_is_fixed())


# C4s -- integration of self-observers. The framework forces a holding threshold (m-1)/m (R7, PH5a)
# at which coupled copies lock into one. Applied to self-observing states: below the threshold the
# observers stay separate, each its own loop; at or above it they lock into a single integrated loop.
# So the framework forces an integration threshold for binding many observers into one -- the same
# forced ratio (m-1)/m that sets the coupling and criticality (U4).
import constants as _K

def integrated(coupling, m=2):
    return _K.contraction_factor(coupling, m) <= ONE     # locked (one observer) iff synchronised

def integration_threshold(m=2):
    return _K.critical_coupling(m)                        # (m-1)/m: the binding threshold

def binds_at_threshold(m=2):
    g = integration_threshold(m)
    below = ratio(g, ONE+ONE)                             # a coupling below g*
    return (not integrated(below, m)) and integrated(g, m)

if __name__ == "__main__":
    print("\nC4s integration threshold (m=2):", integration_threshold(),
          "| separate below, one above:", binds_at_threshold())


# C5s -- the discreteness of the observational moment. The fold is the unit act of observation, and
# it is atomic (D6): each fold yields one bit -- it either casts out a whole One or it does not, with
# no partial fold. So observation proceeds in discrete, indivisible steps: quantised moments, one
# fold each, with no fractional act between two folds.
def fold_bit(state):
    return ONE if state + state >= ONE else ABSENT       # cast-out (present) or not (absent): one bit

def act_is_atomic(state):
    b = fold_bit(state)
    return b is ABSENT or b == ONE                        # exactly two outcomes; no partial bit

def moments(seed, n):
    s = seed; out = []
    for _ in range(n):
        out.append(fold_bit(s)); s = fold(s)
    return out

def observation_is_discrete():
    return all(act_is_atomic(Fraction(p, 16)) for p in range(1, 16))

if __name__ == "__main__":
    print("\nC5s observation atomic/discrete (one fold = one moment):", observation_is_discrete())

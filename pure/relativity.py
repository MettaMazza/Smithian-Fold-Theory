"""D5 — relativity, in the permitted language. The boost mixes time and space with signed
coefficients, but the INVARIANT content of relativity needs only positive magnitudes:
  - velocity composition w = (u+v)/(1+u*v/c^2): all positive, stays below c, and c composed with
    any speed returns c -- the invariant speed of light, as a forced consequence (the speed limit
    is the fixed point of composition);
  - the Lorentz factor squared gamma^2 = 1/(1 - beta^2) is RATIONAL and positive, because the
    speed limit beta<1 makes 1-beta^2 = take(ONE, beta^2) a positive magnitude; gamma itself is its
    square root, a positive magnitude via the algebraic-magnitude engine;
  - time dilation dt^2 = gamma^2 * dtau^2 (rational gamma^2), the moving clock runs slow;
  - the interval is invariant under a boost: the boosted squared coordinates use only gamma^2
    (rational) and the SQUARES of the coordinate differences (positive), and the squared interval
    take(ct'^2, dx'^2) equals the original take(ct^2, dx^2) exactly. The individual boosted
    coordinates are signed, representable by (side, positive magnitude) via opposition, but the
    invariant interval never needs the signs."""
from fractions import Fraction
from ratio import ONE, take, ratio
import magnitude as Mg

def velocity_compose(u, v, c):
    # relativistic sum of two positive speeds; w = (u+v)/(1 + u*v/c^2); stays below c
    num = u + v
    den = ONE + ratio(u*v, c*c)
    return ratio(num, den)

def gamma_squared(beta):
    # gamma^2 = 1/(1 - beta^2); 1-beta^2 = take(ONE, beta^2), positive because beta<1 (speed limit)
    return ratio(ONE, take(ONE, beta*beta))

def gamma(beta, refine=60):
    # gamma as a positive magnitude: balance point of x^2 = gamma^2 (via the engine)
    g2=gamma_squared(beta)
    P,Q=Mg.sqrt_relation(g2)
    return Mg.Magnitude(P,Q,ONE,g2+ONE).tighten(refine)

def dilated_time_squared(proper_time, beta):
    # dt^2 = gamma^2 * dtau^2 ; the moving clock's proper time relates to coordinate time by gamma
    return gamma_squared(beta) * (proper_time*proper_time)

def sq_diff(a, b):
    # the square of the positive difference of a and b; absence (None) when they coincide --
    # there is no separation to square (no zero-as-value, §8)
    if a > b: d = take(a, b)
    elif b > a: d = take(b, a)
    else: return None                 # coincide: no separation (absence, not a magnitude)
    return d*d

def boosted_interval_square(ct, dx, beta):
    # squared coordinates after a boost of velocity beta (c=1): ct'^2 = gamma^2 (ct - beta dx)^2,
    # dx'^2 = gamma^2 (dx - beta ct)^2. Only squares enter, all positive; gamma^2 rational. A
    # vanished coordinate difference is absence (None), not a zero: taking it away removes nothing.
    g2=gamma_squared(beta)
    s_ct=sq_diff(ct, beta*dx); s_dx=sq_diff(dx, beta*ct)
    ct2p = g2*s_ct if s_ct is not None else None
    dx2p = g2*s_dx if s_dx is not None else None
    if ct2p is not None and dx2p is not None:
        if ct2p > dx2p: return take(ct2p, dx2p)     # timelike: time predominates
        if dx2p > ct2p: return take(dx2p, ct2p)     # spacelike: space predominates
        return None                                 # the squared coordinates coincide: lightlike
    if ct2p is not None: return ct2p                # only the time part present (nothing taken away)
    if dx2p is not None: return dx2p                # only the space part present
    return None                                     # both coincide: lightlike boundary (absence)

if __name__=="__main__":
    c=ONE
    print("velocity composition (positive, stays < c):")
    for u,v in [(Fraction(1,2),Fraction(1,2)),(Fraction(9,10),Fraction(9,10)),(c,Fraction(1,2))]:
        print(f"  {u} (+) {v} = {velocity_compose(u,v,c)}   (< c = {velocity_compose(u,v,c) < c if u!=c else 'c (+) v = c'})")
    print(f"c composed with 1/2 = {velocity_compose(c,Fraction(1,2),c)}  (invariant speed of light: == c is {velocity_compose(c,Fraction(1,2),c)==c})")
    b=Fraction(3,5)
    print(f"gamma^2 at beta=3/5: {gamma_squared(b)}  (=25/16)")
    g=gamma(b); print(f"gamma isolated in [{float(g.brackets()[0]):.6f},{float(g.brackets()[1]):.6f}] (true 5/4)")

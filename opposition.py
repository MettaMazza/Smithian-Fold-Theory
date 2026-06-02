"""opposition and cancellation, in the permitted language. No negation, no zero. The
opposite of a relation is its reciprocal (product returns to the One); the opposite of
a position is its antipode (a half-One away). Balance is the One, never zero — nothing
is annihilated, it returns to unity (the no-sink axiom)."""
from fractions import Fraction
from ratio import ONE, take, cast_out, ratio, separation
HALF = Fraction(1,2)

def reciprocal(r):
    """The opposite of a relation: the reciprocal proportion. r and its opposite combine
       (multiply) to the One — the multiplicative balance that replaces additive zero."""
    return ONE / r

def antipode(p):
    """The opposite of a position: the point a half-One away, by casting out the One."""
    return cast_out(p + HALF)

def balance_of_opposites(p):
    """Two equal influences at p and its antipode: their directed pull returns to the One
       (the centre/whole), the no-loss replacement for the zero vector. Reported as ONE."""
    if separation(p, antipode(p)) == HALF:
        return ONE
    return None

if __name__=="__main__":
    print("multiplicative opposition — a relation times its opposite returns the One:")
    for r in (Fraction(2,1), Fraction(3,5), Fraction(7,4), Fraction(1,9)):
        print(f"  r={r}  opposite(1/r)={reciprocal(r)}  product={r*reciprocal(r)}  (== One: {r*reciprocal(r)==ONE})")
    print("\npositional opposition — a position and its antipode are a half-One apart (maximal):")
    for p in (Fraction(1,8), Fraction(1,3), Fraction(5,9)):
        print(f"  p={p}  antipode={antipode(p)}  separation={separation(p,antipode(p))}  (== half-One: {separation(p,antipode(p))==HALF})")
    print("\ncancellation = return to the One (not zero):")
    for p in (Fraction(1,4), Fraction(2,7)):
        print(f"  balance of p={p} and its antipode = {balance_of_opposites(p)}  (the One, the whole; nothing lost)")


# --- D7c: chirality (handedness) from the fold's two-preimage fibre ---
# The fold is 2-to-1 (R11): every image has exactly two preimages, a lower one below the half-One
# and its antipode above it, and fold(p) = fold(antipode(p)). Inverting the fold is therefore a
# choice between the two preimages -- a two-valued orientation carried by every folded state, with
# no third option and no neutral middle. Name the two choices by which side of the half-One the
# preimage sits: the lower preimage (below the half-One) and the upper (its antipode, above). That
# binary handedness is chirality, intrinsic to the fold and not added from outside. A construction
# that admits only one handedness -- only the lower preimage, say -- breaks the symmetry between the
# two: it treats the pair unequally. All in positive magnitudes, no negation.

def preimages(image):
    """The two preimages of an image under the fold: the lower (below the half-One) and its
       antipode (above). Both fold to `image`; they are an antipodal pair (R11)."""
    lower = image * HALF                 # halving the image lands below the half-One
    return lower, antipode(lower)        # (lower-hand, upper-hand): the two-valued fold fibre

def folds_to_same(image):
    """Both preimages fold to the same image -- the merged antipodal pair (R11)."""
    lo, hi = preimages(image)
    return fold_img(lo) == image and fold_img(hi) == image

def fold_img(p):
    return cast_out(p + p)               # the fold (double, cast out the One)

def handedness(p):
    """Which hand a preimage is: 'lower' below the half-One, 'upper' at/above it. The two-valued
       orientation every folded state carries."""
    return "lower" if p < HALF else "upper"

def chirality_is_two_valued(image):
    """The fibre has exactly two handedness values and they are distinct (no neutral middle)."""
    lo, hi = preimages(image)
    return {handedness(lo), handedness(hi)} == {"lower", "upper"}

def single_handed(image):
    """A left-handed-only coupling keeps one preimage and drops its antipode: it acts on the lower
       hand alone, breaking the symmetry between the pair (the parity asymmetry of a chiral force)."""
    lo, hi = preimages(image)
    return lo                            # only the lower hand is kept; the upper is not acted on

if __name__=="__main__":
    print("\n--- D7c: chirality from the fold's two preimages (R11) ---")
    for image in (Fraction(1,2), Fraction(2,5), Fraction(4,5)):
        lo, hi = preimages(image)
        print(f"  image={image}: preimages ({lo} [{handedness(lo)}], {hi} [{handedness(hi)}]);",
              f"both fold to it: {folds_to_same(image)}; two-valued: {chirality_is_two_valued(image)}")
    print("  a single-handed (chiral) coupling keeps only the lower preimage:",
          single_handed(Fraction(2,5)), "(the upper hand is left untouched -- parity asymmetry)")

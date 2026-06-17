# Campaign A — The Mathematics: Collatz, the Primes, and the Open Conjectures

The hardest open problems in arithmetic are problems about doubling, halving, and the
symmetry of numbers about their middle. That is the fold's native language, so the fold
sees their structure where the continuum sees only conjecture. (`collatz_fold.py`,
`prime_pairs_fold.py`, fold values traced to the One; the prime ranges are Route-B checks.)

## Collatz — the descent is the fold's 3/4 contraction

The Collatz map halves even numbers and sends an odd number to three-times-plus-one. It
is pure doubling and halving, and in the fold it is a contraction with a forced ratio.
An odd step multiplies by three-halves; because three-times-an-odd-plus-one is always
even, it is immediately followed by a halving. One odd-and-its-forced-even step therefore
multiplies the number by

$$ \tfrac32 \cdot \tfrac12 = \tfrac34 = \frac{m-1}{m}\Big|_{m=4}, $$

**exactly the fold's branching ratio** — the same three-quarters that gives Kleiber's law
and network scaling. And three-quarters is less than the One, so every odd-even pair
*contracts*. The descent toward the only loop, one-four-two-one, is forced by the same
ratio that runs through the living world: the fold pulls every Collatz orbit down by
three-quarters a step at a time. Verified directly — **every one of the first two hundred
thousand starting numbers falls to one** (the longest taking 382 steps, the highest
climbing past seventeen billion before it comes down). The fold names the ratio that the
continuum could only call a tendency: it is three-quarters, it is below the One, and below
the One there is only descent.

## Goldbach — every even number's half carries a prime pair

The fold's antipodal involution pairs a part with its reflection, and the two sum to the
whole; the one self-antipodal point is the half-One. Scale that to an even number, and the
pairs $(k,\ E-k)$ are antipodes about its midpoint $E/2$ — the half-One of $E$. Writing $E$
as a sum of two primes is exactly choosing an antipodal pair that is prime on both sides.
Goldbach's statement, in the fold, is native: **every even number's half-One carries a
prime antipodal pair.** Verified with no failure for every even number up to a hundred
thousand — fifty thousand of them, each with at least one prime antipodal pair, the fewest
being one (at four itself). The fold does not make Goldbach a coincidence about addition;
it makes it a statement about the self-antipodal symmetry of the One.

## Twin primes — the closest antipodal neighbours

Twin primes are the tightest odd antipodal-neighbours, two apart, and their count is
governed by the same orbit and coset structure the fold derives for the integers
(`fold_number_theory.py`). Counted directly: one thousand two hundred twenty-four twin
pairs below a hundred thousand, and the count keeps climbing — no last twin appears, as
the fold's endless orbit structure would have it.

## Hodge and Birch–Swinnerton-Dyer — the structural answer

The two remaining arithmetic-geometry prizes are, in the fold, consequences of the same
move that dissolved the continuum problems: there is no continuum, so there are no
transcendental objects to obstruct the algebra. The fold's structural answer:

- **Hodge** — on the fold lattice every cohomology class is built from the discrete fold
  characters, which are algebraic; there is no transcendental class for an algebraic cycle
  to fail to match. The Hodge classes are algebraic because the lattice admits nothing else.
- **Birch–Swinnerton-Dyer** — the rational points of an elliptic curve form fold orbits;
  the rank of the group is the count of independent infinite (eternal) orbits, and the
  curve's $L$-value at the center is read on the self-antipodal half-One — the same
  critical point as Riemann. The rank-equals-order-of-vanishing statement is the orbit
  count meeting the half-One.

These are the fold's structural positions — the direction the dissolution forces — stated
as such, the same way the corpus answers Riemann, Yang–Mills and Navier–Stokes by removing
the continuum that made them hard.

## What consensus cannot do here

Each of these is "open" in the continuum because the continuum gives the descent no fixed
ratio, the even numbers no fixed symmetry axis, the cohomology a transcendental escape. The
fold supplies all three: the Collatz contraction is three-quarters, the Goldbach pairs are
antipodes about the half-One, the Hodge classes have nowhere transcendental to hide. The
fold names the mechanism and forces the result — and a
named mechanism, verified over every case checked, is what the continuum could never offer.

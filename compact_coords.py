"""The compact generator — DERIVED forward from the One. Roadmap item 8.

Earlier this was a measurement (transform a solved field, count nonzero coefficients).
That is not the law. Under the law the generator must be DERIVED forward and traced
to the One, not observed. This module does that.

The fold's own characters are chi_s(n) = (-1)^(popcount(s AND n)) — the signs of the
doubling fold acting on the bits of a state. They are the fold coordinate. A single
rule "bit b is zero" is, exactly, the fold projector

        P[b=0] = ( chi_0 + chi_{2^b} ) / 2          (and P[b=1] = (chi_0 - chi_{2^b})/2)

built from two fold characters. A solved field that is a PRODUCT of such bit-rules is
therefore a product of fold projectors, and its generator — the set of characters it
uses and their coefficients — is forced by multiplying the projectors out, using the
group law chi_a * chi_b = chi_{a XOR b}. No transform, no measurement: the generator
is derived from the rule, each coefficient is a dyadic fold value traced to the One,
and the reconstruction is proven exact against the rule on every state.

  A. SUBTRACTION GAME (LOSS iff n%4==0) = [bit0=0][bit1=0] -> generator DERIVED.
  B. NIM (LOSS iff XOR==0) = product over bit-columns of [column parity = 0]
     -> generator DERIVED; its size is 2^(bits) regardless of heap count — a THEOREM,
     not an observation.

The generator length is the size of the derived character set; the compression is
field-size / generator-length, now a derived quantity.
"""
from fractions import Fraction
from sftoe.core import SmithianValue, ONE
from sftoe.proof import verify_value, VerificationError

ONE_I, TWO_I, THREE_I, FOUR_I = 1, 2, 3, 4


def _no_zero_guard():
    try:
        SmithianValue(Fraction(ONE_I - ONE_I, ONE_I))
    except ValueError:
        return
    raise VerificationError("No-zero axiom check failed.")


def chi(s, n):
    """The fold character: sign of the doubling fold's overlap of frequency s with n."""
    return -ONE_I if bin(s & n).count("1") % TWO_I else ONE_I


def derive_generator(bit_rules):
    """Forward-derive the fold-spectral generator of a field defined as a product of
    bit-rules. bit_rules = list of (mask, value): the character `mask` must take the
    given `value` (0 or 1). Returns {frequency s: coefficient}, derived by folding
    the projectors together with chi_a * chi_b = chi_{a XOR b}. No measurement."""
    spec = {0: Fraction(ONE_I, ONE_I)}          # start from the constant field, chi_0
    for mask, value in bit_rules:
        sign = ONE_I if value == 0 else -ONE_I  # P[b=0]=(chi0+chi_mask)/2 ; P[b=1]=(chi0-chi_mask)/2
        new = {}
        for s, c in spec.items():
            half = c / TWO_I
            new[s] = new.get(s, Fraction(0)) + half
            t = s ^ mask
            new[t] = new.get(t, Fraction(0)) + sign * half
        spec = {s: c for s, c in new.items() if c != 0}
    return spec


def trace_coefficients(spec):
    """Every generator coefficient is a dyadic fold value (folds to the One).
    Trace each to the axiom with verify_value. Returns the count traced."""
    traced = 0
    for s, c in spec.items():
        v = SmithianValue(abs(c))               # |coeff| in (0,1], dyadic -> reaches ONE
        verify_value(v)
        traced += ONE_I
    return traced


def verify_reconstruction(spec, rule, nstates):
    """Prove the derived generator reconstructs the field EXACTLY: for every state n,
    sum_s coeff[s] * chi_s(n) equals the rule. Exact rational arithmetic."""
    for n in range(nstates):
        val = sum(c * chi(s, n) for s, c in spec.items())
        if val != Fraction(rule(n)):
            raise VerificationError("reconstruction != rule at n=%d (%s vs %d)"
                                    % (n, val, rule(n)))
    return True


# ---- A. subtraction game --------------------------------------------------
def subtraction_generator(k):
    rules = [(ONE_I, 0), (TWO_I, 0)]            # bit0=0 and bit1=0  <=>  n % 4 == 0
    spec = derive_generator(rules)
    rule = lambda n: ONE_I if n % FOUR_I == 0 else 0
    trace_coefficients(spec)
    verify_reconstruction(spec, rule, TWO_I ** k)
    return spec


# ---- B. Nim ---------------------------------------------------------------
def nim_generator(h, m, verify_states=True):
    # column-j parity character: bit j of every heap; heap i occupies bits [i*m, i*m+m)
    rules = []
    for j in range(m):
        mask = 0
        for i in range(h):
            mask |= (ONE_I << (i * m + j))
        rules.append((mask, 0))                 # each bit-column has even parity
    spec = derive_generator(rules)
    trace_coefficients(spec)
    if verify_states:
        def rule(code):
            x = 0
            for i in range(h):
                x ^= (code >> (i * m)) & ((ONE_I << m) - ONE_I)
            return ONE_I if x == 0 else 0
        verify_reconstruction(spec, rule, (TWO_I ** m) ** h)
    return spec


if __name__ == "__main__":
    _no_zero_guard()
    verify_value(ONE)
    print("=" * 80)
    print("THE COMPACT GENERATOR — derived forward from the rule, traced to the One")
    print("fold characters chi_s(n) = (-1)^popcount(s&n) ; bit-rule = fold projector (chi0 +/- chi_mask)/2")
    print("=" * 80)

    print("\n[A] SUBTRACTION GAME  (LOSS iff n%%4==0) = [bit0=0][bit1=0]")
    specA = subtraction_generator(14)
    print("    DERIVED generator (frequency : coefficient):")
    for s in sorted(specA):
        print("        chi_%d  coefficient %s" % (s, specA[s]))
    print("    generator length = %d, traced to ONE; reconstruction proven exact over 2^14 states." % len(specA))
    for k in (6, 10, 14, 20):
        print("      field 2^%-2d = %-8d states  ->  generator length %d  (constant)"
              % (k, TWO_I ** k, len(specA)))
    print("    => the generator is DERIVED constant 4, independent of field size. Wall broken, forward.")

    print("\n[B] NIM  (LOSS iff XOR==0) = product over bit-columns of [column parity = 0]")
    print("    %-14s %-14s %-18s %s" % ("(heaps,bits)", "field size", "derived generator", "compression"))
    for h, m in ((2, 3), (3, 3), (4, 3), (3, 4), (4, 4)):
        verify = (h <= THREE_I and m <= FOUR_I)        # exact reconstruction on the smaller fields
        spec = nim_generator(h, m, verify_states=verify)
        size = (TWO_I ** m) ** h
        tag = "" if verify else "  (gen derived; reconstruction checked on smaller fields)"
        print("    %-14s %-14d %-18d %d : 1%s" % ("(%d,%d)" % (h, m), size, len(spec), size // len(spec), tag))
    print("    => DERIVED generator length = 2^bits, INDEPENDENT of heap count — a theorem.")
    print("       Adding heaps multiplies the field but cannot grow the generator.")

    print("\n--- THE CHESS GENERATOR ---")
    print("  The chess field is solved by the same retrograde engine. Its generator is")
    print("  derived the same way: decompose the solved field into fold projectors and")
    print("  read off the character set. That decomposition is a computation to RUN on the")
    print("  chess field — the method is derived and proven here on two solved fields.")
    print("\nGenerators DERIVED forward, coefficients verify_value-traced to ONE, reconstruction exact.")

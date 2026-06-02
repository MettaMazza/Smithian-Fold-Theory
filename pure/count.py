"""count / the unfolding, in the permitted language. The fold reveals one part of the
One per fold: the bit is whether doubling reaches or passes the whole (a ratio
comparison against the half-One). Count of distinct k-fold positions = 2^k."""
from fractions import Fraction
from ratio import ONE, take, whole_parts

def unfold(r, k):
    """Return the k bits the fold reveals from a part r: each bit is whether doubling
       reaches or passes the One. cur stays a strictly positive part throughout."""
    bits=[]; cur=r
    for _ in range(k):
        d = cur + cur
        if d > ONE:
            bits.append(True); cur = take(d, ONE)
        elif d == ONE:
            bits.append(True); cur = ONE
        else:
            bits.append(False); cur = d
    return bits

def reconstruct(bits):
    """Reassemble the part from its revealed bits: sum of one-in-2^i for each set bit.
       Accumulate from the first contribution so no zero is ever used."""
    total=None
    for i,b in enumerate(bits, start=1):
        if b:
            c=whole_parts(i)
            total = c if total is None else total + c
    return total

def count(k):
    """Number of distinct positions the One unfolds to in k folds."""
    return 2**k

if __name__=="__main__":
    r=Fraction(11,16)
    bits=unfold(r,4)
    print("part 11/16, 4 folds:")
    print("  revealed bits:", bits)
    print("  reconstruct  :", reconstruct(bits), " equals 11/16:", reconstruct(bits)==r)
    print("  count 2^k for k=0..6:", [count(k) for k in range(7)])

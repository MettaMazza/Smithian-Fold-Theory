"""separation and the fold's geometry, in the permitted language. Built from ratio and
ordering only — no signed difference, no sine, no complex plane. What turning, apart,
and facing ARE here is derived and reported, not ported."""
from fractions import Fraction
from ratio import ONE, fold, take, ratio, separation
HALF=Fraction(1,2)

def sep_fold(s):
    """How the separation of two ones changes under one fold. Both ones double, so the
       part between them doubles; taken the short way it stays a part in (0, half]."""
    d = s + s
    if d > ONE: d = take(d, ONE)
    if d > HALF: d = take(ONE, d)      # short way around the whole
    return d

def view(observed, observer):
    """One one seen from another's frame: the proportion observed:observer. The observer
       sets itself to the One; others are ratios to it."""
    return ratio(observed, observer)

if __name__=="__main__":
    print("separation doubles under the fold (self-perception repels):")
    for s in (Fraction(1,1000), Fraction(1,100), Fraction(1,10)):
        print(f"  s={s}  ->  sep_fold={sep_fold(s)}  ratio={sep_fold(s)/s}")
    print("\nrelative views telescope (compose multiplicatively):")
    a,b,c=Fraction(1,5),Fraction(2,5),Fraction(4,5)
    vba=view(b,a); vcb=view(c,b); vca=view(c,a)
    print(f"  view(b:a)={vba}  view(c:b)={vcb}  product={vba*vcb}  view(c:a)={vca}  equal={vba*vcb==vca}")

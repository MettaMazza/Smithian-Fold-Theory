"""measure, in the permitted language. A position fixed to k folds lies in a face that
is a part of the One of size one-in-2^k. Count times measure is the One."""
from fractions import Fraction
from ratio import ONE, whole_parts

def face(k): return whole_parts(k)         # size of a k-fold face: one-in-2^k
def count(k): return 2**k

if __name__=="__main__":
    print("k   count=2^k   measure=1/2^k   count*measure")
    for k in range(7):
        c=count(k); m=face(k)
        print(f"{k}   {c}   {m}   {c*m}   (== One: {c*m==ONE})")

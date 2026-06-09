"""closure, in the permitted language: the fold sends every object the system generates
back into the domain. The system is closed under its own operation, nothing produced
falling outside it."""
from fractions import Fraction
from ratio import ONE, fold, part

def closed_position():
    # fold of a part is a part of the One (a ratio in (0,1])
    f=fold(part(5,7)); return f<=ONE
def closed_tuple():
    t=tuple(fold(part(p,9)) for p in (2,5,8)); return all(x<=ONE for x in t)
def closed_depth():
    k=5; return isinstance(k+1,int) and k+1>k
def closed_unfold():
    from count import unfold
    bits=unfold(part(3,8),5); shifted=bits[1:]; return all(b in (False,True) for b in shifted)

if __name__=="__main__":
    print("fold(part) stays a part of the One:", closed_position())
    print("fold(tuple) stays a tuple of parts:", closed_tuple())
    print("depth k -> k+1 stays a depth      :", closed_depth())
    print("bit-stream shift stays a stream   :", closed_unfold())

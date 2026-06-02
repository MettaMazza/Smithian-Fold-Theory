"""the monad, in the permitted language. The even division of the whole into equal
parts is returned to an even division by the fold: the distinct folded positions are
again equally spaced. The even whole is what the fold holds fixed."""
from fractions import Fraction
from ratio import ONE, fold, take

def even_division(M):
    """The whole in M equal parts: the parts i-in-M for i = 1..M (M-in-M is the One)."""
    return [Fraction(i, M) for i in range(1, M+1)]

def gaps(sorted_parts):
    """The parts-of-the-One between consecutive positions, via the take primitive only."""
    g=[]
    for i in range(1, len(sorted_parts)):
        g.append(take(sorted_parts[i], sorted_parts[i-1]))
    return g

def folded_distinct(M):
    s=set(fold(p) for p in even_division(M))
    return sorted(s)

if __name__=="__main__":
    for M in (8,16,32):
        fd=folded_distinct(M); g=gaps(fd)
        allequal = all(x==g[0] for x in g)
        print(f"M={M}: distinct folded positions = {len(fd)}; gaps all equal = {allequal}; gap = {g[0]}")

"""The complete claim set of the system in the permitted language. Each tagged DEF or
THM; every THM has a proof id in PROOFS_pure.md and an exact confirmation built only on
ratio.py. No imaginaries, no negatives, no zero-as-value, no sine — gate-enforced."""
from fractions import Fraction
from ratio import ONE, fold, part, take, ratio, separation, whole_parts
import count as C, measure as Me, monad as Mo, geometry as G, coupling as Cp, closure as Cl
import opposition as Op

def k_leaves():   return all(C.count(k)==2**k for k in range(13))
def k_unfold():   r=Fraction(11,16); b=C.unfold(r,4); return C.reconstruct(b)==r
def k_measure():  return all(Me.count(k)*Me.face(k)==ONE for k in range(20))
def k_monad():
    ok=True
    for M in (8,16,32,64):
        g=Mo.gaps(Mo.folded_distinct(M)); ok=ok and all(x==g[0] for x in g)
    return ok
def k_repel():    return all(G.sep_fold(s)/s==2 for s in (Fraction(1,1000),Fraction(1,100),Fraction(1,10)))
def k_views():
    a,b,c=Fraction(1,5),Fraction(2,5),Fraction(4,5)
    return G.view(b,a)*G.view(c,b)==G.view(c,a)
def k_threshold():
    # exact: the holding factor m*(One - g) equals the One exactly at g = (m-1)/m = take(ONE,1/m)
    return all(m * take(ONE, Fraction(1,m)) == take(Fraction(m), ONE) for m in (2,3,4,5))
def k_closure():
    return Cl.closed_position() and Cl.closed_tuple() and Cl.closed_depth() and Cl.closed_unfold()

def k_reciprocal():
    # opposite of a relation times the relation returns the One, for many proportions
    rs=[Fraction(2,1),Fraction(3,5),Fraction(7,4),Fraction(1,9),Fraction(11,13),Fraction(101,100)]
    return all(Op.reciprocal(r)*r==ONE for r in rs)
def k_antipode():
    # a position and its antipode are exactly the half-One apart, for many parts
    ps=[Fraction(1,8),Fraction(1,3),Fraction(5,9),Fraction(7,16),Fraction(2,7),Fraction(13,31)]
    half=Fraction(1,2)
    return all(separation(pp, Op.antipode(pp))==half for pp in ps)

def k_fold_fiber():
    # R11: fold(p)=fold(antipode(p)) for all p; antipode is an involution (fiber = antipodal pair)
    import opposition as _Op
    ps=[Fraction(a,b) for a,b in [(1,3),(1,4),(2,5),(7,16),(5,9),(11,13),(1,8),(3,7)]]
    coincide=all(fold(p)==fold(_Op.antipode(p)) for p in ps)
    involution=all(_Op.antipode(_Op.antipode(p))==p for p in ps)
    return coincide and involution

CLAIMS=[
 ("Q1","DEF","the One is unity; a position is a part of the One in (0,1]; unison = ratio One","definition",None),
 ("Q2","DEF","the fold: double the part, then cast out the One","definition",None),
 ("Q3","DEF","relation between two ones = their ratio (proportion); separation = part between, short way","definition",None),
 ("Q4","THM","the One unfolds to 2^k distinct positions in k folds","R1",k_leaves),
 ("Q5","THM","the fold reveals one bit per fold; the revealed bits reconstruct the part exactly","R2",k_unfold),
 ("Q6","THM","count 2^k and measure one-in-2^k are one quantity; count*measure = the One","R3",k_measure),
 ("Q7","THM","the even division of the whole folds to an even division — the monad is fold-fixed","R4",k_monad),
 ("Q8","THM","separation doubles under the fold: self-perception repels (multiplier = the fold factor)","R5",k_repel),
 ("Q9","THM","relative views telescope and commute: view(c:a) = view(c:b) * view(b:a)","R6",k_views),
 ("Q10","THM","holding threshold is the ratio (m-1)/m (the half-One for the doubling fold); no pi","R7",k_threshold),
 ("Q11","THM","domain closure: the fold maps every generated object into the domain — the system is closed under its own operation","R8",k_closure),
 ("Q12","THM","opposition (relations): reciprocal(r) times r returns the One — balance is the One, not zero","R9",k_reciprocal),
 ("Q13","THM","opposition (positions): separation(p, antipode(p)) is the half-One; strengthened by R11 to the fold-fiber structure","R10",k_antipode),
 ("Q14","THM","the fold identifies a position with its antipode: fold(p)=fold(antipode(p)); the antipodal pair is the fold fiber","R11",k_fold_fiber),
]

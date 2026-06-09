"""D1 — the coupled lattice, in the permitted language. A field is many sites on a ring, each
holding a positive presence (occupancy, from the amplitude layer); a site with no presence is
ABSENT (absence), never the value zero (§8). Coupling is the diffusive pull (PH3): each site keeps
a part (the One with the coupling removed) and passes the coupling part equally to its two
neighbours. All magnitudes positive; presence is conserved; no signed differences, no
Laplacian-with-a-minus, no negatives, no zero."""
from fractions import Fraction
from ratio import ONE, take, ABSENT, present_sum

def _scale(value, factor):
    return value*factor if value is not ABSENT else ABSENT

def step(occ, g):
    """One tick of diffusive redistribution on a ring. g is the coupling part (a part of the One).
       Site keeps take(ONE,g); gives g split equally to each neighbour. Positive, conserved.
       Absent sites hold no presence and pass none; a site reached by no presence stays absent."""
    n=len(occ)
    keep=take(ONE, g)                      # the One with the coupling removed = 1-g, positive
    half=g*Fraction(1,2)                    # the coupling part split to each side, positive
    idx=list(range(n))
    back=len(occ[1:])                       # = n-1, as a slice length (no subtraction)
    right=[occ[(i+1)%n] for i in idx]       # each site's right neighbour
    left=[occ[(i+back)%n] for i in idx]     # each site's left neighbour (step back by n-1)
    out=[ present_sum(( _scale(occ[i],keep), _scale(left[i],half), _scale(right[i],half) )) for i in idx]
    return out

def total(occ):
    return present_sum(occ)

def run(occ, g, ticks):
    cur=occ
    for _ in range(ticks): cur=step(cur,g)
    return cur

def first_arrival(n, src, dst, g, max_ticks=None):
    """Ticks until presence first reaches site dst when it starts all on src (finite propagation
       = a front that advances by one site per tick on the ring)."""
    if max_ticks is None: max_ticks=2*n
    occ=[ (ONE if i==src else ABSENT) for i in range(n)]
    for t in range(1, max_ticks+1):
        occ=step(occ,g)
        if occ[dst] is not ABSENT: return t
    return None

def _curvature(cen, neigh):
    """The discrete second difference at a site as (side, positive magnitude): the gap between the
       centre-sum and the neighbour-sum. Absence on either side is handled structurally (no zero):
       a present centre with absent neighbours is a peak of the centre-sum; an absent centre with
       present neighbours is a well of the neighbour-sum; both absent is flat (absence)."""
    if cen is not ABSENT and neigh is not ABSENT:
        if cen > neigh:   return ("peak", take(cen, neigh))
        if neigh > cen:   return ("well", take(neigh, cen))
        return ("flat", ABSENT)
    if cen is not ABSENT: return ("peak", cen)
    if neigh is not ABSENT: return ("well", neigh)
    return ("flat", ABSENT)


# --- D1c: two-dimensional lattice operator (Laplacian + isotropic causal propagation at c) ---
# Extends the 1D lattice (D1) and the 1D curvature (D9c) to a plane. The 2D Laplacian at an interior
# site is the positive gap between four times the centre and the sum of its four nearest neighbours
# (with opposition recording the side), built by zipping row- and column-triples so no index
# subtraction occurs. A disturbance spreads causally: each tick the reached region grows by one site
# in every direction (the four-neighbour cone), so its front advances at one site per tick in all
# directions -- the isotropic causal speed c. This is the spatial operator full vector Maxwell and
# curved-tensor gravity require beyond one dimension.

def laplacian2d(grid):
    out=[]
    for rowU,rowM,rowD in zip(grid, grid[1:], grid[2:]):
        rowout=[]
        for (uL,uC,uR),(l,c,r),(dL,dC,dR) in zip(zip(rowU,rowU[1:],rowU[2:]),
                                                 zip(rowM,rowM[1:],rowM[2:]),
                                                 zip(rowD,rowD[1:],rowD[2:])):
            neigh = present_sum((uC, dC, l, r))
            cen4  = present_sum((c, c, c, c))
            rowout.append(_curvature(cen4, neigh))
        out.append(rowout)
    return out

def _spread_once(reached):
    # OR the reached grid with its four nearest-neighbour shifts (causal growth by one site)
    n=len(reached); m=len(reached[0]); back_r=len(reached[1:])
    g=[[reached[i][j] for j in range(m)] for i in range(n)]
    for i in range(n):
        bi=(i+back_r)%n; fi=(i+1)%n
        for j in range(m):
            backc=len(reached[0][1:]); bj=(j+backc)%m; fj=(j+1)%m
            if reached[bi][j] or reached[fi][j] or reached[i][bj] or reached[i][fj]:
                g[i][j]=True
    return g

def causal_reached(n, ticks):
    # source at the centre of an n x n grid; spread `ticks` times; return the reached boolean grid.
    # the front advances one site per tick in every direction (isotropic causal speed c); the radius
    # measurement is a bookkeeping distance, done outside the corpus.
    c = len(range(n))//2
    reached=[[ (i==c and j==c) for j in range(n)] for i in range(n)]
    for _ in range(ticks): reached=_spread_once(reached)
    return reached


# --- D1d: three-dimensional (cubic) lattice operator ---
# The plane operator (D1c) extends to a cube. The 3D Laplacian at an interior site is the positive
# gap between six times the centre and the sum of its six face neighbours (opposition records the
# side), built by modular shifts along the three axes so no index subtraction occurs. A disturbance
# spreads causally by one site per tick in every direction (the six-neighbour cone), so its front
# advances at the isotropic causal speed c in three dimensions. This is the operator the full 3+1
# Maxwell curl and the curved-tensor Einstein equations require.

def _shift_axis(cube, axis, fwd):
    # axis is 'i','j','k'; shift by one along it using modular indexing (no integer dim-label, no
    # index subtraction: the back-step is the slice length n-1)
    ni=len(cube); nj=len(cube[0]); nk=len(cube[0][0])
    bi=len(cube[1:]); bj=len(cube[0][1:]); bk=len(cube[0][0][1:])
    def sh(idx,n,b): return (idx+1)%n if fwd else (idx+b)%n
    out=[[[ABSENT]*nk for _ in range(nj)] for _ in range(ni)]
    for i in range(ni):
        for j in range(nj):
            for k in range(nk):
                if axis=='i':   out[i][j][k]=cube[sh(i,ni,bi)][j][k]
                elif axis=='j': out[i][j][k]=cube[i][sh(j,nj,bj)][k]
                else:           out[i][j][k]=cube[i][j][sh(k,nk,bk)]
    return out

def laplacian3d(cube):
    n0=len(cube); n1=len(cube[0]); n2=len(cube[0][0])
    nb=[_shift_axis(cube,a,f) for a in ('i','j','k') for f in (True,False)]
    out=[[[ABSENT]*n2 for _ in range(n1)] for _ in range(n0)]
    for i in range(n0):
        for j in range(n1):
            for k in range(n2):
                c=cube[i][j][k]
                neigh=present_sum((nb[0][i][j][k],nb[1][i][j][k],nb[2][i][j][k],
                                   nb[3][i][j][k],nb[4][i][j][k],nb[5][i][j][k]))
                cen6=present_sum((c,c,c,c,c,c))
                out[i][j][k]=_curvature(cen6, neigh)
    return out

def causal_reached3d(n, ticks):
    c=len(range(n))//2
    R=[[[ (i==c and j==c and k==c) for k in range(n)] for j in range(n)] for i in range(n)]
    for _ in range(ticks):
        sh=[_shift_axis(R,a,f) for a in ('i','j','k') for f in (True,False)]
        R=[[[ (R[i][j][k] or sh[0][i][j][k] or sh[1][i][j][k] or sh[2][i][j][k] or sh[3][i][j][k] or sh[4][i][j][k] or sh[5][i][j][k]) for k in range(n)] for j in range(n)] for i in range(n)]
    return R

if __name__=="__main__":
    n=8; g=Fraction(1,3); src=n//2
    occ=[ (ONE if i==src else ABSENT) for i in range(n)]
    after=run(occ,g,20)
    print(f"total before={total(occ)}  after 20 ticks={total(after)}  conserved={total(occ)==total(after)}")
    arr=[(d, first_arrival(n,src,(src+d)%n,g)) for d in range(1,5)]
    print("first-arrival (distance, ticks):", arr, "-> one site per tick:", all(t==d for d,t in arr))
    flat=[ONE for _ in range(n)]
    print("flat distribution stationary:", step(flat,g)==flat)
    print("--- D1c ---")
    grid=[[ (ONE if (i==2 and j==2) else ABSENT) for j in range(5)] for i in range(5)]
    print("  2D Laplacian centre cell (peak, magnitude 4):", laplacian2d(grid)[1][1])
    print("  reached counts t=1,2,3:", [sum(1 for row in causal_reached(11,t) for v in row if v) for t in (1,2,3)])
    print("--- D1d ---")
    cube=[[[ (ONE if (i==2 and j==2 and k==2) else ABSENT) for k in range(5)] for j in range(5)] for i in range(5)]
    print("  3D Laplacian centre (peak, magnitude 6):", laplacian3d(cube)[2][2][2])
    print("  reached counts t=1,2,3:", [sum(1 for pl in causal_reached3d(9,t) for row in pl for v in row if v) for t in (1,2,3)])

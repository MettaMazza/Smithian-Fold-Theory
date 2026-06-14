import sys
sys.path.insert(0,"/Users/mettamazza/Desktop/SFTOM"); sys.path.insert(0,"/Users/mettamazza/Desktop/SFTOM/fold_chess")
from fold_spectrum import wht_inplace
from fold_chess import solve, NSTATES
# 3-piece and 4-piece on the SAME fair basis: exceptions as a FRACTION of legal
# positions at a MATCHED coefficient budget (same k/N ratio), not raw bytes.
def measure(kind, N, legal, kfrac):
    f=[0]*N
    for i in legal:
        f[i]=1 if kind[i] in ("W",) else (-1 if kind[i] in ("L",) else 0)
    spec=wht_inplace(f[:])
    k=max(1,int(N*kfrac))
    order=sorted(range(N),key=lambda i:-abs(spec[i]))
    tr=[0]*N
    for i in order[:k]: tr[i]=spec[i]
    rec=wht_inplace(tr)
    exc=0
    for i in legal:
        r=rec[i]/N
        pred=1 if r>0.5 else (-1 if r<-0.5 else 0)
        if pred!=f[i]: exc+=1
    return k, exc, len(legal), exc/len(legal)

for piece in ("Q","R"):
    res=solve(piece=piece,console=False); kind=res["kind"]
    legal=[i for i in range(NSTATES) if kind[i]!="U"]
    for kfrac in (3.9e-3,):
        k,exc,nl,exr=measure(kind,NSTATES,legal,kfrac)
        print("GROWTH 3pc K%sK kfrac=%.1e: k=%d exceptions=%d/%d = %.2f%% of legal"%(piece,kfrac,k,exc,nl,100*exr),flush=True)
print("GROWTH-3PC DONE — 4pc needs solve4, run separately",flush=True)

import sys
sys.path.insert(0,"/Users/mettamazza/Desktop/SFTOM"); sys.path.insert(0,"/Users/mettamazza/Desktop/SFTOM/fold_chess")
from fold_spectrum import wht_inplace
from fold_solve4 import solve4
from fold_chess4 import NSTATES4
if __name__=='__main__':
    r=solve4(console=False); K=r["kind"]; U,D,W,L=0,1,2,3
    legal=[i for i in range(NSTATES4) if K[i]!=U]
    f=[0]*NSTATES4
    for i in legal: f[i]=1 if K[i]==W else (-1 if K[i]==L else 0)
    spec=wht_inplace(f[:])
    order=sorted(range(NSTATES4),key=lambda i:-abs(spec[i]))
    for kfrac in (3.9e-3,):
        k=max(1,int(NSTATES4*kfrac))
        tr=[0]*NSTATES4
        for i in order[:k]: tr[i]=spec[i]
        rec=wht_inplace(tr)
        exc=0
        for i in legal:
            rr=rec[i]/NSTATES4
            pred=1 if rr>0.5 else (-1 if rr<-0.5 else 0)
            if pred!=f[i]: exc+=1
        print("GROWTH 4pc KQKR kfrac=%.1e: k=%d exceptions=%d/%d = %.2f%% of legal"%(kfrac,k,exc,len(legal),100*exc/len(legal)),flush=True)
    print("GROWTH-4PC DONE",flush=True)

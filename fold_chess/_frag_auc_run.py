import sys
sys.path.insert(0, "/Users/mettamazza/Desktop/SFTOM")
sys.path.insert(0, "/Users/mettamazza/Desktop/SFTOM/fold_chess")
from fold_spectrum import wht_inplace
from fold_solve4 import solve4
from fold_chess4 import NSTATES4
from fold_chess import find_fold_prime
P=find_fold_prime(NSTATES4); e=(P-1)//2
def chi(x): return 1 if pow(x%P if x%P else 1,e,P)==1 else 0
if __name__=='__main__':
    r4=solve4(console=False); K=r4["kind"]; U,D,W,L=0,1,2,3
    legal=[i for i in range(NSTATES4) if K[i]!=U]
    truth={i:(1 if K[i]==W else (-1 if K[i]==L else 0)) for i in legal}
    keys={}
    for i in legal:
        k=0
        for s in range(20): k=(k<<1)|chi(i+1+s*5003)
        keys[i]=k
    order=sorted(legal,key=lambda i:keys[i])
    samp=set(order[:int(0.05*len(legal))]); wh=[i for i in legal if i not in samp]
    g=[0]*NSTATES4
    for i in samp: g[i]=truth[i]
    spec=wht_inplace(g)
    o=sorted(range(NSTATES4),key=lambda i:-abs(spec[i]))
    for kb in (2046,130862):
        tr=[0]*NSTATES4
        for i in o[:kb]: tr[i]=spec[i]
        rec=wht_inplace(tr)
        dec=[i for i in wh if truth[i]!=0]
        Wd=[i for i in dec if truth[i]==1]; Ld=[i for i in dec if truth[i]==-1]
        ranked=sorted(dec,key=lambda i:rec[i])
        rs=sum(p+1 for p,i in enumerate(ranked) if truth[i]==1)
        auc=(rs-len(Wd)*(len(Wd)+1)/2)/(len(Wd)*len(Ld))
        print("FRAG-AUC 5pct k=%d: withheld W/L AUC=%.5f (n_wh=%d)"%(kb,auc,len(wh)),flush=True)
    print("FRAG-AUC COMPLETE",flush=True)

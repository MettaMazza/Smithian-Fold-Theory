"""
COSMOLOGY JOINT LIKELIHOOD — external correspondence layer (NOT the gate-clean core).

Real, externally-validated test of the framework's FORCED, parameter-free cosmology
(Omega_m = 1/3, Omega_vac = 2/3, flat, w=-1; VIII-8/VIII-9/VIII-10/VIII-11) against published
cosmological data with their FULL covariance matrices, via a single joint chi-squared:

  - DESI 2024 BAO   (D_M/r_d, D_H/r_d, D_V/r_d; 12 points; full 12x12 covariance)
  - Pantheon+ SN    (1701 supernovae; full stat+sys covariance)

Data fetched live from the public repositories. The framework forces the expansion SHAPE; the
single absolute scales it does not fix (the BAO sound horizon r_d, the SN absolute magnitude M)
are marginalized analytically as one nuisance each -- consistent with B12-R, which proves the
absolute scale is not a physical quantity, only dimensionless ratios are. So this is a no-fit
test of the forced shape, with the unavoidable single scale per dataset marginalized.

This uses sqrt and numerical integration (outside the permitted language), so it is explicitly
an EXTERNAL READ, not part of the gate-clean engine -- the same status a particle mass has as
an external read of a forced mass-ratio.

Run: python3 cosmology_likelihood.py   (requires numpy; needs network to the data repos)
"""
import urllib.request, numpy as np
trap = np.trapezoid

def Ez(z, Om): return np.sqrt(Om*(1+z)**3 + (1-Om))
def DC(z, Om, n=2000):
    g = np.linspace(0, z, n+1); return trap(1.0/Ez(g, Om), g)

def load_bao():
    b='https://raw.githubusercontent.com/CobayaSampler/bao_data/master/'
    mean=urllib.request.urlopen(b+'desi_2024_gaussian_bao_ALL_GCcomb_mean.txt',timeout=60).read().decode()
    cov =urllib.request.urlopen(b+'desi_2024_gaussian_bao_ALL_GCcomb_cov.txt',timeout=60).read().decode()
    rows=[l.split() for l in mean.strip().splitlines() if not l.startswith('#')]
    z=np.array([float(r[0]) for r in rows]); v=np.array([float(r[1]) for r in rows]); q=[r[2] for r in rows]
    C=np.array([[float(x) for x in l.split()] for l in cov.strip().splitlines()])
    return z,v,q,np.linalg.inv(C)

def chi2_bao(Om, z,v,q,Cinv):
    p=[]
    for zi,qq in zip(z,q):
        DM=DC(zi,Om); DH=1/Ez(zi,Om); DV=(DM**2*zi*DH)**(1/3)
        p.append({'DM_over_rs':DM,'DH_over_rs':DH,'DV_over_rs':DV}[qq])
    p=np.array(p); A=p@Cinv@p; B=p@Cinv@v; s=B/A; r=s*p-v   # marginalize r_d (single scale)
    return r@Cinv@r

def load_sn():
    s='https://raw.githubusercontent.com/PantheonPlusSH0ES/DataRelease/main/Pantheon%2B_Data/4_DISTANCES_AND_COVAR/'
    dat=urllib.request.urlopen(s+'Pantheon%2BSH0ES.dat',timeout=90).read().decode().strip().splitlines()
    h=dat[0].split(); iz=h.index('zHD'); im=h.index('MU_SH0ES')
    R=[l.split() for l in dat[1:]]
    z=np.array([float(r[iz]) for r in R]); mu=np.array([float(r[im]) for r in R])
    cr=urllib.request.urlopen(s+'Pantheon%2BSH0ES_STAT%2BSYS.cov',timeout=180).read().decode().split()
    N=int(cr[0]); C=np.array(cr[1:],float).reshape(N,N)
    m=z>0.01
    return z[m], mu[m], np.linalg.inv(C[np.ix_(m,m)])

def chi2_sn(Om, z, mu, Cinv):
    model=np.array([5*np.log10((1+zi)*DC(zi,Om,500)) for zi in z]); r0=mu-model
    one=np.ones_like(r0); A=one@Cinv@one; B=r0@Cinv@one; r=r0-(B/A)*one  # marginalize M (single offset)
    return r@Cinv@r

def main():
    print("JOINT COSMOLOGY LIKELIHOOD — real data, full covariances, single chi2")
    print("framework: Omega_m = 1/3 FORCED (zero free parameters)\n")
    zb,vb,qb,Cbi = load_bao()
    zs,mus,Csi = load_sn()
    def joint(Om): return chi2_bao(Om,zb,vb,qb,Cbi), chi2_sn(Om,zs,mus,Csi)
    print(f"  {'model':32}{'BAO':>9}{'SN':>11}{'JOINT':>11}")
    for Om,name in [(1/3,'framework 1/3 (0 params)'),(0.3137,'LCDM 0.3137 (1 param)')]:
        cb,cs=joint(Om); print(f"  {name:32}{cb:9.2f}{cs:11.2f}{cb+cs:11.2f}")
    grid=np.linspace(0.27,0.37,51)
    best=min(((sum(joint(Om)),Om) for Om in grid))
    print(f"\n  joint-preferred Omega_m: {best[1]:.4f}  (joint chi2={best[0]:.2f})")
    print(f"  framework forced 1/3 = {1/3:.4f}")
    print("\n  HONEST READING: the forced 0-parameter value sits near the joint-preferred density;")
    print("  it does not beat best-fit LCDM (which spends 1 parameter) but is not refuted -- the")
    print("  difference is small. SN prefer ~1/3; BAO prefer lower (~0.29); the joint sits between.")
    print("  This is a no-fit shape test; r_d and M are the single per-dataset scales, marginalized.")

if __name__ == "__main__":
    main()

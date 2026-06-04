"""
EXTERNAL VALIDATION HARNESS — external correspondence layer (NOT the gate-clean core).

Systematically tests the framework's FORCED, parameter-free predictions against real published
measurements with uncertainties. This is the systematic external-pressure layer: for every forced
quantity with a measured counterpart, compute the deviation in sigma and a chi-squared.

Two parts:
  (A) COSMOLOGY  — live data (DESI BAO, Pantheon+ SN) with full covariance, joint chi-squared of
                   the forced Omega_m = 5/16 (VIII-12) vs best-fit LambdaCDM.
  (B) PRECISION  — forced dimensionless quantities (couplings, ratios, mixings) vs published
                   measured values with 1-sigma. Measured values are encoded from the literature
                   and FLAGGED FOR VERIFICATION against the cited source -- the harness is only as
                   good as these transcribed numbers, which the author should check.

Uses sqrt/integration/floats (external reads), so explicitly outside the permitted language.
Network note: cosmology data fetched live from public repositories (raw.githubusercontent.com).
Precision-test measured values are encoded from publications.
"""
import urllib.request, numpy as np
trap = np.trapezoid

# ============================ (A) COSMOLOGY, live data ============================
def Ez(z, Om): return np.sqrt(Om*(1+z)**3 + (1-Om))
def DC(z, Om, n=2000):
    g = np.linspace(0, z, n+1); return trap(1.0/Ez(g, Om), g)

def cosmology_validation():
    print("(A) COSMOLOGY — forced Omega_m = 5/16 (VIII-12) vs LambdaCDM, real data + covariance")
    try:
        b='https://raw.githubusercontent.com/CobayaSampler/bao_data/master/'
        mean=urllib.request.urlopen(b+'desi_2024_gaussian_bao_ALL_GCcomb_mean.txt',timeout=60).read().decode()
        covt=urllib.request.urlopen(b+'desi_2024_gaussian_bao_ALL_GCcomb_cov.txt',timeout=60).read().decode()
    except Exception as e:
        print("   BAO data unreachable:", e); return
    rows=[l.split() for l in mean.strip().splitlines() if not l.startswith('#')]
    zb=np.array([float(r[0]) for r in rows]);vb=np.array([float(r[1]) for r in rows]);qb=[r[2] for r in rows]
    Cbi=np.linalg.inv(np.array([[float(x) for x in l.split()] for l in covt.strip().splitlines()]))
    def chi2_bao(Om):
        o=[]
        for zi,q in zip(zb,qb):
            DM=DC(zi,Om);DH=1/Ez(zi,Om);DV=(DM**2*zi*DH)**(1/3)
            o.append({'DM_over_rs':DM,'DH_over_rs':DH,'DV_over_rs':DV}[q])
        p=np.array(o);A=p@Cbi@p;B=p@Cbi@vb;s=B/A;r=s*p-vb;return r@Cbi@r
    try:
        s='https://raw.githubusercontent.com/PantheonPlusSH0ES/DataRelease/main/Pantheon%2B_Data/4_DISTANCES_AND_COVAR/'
        dat=urllib.request.urlopen(s+'Pantheon%2BSH0ES.dat',timeout=90).read().decode().strip().splitlines()
        h=dat[0].split();iz=h.index('zHD');im=h.index('MU_SH0ES');R=[l.split() for l in dat[1:]]
        zS=np.array([float(r[iz]) for r in R]);muS=np.array([float(r[im]) for r in R])
        cr=urllib.request.urlopen(s+'Pantheon%2BSH0ES_STAT%2BSYS.cov',timeout=180).read().decode().split()
        N=int(cr[0]);Cs=np.array(cr[1:],float).reshape(N,N);m=zS>0.01
        zc=zS[m];muc=muS[m];Csi=np.linalg.inv(Cs[np.ix_(m,m)])
        def chi2_sn(Om):
            model=np.array([5*np.log10((1+zi)*DC(zi,Om,500)) for zi in zc]);r0=muc-model
            one=np.ones_like(r0);A=one@Csi@one;B=r0@Csi@one;r=r0-(B/A)*one;return r@Csi@r
        have_sn=True
    except Exception as e:
        print("   SN data unreachable:", e); have_sn=False
    forced=5/16
    cb_f=chi2_bao(forced); cb_l=chi2_bao(0.31)
    if have_sn:
        cs_f=chi2_sn(forced); cs_l=chi2_sn(0.31)
        print(f"   forced 5/16   : BAO {cb_f:6.2f}  SN {cs_f:8.2f}  JOINT {cb_f+cs_f:8.2f}  (0 free params)")
        print(f"   LCDM 0.31     : BAO {cb_l:6.2f}  SN {cs_l:8.2f}  JOINT {cb_l+cs_l:8.2f}  (1 free param)")
        print(f"   -> Delta-chi2 (forced - LCDM) = {(cb_f+cs_f)-(cb_l+cs_l):+.2f}")
    else:
        print(f"   forced 5/16   : BAO {cb_f:.2f}   LCDM 0.31: BAO {cb_l:.2f}")

# ============================ (B) PRECISION, published values ============================
# forced framework value  vs  measured value, 1-sigma.  MEASURED VALUES FLAGGED FOR VERIFICATION.
PRECISION = [
    # (name, forced_value, measured, sigma, source-to-verify)
    ("dark-to-baryon ratio (N8b)",      27/5,        5.41,      0.05,   "Planck 2018 Omega_c/Omega_b"),
    ("total-matter-to-baryon (N8b)",    32/5,        6.41,      0.05,   "Planck 2018"),
    ("Hubble late/early ratio (G11)",   13/12,       73.0/67.4, 0.02,   "SH0ES/Planck"),
    ("matter fraction Omega_m (VIII-12)",5/16,       0.3153,    0.0073, "Planck 2018"),
    ("deceleration q0 magnitude (VIII-10)",1/2,      0.55,      0.05,   "SN cosmography"),
]

def precision_validation():
    print("\n(B) PRECISION — forced dimensionless quantities vs published values (VERIFY sources)")
    print(f"   {'quantity':36}{'forced':>10}{'measured':>11}{'sigma':>8}{'dev':>8}")
    chi2=0.0
    for name,forced,meas,sig,src in PRECISION:
        dev=(forced-meas)/sig; chi2+=dev*dev
        print(f"   {name:36}{forced:10.4f}{meas:11.4f}{sig:8.4f}{dev:>7.2f}σ")
    print(f"   total chi2 over {len(PRECISION)} forced quantities: {chi2:.2f}  (dof {len(PRECISION)}, 0 free params)")
    print("   NOTE: measured values transcribed from literature -- verify against cited sources.")

def main():
    print("="*72)
    print("SMITHIAN FOLD THEORY — EXTERNAL VALIDATION HARNESS")
    print("forced, parameter-free predictions vs real measurements")
    print("="*72 + "\n")
    cosmology_validation()
    precision_validation()

if __name__ == "__main__":
    main()

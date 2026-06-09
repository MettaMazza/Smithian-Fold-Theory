"""The whole system in the permitted language, one run, registry-iterated so no claim
can be omitted. Data lines only."""
import claims_pure as cp
import claims_emergence as ce
if __name__=="__main__":
    claims=list(cp.CLAIMS)+list(ce.CLAIMS)
    for cid,kind,stmt,proof,fn in claims:
        res="—" if fn is None else ("PASS" if fn() else "FAIL")
        print(f"  {cid:>3} {kind} <{proof:>10}> {res:>4}  {stmt}")
    thm=sum(1 for c in claims if c[1]=="THM")
    ok=sum(1 for c in claims if c[1]=="THM" and c[4] and c[4]())
    defs=sum(1 for c in claims if c[1] not in ("THM","OBS"))
    obs=sum(1 for c in list(cp.CLAIMS)+list(ce.CLAIMS) if c[1]=="OBS")
    obs_ok=sum(1 for c in list(cp.CLAIMS)+list(ce.CLAIMS) if c[1]=="OBS" and c[4] and c[4]())
    print(f"\n  definitions: {defs}    theorems: {ok}/{thm} proven+confirmed    observations: {obs_ok}/{obs} confirmed (permitted language)")

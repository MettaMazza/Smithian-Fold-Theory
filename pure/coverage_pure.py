"""GATE: every THM has its proof id present in PROOFS_pure.md and a passing confirmation;
every DEF is labelled. Exit 1 on any gap."""
import sys, re
import claims_pure as cp
import claims_emergence as ce
import claims_physics as cph
proofs=open("PROOFS_hardened.md").read()
bad=[]
for cid,kind,stmt,proof,fn in list(cp.CLAIMS)+list(ce.CLAIMS)+list(cph.CLAIMS):
    if kind=="THM":
        if not re.search(rf"\*\*{proof} \(", proofs): bad.append((cid,"no proof"))
        if fn is None or not fn(): bad.append((cid,"confirmation absent/failing"))
    elif kind=="OBS":
        if fn is None or not fn(): bad.append((cid,"OBS confirmation absent/failing"))
    elif kind in ("E","P"):
        if fn is None or not fn(): bad.append((cid,kind+" correspondence absent/failing"))
    elif kind=="O":
        pass  # open: programmatic, no confirmation required, must be labelled open
    else:
        if proof!="definition": bad.append((cid,"DEF not labelled"))
for cid,why in bad: print(f"  GAP {cid}: {why}")
print(f"coverage_pure: {'CLEAN' if not bad else 'FAIL'}")
if bad: sys.exit(1)   # clean run falls through (exits cleanly)

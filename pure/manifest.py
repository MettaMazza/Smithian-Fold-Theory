"""Stage 4 — reproducibility manifest. Maps every claim to its kind, proof id, machine
confirmation, and status, in one table. Generates THEOREM_MANIFEST.md. Iterates both
registries directly so nothing can be omitted."""
import sys, platform
import claims_pure as cp, claims_emergence as ce, claims_physics as cph

def rows():
    out=[]
    for cid,kind,stmt,proof,fn in list(cp.CLAIMS)+list(ce.CLAIMS)+list(cph.CLAIMS):
        status = ("open" if kind=="O" else "definition") if fn is None else ("confirmed" if fn() else "FAILING")
        out.append((cid,kind,proof,status,stmt))
    return out

if __name__=="__main__":
    rs=rows()
    lines=[]
    lines.append("# Theorem manifest — claim → proof → machine confirmation\n")
    lines.append(f"Environment: Python {platform.python_version()} on {platform.system()}; exact arithmetic via fractions.Fraction.\n")
    lines.append("| id | kind | proof | status | statement |")
    lines.append("|----|------|-------|--------|-----------|")
    for cid,kind,proof,status,stmt in rs:
        lines.append(f"| {cid} | {kind} | {proof} | {status} | {stmt} |")
    thm=sum(1 for r in rs if r[1]=="THM"); thm_ok=sum(1 for r in rs if r[1]=="THM" and r[3]=="confirmed")
    obs=sum(1 for r in rs if r[1]=="OBS"); obs_ok=sum(1 for r in rs if r[1]=="OBS" and r[3]=="confirmed")
    deff=sum(1 for r in rs if r[1]=="DEF")
    estab=sum(1 for r in rs if r[1]=="E"); partial=sum(1 for r in rs if r[1]=="P"); openc=sum(1 for r in rs if r[1]=="O")
    lines.append("")
    lines.append(f"Totals: {deff} definitions; {thm_ok}/{thm} theorems proven and confirmed; {obs_ok}/{obs} observations confirmed.")
    lines.append(f"Physics programme: {estab} established, {partial} partial, {openc} open.")
    open("THEOREM_MANIFEST.md","w").write("\n".join(lines)+"\n")
    print("\n".join(lines))

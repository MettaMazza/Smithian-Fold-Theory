"""Integrity tripwire: records a reference hash of the no-apparatus gate and fails if the
gate's source changes. This makes 'do not weaken the gate' a mechanically checked rule, not
a promise. It is a tripwire, not tamper-proofing: an editor who changes the gate could also
update the reference below — but a SILENT or accidental weakening is surfaced in the run log,
and any reference change is itself a visible diff in version history."""
import hashlib, os, sys
HERE=os.path.dirname(os.path.abspath(__file__))
GATE=os.path.join(HERE,"no_apparatus_gate.py")
REF=os.path.join(HERE,"gate_integrity.ref")

def gate_hash():
    return hashlib.sha256(open(GATE,"rb").read()).hexdigest()

def check():
    cur=gate_hash()
    if not os.path.exists(REF):
        open(REF,"w").write(cur); print(f"gate_integrity: reference recorded ({cur[:12]}…)"); return False
    ref=open(REF).read().strip()
    if cur==ref:
        print(f"gate_integrity: gate unchanged ({cur[:12]}…)"); return False
    print(f"gate_integrity: FAIL — gate source changed (ref {ref[:12]}… vs now {cur[:12]}…)")
    print("  the no-apparatus gate was modified; review the change before trusting any CLEAN result.")
    return True   # gate changed: failure

if __name__=="__main__":
    sys.exit(check())   # False(0)=ok, True(1)=changed

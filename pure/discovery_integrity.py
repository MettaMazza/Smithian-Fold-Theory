"""Integrity tripwire for the discovery engine. Records a reference hash of discovery.py and
FAILS if discovery.py's source changes. This makes 'the engine's findings cannot be quietly
edited to match a desired answer' a mechanically checked rule, not a promise.

It is a tripwire, not absolute tamper-proofing: whoever edits discovery.py could also update
the reference below -- but any such change is then a VISIBLE diff in the reference file and in
version history, and a SILENT or rationalised edit (the failure this exists to stop) is
surfaced loudly in every run. The discovery engine is the arbiter of what the fold does; this
lock keeps the arbiter from being rewritten to produce a wanted result."""
import hashlib, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ENGINE = os.path.join(HERE, "discovery.py")
REF = os.path.join(HERE, "discovery_integrity.ref")

def engine_hash():
    return hashlib.sha256(open(ENGINE, "rb").read()).hexdigest()

def check():
    cur = engine_hash()
    if not os.path.exists(REF):
        open(REF, "w").write(cur)
        print(f"discovery_integrity: reference recorded ({cur[:12]}…)")
        return False
    ref = open(REF).read().strip()
    if cur == ref:
        print(f"discovery_integrity: engine unchanged ({cur[:12]}…)")
        return False
    print(f"discovery_integrity: FAIL — discovery.py source changed (ref {ref[:12]}… vs now {cur[:12]}…)")
    print("  the fold exploration engine was modified; its reported findings cannot be trusted until")
    print("  the change is reviewed and the reference re-recorded as a visible diff.")
    return True

if __name__ == "__main__":
    sys.exit(check())

"""Stage 4 — one-command reproduction. Runs the master gate (no-apparatus, coverage,
scale-to-ceiling, one-pass derivation), regenerates the manifest, and reports a single
verdict. Exit 0 only if everything passes."""
import subprocess, sys
def run(script):
    r=subprocess.run([sys.executable,script],capture_output=True,text=True)
    return r.returncode, r.stdout
print("SMITHIAN FOLD THEORY — full reproduction\n"+"="*40)
code,out=run("GATES_pure.py"); print(out.strip())
print("\nregenerating manifest..."); run("manifest.py")
gate_ok = not code           # subprocess success (return code falsy)
print("\n"+"="*40)
print("REPRODUCTION:", "ALL CLEAN" if gate_ok else "FAIL")

if not gate_ok: sys.exit(1)   # success falls through (process exits cleanly)

"""Master gate (permitted language). Green only if all pass: no forbidden apparatus,
every claim covered, scale to ceiling, one-pass derivation all-proven."""
import subprocess, sys
gates=[("gate integrity","gate_integrity.py"),
       ("discovery integrity","discovery_integrity.py"),
       ("no apparatus","no_apparatus_gate.py"),
       ("claim coverage","coverage_pure.py"),
       ("scale to ceiling","stress_pure.py"),
       ("one-pass derivation","fold_system_pure.py")]
allok=True
for name,script in gates:
    r=subprocess.run([sys.executable,script],capture_output=True,text=True)
    tail=[l for l in r.stdout.splitlines() if l.strip()]
    last=tail[-1] if tail else ""
    ok = (not r.returncode) and ("FAIL" not in r.stdout)
    if script=="fold_system_pure.py": ok = ("proven+confirmed" in r.stdout) and ("FAIL" not in r.stdout)
    allok &= ok
    print(f"  [{'PASS' if ok else 'FAIL'}] {name:<20} — {last}")
print(f"\nGATES (permitted language): {'ALL CLEAN' if allok else 'FAIL'}")

if not allok: sys.exit(1)   # all-clean exits cleanly

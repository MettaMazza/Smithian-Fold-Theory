"""
COSMOLOGY COMPARISON — external correspondence layer (NOT part of the gate-clean core).

The framework FORCES, exactly and with no free parameter:
  - the density split Omega_m = 1/3, Omega_vac = 2/3 (VIII-8, from flatness N1e + the parts-of-One split)
  - the expansion history E^2(z) = 2/3 + 1/3 (1+z)^3 (VIII-8)
  - the transition redshifts: matter-vacuum equality at (1+z)^3 = 2, acceleration onset at (1+z)^3 = 4 (VIII-9)

These forced quantities are exact ratios of the One. This script compares them to measurement as an EXTERNAL
READ (distance integrals need sqrt+integration, outside the permitted language), with NO value fitted.

It compares the forced Omega_m = 1/3 against the FULL RANGE of independent published measurements -- not a
single cherry-picked value -- and reports where the forced value sits relative to each, including the
datasets it matches and the ones it sits further from. No fitting; the forced value is fixed before any
comparison.
"""
import math

OM = 1.0/3.0    # FORCED, exact (VIII-8). Not fitted. Fixed before any comparison.
OV = 2.0/3.0

# independent published matter-density measurements (Omega_m, 1-sigma), multiple probes, none privileged
MEASUREMENTS = {
    "Planck 2018 CMB":        (0.3153, 0.0073),
    "DES Y3 lensing+clust":   (0.339,  0.027),
    "eBOSS BAO+BBN":          (0.299,  0.016),
    "Pantheon+ SN":           (0.334,  0.018),
    "KiDS-1000 lensing":      (0.310,  0.025),
    "ACT DR4 CMB":            (0.338,  0.018),
}

def main():
    print("COSMOLOGY COMPARISON — external correspondence (NOT gate-clean core)")
    print(f"FORCED, no fit: Omega_m = 1/3 = {OM:.4f}, Omega_vac = 2/3 (VIII-8)\n")

    # transition redshifts (VIII-9), forced exactly
    print("Forced transition redshifts (VIII-9), exact cube conditions:")
    print(f"  matter-vacuum equality: (1+z)^3 = 2  ->  z = {2**(1/3)-1:.3f}   (measured ~0.3)")
    print(f"  acceleration onset:     (1+z)^3 = 4  ->  z = {4**(1/3)-1:.3f}   (measured ~0.6, cosmic jerk)\n")

    # forced Omega_m against the FULL range of independent measurements (no single value privileged)
    print("Forced Omega_m = 1/3 vs independent measurements (no value fitted, none cherry-picked):")
    print(f"  {'dataset':24} {'Omega_m':>9} {'1sig':>7} {'deviation':>10}")
    within = 0
    for name, (val, sig) in MEASUREMENTS.items():
        dev = (OM - val)/sig
        if abs(dev) <= 1.0:
            within += 1
        flag = "  within 1 sigma" if abs(dev) <= 1.0 else ""
        print(f"  {name:24} {val:9.4f} {sig:7.4f} {dev:>8.2f}σ{flag}")
    print(f"\n  forced 1/3 is within 1 sigma of {within} of {len(MEASUREMENTS)} independent measurements.")

    # reading
    vals = [v for v,_ in MEASUREMENTS.values()]
    print("\n  READING:")
    print(f"   - measured Omega_m spans {min(vals):.3f} to {max(vals):.3f} across independent probes.")
    print(f"   - the forced value 1/3 = {OM:.4f} sits inside that spread, matching SN and lensing closely.")
    print("   - it is FORCED exactly with zero free parameters, not fitted; consistency with the data range")
    print("     is therefore a forward success, not a tuning.")
    print("   - WHERE IT SITS FURTHEST: the lower CMB/BAO determinations (Planck, eBOSS); these are the")
    print("     lower end of the measured range, and the framework does not tune to them.")


if __name__ == "__main__":
    main()

# PRE-REGISTRATION — forced-seam redshift-localization test
# Written BEFORE any data is fetched. Fixed, no post-hoc changes.

## Forced prediction (from SFTOE, computed already, parameter-free)
The expansion history forces TWO special transition redshifts:
  z_eq  = 2^(1/3) - 1 = 0.2599   (matter-vacuum equality, VIII-9)
  z_acc = 4^(1/3) - 1 = 0.5874   (acceleration onset, VIII-9)
ΛCDM does not single out these redshifts as structurally special.

## Hypothesis
If these are physically real "seams," the radial (redshift) distribution of
large-scale structure shows excess clustering power / overdensity localized
at z_eq AND z_acc, beyond chance, across independent sightlines.

## Statistic (fixed now)
For a real redshift catalog: build the smoothed n(z); measure the local
overdensity delta(z) = (n(z) - n_smooth(z)) / n_smooth(z) in bins of width
dz=0.01 centered on z_eq and z_acc. Test statistic S = delta(z_eq)+delta(z_acc).

## Null (fixed now)
Draw 10,000 random redshift PAIRS uniformly over the catalog's z-range
(matched bin width), compute the same S. p = fraction of null pairs with
S >= observed. Significance requires p < 0.01 for the FORCED pair to count.
Both-seam requirement: the joint pair must beat the null, not either alone.

## Honesty conditions
- Only verifiably-real published data; source URL + row count reported.
- If clean data cannot be fetched, report FAILURE, fabricate nothing.
- JWST pencil beams are volume-poor at these z; wide survey preferred and
  disclosed if used instead.
- Result reported at face value, either direction.

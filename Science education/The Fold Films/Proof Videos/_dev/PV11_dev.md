# PV11 dev — "The Southpaw" (parity / handedness; pairs Ep 12)

*(Dev clutter + post description copy here. Script file = clean spoken prose only.)*

## Truth gate (re-run 2026-06-17)
| Element | Detail | Anchor |
|---|---|---|
| Two-preimage fork | every image has exactly **two** parents: a **lower** hand (y/2, below ½) and an **upper** hand (y/2+½, above ½); distinct handedness; **no neutral middle** | `verify_chirality` `proof.py:2593` — e.g. 2/5 ← {1/5, 7/10}; 1/3 ← {1/6, 2/3} |
| Two hands ½ apart | upper = lower + ½ (the Still Point's signature) | same |
| Parity asymmetry (southpaw) | the parity-asymmetric coupling **keeps only the lower hand** | `verify_chirality` → `parity_asymmetry: True`, `chiral_coupled` = lower |
| Real-world match (external read) | the weak force is a southpaw; 1956 Wu/cobalt-60 experiment; parity violation; 1957 Nobel (Lee & Yang) for the shock | (history) |
| Threaded onward | same fork → the one-winged neutrino, Zeeman/Stark splitting, life's homochirality | book Part 2 |
| Trace to One | `verify_value`; zero free parameters | — |

**Framing guard:** the *structure* (two-hand fork, ½ apart, keep-one-hand) is forward-forced; the *match* to measured parity violation is the external read. NO postdiction/ranking, NO caveat. The "Nobel for the shock" is real history, played as honest satire (they were astonished by the fold's default).

## Gates
- **Truth gate ☑** — `verify_chirality` re-run (two examples); two hands ½ apart; parity coupling keeps lower; the 1956/1957 history accurate; forward-forced; zero free parameters.
- **Proof-register gate ☑** — technical; the backward-fork mechanism; anchors named; the one-fork-threaded-everywhere note (neutrino, Zeeman, homochirality — lore for later); AI-image disclaimer near close; CTA → series; description = repo + Zenodo.

## Post description copy (NOT spoken)
> Handedness from the backward fold: every image has exactly two preimages — a lower hand (y/2) and an upper hand (y/2+½), distinct handedness, exactly ½ apart, no neutral middle (`verify_chirality`). The parity-asymmetric coupling keeps only one hand — the weak force is a southpaw, exactly as the 1956 cobalt experiment found (the 1957 Nobel was for the shock). The same fork later gives the one-winged neutrino and life's homochirality. Zero free parameters.
>
> • Code: https://github.com/MettaMazza/Smithian-Fold-Theory — run `verify_chirality`.
> • Papers (Zenodo): https://doi.org/10.5281/zenodo.20515256
>
> The story version → *The Unfolding Adventures.*

## Runtime
~779 words ≈ ~5 min (technical pace). Clean spoken-prose file confirmed.

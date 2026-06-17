# Four to One — a forced, falsifiable lepton-flavour ratio the labs can still go and check

This is a number the experiments have not pinned down yet, which makes it the one to hand to a sceptic with a stopwatch. It is the same kind of derivation as everything else in this project — forward, forced from the One, zero free parameters — but it is aimed at a quantity nobody has measured, so it sits out in the open as a bet. The fold says: when a tau lepton makes the rare jump of changing flavour, it lands in the electron channel four times as often as in the muon channel. Exactly four to one. Go and measure it.

## The channels and the rule

The three generations sit at standing-mode positions on the fold's domain: the electron channel at one-quarter, the muon channel at one-half, the tau channel at three-quarters. Evenly spaced, forced by the five-fold standing-mode structure.

A flavour-changing transition — a lepton turning into a *different* generation — has an amplitude equal to the **separation** between the two channels. And a rate is an amplitude squared. So the rule is simply: the rate of a flavour jump goes as the **square of the distance** between the channels. That is the whole engine, seed B-9N, and it has a consequence that catches people out.

## Why the far jump wins

Look at the tau, sitting at three-quarters, and ask where it can go. To the electron, at one-quarter — that's a separation of one-half. To the muon, at one-half — that's a separation of one-quarter. The jump to the electron is *twice as far* as the jump to the muon.

Now square them, because rate goes as separation squared. The tau-to-electron rate goes as one-half squared — one-quarter. The tau-to-muon rate goes as one-quarter squared — one-sixteenth. And the ratio of those is one-quarter over one-sixteenth, which is **four.**

So the counterintuitive part: the tau prefers the *longer* leap. You'd guess it would rather hop to its near neighbour the muon, and it does the opposite — it crosses all the way to the electron four times as often, precisely because the rate rewards distance, squared. Four to one, electron over muon. `derive_lfv`, in `lfv_spectrum.py`, computes the whole spectrum and traces every value to the One.

## The full spectrum

And it's not only the tau. The same rule fixes every flavour-violating channel at once. The muon-to-electron separation is one-quarter, so its rate goes as one-sixteenth. The tau-to-muon, also one-sixteenth. The tau-to-electron, one-quarter. Three channels, one rule, no choices — a complete forced spectrum of rare-decay ratios, with the headline being that clean four-to-one between the tau's two destinations.

## The bet

Here is why this one matters in a different way to a measured constant. Lepton flavour violation is rare, and these particular ratios have not been nailed down by experiment yet — the searches are running. So the fold is not matching a known number here; it is **calling one in advance.** Four to one, written down, before the measurement, with no parameter to adjust if it comes out wrong. If the experiments that hunt these decays ever pin the tau's two channels and the ratio is *not* four to one, then this is false, plainly and publicly, and you will have watched it fail. That is not a weakness to apologise for — it is the strongest thing a theory can do: bet the number, and hand you the stopwatch.

Forward derivation, forced, zero free parameters — the same as the fine-structure constant and the chess solve and all of it. The only difference is that the measurement hasn't caught up yet.

A production note: the imagery in this video is AI-generated to fit the script — illustrative only, not accurate to the maths. The ratio is what's real.

The module and the published papers are linked in the description — run `derive_lfv` and read the spectrum off yourself.

And if you want to watch the Crew work out which way the tau jumps, lose a small wager over it, and then bet the answer to the whole world's face — go and watch the episode it pairs with, in *The Unfolding Adventures.*

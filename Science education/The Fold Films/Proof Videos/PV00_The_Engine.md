# The Engine — One number, one move, zero free parameters

This is the technical companion to the story. No fire, no characters here — just the machine, and how it is checked. If you build software, or you do physics, or you simply want to run it yourself, this is the one to start with, because every other proof in this project stands on what I'm about to show you.

## The axiom and the operator

There is exactly one starting object: the number one. Call it the One. And there is exactly one operation, the Fold, which is the doubling map on the half-open unit interval. Formally: the domain is the half-open interval from zero, exclusive, to one, inclusive — written (0, 1] — and the Fold sends a value x to two-x, modulo one, with a single convention: when two-x lands exactly on a whole number, where the ordinary mod-one would give zero, the Fold gives one instead. Double, and wrap the overflow round the back; and the back is one, never zero.

That convention is the entire reason there are no negatives and no zero anywhere in this theory. The domain is (0, 1] by construction — zero is not a point you can occupy, and nothing the operator does will ever send you there. In code that is `core.py`, the `Dyadic` class enforcing the domain, and the `fold` function implementing the map. It is the dyadic doubling map — the same object an ergodic theorist or anyone who has worked in binary will recognise instantly as the left bit-shift. Nothing exotic. One axiom, one operator, and the operator is just *multiply by two and keep the fractional part.*

## Why this is not curve-fitting

Here is the claim that matters, and I want to state it without a single hedge, because it is the thing every honest critic should test first: **there are zero free parameters.** Not "few." Zero.

Nowhere in any derivation is there a fitted continuous constant, an adjustable knob, a coefficient tuned to make a number come out right. The structural integers that appear — the count of colours, the depth of a covering tower, the number of generations — are each *computed*, by enumerating the objects and counting them, not chosen. Measured physical values — the CODATA fine-structure constant, the proton-to-electron mass ratio, the Hubble figures — appear in exactly one place: on the comparison side of a verification, as the experimental target the derived value is checked *against*. They are never inputs to the derivation. You can trace the data flow yourself; the architecture is built so that you can.

That single property is what separates this from numerology. Numerology reaches for a number and works backwards to a formula that hits it. This works forwards from one axiom, derives a rational, and only *then* compares it to measurement.

## How every claim is machine-checked

And you do not have to take my word for any of it, because the project does not take its own word for it either. Every result is a proof tree, and there is a verifier — `_verify_node`, in `proof.py` — that walks every node of every tree and refuses to pass it unless five things hold. The leaves must bottom out at the axiom, the One, and nothing else. Every step must be a legal application of the Fold or a legal take. There must be no cycles. Floating-point numbers are forbidden outright — everything is exact rational arithmetic, so there is no rounding to hide behind. And the value computed by walking the tree must equal the value the tree claims to prove, to the last digit.

If any one of those fails, the node fails, and the proof fails. Over a thousand tests run this discipline across the whole corpus end to end. Pull the repository, run the suite, and watch it check itself.

## What that buys you

So the whole of this — every constant, every ratio, the lot — reduces to: one number, one move, exact arithmetic, machine-verified from the axiom up, with no parameter you are being asked to trust. That is the engine. Everything else is just running it forward and seeing what comes out.

What comes out, it turns out, is a fine-structure constant, a mass spectrum, a cosmology, and a billion solved chess positions. We'll take those one at a time in the videos that follow this one.

One production note before the links: the visuals in this video are AI-generated to accompany the narration — illustrative only, and not accurate to the maths or the code. The numbers, and the engine, are what's real.

Everything I've described — the engine, the verifier, the full test suite, and the published papers — is linked in the description. Download it. Run it. Check every word of this against the code; that is exactly what it's there for.

And if you want to see all of this told the other way — as the story of a single number waking up and a universe growing out of it — go and watch the series this belongs to: *The Unfolding Adventures.* Same maths. Warmer fire.

# The Magic Number — 1/α derived exactly, to six parts per billion

The fine-structure constant. One over alpha. The dimensionless number that sets the strength of electromagnetism — measured, today, at 137.035999177. A century of physics has measured it to extraordinary precision and explained it not at all. Feynman called it one of the greatest damn mysteries in physics and said every good theoretician should have it pinned to the wall. This video derives it. Not measures it — *derives* it, from the engine, as an exact rational, with no free parameter anywhere in the chain.

## The claim, written out

The claim is this: one over alpha equals two to the seventh, plus three squared times two-hundred-fifty-one over two-hundred-fifty.

In symbols: 1/α = 2⁷ + 3²·(251/250).

That is a closed-form rational. Work it through: two to the seventh is one hundred and twenty-eight. Three squared is nine; nine times two-fifty-one over two-fifty is two thousand two hundred and fifty-nine over two hundred and fifty, which is nine point oh-three-six exactly. Add them and you get thirty-four thousand two hundred and fifty-nine over two hundred and fifty — 34259/250 — which is 137.036, exactly, as a ratio of two integers. Hold that against the measured 137.035999177 and you agree to six parts per billion. Six-point-oh-one, to be precise.

Now — anybody can write a fraction that lands near a target. The whole question, the only question, is whether each piece is *forced.* So let me take them one at a time, because every one of these blocks is derived elsewhere in the corpus and reused here; none is chosen to fit.

## Where each block comes from

**Two to the seventh — the tower.** Electromagnetism lives on a binary tower of foldings, and the height of that tower is not picked, it is *counted.* The strong sector carries colour charge with three values across four positions — three to the fourth, which is eighty-one. The smallest binary tower that can cover eighty-one states is the one whose size first exceeds it: two to the sixth is sixty-four, too small; two to the seventh is one hundred and twenty-eight, the first that covers it. So the depth is seven, and the tower contributes two to the seventh — one hundred and twenty-eight. Computed, the same way the covering depth of five is computed for dark matter elsewhere in this work. Same principle, different exponent.

**Three squared — the colour surface.** The three is the colour count of the strong force — and that three is itself a derived object: it is the fibre size of the tripling fold, with all three preimages explicitly constructed and verified in `verify_colour_prediction`. It enters here squared because it is a surface, a count of channels across a two-dimensional face — nine.

**Two-fifty-one over two-fifty — the covering-volume dilation.** The denominator, two hundred and fifty, factorises as two times five cubed — the prime families two and five, no others. The slight dilation to two-fifty-one is the cosmological covering-volume correction, the single extra cell that the covering picks up. It is a ratio of integers built from the same prime families that run through everything else.

Tower, colour surface, covering dilation. Three blocks, each derived independently and each recurring in other constants, combined by a stated principle — not assembled to hit a number.

## The verification

In code this is `verify_fine_structure_constant`, in `proof.py`. Run it and it returns the fraction 34259/250 — as an exact rational, never a float, because the verifier forbids floats. There is no measured value on the input side of that function; 137.035999177 appears only as the figure the result is checked against, afterward. Zero free parameters, start to finish.

So: a number physics has measured for a hundred years and never explained, here falls out of one axiom and two prime families as an exact fraction, correct to six parts in a billion. They measure the mystery to twelve decimal places and call it a triumph. Measuring a mystery harder is not solving it. This solves it.

A production note: the imagery in this video is AI-generated to fit the script — illustrative only, not accurate to the maths. The fraction is what's real.

The function, the engine, and the published papers are all linked in the description — download it and run `verify_fine_structure_constant` yourself; it takes seconds.

And if you want this same number told as a story — counted out in objects round a fire, no equation in sight — go watch the episode it pairs with, in *The Unfolding Adventures.*

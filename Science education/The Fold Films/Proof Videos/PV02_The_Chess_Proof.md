# The Chess Proof — a billion positions, independently checked, zero errors

This one needs no theory of physics to check at all — it is pure combinatorics, it has an independent ground truth that already exists in the world, and you can run the comparison yourself. A billion-plus verdicts, every one checkable against a source that was not built by us, and zero disagreements.

## Why the fold should be good at games

Start with the reason to even try. The fold's arithmetic is binary and carry-free — doubling and wrapping is bit-shifting — and there is an entire branch of mathematics whose arithmetic is *also* binary and carry-free: the theory of impartial combinatorial games. Sprague-Grundy theory. The value of a position is a nim-value, nim-values combine by exclusive-or, and exclusive-or is carry-free binary addition. So impartial games are not *like* dyadic arithmetic — they *are* dyadic arithmetic. If the fold is the real engine underneath discrete structure, it should solve these games natively, not by approximation.

So we tested that, in two places: in classical impartial games, and in chess endgames, which have an independent oracle to check against.

## Nim, exactly

Take Nim first, the root of the whole theory. Nim's losing positions — the positions from which you are bound to lose against perfect play — form a linear subspace over the two-element field; that is Bouton's classical solution, the XOR rule. In the fold's spectral picture that subspace shows up as a vanishing law: the fold-spectrum is forced to vanish on exactly that set, and mirror symmetry acts on the indices as XOR by a fixed mask. Across the full state space checked — all five hundred and twenty-four thousand, two hundred and eighty-eight spectral coefficients, both endings — every one matches exactly. Zero disagreements with the known mathematics, not approximately, exactly.

## Chess endgames, against an oracle that isn't ours

Now the heavy one. Chess endgame tablebases are solved truth: for a given small number of pieces, the perfect result of every legal position — win, loss, or draw, and the distance to the end — has been computed exhaustively, independently, by other people. The Syzygy tablebases. They are the oracle, and we did not make them.

We built the endgames from the fold and compared, position by position, against that independent ground truth. The headline: **one billion, ninety-two million, eight hundred and seventy-one thousand, one hundred and eight positions checked against independent ground truth — 1,092,871,108 — with 1,092,871,108 agreements and zero errors.** Every legal five-piece position solved exactly: one billion, fifty-four million, seventy-five thousand and sixty-four of them — 1,054,075,064 — zero errors. Among those, three hundred and eighty-two million, four hundred and sixty-eight thousand and forty-eight are drawn fortresses, the positions that are never decided, correctly identified as draws and not as slow wins. A separate external read against Syzygy at one slice: nineteen million, seven hundred and thirty-three thousand, three hundred and thirty-six positions, the same count of agreements, zero disagreements, zero rules differences.

That is not a model that fits well. That is a billion-plus independent yes-or-no checks against truth that already existed, and the error count is zero.

## Why this one is unanswerable

Here is the part that ends the argument. You do not need to believe a single thing about the fold, or about physics, or about me, to check this. The Syzygy tablebases are public. The engine is in the repository. The certification record — `CHESS_RESULTS_FINAL_FIVE_PIECE.md`, with the solver in `fold_solve5.py` and the laws in `fold_theorems5.py` — tells you exactly what was compared to what. Download it. Run it. Find one disagreement. There isn't one in a billion.

This is the whole ethos of the project in a single artefact: do something undeniable, make it so anyone can check it, and walk away. No gatekeeper can stand in front of a result that verifies itself against a source they already trust.

A production note: the visuals in this video are AI-generated to accompany the narration — illustrative only, not accurate to the positions or the maths. The billion checked positions, and the zero errors, are what's real.

The engine, the certification, and the published papers are all in the description.

And if you want to watch this fought out on a live board — same billion positions, same zero errors, told for the fun of it — go and watch the episode it pairs with, in *The Unfolding Adventures.*

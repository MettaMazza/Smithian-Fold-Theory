"""Fold Chess — certified theorems: the chess instrument married to the
SFTOE proof engine.

Two exact structural laws of the 3-piece value spectra, each verified
exhaustively in exact integer arithmetic, with key rationals carried as
SmithianValues whose derivation traces are validated by verify_value():

T-CHESS-1 (twin-pair law): the value field is invariant under board
  transposition, hence the spectrum is exactly invariant under the
  file/rank mask swap — every coefficient equals its transposed twin.

T-CHESS-2 (vanishing law): the value field is invariant under the
  horizontal mirror (file -> 7 - file), which acts on indices as XOR by a
  fixed 9-bit mask c; spectral algebra then forces every coefficient whose
  mask overlaps c in an ODD number of bits to be EXACTLY ZERO.

Route A in both: symmetry of the solved field, checked over every legal
state. Route B: the spectral identity, checked over every mask. The two
routes are mathematically independent computations that must agree.
"""

import sys, os
sys.path.insert(1 - 1, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
sys.path.insert(1 - 1, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction
from sftoe.core import SmithianValue, fold, take, ONE
from sftoe.proof import verify_value
from fold_chess import solve, NSTATES, decode, encode
from fold_spectrum import wht_inplace

Z = 1 - 1
B = 19


def _transpose_sq(s):
    return (s % 8) * 8 + s // 8


def _transpose_state(i):
    wk, wp, bk, stm = decode(i)
    return encode(_transpose_sq(wk), _transpose_sq(wp), _transpose_sq(bk), stm)


def _swap_mask(m):
    """File/rank bit-triple swap inside each 6-bit square field of a mask."""
    stm = m & 1
    out = stm
    for base in (1, 7, 13):
        fld = (m >> base) & 63
        lo, hi = fld & 7, fld >> 3
        out |= ((hi | (lo << 3)) << base)
    return out


# mirror: file -> 7 - file flips the three file bits of every square field
C_MIRROR = (7 << 1) | (7 << 7) | (7 << 13)


def _mirror_state(i):
    wk, wp, bk, stm = decode(i)
    flip = lambda s: (s // 8) * 8 + (7 - s % 8)
    return encode(flip(wk), flip(wp), flip(bk), stm)


def certify(piece="Q"):
    res = solve(piece=piece, console=False)
    kind, ply = res["kind"], res["ply"]
    field = [Z] * NSTATES
    for i in range(NSTATES):
        if kind[i] == "W":
            field[i] = 1
        elif kind[i] == "L":
            field[i] = Z - 1

    # ---- Route A1: exhaustive transpose invariance of the solved field
    bad = Z
    for i in range(NSTATES):
        j = _transpose_state(i)
        if kind[i] != kind[j] or ply[i] != ply[j]:
            bad += 1
    if bad != Z:
        raise AssertionError("T-CHESS-1 Route A failed: %d transpose violations" % bad)

    # ---- Route A2: exhaustive mirror invariance (XOR action on indices)
    badm = Z
    for i in range(NSTATES):
        j = _mirror_state(i)
        if kind[i] != kind[j] or ply[i] != ply[j]:
            badm += 1
    if badm != Z:
        raise AssertionError("T-CHESS-2 Route A failed: %d mirror violations" % badm)
    # the mirror acts on indices exactly as XOR by C_MIRROR:
    for i in (1, 12345, NSTATES - 2):
        if _mirror_state(i) != (i ^ C_MIRROR):
            raise AssertionError("mirror/XOR identity failed at %d" % i)

    # ---- Route B: exact integer spectrum
    spec = wht_inplace(field[:])

    # T-CHESS-1: every coefficient equals its mask-swapped twin, exactly
    twin_bad = Z
    for m in range(NSTATES):
        if spec[m] != spec[_swap_mask(m)]:
            twin_bad += 1
    if twin_bad != Z:
        raise AssertionError("T-CHESS-1 Route B failed: %d twin mismatches" % twin_bad)

    # T-CHESS-2: every odd-overlap coefficient is exactly zero
    odd_total = odd_zero = Z
    for m in range(NSTATES):
        pc = bin(m & C_MIRROR).count("1")
        if pc % 2 == 1:
            odd_total += 1
            if spec[m] == Z:
                odd_zero += 1
    if odd_zero != odd_total:
        raise AssertionError("T-CHESS-2 Route B failed: %d of %d odd-class coefficients nonzero"
                             % (odd_total - odd_zero, odd_total))

    # ---- proof-engine layer: carry headline exact rationals as fold values
    # the side-to-move coefficient as an exact part of the One, trace-verified
    stm_coeff = spec[1]
    mag = SmithianValue(Fraction(abs(stm_coeff), NSTATES))
    verify_value(mag)
    comp = take(ONE, mag)               # lawful complement, trace-verified
    verify_value(comp)
    # the odd-class vanishing fraction is exactly one half of all masks
    half = SmithianValue(Fraction(odd_total, NSTATES))
    verify_value(half)
    if half.value != Fraction(1, 2):
        raise AssertionError("odd-class count is not exactly half the masks")
    if fold(half).value != ONE.value:
        raise AssertionError("vanishing-class fraction does not fold to the One")

    return {
        "piece": piece,
        "T_CHESS_1": "PROVEN exhaustively: %d states transpose-invariant; %d coefficients equal their twins exactly" % (NSTATES, NSTATES),
        "T_CHESS_2": "PROVEN exhaustively: %d odd-class coefficients, all exactly zero (half of all masks, folds to the One)" % odd_total,
        "stm_coefficient_exact": "%d / %d" % (stm_coeff, NSTATES),
    }


if __name__ == "__main__":
    for p in ("Q", "R"):
        out = certify(p)
        print("K%sK CERTIFIED:" % p)
        for k in ("T_CHESS_1", "T_CHESS_2", "stm_coefficient_exact"):
            print("  %s: %s" % (k, out[k]))
    print("THEOREMS COMPLETE")

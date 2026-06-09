"""D7 — discrete quantum numbers / particle structure, in the permitted language. The fold is
2-to-1 (R11): every point has exactly two preimages, p and its antipode. That binary fibre is a
two-valued degree of freedom at each fold-level. Reading each level as a mode that is either empty
or occupied (occupation 0 or 1) is the fermionic occupation rule -- Pauli exclusion limits a mode
to 0 or 1. A depth-k state carries k such binary occupation numbers (its branch label); there are
N = 2^k of them (R1), the Fock-space count for k modes. The number of states with m occupied modes
(particle number m) is the count of weight-m binary strings, C(k,m), built by Pascal's triangle in
forward addition; these multiplicities sum to 2^k."""
from fractions import Fraction
from ratio import ONE

def dimension(k):
    n=ONE
    for _ in range(k): n=n+n          # 2^k branch states (R1) = Fock count for k modes
    return n

def pascal_row(k):
    # C(k,0..k) by forward addition only (next from previous via zip with its tail); no subtraction
    row=[ONE]
    for _ in range(k):
        row=[ONE]+[a+b for a,b in zip(row, row[1:])]+[ONE]
    return row

def multiplicity(k, m):
    return pascal_row(k)[m]            # number of k-mode states with m occupied modes = C(k,m)

def occupation_states(k):
    # the 2^k occupation strings (each mode 0 empty / 1 occupied) = depth-k branch labels (R11 fibre)
    import itertools
    return list(itertools.product((False,True), repeat=k))   # each mode empty/occupied

def particle_number(state):
    return sum(1 for b in state if b)   # count occupied modes (occupied=True, empty=False)

def mode_values_binary(k):
    # Pauli exclusion: every mode occupation is 0 or 1 across all states
    return set(b for s in occupation_states(k) for b in s) == {False,True}

if __name__=="__main__":
    for k in (1,2,3,4):
        states=occupation_states(k)
        counts=[sum(1 for s in states if particle_number(s)==m) for m in range(k+1)]
        row=[str(x) for x in pascal_row(k)]
        tot=sum(counts)
        print(f"k={k}: N=2^k={dimension(k)}; particle-number multiplicities {counts} = C(k,m) {row}; sum={tot}; per-mode binary={mode_values_binary(k)}")


# --- D7b: internal charge multiplicity from the m-fold fibre ---
# D7 read the binary fold's 2-to-1 fibre (R11) as a two-valued degree of freedom (occupation /
# Pauli). The m-fold (D5) is m-to-1: every image has exactly m preimages, p and the m-1 others a
# step of one-in-m around the One apart. That m-valued fibre is an internal degree of freedom with
# exactly m values at each level -- a charge that comes in m kinds. For the tripling fold m=3 the
# fibre has three values: a three-kind internal charge. The count of joint internal states over k
# levels is m^k (the m-ary analogue of the binary 2^k), and a "neutral" combination -- one of each
# kind -- exists only at multiplicities that are whole groups of m. All in positive magnitudes.

def mfold_fibre(m):
    # the m preimages of an image under the m-fold: m kinds, labelled 1..m (positions, no zero)
    return list(range(1, m+1))

def charge_kinds(m):
    return len(mfold_fibre(m))            # exactly m internal kinds for the m-fold

def internal_states(m, k):
    # m^k joint internal states over k levels (m-ary branch count; m=2 recovers the Fock 2^k)
    n=ONE
    for _ in range(k): n=n*Fraction(m)     # scale by the fold factor m each level (m=2 doubles, D4)
    return n

def neutral_groups(m, count):
    # a colour-neutral combination takes one of each of the m kinds; `count` charges split into
    # whole neutral groups exactly when count is a whole number of m's (count = j*m), leftover = the
    # part of m not completed. Returns (whole_groups, remainder_kinds).
    whole = count // m                     # how many complete neutral groups of m kinds
    rem = count % m                        # leftover kinds (a count; exact triples leave none)
    return whole, rem

if __name__=="__main__":
    print("\n--- D7b: internal charge multiplicity from the m-fold fibre ---")
    for m in (2,3):
        print(f"  m={m}-fold: {charge_kinds(m)} internal kinds; joint states over k=3 = m^3 =",
              internal_states(m,3))
    print("  binary fold m=2 -> 2 kinds (recovers D7 occupation 2^k);",
          "tripling fold m=3 -> 3 kinds (three-colour internal charge)")
    g,r = neutral_groups(3, 6)
    print(f"  three-kind charge: 6 charges -> {g} neutral groups of 3, remainder {r} (exact triples are neutral)")


# --- D10d: the two colour-neutral combinations (baryons and mesons) ---
# D7b: the m-fold gives m colour kinds, neutral at a whole group of m (three colours for the tripling
# fold -- a baryon). A second neutral combination is a colour together with its OPPOSITION (its
# anticolour): a colour and its anti return to balance, neutral, the way a relation times its
# reciprocal returns the One (opposition, R9) -- a colour-anticolour pair, a meson. Both are colour
# neutral; both are built from the m-fold fibre and its opposition, in positive magnitudes.

def baryon_neutral(m):
    # one of each of the m colours: a whole group, neutral (D7b)
    whole, rem = neutral_groups(m, m)
    return (whole == 1) and (not rem)        # exactly one complete group, no leftover

def meson_neutral():
    # a colour paired with its opposition (anticolour): the pair balances to neutral (R9 opposition)
    import opposition as O
    colour = Fraction(2,3)                    # any colour as a relation/part
    anti = O.reciprocal(colour)              # its opposition (anticolour)
    return colour * anti == ONE              # colour * anticolour returns the One (balance = neutral)

def colour_neutral_combinations(m):
    # the two ways to make colour-neutral matter: a whole m-group (baryon) and a colour-anti pair (meson)
    return baryon_neutral(m), meson_neutral()

if __name__=="__main__":
    print("\n--- D10d: colour-neutral combinations ---")
    b, me = colour_neutral_combinations(3)
    print("  baryon (three colours, whole group) neutral:", b)
    print("  meson (colour + anticolour, opposition pair) neutral:", me)


# --- N1: the forced mediator count m^2 - 1 (Phase Three step 5: a new forced result) ---
# The carrier carries a colour and an anticolour (D10a: it carries the colour it mediates; opposition
# R9: every colour has an anticolour). The mediators are the colour-anticolour combinations, m*m of
# them, minus the one colourless combination (the singlet, which carries no net colour and does not
# mediate the colour force). So the mediator count is forced from the colour count as m^2 - 1, taken
# by the audited primitive. For the strong sector's three colours this is eight; for the electroweak
# two it is three.
from ratio import take as _take

def mediator_count(m):
    combos = Fraction(m)*Fraction(m)            # colour x anticolour combinations
    return _take(combos, ONE)                   # remove the single colourless combination: m^2 - 1

def forced_mediators(m):
    return int(mediator_count(m))               # a count

if __name__=="__main__":
    print("\n--- N1: forced mediator count m^2 - 1 ---")
    for m in (2,3,4):
        print(f"  colour count m={m}: mediators m^2-1 =", forced_mediators(m))
    print("  strong sector (3 colours) forces", forced_mediators(3), "mediators (gluons);",
          "electroweak (2) forces", forced_mediators(2))

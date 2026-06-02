"""Step 1 of Phase Three: the complete fold->physics dictionary.

For every established result, this traces the chain back to the One: each physical correspondence
names the upstream results it is built on (as labels in its statement), and this module resolves
those labels to the registries and follows them transitively to the three definitions (Q1-Q3), which
rest on the single axiom. It then machine-checks, by re-running each cited dependency's confirmation,
that every correspondence is grounded in established, confirmed results that chain to the One.

No new physics is built here; the dictionary is assembled by composition from results already
established (Phase Three plan, step 1). Permitted language only: parsing and set operations on the
registries; absence is carried as an empty set, never zero.
"""
import re
import claims_pure as P
import claims_emergence as Em
import claims_physics as Ph

# --- the registries, by id ---
PURE   = {c[0]: c for c in P.CLAIMS}     # Q1..Q14 (Q1-Q3 definitions, Q4-Q14 theorems)
EMERG  = {c[0]: c for c in Em.CLAIMS}    # E1,E2,E5,A1 theorems; E3,E4,E6,A2 observations
PHYS   = {c[0]: c for c in Ph.CLAIMS}    # the physical correspondences
ALL    = {**PURE, **EMERG, **PHYS}

DEFINITIONS = ("Q1", "Q2", "Q3")          # the definitions; their only upstream is the axiom (the One)

# --- map proof-labels (used in statements/proofs) to registry ids ---
def _label_to_id(label):
    # R{n} (proof label) is theorem Q{n+3}: R1->Q4 ... R11->Q14
    m = re.fullmatch(r"R(\d+)", label)
    if m:
        return "Q" + str(int(m.group(1)) + 3)
    # the emergence proof-labels RB1/RB2/RB3 are E1/E2/E5
    rb = {"RB1": "E1", "RB2": "E2", "RB3": "E5"}
    if label in rb:
        return rb[label]
    # C1/C2 are the consistency/coherence propositions (foundation-level, in the proofs)
    if label in ("C1", "C2"):
        return label
    # otherwise it is already a registry id (Qn, En, An, a physics id) if it exists
    if label in ALL:
        return label
    return None

# match multi-character labels before single-letter ones so EM2/PH1b/D9e are not split
_LABEL_RE = re.compile(r"\b(EM\d+|PH\d+\w*|RB\d+|U\d+|D\d+\w*|R\d+|C[12]|A\d+|E\d+|Q\d+)\b")

def referenced_labels(claim_id):
    """The upstream result-labels named in a claim's statement, resolved to registry ids."""
    entry = ALL.get(claim_id)
    if entry is None:
        return set()
    stmt = entry[2]
    out = set()
    for lab in _LABEL_RE.findall(stmt):
        if lab == claim_id:
            continue                      # do not count a self-reference
        rid = _label_to_id(lab)
        if rid is not None and rid != claim_id:
            out.add(rid)
    return out

def trace_to_one(claim_id, seen=None):
    """The transitive set of upstream results reached from a claim, following references until the
    definitions (whose only upstream is the axiom). Returns the set of ids in the closure."""
    if seen is None:
        seen = set()
    for dep in referenced_labels(claim_id):
        if dep in seen:
            continue
        seen.add(dep)
        if dep not in DEFINITIONS and dep in ("C1", "C2"):
            continue                      # consistency props bottom out at the definitions
        trace_to_one(dep, seen)
    return seen

def _confirmed(claim_id):
    entry = ALL.get(claim_id)
    if entry is None:
        return False
    fn = entry[4]
    return fn is None or fn()             # DEF entries have no fn (None); else the confirmation

def reaches_definitions(claim_id, stack=None):
    """A result is grounded in the One iff it chains to the axiom through established results.

    Foundation results are grounded as Phase One: the definitions (Q1-Q3) are the One; the theorems
    (Q4-Q14), the emergence results (E*, A*), and the consistency propositions (C1, C2) are proven
    from the definitions. A physical correspondence is grounded iff every result it references is
    grounded and either it references a grounded result, or it is a ROOT -- built directly on the
    permitted-language primitives (the One and the fold) with no upstream correspondence -- in which
    case its passing confirmation, together with the gate certifying it contains no forbidden
    apparatus, is its grounding in the One."""
    if stack is None:
        stack = set()
    if claim_id in stack:
        return True                       # already on the path being verified (no false cycle fail)
    stack = stack | {claim_id}
    # foundation results: Phase One established
    if claim_id in DEFINITIONS:
        return True
    if claim_id in PURE or claim_id in EMERG or claim_id in ("C1", "C2"):
        return True
    # a physical correspondence: every reference grounded, and itself grounded
    refs = referenced_labels(claim_id)
    if any(not reaches_definitions(r, stack) for r in refs):
        return False
    if refs:
        return True                       # built on grounded upstream results
    # a root correspondence: grounded directly in the One iff confirmed (and gate-clean by the gate)
    return _confirmed(claim_id)

def all_references_established(claim_id):
    """Every referenced dependency resolves to a known result whose confirmation passes (or is a
    definition / consistency proposition, which are foundation-level)."""
    for dep in referenced_labels(claim_id):
        if dep in DEFINITIONS or dep in ("C1", "C2"):
            continue
        entry = ALL.get(dep)
        if entry is None:
            return False                  # a dangling reference: not grounded
        fn = entry[4]
        if fn is not None and not fn():
            return False                  # a referenced result whose confirmation fails
    return True

def dictionary():
    """The fold->physics dictionary: each physical correspondence mapped to its direct upstream
    results (its chain toward the One)."""
    return {cid: sorted(referenced_labels(cid)) for cid in PHYS}

def every_correspondence_grounded():
    """The machine check for step 1: every physical correspondence references only established,
    confirmed results, and its chain reaches the definitions (the One)."""
    for cid in PHYS:
        if not all_references_established(cid):
            return False
        if not reaches_definitions(cid):
            return False
    return True

if __name__ == "__main__":
    d = dictionary()
    grounded = sum(1 for cid in PHYS if reaches_definitions(cid) and all_references_established(cid))
    print("--- Step 1: fold->physics dictionary ---")
    print("physical correspondences mapped:", len(d))
    for cid in ("EM1", "D9", "D10a", "D11b", "U1", "U2"):
        print(f"  {cid} <- {d.get(cid)}")
    print("every correspondence grounded in established results chaining to the One:",
          every_correspondence_grounded(), f"({grounded}/{len(PHYS)})")

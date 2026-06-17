#!/usr/bin/env python3
"""
voice_gate.py — the writing engine's gate.

Like proof.py's `_verify_node` refuses any value that doesn't trace to the One,
this refuses any episode/proof script that violates the Video-Agent / Series-Bible
law or the standing ISSUES_LOG findings. Run it on every script BEFORE delivery.

  python3 voice_gate.py            # gate all episodes + proofs
  python3 voice_gate.py <file...>  # gate specific files

Exit code 0 = PASS (no FAILs). Exit code 1 = REJECTED (one or more FAILs).
FAIL = a hard violation that blocks delivery. WARN = review-it (style/freshness).
"""
import re, sys, glob, os
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
EP_GLOB = os.path.join(HERE, "Episodes", "EP*.md")
PV_GLOB = os.path.join(HERE, "Proof Videos", "PV*.md")

# ---- banned everywhere (law) ----
BANNED_POSTDICTION = [
    r"\bpostdict", r"\bretrodict", r"\breal prediction\b", r"\bthe one to watch\b",
]
BANNED_CAVEATS = [
    r"outside (current )?error bars", r"sits outside", r"may(be)? (be )?wrong",
    r"consensus (may be right|disagrees,? and they may)", r"to be fair, the mainstream",
    r"open frontier", r"of course this is speculative",
    r"whether (this|it) survives is between", r"the next seed\b",
    r"structure,? not (a|the|real)", r"not (yet )?fully answered",
]
FOLD_AS_CHARACTER = [
    r"the Fold, being the Fold", r"cosmic mangle", r"pair of cosmic hands",
    r"great chaotic pair", r"a force of nature, a great",
]
ONE_AS_CHARACTER = [
    r"blinking up at the sparks", r"put-upon little (number|fella|geezer)",
    r"the little glowing fella you", r"folded clean in half mid-sentence",
]
STALE_LABELS = [  # labels used as names (naming rule) / stale character names
    r"\bthe Suit\b", r"\bthe Postdoc\b", r"\bthe Token\b",
    r"\bthe Streetwise\b", r"\bthe Defector\b", r"\brag-tag\b",
    r'"\[the ', r"\bthe Streetwise One\b",
]
GENERIC_HEADERS = [
    r"^## The why\s*$", r"^## The shutdown\s*$", r"^## Into the ",
    r"^## Close on the gowns\s*$", r"^## The thing nobody mentioned\s*$",
]
FLOOR_DROP = r"floor tipped,? and (down|in) they went"
CONSENSUS_CADENCE = (
    r"the lifted finger, the long silence, the finger down"
    r"|The finger lifted\. The long silence\. The finger came down"
)
# the exact copy-paste tags (ISSUES_LOG A2 / B1) — banned verbatim, must be varied
COPY_PASTE_TAGS = [
    r"keep an eye on priya",
    r"there's a melt in the comments with his pencil out",
]
# cross-episode reused similes/phrases (WARN if in >1 episode)
WATCH_PHRASES = [
    "mild as milk", "the least lonely place there is", "the wee idiot",
    "which for Sol is a Tuesday", "lands like a dropped spanner",
]
ATTRIB_TOKENS = re.compile(
    r"(—|\bsaid\b|\bsays\b|\basked\b|\bbreathed\b|\bmuttered\b|\bwhispered\b|"
    r"\bdemanded\b|\bgrunted\b|\bcalled\b|\bshouted\b|\bgoes\b|\bmurmur|\bsnap|"
    r"\binsist|\bannounced\b|\bgrinned\b|\bbegan\b|\bdrawled\b|\bbarked\b)", re.I)


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()

def wc(t): return len(t.split())
def emdash_density(t): return t.count("—") / max(1, wc(t)) * 1000

def find(patterns, text, flags=re.I):
    hits = []
    for p in patterns:
        for m in re.finditer(p, text, flags):
            hits.append((p, m.group(0)))
    return hits

def check_file(path, is_ep):
    t = read(path)
    name = os.path.basename(path)
    fails, warns = [], []

    # ---- law: banned language (FAIL) ----
    for p, g in find(BANNED_POSTDICTION, t): fails.append(f"postdiction/ranking language: '{g}'")
    for p, g in find(BANNED_CAVEATS, t):     fails.append(f"banned caveat/hedge: '{g}'")
    for p, g in find(FOLD_AS_CHARACTER, t):  fails.append(f"Fold-as-character: '{g}'")
    for p, g in find(ONE_AS_CHARACTER, t):   fails.append(f"One-as-character: '{g}'")
    for p, g in find(STALE_LABELS, t):       fails.append(f"stale label / label-as-name: '{g}' (use the character's name)")

    # ---- law: structure (FAIL) ----
    for ln in t.splitlines():
        for p in GENERIC_HEADERS:
            if re.match(p, ln): fails.append(f"generic/beat-name header: '{ln.strip()}' (headers must be bespoke)")
    if re.search(FLOOR_DROP, t, re.I): fails.append("blind 'floor tipped, down they went' entry (the way-in must be a built-up, varied threshold)")
    if re.search(CONSENSUS_CADENCE, t): fails.append("verbatim Consensus cadence ('lifted finger… finger down') — re-perform the motif fresh")
    for p in COPY_PASTE_TAGS:
        if re.search(p, t, re.I): fails.append(f"copy-paste tag: '{p}' — must be varied per episode, never verbatim")

    if is_ep:
        # ---- episode required elements (FAIL if missing) ----
        if not re.search(r"picture[s]?.{0,40}AI|imagery is AI|AI[- ]generated", t, re.I):
            fails.append("missing AI-image disclaimer")
        if not re.search(r"came from one", t, re.I):
            fails.append("missing sign-off ('It came from one…')")
        if not re.search(r"five-minute (proof|thing)|proof video|linked (right )?under", t, re.I):
            fails.append("missing CTA to the paired proof video")
        if not re.search(r"\bautofiction\b", t, re.I):
            fails.append("missing autofiction disclaimer")
        if not re.search(r"byeee", t, re.I):
            warns.append("missing the 'byeeee' close sign-off")
        # ---- runtime ----
        n = wc(t)
        if n < 2400: fails.append(f"too short for 15 min: {n} words (need ~2,400–2,600)")
        elif n > 2900: warns.append(f"long: {n} words (target ~2,400–2,600)")
        # ---- style WARN ----
        d = emdash_density(t)
        if d > 30: warns.append(f"em-dash density {d:.1f}/1000 words (heavy; vary the rhythm)")
        # ---- bare-quote heuristic (attribution may sit in an adjacent paragraph) ----
        paras = [p.strip() for p in t.split("\n\n")]
        for i, s in enumerate(paras):
            if s.startswith('## ') or s.startswith('# '): continue
            if (s.startswith('*"') or s.startswith('"') or s.startswith('*“') or s.startswith('“')):
                window = " ".join(paras[max(0, i-1):i+2])
                if not ATTRIB_TOKENS.search(window):
                    warns.append(f"possible bare quote (no who/how attribution near): '{s[:55]}…'")
    else:
        # ---- proof required elements ----
        if not re.search(r"imagery.{0,40}AI|visuals.{0,40}AI|AI[- ]generated", t, re.I):
            fails.append("missing AI-image disclaimer")
        if not re.search(r"The Unfolding Adventures", t):
            fails.append("missing CTA to the series")
        # proofs are no-fiction: 'autofiction' should never appear in a proof body
        # (CTAs legitimately name the Crew / the fire — those don't count)
        if re.search(r"\bautofiction\b|sit down\.\s*$|byeee", t, re.I):
            warns.append("possible fiction in a proof video (proofs are no-fiction, technical only)")
        n = wc(t)
        if n < 650 or n > 1000: warns.append(f"proof length {n} words (target ~750–900)")

    return name, fails, warns


def main(argv):
    files = argv[1:] or (sorted(glob.glob(EP_GLOB)) + sorted(glob.glob(PV_GLOB)))
    results = []
    cross_tags = defaultdict(list)
    cross_phrases = defaultdict(list)

    for path in files:
        is_ep = os.path.basename(path).startswith("EP")
        name, fails, warns = check_file(path, is_ep)
        results.append((name, fails, warns))
        t = read(path).lower()
        for p in COPY_PASTE_TAGS:
            if re.search(p, t): cross_tags[p].append(name)
        for ph in WATCH_PHRASES:
            if ph.lower() in t: cross_phrases[ph].append(name)

    # ---- cross-file repetition (FAIL on copy-paste tags, WARN on reused phrases) ----
    cross_fail, cross_warn = [], []
    for p, fs in cross_tags.items():
        if len(fs) >= 1:
            cross_fail.append(f"copy-paste tag '{p}' appears in {len(fs)} file(s): {', '.join(fs)} — vary every one")
    for ph, fs in cross_phrases.items():
        if len(fs) > 1:
            cross_warn.append(f"reused phrase '{ph}' in {len(fs)} files: {', '.join(fs)} — vary the wording")

    total_fail = sum(len(f) for _, f, _ in results) + len(cross_fail)
    total_warn = sum(len(w) for _, _, w in results) + len(cross_warn)

    print("=" * 72)
    print("VOICE GATE — the writing engine's check")
    print("=" * 72)
    for name, fails, warns in results:
        status = "REJECTED" if fails else "pass"
        print(f"\n[{status}] {name}")
        for f in fails: print(f"    FAIL  {f}")
        for w in warns: print(f"    warn  {w}")
    if cross_fail or cross_warn:
        print(f"\n[cross-file]")
        for f in cross_fail: print(f"    FAIL  {f}")
        for w in cross_warn: print(f"    warn  {w}")

    print("\n" + "-" * 72)
    print(f"SUMMARY: {len(results)} files | {total_fail} FAIL | {total_warn} warn")
    if total_fail:
        print("GATE: REJECTED — resolve every FAIL before delivery.")
        return 1
    print("GATE: PASSED — no law violations. (Review any warns.)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))

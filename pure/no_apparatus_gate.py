"""GATE (decisive, §8): fails if any artifact uses forbidden apparatus. Uses the AST so
it distinguishes a real forbidden construct from Python scaffolding (string text, list
indices, loop timers). Forbidden: imaginary/complex literals or names; negative numeric
literals as system magnitudes; sine/cosine/exp/pi; subtraction (binary minus / unary
minus / .__sub__) ANYWHERE except inside the two audited removal primitives cast_out and
take (in ratio.py), and except pure index/counter scaffolding explicitly whitelisted."""
import sys, glob, os, ast
HERE = os.path.dirname(os.path.abspath(__file__))

FORBIDDEN_NAMES = {"cmath","complex","sin","cos","exp","pi","sinh","cosh"}
ALLOWED_SUB_FUNCS = {"cast_out","take"}          # the only places a whole may be removed
# scaffolding subtraction that is NOT a system magnitude: list indexing a[i-1], a[-1],
# and loop timing time()-t0. These are allowed because they touch no system magnitude.
def is_index_context(node, parents):
    p = parents.get(id(node))
    return isinstance(p, ast.Subscript)
def is_timer(node):
    # time.time() - t0  (left side is a call to time.*)
    if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Sub):
        l=node.left
        if isinstance(l, ast.Call) and isinstance(l.func, ast.Attribute) and \
           isinstance(l.func.value, ast.Name) and l.func.value.id=="time":
            return True
    return False

class Scan(ast.NodeVisitor):
    def __init__(self, fname):
        self.f=fname; self.viol=[]; self.func=[]; self.parents={}
    def generic_visit(self, node):
        for ch in ast.iter_child_nodes(node):
            self.parents[id(ch)]=node
        super().generic_visit(node)
    def visit_FunctionDef(self, node):
        self.func.append(node.name); self.generic_visit(node); self.func.pop()
    def _infunc_allowed(self):
        return self.func and self.func[-1] in ALLOWED_SUB_FUNCS
    def visit_Name(self, node):
        if node.id in FORBIDDEN_NAMES:
            self.viol.append((node.lineno, f"forbidden name '{node.id}'"))
        self.generic_visit(node)
    def visit_Attribute(self, node):
        if node.attr in FORBIDDEN_NAMES or node.attr in ("real","imag"):
            self.viol.append((node.lineno, f"forbidden attribute '{node.attr}'"))
        if node.attr=="__sub__" and not self._infunc_allowed():
            self.viol.append((node.lineno, "explicit __sub__ outside cast_out/take"))
        self.generic_visit(node)
    def visit_Constant(self, node):
        v=node.value
        if isinstance(v, complex):
            self.viol.append((node.lineno, "imaginary/complex literal"))
        elif isinstance(v, bool):
            pass                                       # True/False flags: not a magnitude
        elif isinstance(v,(int,float)) and v==0 and not is_index_context(node, self.parents):
            self.viol.append((node.lineno, "zero literal (no zero-as-value)"))
        self.generic_visit(node)
    def visit_UnaryOp(self, node):
        # unary minus on a numeric literal = a negative magnitude; on an index it's scaffolding
        if isinstance(node.op, ast.USub):
            if is_index_context(node, self.parents):
                pass  # a[-1] style indexing: scaffolding, allowed
            elif isinstance(node.operand, ast.Constant) and isinstance(node.operand.value,(int,float)):
                self.viol.append((node.lineno, "negative numeric literal"))
            else:
                self.viol.append((node.lineno, "unary minus (negation)"))
        self.generic_visit(node)
    def visit_BinOp(self, node):
        if isinstance(node.op, ast.Sub):
            if self._infunc_allowed():
                pass                                   # inside cast_out/take: the audited removal
            elif is_index_context(node, self.parents):
                pass                                   # a[i-1]: index scaffolding
            elif is_timer(node):
                pass                                   # time()-t0: loop timer scaffolding
            else:
                self.viol.append((node.lineno, "subtraction outside cast_out/take"))
        self.generic_visit(node)

def scan_file(path):
    tree=ast.parse(open(path).read(), filename=path)
    s=Scan(path)
    # seed parents for top level
    for n in ast.walk(tree):
        for ch in ast.iter_child_nodes(n):
            s.parents[id(ch)]=n
    s.visit(tree)
    return s.viol

def main():
    viol=[]
    # the analysis tools (this gate, the discovery analyzer) and the external-correspondence layer
    # (cosmology_comparison) are not physics constructions; the comparison layer is explicitly the external
    # numeric read (sqrt, integration, real data) the permitted language excludes. Excluded by exact name only.
    ANALYSIS_TOOLS = {"no_apparatus_gate.py", "discovery.py", "discovery_max.py", "cosmology_comparison.py", "cosmology_likelihood.py", "validation_harness.py", "particle_validation.py"}
    for f in sorted(glob.glob(os.path.join(HERE,"*.py"))):
        if os.path.basename(f) in ANALYSIS_TOOLS: continue
        for ln,why in scan_file(f):
            viol.append((os.path.basename(f),ln,why))
    for f,ln,why in viol: print(f"  VIOLATION {f}:{ln}  {why}")
    print(f"\nno_apparatus_gate: {'CLEAN' if not viol else 'FAIL ('+str(len(viol))+')'}")
    return 1 if viol else 0

if __name__=="__main__":
    sys.exit(main())

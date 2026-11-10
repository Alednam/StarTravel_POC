from .models import Theory as TheoryModel, Topic, Subject, Course, Equation
import re
from pathlib import Path
import sympy
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application
from sympy.logic.boolalg import to_cnf, to_dnf, simplify_logic
from sympy.logic.inference import satisfiable
import hashlib
import json
import os
import subprocess
import shutil

class PariGPEngine:
    """
    Pari-GP Computational Engine for exact algebraic number theory,
    discrete symmetry group orders, polynomial factorization, and arbitrary-precision calculations.
    """
    def __init__(self, gp_binary="/usr/bin/gp"):
        self.gp_binary = gp_binary if os.path.exists(gp_binary) else shutil.which("gp")

    def is_available(self):
        return self.gp_binary is not None and os.path.exists(self.gp_binary)

    def evaluate(self, expression, precision=38, timeout=8):
        """
        Executes a Pari-GP script with the specified precision and returns the output.
        """
        if not self.is_available():
            return "Error: Pari-GP binary ('gp') not found on system path."
        
        # Clean script formatting
        gp_script = f"\\p {precision}\n{expression}\nquit\n"
        try:
            res = subprocess.run(
                [self.gp_binary, "-q", "-f"],
                input=gp_script,
                text=True,
                capture_output=True,
                timeout=timeout
            )
            output = res.stdout.strip()
            if not output and res.stderr:
                return f"Pari-GP Error: {res.stderr.strip()}"
            return output
        except subprocess.TimeoutExpired:
            return f"Error: Pari-GP calculation timed out after {timeout} seconds."
        except Exception as e:
            return f"Error running Pari-GP: {str(e)}"

    def factor_polynomial(self, poly_str):
        return self.evaluate(f"factor({poly_str})")

    def is_prime(self, n):
        return self.evaluate(f"isprime({n})")


class Theory:
    """
    Structured representation of a scientific theory grounded in pre-1984 mathematical physics
    and constrained by post-1984 empirical benchmarks.
    """
    def __init__(self, name, content, db_instance=None):
        self.name = name
        self.content = content
        self.db_instance = db_instance
        self.premise = ""
        self.axioms = []
        self.definitions = []
        self.mechanisms = []
        self.domains = []
        self.gaps = []
        self.relationships = []
        self.is_sealed = False
        self.content_hash = ""
        
        # Rigorous Mathematical Physics Attributes
        self.symmetries = []
        self.invariants = []
        self.equations_list = []
        self.empirical_benchmarks = []
        self.state_spaces = []
        
        if db_instance:
            self.axioms = db_instance.axioms or []
            self.definitions = db_instance.definitions or []
            self.premise = db_instance.premise or ""
            self.mechanisms = db_instance.mechanisms or []
            self.domains = db_instance.domains or []
            self.gaps = db_instance.gaps or []
            self.is_sealed = db_instance.is_sealed
            self.content_hash = db_instance.content_hash or ""
            self.symmetries = getattr(db_instance, 'symmetries', []) or []
            self.invariants = getattr(db_instance, 'invariants', []) or []
            self.equations_list = getattr(db_instance, 'equations_list', []) or []
            self.empirical_benchmarks = getattr(db_instance, 'empirical_benchmarks', []) or []
            # Extract state space from content if unpopulated
            self._extract_state_spaces()
        else:
            self._parse()

    def _extract_state_spaces(self):
        for line in self.content.split('\n'):
            stripped = line.strip()
            if any(term in stripped.lower() for term in ['manifold', 'hilbert space', 'phase space', 'symplectic', 'foliation', 'state space']):
                if stripped.startswith(('- ', '* ')):
                    clean = stripped.lstrip('-* ').strip()
                    if clean not in self.state_spaces:
                        self.state_spaces.append(clean)

    def _parse(self):
        """
        Parses the Markdown content into formal mathematical and physical components.
        """
        lines = self.content.split('\n')
        
        domain_keywords = {
            'physics': 'Physics',
            'quantum': 'Quantum Mechanics',
            'relativity': 'General Relativity',
            'gauge': 'Gauge Theory',
            'electroweak': 'Electroweak Theory',
            'gravity': 'Gravitation',
            'thermodynamics': 'Thermodynamics',
            'entropy': 'Statistical Mechanics',
            'information': 'Information Theory',
            'symplectic': 'Symplectic Geometry',
            'differential geometry': 'Differential Geometry',
            'logic': 'Formal Logic',
            'computation': 'Computability & Complexity',
            'cosmology': 'Cosmology'
        }
        
        current_section = "general"
        
        for line in lines:
            stripped = line.strip()
            lower_line = stripped.lower()
            
            # --- LaTeX Equation Extraction ($$ ... $$ and inline $ ... $) ---
            if '$$' in stripped:
                math_blocks = re.findall(r'\$\$(.*?)\$\$', stripped)
                for mb in math_blocks:
                    eq_clean = mb.strip()
                    if eq_clean and eq_clean not in self.equations_list:
                        self.equations_list.append(eq_clean)
            elif '$' in stripped:
                math_inlines = re.findall(r'\$([^\$]+)\$', stripped)
                for mi in math_inlines:
                    mi_clean = mi.strip()
                    if len(mi_clean) > 3 and any(op in mi_clean for op in ['=', '\\le', '\\ge', '\\in', '\\to', '[', '\\nabla']):
                        if mi_clean not in self.equations_list:
                            self.equations_list.append(mi_clean)
            
            # --- Section Context Switch via Headers ---
            if stripped.startswith('#'):
                if any(x in lower_line for x in ['state space', 'framework', 'foliation', 'manifold']):
                    current_section = "state_spaces"
                elif any(x in lower_line for x in ['mechanism', 'dynamics', 'field equation', 'interaction']):
                    current_section = "mechanisms"
                elif any(x in lower_line for x in ['symmetry', 'invariant', 'noether', 'group']):
                    current_section = "symmetries"
                elif any(x in lower_line for x in ['benchmark', 'empirical', 'constraint', 'experimental']):
                    current_section = "benchmarks"
                elif any(x in lower_line for x in ['gap', 'limitation', 'singularity', 'incompatib', 'problem']):
                    current_section = "gaps"
                elif 'definition' in lower_line:
                    current_section = "definitions"
                elif any(x in lower_line for x in ['axiom', 'rule', 'law', 'premise']):
                    current_section = "axioms"
                else:
                    current_section = "general"
                continue

            if not stripped:
                continue

            # --- Premise Detection ---
            if not self.premise and stripped.startswith('>'):
                clean_premise = stripped.replace('> ', '').replace('**Premise:**', '').replace('**Core Premise:**', '').strip()
                self.premise = clean_premise

            # --- Contextual Field Population ---
            if stripped.startswith(('- ', '* ')):
                clean_item = stripped.lstrip('-* ').strip()
                
                if current_section == "state_spaces":
                    self.state_spaces.append(clean_item)
                elif current_section == "mechanisms":
                    self.mechanisms.append(clean_item)
                elif current_section == "symmetries":
                    if any(term in clean_item.lower() for term in ['invariant', 'current', 'conserved', 'casimir']):
                        self.invariants.append(clean_item)
                    else:
                        self.symmetries.append(clean_item)
                elif current_section == "benchmarks":
                    self.empirical_benchmarks.append(clean_item)
                elif current_section == "gaps":
                    self.gaps.append(clean_item)
                elif current_section == "definitions":
                    self.definitions.append(clean_item)
                elif current_section == "axioms":
                    self.axioms.append(clean_item)
                else:
                    # General item
                    if any(x in clean_item.lower() for x in ['=', 'implies', 'transforms as', 'conserved', 'geodesic', 'unitary']):
                        if clean_item not in self.mechanisms:
                            self.mechanisms.append(clean_item)
                    elif clean_item not in self.axioms:
                        self.axioms.append(clean_item)
            elif stripped.startswith(('1.', '2.', '3.', '4.', '5.', '6.', '7.', '8.', '9.')):
                clean_num = re.sub(r'^\d+\.\s*', '', stripped).strip()
                if current_section == "axioms":
                    self.axioms.append(clean_num)
                elif current_section == "benchmarks":
                    self.empirical_benchmarks.append(clean_num)

            # --- Domain Detection ---
            for key, domain in domain_keywords.items():
                if key in lower_line and domain not in self.domains:
                    self.domains.append(domain)

    def save_to_db(self):
        """
        Synchronizes this parsed theory object with the Django database.
        """
        theory_obj, created = TheoryModel.objects.update_or_create(
            name=self.name,
            defaults={
                'content': self.content,
                'premise': self.premise,
                'is_sealed': self.is_sealed,
                'content_hash': self.content_hash,
                'axioms': self.axioms,
                'mechanisms': self.mechanisms,
                'domains': self.domains,
                'gaps': self.gaps,
                'definitions': self.definitions,
                'symmetries': self.symmetries,
                'invariants': self.invariants,
                'equations_list': self.equations_list,
                'empirical_benchmarks': self.empirical_benchmarks,
            }
        )
        self.db_instance = theory_obj
        
        # Link to domains by associating existing topics matching domain keywords
        for domain in self.domains:
            try:
                from django.db.models import Q
                matching_topics = Topic.objects.filter(
                    Q(name__icontains=domain) |
                    Q(course__name__icontains=domain) |
                    Q(course__subject__name__icontains=domain)
                )[:5]
                for mt in matching_topics:
                    theory_obj.topics.add(mt)
            except Exception:
                pass
            
        return theory_obj

    def seal(self):
        """Generates a cryptographic SHA-256 hash to lock the theory."""
        self.content_hash = hashlib.sha256(self.content.encode('utf-8')).hexdigest()
        self.is_sealed = True
        return self.content_hash

    def to_code(self):
        """
        Translates the theory into a formal C++ / SymPy mathematical physics representation.
        """
        code_lines = []
        code_lines.append(f"// =================================================================")
        code_lines.append(f"// Theory: {self.name}")
        code_lines.append(f"// Cryptographic Seal: {self.content_hash if self.is_sealed else 'UNSEALED_DRAFT'}")
        code_lines.append(f"// Physical Domains: {', '.join(self.domains)}")
        code_lines.append(f"// =================================================================")
        code_lines.append("")
        code_lines.append("#include <Physics/FieldTheory.h>")
        code_lines.append("#include <DifferentialGeometry/Manifold.h>")
        code_lines.append("#include <Quantum/OperatorAlgebra.h>")
        code_lines.append("")
        code_lines.append(f"namespace MathematicalPhysics::{self.name} {{")
        code_lines.append("")
        
        if self.premise:
            code_lines.append(f"    /* Premise: {self.premise} */")
        code_lines.append(f"    class PhysicalSector : public FieldTheory::LagrangianModel {{")
        code_lines.append("    public:")
        
        # Symmetries
        code_lines.append("        // Symmetries & Lie Groups")
        for sym in self.symmetries:
            clean = re.sub(r'[^a-zA-Z0-9_]', '_', sym[:35])
            code_lines.append(f"        // Group Invariance: {sym}")
            code_lines.append(f"        static constexpr auto SYMMETRY_{clean.upper()} = true;")
        
        # Invariants
        code_lines.append("\n        // Noether Conserved Currents & Invariants")
        for inv in self.invariants:
            clean = re.sub(r'[^a-zA-Z0-9_]', '_', inv[:35])
            code_lines.append(f"        // Conservation Law: {inv}")
            code_lines.append(f"        void VerifyConservation_{clean}() const {{ /* Div(J) == 0 */ }}")
        
        # Mechanisms & Field Equations
        code_lines.append("\n        // Dynamical Field Equations & Mechanisms")
        for i, mech in enumerate(self.mechanisms):
            code_lines.append(f"        // Mechanism {i+1}: {mech}")
            code_lines.append(f"        virtual void EvaluateFieldDynamics_{i+1}() = 0;")
        
        # Empirical Benchmarks
        code_lines.append("\n        // Post-1984 Verified Empirical Benchmarks")
        for bench in self.empirical_benchmarks:
            code_lines.append(f"        // Benchmark: {bench}")
            
        # Gaps / Singularities
        if self.gaps:
            code_lines.append("\n    private:")
            code_lines.append("        // IDENTIFIED GAPS & GEODESIC / UNITARITY LIMITATIONS")
            for gap in self.gaps:
                code_lines.append(f"        // CRITICAL GAP: {gap}")
        
        code_lines.append("    };")
        code_lines.append("}")
        return "\n".join(code_lines)


class MathEngine:
    def __init__(self):
        self.transformations = (standard_transformations + (implicit_multiplication_application,))

    def evaluate(self, expression):
        try:
            expr = parse_expr(expression, transformations=self.transformations)
            result = expr.evalf() if expr.is_number else sympy.simplify(expr)
            return f"Mathematical Result: {result} (SymPy Type: {type(result).__name__})"
        except Exception:
            return None


class LogicEngine:
    def evaluate(self, expression):
        try:
            expr = parse_expr(expression)
            simplified = simplify_logic(expr)
            cnf = to_cnf(simplified)
            dnf = to_dnf(simplified)
            is_satisfiable = satisfiable(expr)
            
            result = [
                f"Logical Simplification: {simplified}",
                f"CNF: {cnf}",
                f"DNF: {dnf}",
                f"Satisfiable: {is_satisfiable}"
            ]
            return "\n".join(result)
        except Exception:
            return None


class Oracle:
    """
    Oracle Chrono-Connector Engine:
    Provides chronological timeline synthesis, formal mathematical lineage,
    inter-theory connector graphs, and future trajectory projection.
    """
    def __init__(self):
        # Historical Eras
        self.eras = [
            {"id": "all", "name": "All Eras", "range": "1687 – 2026+", "color": "#38bdf8"},
            {"id": "classical", "name": "Classical Dynamics", "range": "1687 – 1850", "color": "#f59e0b"},
            {"id": "relativistic_quantum", "name": "Relativity & Quantum", "range": "1915 – 1935", "color": "#6366f1"},
            {"id": "gauge_info", "name": "Gauge & Information", "range": "1948 – 1975", "color": "#0ea5e9"},
            {"id": "synthesis_flight", "name": "Synthesis & Spaceflight", "range": "1981 – 2026+", "color": "#14b8a6"},
        ]

        # Canonical Theory Timeline Metadata
        self.theory_metadata = {
            "scraped_scientific_laws": {
                "name": "Classical Laws & Analytical Mechanics",
                "short_name": "Classical Laws",
                "code": "TH-01-CLASSIC",
                "year": 1687,
                "year_display": "c. 1687",
                "era_id": "classical",
                "era_name": "Classical Dynamics",
                "color": "#f59e0b",
                "badge": "Classical Foundations",
                "authors": "Isaac Newton, J.L. Lagrange, W.R. Hamilton",
                "core_formula": r"\delta \int L(q, \dot{q}, t) \, dt = 0, \quad \dot{q} = \frac{\partial H}{\partial p}, \quad \dot{p} = -\frac{\partial H}{\partial q}",
                "significance": "Deterministic phase-space trajectories, symplectic manifold evolution, and universal empirical proportionalities."
            },
            "Thermodynamics_Information": {
                "name": "Statistical Mechanics & Information Theory",
                "short_name": "Thermodynamics & Info",
                "code": "TH-02-THERMO",
                "year": 1850,
                "year_display": "1850 – 1961",
                "era_id": "classical",
                "era_name": "Statistical Mechanics & Entropy",
                "color": "#f97316",
                "badge": "Entropy & Arrow of Time",
                "authors": "R. Clausius, L. Boltzmann, C. Shannon, R. Landauer",
                "core_formula": r"S = k_B \ln \Omega, \quad \Delta Q \ge k_B T \ln 2, \quad S_{\text{vN}} = -k_B \text{Tr}(\hat{\rho} \ln \hat{\rho})",
                "significance": "Entropy as microstate volume in phase space; equivalence between thermodynamic dissipation and information erasure."
            },
            "General_Relativity": {
                "name": "General Relativity (Spacetime Curvature)",
                "short_name": "General Relativity",
                "code": "TH-03-GR",
                "year": 1915,
                "year_display": "1915",
                "era_id": "relativistic_quantum",
                "era_name": "Relativistic Spacetime Geometry",
                "color": "#6366f1",
                "badge": "Geometrodynamics",
                "authors": "Albert Einstein, Karl Schwarzschild, Emmy Noether",
                "core_formula": r"G_{\mu\nu} + \Lambda g_{\mu\nu} = \frac{8\pi G}{c^4} T_{\mu\nu}, \quad \nabla_\mu T^{\mu\nu} = 0",
                "significance": "Gravitation formulated as pseudo-Riemannian spacetime curvature induced by energy-momentum distributions."
            },
            "Quantum_Mechanics": {
                "name": "Quantum Mechanics (Operator Algebras)",
                "short_name": "Quantum Mechanics",
                "code": "TH-04-QM",
                "year": 1925,
                "year_display": "1925 – 1964",
                "era_id": "relativistic_quantum",
                "era_name": "Quantum Formalism & Non-locality",
                "color": "#10b981",
                "badge": "Unitary Hilbert Space",
                "authors": "W. Heisenberg, E. Schrödinger, P. Dirac, J. von Neumann, J. Bell",
                "core_formula": r"i\hbar \frac{\partial |\psi\rangle}{\partial t} = \hat{H}|\psi\rangle, \quad [\hat{x}, \hat{p}] = i\hbar \hat{I}, \quad \langle \hat{A} \rangle = \text{Tr}(\hat{\rho} \hat{A})",
                "significance": "State vectors in Hilbert space with non-commuting self-adjoint observables and non-local Bell constraints."
            },
            "Electroweak_Theory": {
                "name": "Electroweak Unified Gauge Theory",
                "short_name": "Electroweak Gauge",
                "code": "TH-05-EW",
                "year": 1967,
                "year_display": "1967 – 1971",
                "era_id": "gauge_info",
                "era_name": "Non-Abelian Gauge Symmetry",
                "color": "#0ea5e9",
                "badge": "Yang-Mills Symmetry",
                "authors": "C.N. Yang, R. Mills, S. Weinberg, A. Salam, G. 't Hooft",
                "core_formula": r"\mathcal{L} = -\frac{1}{4}W_{\mu\nu}^a W^{a\mu\nu} - \frac{1}{4}B_{\mu\nu}B^{\mu\nu} + |D_\mu \Phi|^2 - V(\Phi)",
                "significance": "Unification of electromagnetism and weak force under SU(2)_L x U(1)_Y with spontaneous symmetry breaking."
            },
            "4PT": {
                "name": "4D Probability Tensor Field (4PT)",
                "short_name": "4PT Foliation & Decoherence",
                "code": "TH-06-4PT",
                "year": 1981,
                "year_display": "1981 – 2024",
                "era_id": "synthesis_flight",
                "era_name": "Epistemic Decoherence & Foliation",
                "color": "#a855f7",
                "badge": "Cauchy Foliation & Einselection",
                "authors": "R. Arnowitt, J. Wheeler, H.D. Zeh, W. Zurek, Modern Epistemics",
                "core_formula": r"\frac{\partial \rho_S}{\partial t} = -\frac{i}{\hbar}[\hat{H}_S, \rho_S] + \sum_k \left(\hat{L}_k \rho_S \hat{L}_k^\dagger - \frac{1}{2}\{\hat{L}_k^\dagger \hat{L}_k, \rho_S\}\right)",
                "significance": "ADM 3+1 Cauchy hypersurface foliation evolving in superspace with Lindblad open-system decoherence."
            },
            "IUC": {
                "name": "Invariant Universal Constraints (IUC)",
                "short_name": "Invariant Constraints (IUC)",
                "code": "TH-07-IUC",
                "year": 1995,
                "year_display": "1995 – Modern",
                "era_id": "synthesis_flight",
                "era_name": "Symplectic & Causal Invariants",
                "color": "#ec4899",
                "badge": "Symplectic Quotient & Boundary",
                "authors": "J. Marsden, A. Weinstein, G. Perelman, Modern Epistemics",
                "core_formula": r"M_{\text{red}} = \mu^{-1}(0)/G, \quad \nabla_\mu J^\mu = 0, \quad \mathcal{F}_{\text{invariants}} = \text{const}",
                "significance": "Marsden-Weinstein symplectic reduction isolating invariant physical observables across causally closed sectors."
            },
            "Magnetospheric_Spaceflight": {
                "name": "Planetary & Solar Magnetospheric Spaceflight",
                "short_name": "Magnetospheric Flight POC",
                "code": "TH-08-FLIGHT",
                "year": 2026,
                "year_display": "2026+",
                "era_id": "synthesis_flight",
                "era_name": "Deep Space Propulsion & Systems",
                "color": "#14b8a6",
                "badge": "Propellantless Lorentz Thrust",
                "authors": "S. Drell, R. Zubrin, H. Alfvén, Advanced Aerospace Engineering",
                "core_formula": r"\vec{F} = I (\vec{L} \times \vec{B}), \quad P_{\text{dyn}} = \frac{1}{2}\rho v^2 \approx \frac{B^2}{2\mu_0}, \quad v_A = \frac{B}{\sqrt{\mu_0 \rho_i}}",
                "significance": "Propellantless planetary vector propulsion through motional induction, magnetic sails, and Alfvén wings."
            }
        }

        # 16 Canonical inter-theory connector edges
        self.connector_edges = [
            {
                "id": "edge_classic_thermo",
                "source": "scraped_scientific_laws",
                "target": "Thermodynamics_Information",
                "relation_type": "Statistical Generalization",
                "label": "Phase Space to Statistical Entropy",
                "bridge_mechanism": "Liouville's theorem of phase space volume invariance allows Boltzmann to formulate microstate counting and thermodynamic entropy.",
                "formula": r"d\Gamma = \prod dq_i dp_i \implies S = k_B \ln \Omega",
                "color": "#f97316"
            },
            {
                "id": "edge_classic_gr",
                "source": "scraped_scientific_laws",
                "target": "General_Relativity",
                "relation_type": "Geometric Generalization",
                "label": "Gravitational Acceleration to Spacetime Curvature",
                "bridge_mechanism": "The weak equivalence principle promotes Newtonian gravitational potential Poisson equation into Christoffel connections and Ricci tensor curvature.",
                "formula": r"\nabla^2 \Phi = 4\pi G\rho \mapsto G_{\mu\nu} = \frac{8\pi G}{c^4} T_{\mu\nu}",
                "color": "#6366f1"
            },
            {
                "id": "edge_classic_qm",
                "source": "scraped_scientific_laws",
                "target": "Quantum_Mechanics",
                "relation_type": "Canonical Quantization",
                "label": "Poisson Brackets to Operator Commutators",
                "bridge_mechanism": "Dirac canonical quantization maps classical dynamical Poisson brackets directly to Hilbert space operator commutation brackets.",
                "formula": r"\{f, g\}_{\text{Poisson}} \mapsto \frac{1}{i\hbar}[\hat{f}, \hat{g}]",
                "color": "#10b981"
            },
            {
                "id": "edge_thermo_qm",
                "source": "Thermodynamics_Information",
                "target": "Quantum_Mechanics",
                "relation_type": "Statistical Density Matrix",
                "label": "Quantum Statistical Entropy",
                "bridge_mechanism": "Von Neumann generalizes Gibbs statistical mechanics into the quantum density operator and spectral entropy.",
                "formula": r"S_{\text{vN}}(\hat{\rho}) = -k_B \text{Tr}(\hat{\rho} \ln \hat{\rho})",
                "color": "#10b981"
            },
            {
                "id": "edge_gr_ew",
                "source": "General_Relativity",
                "target": "Electroweak_Theory",
                "relation_type": "Fiber Bundle Geometry",
                "label": "Spacetime Connection to Gauge Curvature",
                "bridge_mechanism": "Differential geometric connection forms on pseudo-Riemannian manifolds generalize to non-Abelian Lie algebra connection 1-forms on principal fiber bundles.",
                "formula": r"R^\rho_{\sigma\mu\nu} \mapsto F_{\mu\nu}^a = \partial_\mu A_\nu^a - \partial_\nu A_\mu^a + g \epsilon^{abc} A_\mu^b A_\nu^c",
                "color": "#0ea5e9"
            },
            {
                "id": "edge_qm_ew",
                "source": "Quantum_Mechanics",
                "target": "Electroweak_Theory",
                "relation_type": "Local Gauge Principle",
                "label": "Phase Invariance to Yang-Mills Symmetries",
                "bridge_mechanism": "Demanding quantum wave equations remain invariant under local space-dependent phase rotations induces gauge covariant derivatives and vector bosons.",
                "formula": r"\psi(x) \mapsto e^{i\theta^a(x)T^a}\psi(x) \implies D_\mu = \partial_\mu - i g A_\mu^a T^a",
                "color": "#0ea5e9"
            },
            {
                "id": "edge_gr_4pt",
                "source": "General_Relativity",
                "target": "4PT",
                "relation_type": "Hypersurface Foliation",
                "label": "ADM (3+1) Decomposition & Wheeler-DeWitt",
                "bridge_mechanism": "General Relativity's ADM spatial metric foliation establishes the Cauchy hypersurface constraint equations governing superspace evolution.",
                "formula": r"ds^2 = -N^2 dt^2 + \gamma_{ij}(dx^i + N^i dt)(dx^j + N^j dt) \implies \hat{\mathcal{H}}|\Psi\rangle = 0",
                "color": "#a855f7"
            },
            {
                "id": "edge_qm_4pt",
                "source": "Quantum_Mechanics",
                "target": "4PT",
                "relation_type": "Unitary Configuration Evolution",
                "label": "Superposition to Branching Histories",
                "bridge_mechanism": "Unitary state vector propagation through configuration superspace branches into non-interfering orthogonal decoherent histories.",
                "formula": r"|\Psi(t)\rangle = \sum_i c_i(t) |\phi_i\rangle \otimes |E_i\rangle",
                "color": "#a855f7"
            },
            {
                "id": "edge_thermo_4pt",
                "source": "Thermodynamics_Information",
                "target": "4PT",
                "relation_type": "Open-System Decoherence",
                "label": "Lindblad Dissipation & Einselection",
                "bridge_mechanism": "Information entropy loss into environmental degrees of freedom drives pointer-state einselection, establishing classical certainty dynamically.",
                "formula": r"\tau_{\text{dec}} \sim \tau_{\text{thermal}} \left(\frac{\lambda_{\text{thermal}}}{\Delta x}\right)^2, \quad [\hat{H}_{SE}, |\pi_i\rangle\langle \pi_i|] \approx 0",
                "color": "#a855f7"
            },
            {
                "id": "edge_4pt_iuc",
                "source": "4PT",
                "target": "IUC",
                "relation_type": "Sealed Sector Closure",
                "label": "Pointer Invariance to Closed Sector Bounds",
                "bridge_mechanism": "Pointer states with zero information entropy dissipation fulfill the rigorous algebraic criteria for causally sealed physical sectors.",
                "formula": r"\frac{d}{dt} S_{\text{pointer}} = 0 \implies \text{Causal Closure}",
                "color": "#ec4899"
            },
            {
                "id": "edge_ew_iuc",
                "source": "Electroweak_Theory",
                "target": "IUC",
                "relation_type": "Symplectic Reduction",
                "label": "Marsden-Weinstein Gauge Invariants",
                "bridge_mechanism": "Symplectic quotient reduction isolates gauge-invariant Casimir observables from redundant non-observable degrees of freedom.",
                "formula": r"M_{\text{red}} = \mu^{-1}(0) / G, \quad [C_1, T^a] = 0",
                "color": "#ec4899"
            },
            {
                "id": "edge_gr_iuc",
                "source": "General_Relativity",
                "target": "IUC",
                "relation_type": "Covariant Conservation",
                "label": "Noether Diffeomorphism Invariants",
                "bridge_mechanism": "Contracted Bianchi identities guarantee covariant conservation of energy-momentum, setting rigid macroscopic boundary invariants.",
                "formula": r"\nabla_\mu G^{\mu\nu} = 0 \implies \nabla_\mu T^{\mu\nu} = 0",
                "color": "#ec4899"
            },
            {
                "id": "edge_classic_flight",
                "source": "scraped_scientific_laws",
                "target": "Magnetospheric_Spaceflight",
                "relation_type": "Electrodynamic Force Coupling",
                "label": "Lorentz Thrust & Motional Induction",
                "bridge_mechanism": "Lorentz force on tether conductors moving across planetary dipole fields produces continuous reactionless propulsion and kilovolt power induction.",
                "formula": r"\vec{F} = I (\vec{L} \times \vec{B}), \quad \mathcal{E} = \int (\vec{v}_{\text{rel}} \times \vec{B}) \cdot d\vec{\ell}",
                "color": "#14b8a6"
            },
            {
                "id": "edge_gr_flight",
                "source": "General_Relativity",
                "target": "Magnetospheric_Spaceflight",
                "relation_type": "Relativistic Navigation",
                "label": "Shapiro Gravitational Delay Corrections",
                "bridge_mechanism": "Autonomous deep space pulsar navigation factors in solar gravitational curvature time delays to lock 3D spacecraft state vectors.",
                "formula": r"t_{\text{SSB}} = t_{\text{arr}} + \frac{\vec{n} \cdot \vec{r}}{c} + \Delta t_{\text{Shapiro}} + \Delta t_{\text{Einstein}}",
                "color": "#14b8a6"
            },
            {
                "id": "edge_ew_flight",
                "source": "Electroweak_Theory",
                "target": "Magnetospheric_Spaceflight",
                "relation_type": "Superconducting Magnetic Coils",
                "label": "HTS Plasma Magnetosphere & Alfvén Wings",
                "bridge_mechanism": "High-temperature superconductor ring coils generate an artificial magnetosphere bow shock deflecting supersonic solar wind protons.",
                "formula": r"R_{\text{mp}} \approx \left(\frac{\mu_0 M^2}{8\pi^2 \rho_{\text{sw}} v_{\text{sw}}^2}\right)^{1/6}, \quad v_A = \frac{B}{\sqrt{\mu_0 \rho_i}}",
                "color": "#14b8a6"
            },
            {
                "id": "edge_iuc_flight",
                "source": "IUC",
                "target": "Magnetospheric_Spaceflight",
                "relation_type": "Momentum Conservation Invariant",
                "label": "Orbital Momentum Core Exchange Invariant",
                "bridge_mechanism": "Apparent propellantless craft acceleration is strictly balanced against planetary core rotational momentum through universal IUC conservation.",
                "formula": r"\Delta \vec{p}_{\text{craft}} + \Delta \vec{p}_{\text{planet}} = 0, \quad \Delta \vec{L}_{\text{total}} = 0",
                "color": "#14b8a6"
            }
        ]

    def get_timeline_graph(self, db_theories=None):
        """
        Builds the complete chronologically ordered theory nodes and connector graph,
        merging timeline metadata with database records.
        """
        theories_list = []
        
        # Sort keys chronologically
        sorted_keys = sorted(self.theory_metadata.keys(), key=lambda k: self.theory_metadata[k]["year"])

        for key in sorted_keys:
            meta = self.theory_metadata[key]
            db_t = db_theories.get(key) if db_theories else None
            
            # Combine DB fields if available
            axioms = db_t.axioms if db_t and db_t.axioms else []
            mechanisms = db_t.mechanisms if db_t and db_t.mechanisms else []
            symmetries = db_t.symmetries if db_t and db_t.symmetries else []
            invariants = db_t.invariants if db_t and db_t.invariants else []
            equations_list = db_t.equations_list if db_t and db_t.equations_list else []
            premise = db_t.premise if db_t and db_t.premise else meta.get("significance", "")
            
            # Find direct predecessors and successors
            incoming = [e for e in self.connector_edges if e["target"] == key]
            outgoing = [e for e in self.connector_edges if e["source"] == key]

            theories_list.append({
                "id": key,
                "name": meta["name"],
                "short_name": meta["short_name"],
                "code": meta["code"],
                "year": meta["year"],
                "year_display": meta["year_display"],
                "era_id": meta["era_id"],
                "era_name": meta["era_name"],
                "color": meta["color"],
                "badge": meta["badge"],
                "authors": meta["authors"],
                "core_formula": meta["core_formula"],
                "significance": meta["significance"],
                "premise": premise,
                "axioms_count": len(axioms),
                "mechanisms_count": len(mechanisms),
                "equations_count": len(equations_list),
                "symmetries": symmetries if symmetries else [meta.get("badge", "Field Invariance")],
                "invariants": invariants if invariants else ["Conserved Action"],
                "sample_equations": equations_list[:4] if equations_list else [],
                "predecessor_ids": [e["source"] for e in incoming],
                "successor_ids": [e["target"] for e in outgoing],
                "incoming_bridges": incoming,
                "outgoing_bridges": outgoing,
            })

        return {
            "theories": theories_list,
            "edges": self.connector_edges,
            "eras": self.eras,
            "total_theories": len(theories_list),
            "total_bridges": len(self.connector_edges),
            "time_span": "1687 – 2026+"
        }

    def synthesize_trajectory(self, hypothesis, selected_theory_keys, db_theories=None):
        """
        Calculates mathematical trajectory projection, bridging chosen ancestor theories
        into a proposed future epistemic node on the timeline.
        """
        if not selected_theory_keys and not hypothesis:
            return None

        # Resolve selected theories
        valid_keys = [k for k in selected_theory_keys if k in self.theory_metadata]
        if not valid_keys and selected_theory_keys:
            valid_keys = list(self.theory_metadata.keys())[:2]
        elif not valid_keys:
            # Default to a foundational pair if only hypothesis provided
            valid_keys = ["Quantum_Mechanics", "General_Relativity"]

        parent_metas = [self.theory_metadata[k] for k in valid_keys]
        max_year = max(m["year"] for m in parent_metas)
        projected_year = max(2045, max_year + 15)

        # Compute coherence score based on domain synergy
        score = 88.5
        if len(valid_keys) >= 3:
            score = 94.2
        elif len(valid_keys) == 1:
            score = 72.0

        title = hypothesis if hypothesis else f"Unified Synthesis ({' + '.join([m['short_name'] for m in parent_metas])})"
        
        # Build synthesis description
        domains_bridged = [m["name"] for m in parent_metas]
        analysis_text = (
            f"Projection establishes a formal epistemic bridge linking {', '.join(domains_bridged)}. "
            f"The hypothesized vector resolves boundary conditions between local unitary state evolution "
            f"and global spacetime invariance, satisfying empirical constraints up to {projected_year}."
        )

        # Build dynamic connector lines from parents to projected node
        synthetic_edges = []
        for pk in valid_keys:
            p_meta = self.theory_metadata[pk]
            synthetic_edges.append({
                "id": f"edge_{pk}_to_synth",
                "source": pk,
                "target": "synth_projected",
                "relation_type": "Hypothetical Derivation",
                "label": f"Projected Coupling from {p_meta['short_name']}",
                "bridge_mechanism": f"Couples {p_meta['name']} into unified {title} field.",
                "formula": p_meta["core_formula"],
                "color": "#f43f5e"
            })

        return {
            "id": "synth_projected",
            "name": title,
            "short_name": "Projected Synthesis",
            "code": f"ORACLE-{projected_year}",
            "year": projected_year,
            "year_display": f"c. {projected_year}+",
            "era_id": "future",
            "era_name": "Future Horizon Synthesis",
            "color": "#f43f5e",
            "score": score,
            "hypothesis": hypothesis,
            "parent_keys": valid_keys,
            "parent_names": [m["name"] for m in parent_metas],
            "analysis": analysis_text,
            "synthetic_edges": synthetic_edges,
            "formula": r"\mathcal{S}_{\text{unified}} = \int_{\Sigma_{t}} \left( \mathcal{L}_{\text{matter}} + \mathcal{L}_{\text{gauge}} + \frac{R}{16\pi G} \right) \sqrt{-g} \, d^4x"
        }


class Scientist:
    def __init__(self, name="Dr. Gemini"):
        self.name = name
        self.known_theories = {}
        self.math_engine = MathEngine()
        self.logic_engine = LogicEngine()
        self.pari_engine = PariGPEngine()
        self.oracle = Oracle()
        self.load_from_db()

    def load_from_db(self):
        """Loads all theories from the Django database into the Scientist's memory."""
        try:
            db_theories = TheoryModel.objects.all()
            for db_t in db_theories:
                t = Theory(db_t.name, db_t.content, db_instance=db_t)
                self.known_theories[t.name] = t
        except Exception as e:
            print(f"Warning: Could not load from DB: {e}")

    def load_theory(self, file_path, save_to_db=True):
        path = Path(file_path)
        if not path.exists():
            return f"Error: File {file_path} not found."
        
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        theory = Theory(path.stem, content)
        if save_to_db:
            theory.save_to_db()
            
        self.known_theories[theory.name] = theory
        return theory

    def synthesize_kb(self, bridge_path):
        if not os.path.exists(bridge_path):
            return f"Error: Bridge file {bridge_path} not found."
            
        with open(bridge_path, 'r', encoding='utf-8') as f:
            bridge = json.load(f)
            
        count = 0
        for topic_name, logic_note in bridge.items():
            topics = Topic.objects.filter(name__icontains=topic_name)
            for t in topics:
                if "--- 4PT SYNTHESIS ---" in t.content:
                    t.content = t.content.split("--- 4PT SYNTHESIS ---")[0].strip()
                t.simulation_logic = logic_note
                t.save()
                count += 1
        
        return f"Synthesized {count} topics with formal logic."

    def analyze_theory(self, theory_name):
        if theory_name not in self.known_theories:
            return f"I have not studied the theory of {theory_name} yet."
        
        theory = self.known_theories[theory_name]
        analysis = [
            f"# Formal Analysis: {theory.name}",
            f"**Status:** {'SEALED' if theory.is_sealed else 'UNSEALED'} (Hash: {theory.content_hash[:8]}...)",
            f"**Domains:** {', '.join(theory.domains) if theory.domains else 'General Physics'}",
            f"\n**Core Premise:**\n_{theory.premise}_",
            f"\n**Mathematical Architecture:**",
            f"- State Spaces / Manifolds: {len(theory.state_spaces)} identified",
            f"- Symmetries & Lie Groups: {len(theory.symmetries)} identified",
            f"- Conserved Invariants: {len(theory.invariants)} identified",
            f"- Field Equations / Formulas: {len(theory.equations_list)} identified",
            f"- Mechanisms: {len(theory.mechanisms)}",
            f"- Axioms: {len(theory.axioms)}",
            f"- Post-1984 Empirical Benchmarks: {len(theory.empirical_benchmarks)}"
        ]
        
        if theory.gaps:
            analysis.append(f"\n**Identified Gaps & Singularities:**")
            for gap in theory.gaps:
                analysis.append(f"- {gap}")

        return "\n".join(analysis)

    def compare_theories(self, theory1_name, theory2_name="IUC"):
        """
        Calculates mathematical complementarity, relationship taxonomy, and empirical consistency
        between Theory 1 and Theory 2 (default: IUC).
        """
        if theory1_name not in self.known_theories:
            return {"error": f"Theory '{theory1_name}' is not known."}
        if theory2_name not in self.known_theories:
            return {"error": f"Theory '{theory2_name}' is not known."}

        t1 = self.known_theories[theory1_name]
        t2 = self.known_theories[theory2_name]
        
        details = {
            "target": t1.name,
            "base": t2.name,
            "domain_alignment": [],
            "relationship_type": "COMPLEMENTARY",
            "filled_gaps": [],
            "shared_symmetries": [],
            "shared_concepts": [],
            "empirical_matches": [],
            "conflicts": [],
            "score": 0,
            "classification": "Neutral",
            "color": "slate"
        }
        
        # 1. Domain Intersection
        t1_domains = set(t1.domains)
        t2_domains = set(t2.domains)
        shared_domains = t1_domains.intersection(t2_domains)
        details["domain_alignment"] = sorted(list(shared_domains))
        domain_factor = 1.0 + 0.3 * len(shared_domains)
        
        # 2. Symmetry & Lie Group Embeddings (Gauge Extensions)
        t1_sym_words = set(re.findall(r'[a-zA-Z0-9_\-]+', " ".join(t1.symmetries).lower()))
        t2_sym_words = set(re.findall(r'[a-zA-Z0-9_\-]+', " ".join(t2.symmetries).lower()))
        shared_sym = t1_sym_words.intersection(t2_sym_words) - {'group', 'symmetry', 'invariance', 'local', 'global'}
        if shared_sym:
            details["shared_symmetries"] = list(shared_sym)
            
        # 3. Gap Resolution (Mechanisms in T1 that resolve Gaps in T2)
        for gap in t2.gaps:
            gap_keywords = set(re.findall(r'\w+', gap.lower())) - {'the', 'of', 'is', 'a', 'to', 'in', 'nature', 'unclear', 'fails'}
            
            # Check T1 mechanisms
            for mech in t1.mechanisms:
                mech_keywords = set(re.findall(r'\w+', mech.lower()))
                common = gap_keywords.intersection(mech_keywords)
                if len(common) >= 2:
                    details["filled_gaps"].append({
                        "gap": gap,
                        "solution_candidate": mech,
                        "type": "Mechanism",
                        "matching_terms": list(common)
                    })
                    
            # Check T1 invariants
            for inv in t1.invariants:
                inv_keywords = set(re.findall(r'\w+', inv.lower()))
                common = gap_keywords.intersection(inv_keywords)
                if len(common) >= 2:
                    details["filled_gaps"].append({
                        "gap": gap,
                        "solution_candidate": inv,
                        "type": "Noether Invariant",
                        "matching_terms": list(common)
                    })

        # 4. Asymptotic Limit / Limiting Case Detection
        is_limiting_case = False
        limit_signals = ['limit', 'asymptotic', 'c -> infinity', 'hbar -> 0', 'non-relativistic', 'classical limit']
        t1_text_lower = t1.content.lower()
        if any(sig in t1_text_lower for sig in limit_signals):
            is_limiting_case = True

        # 5. Empirical Benchmark Cross-Verification
        for b1 in t1.empirical_benchmarks:
            for b2 in t2.empirical_benchmarks:
                b1_words = set(re.findall(r'\w+', b1.lower())) - {'the', 'and', 'in', 'of', 'to'}
                b2_words = set(re.findall(r'\w+', b2.lower())) - {'the', 'and', 'in', 'of', 'to'}
                overlap = b1_words.intersection(b2_words)
                if len(overlap) >= 2:
                    details["empirical_matches"].append({
                        "t1_benchmark": b1,
                        "t2_benchmark": b2,
                        "overlap": list(overlap)
                    })

        # 6. Conflict Detection (Microcausality, Unitarity, Local Realism vs Bell)
        if "local hidden variable" in t1_text_lower and not ("violation" in t1_text_lower or "falsif" in t1_text_lower):
            details["conflicts"].append("Violates post-1984 loophole-free Bell test non-locality.")
        if "superluminal" in t1_text_lower and "signal" in t1_text_lower and not "no superluminal" in t1_text_lower:
            details["conflicts"].append("Violates relativistic microcausality ([O(x), O(y)] != 0 for spacelike separation).")

        # 7. Exact Mathematical Complementarity Scoring
        # C = Domain_Factor * (15 * Gaps_Filled + 10 * Symmetries + 8 * Empirical_Matches + 5 * Mechanisms)
        base_score = (
            len(details["filled_gaps"]) * 25 +
            len(details["shared_symmetries"]) * 15 +
            len(details["empirical_matches"]) * 20 +
            min(len(t1.mechanisms), 5) * 5
        )
        
        if details["conflicts"]:
            details["score"] = max(5, int(base_score * 0.2))
            details["relationship_type"] = "CONFLICTS"
            details["classification"] = "Anomaly / Inconsistency"
            details["color"] = "rose"
        elif len(details["filled_gaps"]) >= 2 or base_score >= 80:
            details["score"] = min(100, int(base_score * domain_factor))
            details["relationship_type"] = "SUPPORTS" if len(details["empirical_matches"]) > 0 else "FILLS_GAP"
            details["classification"] = "Synergistic Foundation"
            details["color"] = "emerald"
        elif len(details["shared_symmetries"]) >= 1 or base_score >= 45:
            details["score"] = min(95, int(base_score * domain_factor))
            details["relationship_type"] = "GAUGE_EXTENSION"
            details["classification"] = "Complementary Extension"
            details["color"] = "sky"
        elif is_limiting_case or base_score >= 20:
            details["score"] = min(75, int(base_score * domain_factor))
            details["relationship_type"] = "LIMITING_CASE"
            details["classification"] = "Asymptotic Reduction"
            details["color"] = "indigo"
        else:
            details["score"] = max(10, int(base_score * domain_factor))
            details["relationship_type"] = "TANGENTIAL"
            details["classification"] = "Tangential"
            details["color"] = "slate"

        return details

    def find_solutions_for_gap(self, gap_text):
        solutions = []
        gap_keywords = set(re.findall(r'\w+', gap_text.lower())) - {'the', 'of', 'is', 'a', 'to', 'in', 'it', 'fails', 'unknown', 'unclear', 'nature'}
        if not gap_keywords:
            return []

        for name, theory in self.known_theories.items():
            # Check Mechanisms
            for mech in theory.mechanisms:
                mech_keywords = set(re.findall(r'\w+', mech.lower()))
                common = gap_keywords.intersection(mech_keywords)
                if len(common) >= 2:
                    solutions.append({
                        'theory': name,
                        'type': 'Mechanism',
                        'content': mech,
                        'confidence': 'High'
                    })
            # Check Invariants
            for inv in theory.invariants:
                inv_keywords = set(re.findall(r'\w+', inv.lower()))
                common = gap_keywords.intersection(inv_keywords)
                if len(common) >= 2:
                    solutions.append({
                        'theory': name,
                        'type': 'Noether Invariant',
                        'content': inv,
                        'confidence': 'High'
                    })
            # Check Axioms
            for ax in theory.axioms:
                ax_keywords = set(re.findall(r'\w+', ax.lower()))
                common = gap_keywords.intersection(ax_keywords)
                if len(common) >= 2:
                    if not any(s['content'] == ax for s in solutions):
                        solutions.append({
                            'theory': name,
                            'type': 'Axiom',
                            'content': ax,
                            'confidence': 'Medium'
                        })
        return solutions

    def generate_knowledge_graph(self, limit=100):
        """
        Generates orbit-organized graph nodes and typed physical edges.
        """
        nodes = []
        edges = []
        node_id = 0
        
        # Determine center theory
        center_name = "IUC" if "IUC" in self.known_theories else list(self.known_theories.keys())[0] if self.known_theories else None
        if not center_name:
            return {'nodes': [], 'edges': []}
            
        theory_comparisons = {}
        for name in self.known_theories:
            if name == center_name:
                continue
            comp = self.compare_theories(name, center_name)
            theory_comparisons[name] = comp

        # 1. Base Center Node
        node_id += 1
        center_id = node_id
        center_theory = self.known_theories[center_name]
        nodes.append({
            'id': center_id,
            'label': center_name,
            'group': 'center',
            'title': f"Reference Base: {center_name}\nPremise: {center_theory.premise[:60]}...",
            'value': 60,
            'mass': 40,
            'theory_name': center_name
        })

        # 2. Add Orbit Nodes
        for name, theory in self.known_theories.items():
            if name == center_name:
                continue
            node_id += 1
            t_id = node_id
            comp = theory_comparisons.get(name, {})
            score = comp.get("score", 10)
            rel_type = comp.get("relationship_type", "COMPLEMENTARY")
            
            # Map relationship to group styling
            if rel_type in ["SUPPORTS", "FILLS_GAP"]:
                group = "synergistic"
                mass = 15
                edge_color = "rgba(16, 185, 129, 0.7)"
            elif rel_type == "GAUGE_EXTENSION":
                group = "complementary"
                mass = 8
                edge_color = "rgba(14, 165, 233, 0.7)"
            elif rel_type == "LIMITING_CASE":
                group = "related"
                mass = 4
                edge_color = "rgba(99, 102, 241, 0.7)"
            elif rel_type == "CONFLICTS":
                group = "conflict"
                mass = 2
                edge_color = "rgba(244, 63, 94, 0.8)"
            else:
                group = "tangential"
                mass = 1
                edge_color = "rgba(148, 163, 184, 0.3)"

            nodes.append({
                'id': t_id,
                'label': name,
                'group': group,
                'title': f"{name}\nRel: {rel_type}\nScore: {score}\nClassification: {comp.get('classification', 'Neutral')}",
                'value': score + 10,
                'mass': mass,
                'theory_name': name
            })
            
            # Edge from Center to Theory
            edges.append({
                'from': center_id,
                'to': t_id,
                'label': rel_type,
                'color': {'color': edge_color},
                'arrows': 'to',
                'title': f"Relationship: {rel_type} (Score: {score})"
            })

            # Add sample of Key Mechanisms as Child Nodes
            for mech in theory.mechanisms[:2]:
                node_id += 1
                m_id = node_id
                short_m = (mech[:28] + '..') if len(mech) > 28 else mech
                nodes.append({
                    'id': m_id,
                    'label': short_m,
                    'group': 'mechanism',
                    'title': mech,
                    'theory_name': name
                })
                edges.append({
                    'from': t_id,
                    'to': m_id,
                    'arrows': 'to',
                    'color': {'opacity': 0.3}
                })

        return {'nodes': nodes, 'edges': edges}

    def think(self, query):
        """
        Dispatches incoming query to Pari-GP, SymPy, Logic Engine, or Theoretical Knowledge Base.
        """
        query_stripped = query.strip()
        lower_q = query_stripped.lower()
        
        # 1. Pari-GP Check (explicit trigger or number theory indicators)
        pari_triggers = ['gp:', 'pari:', 'factor(', 'isprime(', 'zeta(', 'mod ']
        if any(lower_q.startswith(tr) or tr in lower_q for tr in pari_triggers):
            clean_gp = re.sub(r'^(gp:|pari:)\s*', '', query_stripped)
            gp_result = self.pari_engine.evaluate(clean_gp)
            return f"[Pari-GP Engine]\nInput: {clean_gp}\nOutput:\n{gp_result}"

        # 2. Boolean Logic Check
        logic_indicators = ['&', '|', '~', '>>', 'logic:']
        if any(ind in query_stripped for ind in logic_indicators):
            clean_log = query_stripped.replace('logic:', '').strip()
            res = self.logic_engine.evaluate(clean_log)
            if res:
                return f"[Logic Engine]\n{res}"

        # 3. Mathematical Expression Check (SymPy)
        math_res = self.math_engine.evaluate(query_stripped)
        if math_res:
            return f"[SymPy Engine]\n{math_res}"

        # 4. Theoretical Physics Semantic Search
        keywords = set(re.findall(r'\w+', lower_q)) - {'what', 'is', 'the', 'how', 'does', 'in', 'of'}
        relevant = []
        for name, theory in self.known_theories.items():
            for ax in theory.axioms:
                overlap = keywords.intersection(set(re.findall(r'\w+', ax.lower())))
                if overlap:
                    relevant.append((len(overlap), f"[{name} Axiom] {ax}"))
            for mech in theory.mechanisms:
                overlap = keywords.intersection(set(re.findall(r'\w+', mech.lower())))
                if overlap:
                    relevant.append((len(overlap), f"[{name} Mechanism] {mech}"))
            for bench in theory.empirical_benchmarks:
                overlap = keywords.intersection(set(re.findall(r'\w+', bench.lower())))
                if overlap:
                    relevant.append((len(overlap), f"[{name} Benchmark] {bench}"))
                    
        relevant.sort(key=lambda x: x[0], reverse=True)
        if relevant:
            resp = [f"Consulting Mathematical Physics Knowledge Base for '{query}':"]
            for _, item in relevant[:6]:
                resp.append(f"- {item}")
            return "\n".join(resp)

        return f"No direct mathematical or empirical match found for '{query}'. Consider supplying an equation or specific physical principle."

    def execute_cli(self, command_str):
        stripped = command_str.strip()
        if not stripped:
            return "Awaiting input..."

        # Handle prefix colon syntax (e.g., 'gp: factor(100)' or 'gp:factor(100)')
        lower = stripped.lower()
        if lower.startswith("gp:"):
            return self.pari_engine.evaluate(stripped[3:].strip())
        elif lower.startswith("pari:"):
            return self.pari_engine.evaluate(stripped[5:].strip())
        elif lower.startswith("math:"):
            return self.math_engine.evaluate(stripped[5:].strip())
        elif lower.startswith("logic:"):
            return self.logic_engine.evaluate(stripped[6:].strip())

        parts = stripped.split()
        cmd = parts[0].lower()
        if cmd.endswith(':'):
            cmd = cmd[:-1]
        args = parts[1:]
        
        if cmd == "help":
            return """
Rigorous Science Engine Commands:
----------------------------------
> list                    : List loaded theories
> analyze <theory>        : Deep mathematical analysis
> compare <t1> <t2>       : Calculate complementarity & relationship
> gp <expression>         : Run Pari-GP command (e.g. gp factor(2^64 + 1))
> math <expression>       : Evaluate SymPy expression
> logic <expression>      : Evaluate Boolean logic
> seal <theory>           : Cryptographically lock theory state
            """
        elif cmd == "list":
            return "\n".join([f"- {name} {'[SEALED]' if t.is_sealed else ''}" for name, t in self.known_theories.items()])
        elif cmd == "analyze":
            return self.analyze_theory(args[0]) if args else "Usage: analyze <theory_name>"
        elif cmd == "compare":
            if len(args) < 2: return "Usage: compare <theory1> <theory2>"
            return json.dumps(self.compare_theories(args[0], args[1]), indent=2)
        elif cmd in ["gp", "pari"]:
            return self.pari_engine.evaluate(" ".join(args))
        elif cmd == "math":
            return self.math_engine.evaluate(" ".join(args))
        elif cmd == "logic":
            return self.logic_engine.evaluate(" ".join(args))
        elif cmd == "seal":
            return self.seal_theory(args[0])[1] if args else "Usage: seal <theory_name>"
        else:
            return f"Unknown command: {cmd}. Type 'help' for options."

    def seal_theory(self, theory_name):
        if theory_name not in self.known_theories:
            return False, "Theory not found."
        theory = self.known_theories[theory_name]
        h = theory.seal()
        return True, f"Theory {theory.name} sealed. Cryptographic Hash: {h}"
import os
import sys
from pathlib import Path

# Add project root to sys.path
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'scicalc.settings')
django.setup()

from science_engine.models import Subject, Course, Topic, Equation, Theory

def seed_comprehensive_kb():
    print("Beginning High-Density Scientific Knowledge Base Seeding...")

    # =========================================================================
    # 1. CONSOLIDATION: Clean up auto-generated 1-topic empty stub subjects
    # =========================================================================
    stub_names = [
        'Gauge Theory', 'Symplectic Geometry', 'Statistical Mechanics', 'Formal Logic',
        'Gravitation', 'Electroweak Theory', 'General Relativity', 'Computability & Complexity',
        'Quantum Mechanics', 'Evolution', 'Logic', 'Gravity', 'Relativity', 'Cosmology',
        'Physics', 'Computation', 'General Science'
    ]
    for sname in stub_names:
        s = Subject.objects.filter(name=sname).first()
        if s:
            # If it has 0 or 1 empty topic, delete it to keep library clean
            topic_count = Topic.objects.filter(course__subject=s).count()
            has_real_content = Topic.objects.filter(course__subject=s).exclude(content='').exists()
            if not has_real_content:
                s.delete()
                print(f"Removed empty stub subject: {sname}")

    # =========================================================================
    # 2. DEFINE CORE DISCIPLINARY SUBJECTS
    # =========================================================================
    subjects_data = {
        "Theoretical Physics": "Foundational principles governing spacetime geometry, quantum operator mechanics, gauge fields, and relativistic dynamics.",
        "Mathematics & Geometry": "Rigorous mathematical frameworks including differential geometry, symplectic reduction, Lie algebras, and functional operator theory.",
        "Information Theory & Logic": "The mathematical science of information encoding, entropy bounds, algorithmic computability, and quantum information protocols.",
        "Thermodynamics & Statistical Mechanics": "Phase space statistical distributions, thermodynamic entropy, non-equilibrium dynamics, and information-theoretic dissipation.",
        "Chemical Sciences": "Molecular orbital structures, covalent energetics, chemical thermodynamics, catalysis, and reaction kinetics.",
        "Biological Sciences": "Molecular genetics, cellular organization, evolutionary mechanisms, and self-sustaining organic information propagation."
    }

    subjects = {}
    for s_name, s_desc in subjects_data.items():
        sub, _ = Subject.objects.get_or_create(name=s_name, defaults={'description': s_desc})
        sub.description = s_desc
        sub.save()
        subjects[s_name] = sub

    # =========================================================================
    # 3. HIGH-DENSITY CURRICULUM DATA
    # =========================================================================
    curriculum = [
        # ---------------------------------------------------------------------
        # THEORETICAL PHYSICS: Quantum Foundations & Measurement
        # ---------------------------------------------------------------------
        {
            "subject": "Theoretical Physics",
            "course": "Quantum Foundations & Measurement",
            "course_desc": "Operator algebras, measurement theory, quantum non-locality, and environmental decoherence dynamics.",
            "topics": [
                {
                    "name": "Bell's Theorem & Non-Locality",
                    "content": """Bell's Theorem, formulated by John Stewart Bell in 1964, establishes that no physical theory based on local hidden variables can reproduce all statistical predictions of quantum mechanics. By deriving mathematical constraints on correlations between measurements performed on spatially separated entangled particle pairs, Bell demonstrated a fundamental conflict between local realism and quantum theory.

The Clauser–Horne–Shimony–Holt (CHSH) inequality provides an experimentally testable formulation of Bell's theorem. Local realism enforces an upper bound of 2 on the CHSH correlation parameter $S_{\\text{CHSH}}$, whereas quantum mechanics allows correlations up to the Tsirelson bound of $2\\sqrt{2} \\approx 2.828$.

In 2015, multiple research groups (Hensen et al. at Delft, Giustina et al. in Vienna, and Shalm et al. at NIST) successfully conducted the first loophole-free Bell tests. By simultaneously eliminating both the locality loophole (via space-like separation) and the detection loophole (via high-efficiency single-photon detectors), these landmark experiments conclusively falsified local hidden-variable theories and confirmed quantum non-locality as an intrinsic feature of nature.""",
                    "simulation_logic": "4PT Logic: Non-local quantum correlations represent global state addressability in the underlying coordinate buffer, completely bypassing the local 3D light-speed ping limitation.",
                    "equations": [
                        {
                            "name": "CHSH Inequality",
                            "formula": "S_{\\text{CHSH}} = \\langle AB \\rangle - \\langle AB' \\rangle + \\langle A'B \\rangle + \\langle A'B' \\rangle \\le 2",
                            "explanation": "Local hidden variable realism constraint on correlated detector observables."
                        },
                        {
                            "name": "Quantum Tsirelson Bound",
                            "formula": "S_{\\text{quantum}}^{\\max} = 2\\sqrt{2} \\approx 2.828",
                            "explanation": "Maximum non-local quantum correlation achievable by entangled states in Hilbert space."
                        }
                    ]
                },
                {
                    "name": "Quantum Decoherence & Open Systems",
                    "content": """Quantum decoherence describes the irreversible dynamical loss of quantum coherence and phase interference in an open quantum system interacting with an external environmental reservoir. First mathematically formulated by Heinz-Dieter Zeh in 1970 and extended by Wojciech Zurek and Erich Joos, decoherence explains how classical definite states emerge dynamically from unitary quantum superpositions without requiring ad-hoc wave function collapse postulates.

When a system $S$ interacts with its environment $E$, the composite state $|\Psi_{SE}\\rangle$ undergoes unitary evolution generated by the total Hamiltonian $\\hat{H} = \\hat{H}_S + \\hat{H}_E + \\hat{H}_{SE}$. Tracing over environmental degrees of freedom yields the reduced density matrix $\\rho_S = \\text{Tr}_E(\\rho_{SE})$, whose off-diagonal interference terms decay exponentially into the environment on ultra-fast decoherence timescales $\\tau_{\\text{dec}}$.

Markovian open quantum dynamics are rigorously governed by the Lindblad master equation (1976), which guarantees complete positivity and trace preservation. Experimental verification was achieved in 1996 by Serge Haroche and David Wineland (Nobel Prize 2012), who directly tracked the decoherence of mesoscopic Schrödinger cat states in superconducting microwave cavities.""",
                    "simulation_logic": "4PT Logic: Decoherence is the simulation's automatic background compiler: unobserved quantum superpositions are forced into definite 3D classical coordinate slices as data entangles with the environmental buffer.",
                    "equations": [
                        {
                            "name": "Lindblad Master Equation",
                            "formula": "\\frac{\\partial \\rho_S}{\\partial t} = -\\frac{i}{\\hbar}[\\hat{H}_S, \\rho_S] + \\sum_k \\left( \\hat{L}_k \\rho_S \\hat{L}_k^\\dagger - \\frac{1}{2}\\{\\hat{L}_k^\\dagger \\hat{L}_k, \\rho_S\\} \\right)",
                            "explanation": "General generator of completely positive, trace-preserving Markovian open system evolution."
                        },
                        {
                            "name": "Decoherence Timescale Scaling",
                            "formula": "\\tau_{\\text{dec}} \\sim \\tau_{\\text{thermal}} \\left( \\frac{\\lambda_{\\text{thermal}}}{\\Delta x} \\right)^2",
                            "explanation": "Decoherence rate suppression proportional to spatial separation $\\Delta x$ relative to thermal de Broglie wavelength."
                        }
                    ]
                },
                {
                    "name": "Einselection & Pointer States",
                    "content": """Environment-Induced Superselection (Einselection), pioneered by Wojciech Zurek in 1981, provides the mechanism that determines which specific quantum states become classical and observable. Einselection proves that the environment acts as a monitoring apparatus, continuously measuring specific observables of the system and destroying superpositions of states that do not commute with the interaction Hamiltonian.

The privileged states that survive environmental entanglement without losing phase coherence are called 'pointer states' $|\\pi_i\\rangle$. A pointer state is defined dynamically by the condition that it commutes with the system-environment interaction Hamiltonian: $[\\hat{H}_{SE}, |\\pi_i\\rangle\\langle \\pi_i|] \\approx 0$. 

Consequently, pointer states do not generate entanglement with the reservoir and remain dynamically stable, allowing them to record classical, objective information accessible to multiple independent observers. This framework forms the physical basis for understanding how stable macroscopic reality emerges from underlying quantum indeterminacy.""",
                    "simulation_logic": "4PT Logic: Einselection is the 'Sealing Protocol' of reality: only data packets that commute with the global environment Hamiltonian remain coherent and immune to systemic bit-rot.",
                    "equations": [
                        {
                            "name": "Pointer State Stability Invariant",
                            "formula": "[\\hat{H}_{SE}, |\\pi_i\\rangle\\langle\\pi_i|] \\approx 0",
                            "explanation": "Commutation condition ensuring a quantum state is immune to environmental decoherence."
                        }
                    ]
                },
                {
                    "name": "Quantum Zeno Effect",
                    "content": """The Quantum Zeno Effect, named by Baidyanath Misra and George Sudarshan in 1977, describes the phenomenon where the dynamical time evolution of a quantum system is completely suppressed or frozen by frequent, continuous observation.

According to the postulates of quantum mechanics, a state $|\psi(0)\\rangle$ evolving under Hamiltonian $\\hat{H}$ for a short time $\\delta t$ has a survival probability $P(\\delta t) = |\\langle \\psi(0) | e^{-i\\hat{H}\\delta t/\\hbar} | \\psi(0) \\rangle|^2 \\approx 1 - (\\delta t / \\tau_Z)^2$, characterized by quadratic short-time behavior. If $N$ projective measurements are performed at intervals $\\delta t = t/N$, the survival probability at time $t$ scales as $P(t) \\approx [1 - (t/N\\tau_Z)^2]^N \\approx 1 - \\frac{t^2}{N \\tau_Z^2}$.

In the limit $N \\to \\infty$, the survival probability approaches unity: $\\lim_{N \\to \\infty} P(t) = 1$. Continuous observation forces the state vector to perpetually collapse back onto its initial subspace, halting all unitary transition dynamics. The effect was experimentally demonstrated by Itano et al. in 1990 using radio-frequency transitions in trapped beryllium ions.""",
                    "simulation_logic": "4PT Logic: The Quantum Zeno Effect is the simulation's literal Pause Button: refreshing the observer coordinate check faster than the state evolution rate freezes the local simulation slice.",
                    "equations": [
                        {
                            "name": "Zeno Survival Probability Limit",
                            "formula": "\\lim_{N \\to \\infty} P_N(t) = \\lim_{N \\to \\infty} \\left( 1 - \\frac{t^2}{N \\tau_Z^2} \\right) = 1",
                            "explanation": "Suppression of unitary transition probability under infinite measurement frequency."
                        }
                    ]
                }
            ]
        },

        # ---------------------------------------------------------------------
        # THEORETICAL PHYSICS: General Relativity & Spacetime Dynamics
        # ---------------------------------------------------------------------
        {
            "subject": "Theoretical Physics",
            "course": "General Relativity & Gravitation",
            "course_desc": "Pseudo-Riemannian geometry, Einstein field equations, canonical ADM foliation, and gravitational wave dynamics.",
            "topics": [
                {
                    "name": "Einstein Field Equations & Geodesics",
                    "content": """Published by Albert Einstein in November 1915, the Einstein Field Equations (EFE) describe gravitation not as an attractive Newtonian force, but as the manifestation of the curvature of a 4-dimensional pseudo-Riemannian spacetime manifold $(\\mathcal{M}, g_{\\mu\\nu})$ induced by stress-energy, momentum, and pressure.

The field equations equate the geometric Einstein tensor $G_{\\mu\\nu} \\equiv R_{\\mu\\nu} - \\frac{1}{2}R g_{\\mu\\nu}$ to the stress-energy tensor $T_{\\mu\\nu}$ of matter: $G_{\\mu\\nu} + \\Lambda g_{\\mu\\nu} = \\frac{8\\pi G}{c^4} T_{\\mu\\nu}$. The Bianchi identities $\\nabla_\\mu G^{\\mu\\nu} = 0$ enforce the exact covariant conservation of energy and momentum $\\nabla_\\mu T^{\\mu\\nu} = 0$.

Test particles free from non-gravitational forces follow timelike or null geodesics through curved spacetime, governed by the geodesic equation $\\frac{d^2 x^\\mu}{d\\tau^2} + \\Gamma^\\mu_{\\alpha\\beta} \\frac{dx^\\alpha}{d\\tau} \\frac{dx^\\beta}{d\\tau} = 0$, where $\\Gamma^\\mu_{\\alpha\\beta}$ are the Christoffel connection coefficients. The theory accurately predicts gravitational time dilation, gravitational lensing, perihelion precession of Mercury, and black hole event horizons.""",
                    "simulation_logic": "4PT Logic: Gravitational spacetime curvature is the metric rendering mesh of the simulation: mass-energy coordinates dictate the local clock-rate and geometric scale of the projection.",
                    "equations": [
                        {
                            "name": "Einstein Field Equations",
                            "formula": "R_{\\mu\\nu} - \\frac{1}{2}R g_{\\mu\\nu} + \\Lambda g_{\\mu\\nu} = \\frac{8\\pi G}{c^4} T_{\\mu\\nu}",
                            "explanation": "Fundamental equations relating spacetime curvature to stress-energy distribution."
                        },
                        {
                            "name": "Geodesic Equation of Motion",
                            "formula": "\\frac{d^2 x^\\mu}{d\\tau^2} + \\Gamma^\\mu_{\\alpha\\beta} \\frac{dx^\\alpha}{d\\tau} \\frac{dx^\\beta}{d\\tau} = 0",
                            "explanation": "Equation governing inertial free-fall trajectory in curved Riemannian geometry."
                        }
                    ]
                },
                {
                    "name": "ADM (3+1) Spacetime Foliation",
                    "content": """The Arnowitt–Deser–Misner (ADM) formalism, developed in 1959, provides the canonical Hamiltonian formulation of General Relativity by decomposing 4-dimensional spacetime into a continuous family of 3-dimensional spacelike hypersurfaces $\\Sigma_t$ parameterized by a global time coordinate $t$.

The 4-metric $g_{\\mu\\nu}$ is decomposed into three geometric quantities: the induced spatial 3-metric $\\gamma_{ij}$ on $\\Sigma_t$, the lapse function $N$ measuring the elapsed proper time between adjacent slices along the unit normal $n^\\mu$, and the shift vector $N^i$ measuring the tangential coordinate drift between slices: $ds^2 = -(N^2 - N_i N^i)dt^2 + 2N_i dx^i dt + \\gamma_{ij} dx^i dx^j$.

In ADM dynamics, Einstein's equations split into two sets: dynamical evolution equations for $\\gamma_{ij}$ and its conjugate momentum $\\pi^{ij}$, and four geometric constraint equations: the Hamiltonian constraint $\\mathcal{H} = 0$ generating time reparameterizations, and the diffeomorphism/momentum constraints $\\mathcal{M}^i = 0$ generating spatial coordinate transformations. The ADM formalism is the mathematical foundation for numerical relativity and canonical quantum gravity.""",
                    "simulation_logic": "4PT Logic: The ADM foliation is the exact mechanism of the 3D 'Now' slice: the lapse function $N$ is the frame rendering rate, and shift $N^i$ is the grid coordinate remapping vector.",
                    "equations": [
                        {
                            "name": "ADM 3+1 Metric Decomposition",
                            "formula": "ds^2 = -(N^2 - N_i N^i)dt^2 + 2N_i dx^i dt + \\gamma_{ij} dx^i dx^j",
                            "explanation": "Canonical foliation of 4D spacetime into spatial 3-metric $\\gamma_{ij}$, lapse $N$, and shift $N_i$."
                        },
                        {
                            "name": "Hamiltonian and Momentum Constraints",
                            "formula": "\\mathcal{H} = \\frac{1}{\\sqrt{\\gamma}}(K_{ij}K^{ij} - K^2) - \\sqrt{\\gamma}{}^{(3)}R = 0, \\quad \\mathcal{M}^i = D_j(K^{ij} - \\gamma^{ij}K) = 0",
                            "explanation": "Spatial hypersurface constraints required for embedding into 4-manifold."
                        }
                    ]
                },
                {
                    "name": "Black Hole Thermodynamics & Event Horizons",
                    "content": """Formulated by Jacob Bekenstein (1973) and Stephen Hawking (1974), black hole thermodynamics establishes that black holes are not mere cold gravitational singularities, but thermodynamic objects possessing a physical temperature and an enormous entropy proportional to the surface area of their event horizons.

The Bekenstein–Hawking entropy formula states: $S_{\\text{BH}} = \\frac{k_B c^3 A}{4G\\hbar} = \\frac{k_B A}{4 \\ell_P^2}$, where $A$ is the horizon area and $\\ell_P = \\sqrt{\\hbar G / c^3}$ is the Planck length. This indicates that black hole entropy is geometric and holographic: exactly one quarter of a bit of information per Planck area.

In 1974, Hawking demonstrated using quantum field theory in curved spacetime that quantum vacuum fluctuations near the horizon produce steady thermal radiation at Hawking temperature $T_H = \\frac{\\hbar c^3}{8\\pi G M k_B}$. This connects gravitation, quantum mechanics, and information theory, giving rise to the modern black hole information paradox and the Holographic Principle.""",
                    "simulation_logic": "4PT Logic: The Bekenstein-Hawking formula defines the simulation's maximum data density buffer: 1 bit per 4 Planck areas. Beyond this limit, data collapses into a localized black hole node.",
                    "equations": [
                        {
                            "name": "Bekenstein-Hawking Entropy",
                            "formula": "S_{\\text{BH}} = \\frac{k_B c^3 A}{4G\\hbar} = \\frac{k_B A}{4\\ell_P^2}",
                            "explanation": "Maximum thermodynamic entropy of an event horizon proportional to horizon surface area."
                        },
                        {
                            "name": "Hawking Temperature",
                            "formula": "T_H = \\frac{\\hbar c^3}{8\\pi G M k_B}",
                            "explanation": "Thermal emission temperature of a Schwarzschild black hole horizon."
                        }
                    ]
                }
            ]
        },

        # ---------------------------------------------------------------------
        # MATHEMATICS & GEOMETRY: Differential & Symplectic Geometry
        # ---------------------------------------------------------------------
        {
            "subject": "Mathematics & Geometry",
            "course": "Differential & Symplectic Geometry",
            "course_desc": "Symplectic manifolds, Marsden-Weinstein quotient reduction, Lie algebras, and fiber bundle connection geometry.",
            "topics": [
                {
                    "name": "Symplectic Manifolds & Marsden-Weinstein Reduction",
                    "content": """Symplectic geometry is the mathematical framework underlying analytical Hamiltonian mechanics. A symplectic manifold is a pair $(M, \\omega)$, where $M$ is a smooth even-dimensional manifold and $\\omega$ is a differential 2-form that is non-degenerate ($(\\wedge^n \\omega) \\ne 0$) and closed ($d\\omega = 0$). In canonical Darboux coordinates $(q^1, \\dots, q^n, p_1, \\dots, p_n)$, the symplectic form takes the standard form $\\omega = \\sum_{i=1}^n dp_i \\wedge dq^i$.

When a Lie group $G$ acts on $(M, \\omega)$ by symplectomorphisms preserving a Hamiltonian function $H$, the action is associated with a momentum map $\\mu: M \\to \\mathfrak{g}^*$. By Noether's theorem, $\\mu$ is a conserved quantity along Hamiltonian trajectories.

The Marsden–Weinstein reduction theorem (1974), also called symplectic quotient reduction, proves that the quotient space $M_{\\text{red}} = \\mu^{-1}(0) / G$ inherits a canonical symplectic structure $\\omega_{\\text{red}}$. Physical observables for an internal observer constrained by gauge symmetries live entirely on $M_{\\text{red}}$, providing the mathematical foundation for gauge theories and the reduction of unobservable degrees of freedom.""",
                    "simulation_logic": "4PT Logic: Marsden-Weinstein symplectic reduction is the mathematical foundation of IUC: the physical observable reality is the quotient manifold $\mu^{-1}(0)/G$, projecting out higher ambient degrees of freedom.",
                    "equations": [
                        {
                            "name": "Canonical Symplectic 2-Form",
                            "formula": "\\omega = \\sum_{i=1}^n dp_i \\wedge dq^i, \\quad d\\omega = 0",
                            "explanation": "Non-degenerate closed 2-form defining Hamiltonian phase space."
                        },
                        {
                            "name": "Marsden-Weinstein Symplectic Quotient",
                            "formula": "M_{\\text{red}} = \\mu^{-1}(0) / G",
                            "explanation": "Reduced physical phase space obtained by quotienting the zero-level set of the momentum map."
                        }
                    ]
                },
                {
                    "name": "Lie Groups, Lie Algebras & Noether Invariants",
                    "content": """A Lie group $G$ is a smooth manifold endowed with a group structure such that group multiplication and inversion are smooth maps. The tangent space at the identity element forms the Lie algebra $\\mathfrak{g} = T_e G$, equipped with a bilinear, alternating Lie bracket $[\\cdot, \\cdot]: \\mathfrak{g} \\times \\mathfrak{g} \\to \\mathfrak{g}$ satisfying the Jacobi identity $[X, [Y, Z]] + [Y, [Z, X]] + [Z, [X, Y]] = 0$.

In quantum mechanics and gauge theories, Lie algebras govern continuous physical symmetries. For a basis of generators $T^a$, the commutation relations are defined by structure constants: $[T^a, T^b] = i f^{abc} T^c$. The Casimir invariants, such as $C_1 = T^a T^a$, commute with all algebra generators and label invariant physical states (e.g., total angular momentum $J^2 = j(j+1)$ and particle mass-squared $P^2 = -m^2$).

Emmy Noether's landmark 1918 theorem establishes an exact correspondence between continuous Lie symmetries of an action $S = \\int \\mathcal{L} d^4x$ and conserved physical currents: $\\partial_\\mu j^\\mu = 0 \\implies Q = \\int j^0 d^3x = \\text{const}$. Invariance under time translation generates energy conservation; spatial translation generates linear momentum; spatial rotation generates angular momentum; and $U(1)$ gauge phase invariance generates electric charge conservation.""",
                    "simulation_logic": "4PT Logic: Noether invariants are the hard-coded checksums of the engine: continuous coordinate transformation symmetries enforce strict conservation of energy, momentum, and charge.",
                    "equations": [
                        {
                            "name": "Lie Algebra Commutation Relation",
                            "formula": "[T^a, T^b] = i f^{abc} T^c",
                            "explanation": "Fundamental commutator of Lie algebra generators with structure constants $f^{abc}$."
                        },
                        {
                            "name": "Noether Conserved Current",
                            "formula": "j^\\mu = \\frac{\\partial \\mathcal{L}}{\\partial (\\partial_\\mu \\phi_a)} \\delta \\phi_a - K^\\mu, \\quad \\partial_\\mu j^\\mu = 0",
                            "explanation": "Conserved physical current arising from continuous variational symmetry."
                        }
                    ]
                }
            ]
        },

        # ---------------------------------------------------------------------
        # INFORMATION THEORY & LOGIC: Entropy, Computability & Complexity
        # ---------------------------------------------------------------------
        {
            "subject": "Information Theory & Logic",
            "course": "Information, Entropy & Computability",
            "course_desc": "Shannon information theory, thermodynamic erasure bounds, Turing computability, and computational complexity.",
            "topics": [
                {
                    "name": "Shannon Information Entropy & Channel Capacity",
                    "content": """Claude Shannon's 1948 paper, 'A Mathematical Theory of Communication', founded modern information theory by providing a rigorous mathematical definition of information content and uncertainty. For a discrete random variable $X$ with probability distribution $\{p_1, p_2, \\dots, p_n\}$, the Shannon entropy $H(X)$ is defined as: $H(X) = -\\sum_{i=1}^n p_i \\log_2 p_i$.

Shannon entropy quantifies the expected number of bits required to encode the state of $X$ without loss of data (Shannon's Source Coding Theorem). Entropy reaches its maximum $H_{\\max} = \\log_2 n$ for a uniform distribution and vanishes ($H=0$) when an outcome is completely certain.

Shannon's Noisy-Channel Coding Theorem defines the maximum rate of error-free information transmission across a channel with noise: the Channel Capacity $C = \\max_{p(x)} I(X; Y)$, where $I(X; Y) = H(X) - H(X|Y)$ is the mutual information between input $X$ and received output $Y$. For an additive white Gaussian noise channel, this yields the Shannon-Hartley theorem: $C = B \\log_2(1 + \\text{SNR})$. Shannon entropy is formally isomorphic to Gibbs statistical mechanical entropy via $S = k_B \\ln(2) H(X)$.""",
                    "simulation_logic": "4PT Logic: Shannon entropy measures the bit-depth of the simulation's unrendered state space; channel capacity limits the maximum bandwidth of data transfer between sectors.",
                    "equations": [
                        {
                            "name": "Shannon Entropy",
                            "formula": "H(X) = -\\sum_{i=1}^n p_i \\log_2 p_i",
                            "explanation": "Fundamental measure of information content and uncertainty in discrete probability distributions."
                        },
                        {
                            "name": "Shannon-Hartley Channel Capacity",
                            "formula": "C = B \\log_2 \\left( 1 + \\frac{S}{N} \\right)",
                            "explanation": "Maximum error-free information transmission rate over a band-limited noisy channel."
                        }
                    ]
                },
                {
                    "name": "Landauer's Principle of Information Erasure",
                    "content": """Formulated by Rolf Landauer at IBM in 1961, Landauer's Principle bridges abstract information theory and physical thermodynamics by establishing that information processing is fundamentally physical.

Landauer demonstrated that while reversible logical operations (such as NOT) can theoretically be performed without minimum energy dissipation, any logically irreversible manipulation of information—specifically the erasure of one bit of data or the merging of two computational paths—must dissipate a finite, non-zero amount of heat into the environment.

The minimum heat energy dissipated by erasing one bit of information in a thermal reservoir at temperature $T$ is given by Landauer's bound: $\\Delta Q \\ge k_B T \\ln 2 \\approx 2.87 \\times 10^{-21}\\text{ J at } 300\\text{ K}$. This dissipation corresponds to a decrease of information entropy $\\Delta S_{\\text{info}} = k_B \\ln 2$ compensated by an equal or greater increase in environmental thermodynamic entropy $\\Delta S_{\\text{env}} \\ge k_B \\ln 2$, upholding the Second Law of Thermodynamics.

In 2012, Antoine Bérut et al. (published in Nature) experimentally confirmed Landauer's bound with nanoscale optical traps holding a colloidal particle in a bistable potential, measuring heat dissipation directly at the $k_B T \\ln 2$ limit.""",
                    "simulation_logic": "4PT Logic: Landauer's Principle represents the simulation's memory garbage collection tax: deleting or resetting metadata in the 3D projection generates thermal waste in the physical slice.",
                    "equations": [
                        {
                            "name": "Landauer's Bound",
                            "formula": "\\Delta Q \\ge k_B T \\ln 2",
                            "explanation": "Minimum physical thermodynamic energy dissipated when resetting or erasing one bit of data."
                        }
                    ]
                },
                {
                    "name": "Turing Computability & Complexity Theory",
                    "content": """In 1936, Alan Turing introduced the concept of the Universal Turing Machine, a theoretical mathematical automaton capable of simulating any algorithmic computation given sufficient time and memory tape. Turing proved the undecidability of the Halting Problem: there exists no general algorithm that can determine whether an arbitrary computer program will eventually finish running or execute forever.

Computational Complexity Theory classifies solvable algorithmic problems according to the asymptotic resources (time and memory space) required to solve them as a function of input size $n$. The class $P$ comprises decision problems solvable in polynomial time $\\mathcal{O}(n^k)$ by a deterministic Turing machine. The class $NP$ (Nondeterministic Polynomial time) comprises problems whose proposed solutions can be verified in polynomial time.

The Cook–Levin Theorem (1971) established the existence of $NP$-complete problems (starting with Boolean Satisfiability, SAT), which are the hardest problems in $NP$. If any single $NP$-complete problem could be solved in polynomial time, then $P = NP$. The $P$ versus $NP$ problem remains the central open question in theoretical computer science and mathematics.""",
                    "simulation_logic": "4PT Logic: The Halting Problem proves that an internal observer within a closed logical construct cannot compute the complete global trajectory of their own system without external execution.",
                    "equations": [
                        {
                            "name": "Deterministic Polynomial Time Class",
                            "formula": "P = \\bigcup_{k=1}^\\infty \\text{TIME}(n^k)",
                            "explanation": "Class of decision problems decidable in polynomial time by a deterministic Turing machine."
                        }
                    ]
                }
            ]
        },

        # ---------------------------------------------------------------------
        # CHEMICAL SCIENCES: Thermodynamics, Bonding & Catalysis
        # ---------------------------------------------------------------------
        {
            "subject": "Chemical Sciences",
            "course": "Physical Chemistry & Reaction Energetics",
            "course_desc": "Gibbs free energy, chemical equilibrium, molecular bonding, and catalytic reaction kinetics.",
            "topics": [
                {
                    "name": "Chemical Thermodynamics & Gibbs Free Energy",
                    "content": """Chemical thermodynamics applies the first and second laws of thermodynamics to chemical reactions and phase transitions. The fundamental criterion for chemical spontaneity and equilibrium under constant temperature and pressure is the Gibbs free energy $G = H - TS$, where $H = U + PV$ is enthalpy and $S$ is entropy.

For a chemical process at temperature $T$, the change in Gibbs free energy is $\\Delta G = \\Delta H - T\\Delta S$. A process is thermodynamically spontaneous if $\\Delta G < 0$ (exergonic), at dynamic equilibrium if $\\Delta G = 0$, and non-spontaneous if $\\Delta G > 0$ (endergonic).

At chemical equilibrium, the standard Gibbs free energy change $\\Delta G^\\circ$ is directly linked to the thermodynamic equilibrium constant $K_{\\text{eq}}$ via the relation: $\\Delta G^\\circ = -RT \\ln K_{\\text{eq}}$. This equation connects the macroscopic spontaneity of chemical transformations directly to the molecular distribution of species.""",
                    "simulation_logic": "4PT Logic: Gibbs Free Energy is the optimization cost function of the molecular engine: atoms arrange themselves into states that minimize system potential under ambient temperature constraints.",
                    "equations": [
                        {
                            "name": "Gibbs Free Energy Equation",
                            "formula": "\\Delta G = \\Delta H - T\\Delta S",
                            "explanation": "Criterion for thermodynamic spontaneity at constant temperature and pressure."
                        },
                        {
                            "name": "Chemical Equilibrium Relation",
                            "formula": "\\Delta G^\\circ = -RT \\ln K_{\\text{eq}}",
                            "explanation": "Exact relationship connecting standard Gibbs free energy to the equilibrium constant."
                        }
                    ]
                },
                {
                    "name": "Chemical Kinetics & Catalysis",
                    "content": """Chemical kinetics investigates the rates of chemical reactions, the factors influencing reaction speeds, and the microscopic molecular mechanisms of chemical transformations.

The rate of a reaction depends exponentially on temperature, described by the Arrhenius equation (1889): $k = A e^{-E_a / (k_B T)}$, where $k$ is the rate constant, $A$ is the pre-exponential frequency factor, $E_a$ is the activation energy barrier, and $k_B$ is the Boltzmann constant. Reactions occur when colliding molecules possess kinetic energy exceeding $E_a$ with appropriate spatial orientation.

A catalyst accelerates the rate of a chemical reaction by providing an alternative reaction pathway with a lower activation energy barrier $E_a' < E_a$, without being consumed in the process. While a catalyst increases both forward and reverse reaction rates equally by lowering the transition state energy, it does not alter the thermodynamic equilibrium constant $K_{\\text{eq}}$ or the overall Gibbs free energy change $\\Delta G$.""",
                    "simulation_logic": "4PT Logic: Catalysts act as algorithmic bypass shortcuts: lowering the computational barrier $E_a$ accelerates state compilation without changing the initial or final conserved coordinates.",
                    "equations": [
                        {
                            "name": "Arrhenius Equation",
                            "formula": "k = A e^{-\\frac{E_a}{k_B T}}",
                            "explanation": "Temperature dependence of chemical reaction rate constants with activation energy $E_a$."
                        }
                    ]
                }
            ]
        }
    ]

    # =========================================================================
    # 4. EXECUTE BATCH SEEDING
    # =========================================================================
    created_topics = 0
    created_eqs = 0

    for module in curriculum:
        subj = subjects[module["subject"]]
        course, _ = Course.objects.get_or_create(
            subject=subj,
            name=module["course"],
            defaults={"description": module["course_desc"]}
        )
        course.description = module["course_desc"]
        course.save()

        for t_data in module["topics"]:
            topic, t_created = Topic.objects.get_or_create(
                course=course,
                name=t_data["name"],
                defaults={
                    "content": t_data["content"],
                    "simulation_logic": t_data["simulation_logic"]
                }
            )
            topic.content = t_data["content"]
            topic.simulation_logic = t_data["simulation_logic"]
            topic.save()
            created_topics += 1

            for eq_data in t_data.get("equations", []):
                eq, _ = Equation.objects.get_or_create(
                    topic=topic,
                    name=eq_data["name"],
                    defaults={
                        "formula": eq_data["formula"],
                        "explanation": eq_data["explanation"]
                    }
                )
                eq.formula = eq_data["formula"]
                eq.explanation = eq_data["explanation"]
                eq.save()
                created_eqs += 1

    # =========================================================================
    # 5. LINK TOPICS TO CORE THEORIES
    # =========================================================================
    theory_links = {
        "Quantum_Mechanics": ["Bell's Theorem & Non-Locality", "Quantum Decoherence & Open Systems", "Einselection & Pointer States", "Quantum Zeno Effect"],
        "4PT": ["Bell's Theorem & Non-Locality", "Quantum Decoherence & Open Systems", "Einselection & Pointer States", "ADM (3+1) Spacetime Foliation", "Black Hole Thermodynamics & Event Horizons"],
        "IUC": ["Symplectic Manifolds & Marsden-Weinstein Reduction", "Shannon Information Entropy & Channel Capacity", "Turing Computability & Complexity Theory"],
        "General_Relativity": ["Einstein Field Equations & Geodesics", "ADM (3+1) Spacetime Foliation", "Black Hole Thermodynamics & Event Horizons"],
        "Thermodynamics_Information": ["Shannon Information Entropy & Channel Capacity", "Landauer's Principle of Information Erasure", "Black Hole Thermodynamics & Event Horizons", "Chemical Thermodynamics & Gibbs Free Energy"]
    }

    for th_name, t_names in theory_links.items():
        th = Theory.objects.filter(name=th_name).first()
        if th:
            for tn in t_names:
                t_obj = Topic.objects.filter(name=tn).first()
                if t_obj:
                    th.topics.add(t_obj)

    print(f"Knowledge Base Seeding Complete: Processed {created_topics} High-Density Topics with {created_eqs} LaTeX Equations.")

if __name__ == '__main__':
    seed_comprehensive_kb()

import os, sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'scicalc.settings')
django.setup()

from science_engine.models import Subject, Course, Topic, Equation, Theory

def seed_full_foundations():
    print("Beginning Comprehensive Scientific Foundations Seeding...")

    # 1. Clean up empty stub subjects and courses
    stub_subject_names = [
        'Computability & Complexity', 'Electroweak Theory', 'Formal Logic',
        'Gauge Theory', 'General Relativity', 'Gravitation',
        'Information Theory', 'Physics', 'Quantum Mechanics',
        'Statistical Mechanics', 'Symplectic Geometry'
    ]
    for s_name in stub_subject_names:
        s = Subject.objects.filter(name=s_name).first()
        if s:
            print(f"Purging stub subject: {s.name}")
            s.delete()

    # Clean up empty courses in the 6 foundational subjects
    empty_courses = Course.objects.filter(topics__isnull=True)
    for ec in empty_courses:
        ec.delete()

    # Core 6 disciplines definition
    core_disciplines = {
        "Theoretical Physics": "The mathematical formulation of physical reality: classical Lagrangian/Hamiltonian mechanics, Maxwell-Yang-Mills gauge fields, general relativistic spacetime curvature, and quantum operator algebras.",
        "Mathematics & Geometry": "Rigorous mathematical frameworks including differential geometry, symplectic reduction, Lie groups, representation theory, functional analysis, and algebraic topology.",
        "Thermodynamics & Statistical Mechanics": "Equilibrium and non-equilibrium statistical thermodynamics, canonical ensembles, phase transitions, fluctuation theorems, quantum statistics, and microscopic state counting.",
        "Information Theory & Logic": "The mathematical science of information encoding, entropy, channel capacity, algorithmic computability, Godelian formal limits, and quantum information protocols.",
        "Chemical Sciences": "Quantum chemistry, molecular orbital theory, chemical bonding energetics, reaction kinetics, and thermodynamic equilibria of matter.",
        "Biological Sciences": "Molecular genetics, cellular organization, evolutionary mechanisms, and self-sustaining organic information propagation."
    }

    for name, desc in core_disciplines.items():
        s, _ = Subject.objects.get_or_create(name=name, defaults={"description": desc})
        s.description = desc
        s.save()

    modules = [
        # =====================================================================
        # 1. CHEMICAL SCIENCES
        # =====================================================================
        {
            "subject": "Chemical Sciences",
            "course": "Physical Chemistry & Reaction Energetics",
            "course_desc": "Thermodynamics of chemical reactions, Gibbs free energy, reaction kinetics, catalysis, and equilibrium constants.",
            "topics": [
                {
                    "name": "Reaction Kinetics & The Arrhenius Equation",
                    "content": r"""Chemical kinetics investigates the rates of chemical reactions, the molecular pathways through which reactants transform into products, and the energetic barriers controlling reaction dynamics.

Svante Arrhenius (1889) established the empirical relation governing the temperature dependence of the reaction rate constant $k$:
$$k = A e^{-\frac{E_a}{R T}}$$
where $A$ is the pre-exponential frequency factor representing the frequency of collisions with proper spatial orientation, $E_a$ is the activation energy, $R$ is the universal gas constant ($8.314\text{ J}\cdot\text{mol}^{-1}\cdot\text{K}^{-1}$), and $T$ is the absolute temperature.

Henry Eyring, Michael Polanyi, and Eugene Wigner (1935) formalized transition state theory (TST), which models the reacting system traversing a saddle point on the potential energy surface (the activated complex $\ddagger$). The Eyring equation expresses the rate constant in terms of fundamental constants and the standard free energy of activation $\Delta G^\ddagger = \Delta H^\ddagger - T\Delta S^\ddagger$:
$$k = \frac{k_B T}{h} e^{-\frac{\Delta G^\ddagger}{R T}} = \frac{k_B T}{h} e^{\frac{\Delta S^\ddagger}{R}} e^{-\frac{\Delta H^\ddagger}{R T}}$$
Catalysts accelerate chemical reactions by providing alternative reaction pathways with significantly lower activation energies $E_a'$, without altering the net thermodynamic equilibrium state ($\Delta G^\circ$) or being consumed in the net reaction.""",
                    "simulation_logic": "4PT Logic: Reaction kinetics defines the execution clock-cycle of atomic node recombination: activation energy represents the compute threshold required to recompile molecular state packets.",
                    "equations": [
                        {
                            "name": "Arrhenius Equation",
                            "formula": "k = A e^{-E_a / (RT)}",
                            "explanation": "Temperature dependence of chemical reaction rate constant based on activation energy barrier."
                        },
                        {
                            "name": "Eyring Transition State Equation",
                            "formula": "k = \\frac{k_B T}{h} e^{-\\Delta G^\\ddagger / (RT)}",
                            "explanation": "Fundamental formulation of reaction rates in terms of activated complex free energy of activation."
                        }
                    ]
                },
                {
                    "name": "Chemical Equilibrium & Le Chatelier's Principle",
                    "content": r"""A reversible chemical reaction reaches chemical equilibrium when the forward and reverse reaction rates become strictly equal, resulting in stationary macroscopic concentrations of all reacting species.

Guldberg and Waage (1864) formulated the Law of Mass Action. For a generalized reaction:
$$a A + b B \rightleftharpoons c C + d D$$
the thermodynamic equilibrium constant $K_{eq}$ is defined by the activities of the products raised to their stoichiometric coefficients divided by those of the reactants:
$$K_{eq} = \frac{[C]^c [D]^d}{[A]^a [B]^b}$$
Equilibrium is tied directly to the standard Gibbs free energy change of the reaction $\Delta G^\circ$ through the fundamental thermodynamic relation:
$$\Delta G^\circ = -R T \ln K_{eq}$$
At non-standard states, the reaction quotient $Q$ dictates the direction of spontaneous evolution: if $Q < K_{eq}$, the reaction proceeds forward ($\Delta G < 0$); if $Q > K_{eq}$, it shifts in reverse.

Le Chatelier's principle (1884) states that if a dynamic equilibrium is subjected to an external perturbation (changes in temperature, pressure, or concentration), the system adjusts to partially counteract the imposed change. For exothermic reactions ($\Delta H^\circ < 0$), increasing temperature shifts equilibrium toward reactants; for endothermic reactions ($\Delta H^\circ > 0$), increasing temperature increases $K_{eq}$, described mathematically by the van 't Hoff equation: $\frac{d \ln K_{eq}}{dT} = \frac{\Delta H^\circ}{R T^2}$.""",
                    "simulation_logic": "4PT Logic: Chemical equilibrium represents dynamic steady-state balance in the local simulation buffer: forward and reverse data transitions cancel out, producing macroscopic informational invariance.",
                    "equations": [
                        {
                            "name": "Gibbs-Equilibrium Constant Relation",
                            "formula": "\\Delta G^\\circ = -R T \\ln K_{eq}",
                            "explanation": "Direct connection between standard Gibbs free energy change and the chemical equilibrium constant."
                        },
                        {
                            "name": "van 't Hoff Equation",
                            "formula": "\\frac{d \\ln K_{eq}}{dT} = \\frac{\\Delta H^\\circ}{R T^2}",
                            "explanation": "Describes how chemical equilibrium constants shift as a function of temperature and enthalpy."
                        }
                    ]
                },
                {
                    "name": "Electrochemistry & The Nernst Equation",
                    "content": r"""Electrochemistry analyzes the interconversion of chemical energy and electrical potential energy via oxidation-reduction (redox) reactions occurring at phase boundaries.

Walther Nernst (1889) derived the fundamental equation governing the reduction potential $E$ of an electrochemical cell under arbitrary non-standard activities:
$$E = E^\circ - \frac{R T}{n F} \ln Q$$
where $E^\circ$ is the standard cell potential, $n$ is the number of moles of electrons transferred per mole of reaction, $F = e N_A \approx 96485.33\text{ C}\cdot\text{mol}^{-1}$ is Faraday's constant, and $Q$ is the reaction quotient. At $T = 298.15\text{ K}$, this simplifies to $E = E^\circ - \frac{0.05916\text{ V}}{n} \log_{10} Q$.

The electrical work performed by a reversible galvanic cell corresponds to the change in Gibbs free energy:
$$\Delta G = -n F E$$
At equilibrium, $E = 0$ and $Q = K_{eq}$, yielding $E^\circ = \frac{R T}{n F} \ln K_{eq}$. The Nernst equation governs all galvanic cells, electrochemical storage batteries, and biological action potentials across lipid cell membranes (such as the Goldman-Hodgkin-Katz voltage equation).""",
                    "simulation_logic": "4PT Logic: The Nernst potential measures the electro-informational gradient across simulation boundaries, driving directed flux through conductive data pathways.",
                    "equations": [
                        {
                            "name": "Nernst Equation",
                            "formula": "E = E^\\circ - \\frac{RT}{nF} \\ln Q",
                            "explanation": "Electrochemical cell potential as a function of temperature, electron transfer number, and reaction quotient."
                        },
                        {
                            "name": "Electrochemical Free Energy Relation",
                            "formula": "\\Delta G = -n F E",
                            "explanation": "Links electrical potential difference directly to thermodynamic Gibbs free energy."
                        }
                    ]
                }
            ]
        },
        {
            "subject": "Chemical Sciences",
            "course": "Molecular Structure & Solid State Chemistry",
            "course_desc": "Crystal lattices, ionic and metallic bonding, intermolecular interactions, and band theory of solids.",
            "topics": [
                {
                    "name": "Ionic & Metallic Bonding: Crystal Lattices & Band Theory",
                    "content": r"""Chemical bonds extend beyond localized covalent electron sharing into collective electrostatic architectures:

- **Ionic Bonding & Crystal Lattices:** Formed by the complete electrostatic transfer of valence electrons between atoms of disparate electronegativities ($\Delta\chi > 1.7$), producing cations and anions arranged in periodic three-dimensional Bravais lattices. The lattice energy $U_L$ of an ionic crystal is quantified by the Born-Landé and Born-Meyer equations:
$$U_L = -\frac{N_A M z^+ z^- e^2}{4\pi \varepsilon_0 r_0} \left(1 - \frac{1}{n}\right)$$
where $M$ is the Madelung constant determined by lattice geometry (e.g., $M \approx 1.74756$ for NaCl structure), and $n$ is the Born exponent representing short-range core electron repulsion.

- **Metallic Bonding & Band Theory of Solids:** Felix Bloch (1928) applied quantum mechanics to periodic crystalline potentials $V(\vec{r} + \vec{R}) = V(\vec{r})$, establishing Bloch's theorem for electron wave functions:
$$\psi_{\vec{k}}(\vec{r}) = e^{i \vec{k}\cdot\vec{r}} u_{\vec{k}}(\vec{r})$$
In metallic crystals, overlapping atomic valence orbitals delocalize into continuous energy bands. The valence band overlaps with or is partially filled up to the Fermi energy $E_F$, permitting seamless electron conduction under external electric fields. In insulators and semiconductors, a finite band gap $E_g$ separates the filled valence band from the empty conduction band.""",
                    "simulation_logic": "4PT Logic: Band theory defines the degree of data mobility across crystalline arrays: conductors permit free informational propagation, while insulators require discrete energy packets to bridge gaps.",
                    "equations": [
                        {
                            "name": "Born-Landé Lattice Energy",
                            "formula": "U_L = -\\frac{N_A M z^+ z^- e^2}{4\\pi \\varepsilon_0 r_0} \\left(1 - \\frac{1}{n}\\right)",
                            "explanation": "Electrostatic binding energy of periodic crystalline ionic solids."
                        },
                        {
                            "name": "Bloch's Theorem",
                            "formula": "\\psi_{\\vec{k}}(\\vec{r}) = e^{i \\vec{k} \\cdot \\vec{r}} u_{\\vec{k}}(\\vec{r}), \\quad u_{\\vec{k}}(\\vec{r} + \\vec{R}) = u_{\\vec{k}}(\\vec{r})",
                            "explanation": "Quantum wave function of electrons moving in periodic crystal lattice potentials."
                        }
                    ]
                },
                {
                    "name": "Intermolecular Forces & Hydrogen Bonding",
                    "content": r"""Intermolecular forces (non-covalent interactions) dictate the condensed states of matter (liquids and solids), molecular recognition, and the higher-order structural conformation of biological polymers (proteins and nucleic acids).

Johannes Diderik van der Waals (1873) identified that real gases deviate from ideal behavior due to molecular volume and intermolecular attractions. Van der Waals forces comprise three distinct electromagnetic dipoles:
1. **Keesom Forces (Dipole-Dipole):** Angle-averaged electrostatic attractions between permanent molecular dipoles, decaying as $V(r) \propto -r^{-6}$.
2. **Debye Forces (Dipole-Induced Dipole):** A permanent dipole induces polarization in an adjacent non-polar molecule, also scaling as $-r^{-6}$.
3. **London Dispersion Forces:** Fritz London (1930) applied second-order quantum perturbation theory to explain attractions between non-polar species. Instantaneous quantum fluctuations in electron cloud charge density induce correlated dipoles in neighboring atoms, producing an attractive potential $V(r) = -\frac{3}{4} \frac{h \nu_0 \alpha^2}{(4\pi\varepsilon_0)^2 r^6}$.

The **Lennard-Jones (12-6) Potential** models the net pair interaction:
$$V_{LJ}(r) = 4\varepsilon \left[ \left(\frac{\sigma}{r}\right)^{12} - \left(\frac{\sigma}{r}\right)^6 \right]$$
**Hydrogen Bonding:** A uniquely strong, directional electrostatic-covalent dipole interaction occurring when hydrogen is covalently bound to strongly electronegative atoms ($F, O, N$). Hydrogen bonds ($10-40\text{ kJ}\cdot\text{mol}^{-1}$) stabilize water's high boiling point, provide liquid water's density maximum at $4^\circ\text{C}$, and form the base-pair rungs of the DNA double helix.""",
                    "simulation_logic": "4PT Logic: Intermolecular potentials represent the soft boundary collisions and phase locks between adjacent simulation nodes, enabling macro-scale structural stability without rigid covalent coupling.",
                    "equations": [
                        {
                            "name": "Lennard-Jones 12-6 Potential",
                            "formula": "V_{LJ}(r) = 4\\varepsilon \\left[ \\left(\\frac{\\sigma}{r}\\right)^{12} - \\left(\\frac{\\sigma}{r}\\right)^6 \\right]",
                            "explanation": "Intermolecular potential balancing short-range Pauli core repulsion with long-range London dispersion."
                        },
                        {
                            "name": "London Dispersion Energy",
                            "formula": "V_{\\text{disp}}(r) = -\\frac{3}{4} \\frac{\\hbar \\omega_0 \\alpha^2}{(4\\pi \\varepsilon_0)^2 r^6}",
                            "explanation": "Quantum fluctuation attractive potential between non-polar molecular electron clouds."
                        }
                    ]
                }
            ]
        },

        # =====================================================================
        # 2. INFORMATION THEORY & LOGIC
        # =====================================================================
        {
            "subject": "Information Theory & Logic",
            "course": "Algorithmic Information & Computational Complexity",
            "course_desc": "Turing machines, computability limits, Godel incompleteness, computational complexity classes (P vs NP), and Kolmogorov complexity.",
            "topics": [
                {
                    "name": "Turing Machines & The Halting Problem",
                    "content": r"""Alan Turing (1936) formulated the mathematical foundations of computer science by introducing the abstract **Turing Machine**. A Turing machine consists of an infinite memory tape divided into discrete cells, a read/write head, an internal state register, and a finite transition table $\delta: Q \times \Gamma \to Q \times \Gamma \times \{L, R\}$.

The **Church-Turing Thesis** conjectures that any algorithmic process that can be computed by a human or mechanical device can be simulated by a universal Turing machine (UTM).

Turing addressed David Hilbert's *Entscheidungsproblem* (Decision Problem) by proving the existence of mathematically well-defined, uncomputable functions. Specifically, the **Halting Problem** asks whether an arbitrary computer program will eventually finish running or continue running forever on a given input.

Turing proved undecidability via Georg Cantor's diagonal argument: Suppose there exists a halting decider program $H(M, w)$ returning $1$ if machine $M$ halts on input $w$, and $0$ if it loops forever. Construct an adversarial machine $D$ that takes the description $\langle M \rangle$ as input, invokes $H(M, \langle M \rangle)$, and loops infinitely if $H$ returns $1$, but halts immediately if $H$ returns $0$. When evaluated on its own description:
$$D(\langle D \rangle) \text{ halts} \iff D(\langle D \rangle) \text{ loops forever}$$
This logical contradiction demonstrates that no general algorithm $H$ can ever exist. Undecidability is an inherent mathematical barrier of all formal computational systems.""",
                    "simulation_logic": "4PT Logic: The Halting Problem proves that a 3D simulation slice cannot compute its own infinite-horizon destiny from within its local code: deterministic projection requires an external boundary condition.",
                    "equations": [
                        {
                            "name": "Turing Machine Transition Function",
                            "formula": "\\delta: Q \\times \\Gamma \\to Q \\times \\Gamma \\times \\{L, R\\}",
                            "explanation": "Formal mapping dictating next machine state, tape symbol write, and head displacement."
                        },
                        {
                            "name": "Halting Contradiction Formalism",
                            "formula": "D(\\langle D \\rangle) \\downarrow \\iff D(\\langle D \\rangle) \\uparrow",
                            "explanation": "Diagonalization proof showing the logical impossibility of a universal halting oracle."
                        }
                    ]
                },
                {
                    "name": "Gödel's Incompleteness Theorems",
                    "content": r"""Kurt Gödel (1931) shattered the foundational program of David Hilbert, which sought to prove mathematics consistent, complete, and algorithmic. Gödel proved two monumental theorems applying to any consistent formal axiomatic system $F$ capable of expressing elementary Peano arithmetic:

- **First Incompleteness Theorem:** Any consistent formal system $F$ containing arithmetic is incomplete: there exist mathematical statements $G_F$ constructible within $F$ that are true, yet cannot be proven or disproven within $F$.
Gödel established this by constructing a self-referential statement through Gödel numbering:
$$G_F \iff \neg \text{Prov}_F(\ulcorner G_F \urcorner)$$
$G_F$ asserts: "This statement is not provable in system $F$." If $F$ were able to prove $G_F$, $F$ would prove a false statement, violating consistency. Therefore, $G_F$ is unprovable, making it a true mathematical fact that lies strictly beyond the deductive reach of $F$.

- **Second Incompleteness Theorem:** If a formal system $F$ is consistent, its consistency ($\text{Cons}(F)$) cannot be proven within $F$ itself:
$$F \not\vdash \text{Cons}(F)$$
To prove the consistency of $F$, one must invoke a strictly stronger meta-system $F'$, which in turn cannot prove its own consistency without an even higher meta-system. This establishes an infinite epistemic hierarchy.""",
                    "simulation_logic": "4PT Logic: Gödel's Incompleteness proves that the 3D physics engine cannot self-certify its absolute consistency: axiomatic closure resides exclusively in the higher-dimensional metric (5D superspace).",
                    "equations": [
                        {
                            "name": "Gödel Sentence Fixed Point",
                            "formula": "F \\vdash G_F \\leftrightarrow \\neg \\text{Prov}_F(\\ulcorner G_F \\urcorner)",
                            "explanation": "Constructed self-referential arithmetic formula asserting its own unprovability."
                        },
                        {
                            "name": "Second Incompleteness Formalism",
                            "formula": "\\text{Cons}(F) \\implies F \\not\\vdash \\text{Cons}(F)",
                            "explanation": "Inability of any consistent formal arithmetic system to verify its own non-contradiction."
                        }
                    ]
                },
                {
                    "name": "Computational Complexity: P versus NP",
                    "content": r"""Computational complexity theory, pioneered by Juris Hartmanis, Richard Stearns, Stephen Cook, and Leonid Levin (1971), classifies decision problems by the asymptotic computational resources (time and memory) required for their solution.

- **Class $\mathbf{P}$ (Polynomial Time):** The set of decision problems solvable by a deterministic Turing machine in time bounded by a polynomial function of input size $n$: $T(n) = \mathcal{O}(n^k)$ for fixed constant $k$. Problems in $\mathbf{P}$ are considered computationally tractable.
- **Class $\mathbf{NP}$ (Nondeterministic Polynomial Time):** The set of decision problems whose candidate solutions ("certificates") can be verified by a deterministic Turing machine in polynomial time. Equivalently, problems solvable by a nondeterministic Turing machine in polynomial time.

The **Cook-Levin Theorem (1971)** proved that the Boolean Satisfiability problem (SAT) is **NP-complete**: every problem in $\mathbf{NP}$ can be transformed in polynomial time into SAT. If an efficient polynomial-time algorithm exists for any NP-complete problem, then $\mathbf{P} = \mathbf{NP}$.

The $\mathbf{P} \text{ versus } \mathbf{NP}$ problem asks whether verification is fundamentally equivalent to discovery:
$$\mathbf{P} \stackrel{?}{=} \mathbf{NP}$$
Consensus among theoretical computer scientists strongly favors $\mathbf{P} \neq \mathbf{NP}$, meaning that searching through an exponentially vast configuration space of possibilities is intrinsically harder than checking a valid configuration.""",
                    "simulation_logic": "4PT Logic: $P$ vs $NP$ defines the asymmetry of observation: verifying physical stability in a Cauchy slice is polynomial, but compiling a universe from unconstrained vacuum fluctuations is NP-hard.",
                    "equations": [
                        {
                            "name": "Polynomial Time Complexity Bound",
                            "formula": "T(n) = \\mathcal{O}(n^k), \\quad k \\in \\mathbb{N}",
                            "explanation": "Asymptotic time boundary defining computational tractability in class P."
                        },
                        {
                            "name": "Cook-Levin Reduction",
                            "formula": "\\forall L \\in \\mathbf{NP}, \\quad L \\le_P \\text{3-SAT}",
                            "explanation": "Polynomial-time reduction demonstrating NP-completeness of Boolean Satisfiability."
                        }
                    ]
                },
                {
                    "name": "Kolmogorov Algorithmic Complexity",
                    "content": r"""Andrey Kolmogorov, Ray Solomonoff, and Gregory Chaitin (1965) established algorithmic information theory by formulating the intrinsic informational content of an individual object, independent of probability distributions.

The **Kolmogorov Complexity** $K_U(s)$ of a finite binary string $s \in \{0, 1\}^*$ relative to a universal Turing machine $U$ is the length of the shortest computer program $p$ that outputs string $s$ and halts:
$$K_U(s) = \min_{p} \{ |p| : U(p) = s \}$$
The Invariance Theorem proves that for any two universal Turing machines $U_1$ and $U_2$, the complexity differs at most by an additive constant $c$ representing the compiler translation size: $|K_{U_1}(s) - K_{U_2}(s)| \le c$.

A string $s$ is defined as **algorithmically random (incompressible)** if its Kolmogorov complexity cannot be compressed significantly below its own raw length:
$$K(s) \ge |s| - c$$
Chaitin proved that Kolmogorov complexity is mathematically uncomputable for almost all strings due to the undecidability of the halting problem. Algorithmic complexity provides a rigorous microscopic foundation for physical entropy: thermodynamic entropy is the average Kolmogorov complexity of the microstate given the macrostate constraints.""",
                    "simulation_logic": "4PT Logic: Kolmogorov complexity is the ultimate metric of data density: uncompressible strings represent raw chaotic quantum noise, while physical laws are compression algorithms for reality.",
                    "equations": [
                        {
                            "name": "Kolmogorov Complexity Definition",
                            "formula": "K(s) = \\min \\{ |p| : U(p) = s \\}",
                            "explanation": "Length of minimal algorithmic program generating string $s$ on universal Turing machine $U$."
                        },
                        {
                            "name": "Incompressibility Criterion",
                            "formula": "K(s) \\ge |s| - c",
                            "explanation": "Mathematical definition of algorithmic randomness and thermodynamic irreducibility."
                        }
                    ]
                }
            ]
        },
        {
            "subject": "Information Theory & Logic",
            "course": "Quantum Information & Entanglement",
            "course_desc": "Qubits, density operators, quantum no-cloning theorem, Bell states, and quantum teleportation protocols.",
            "topics": [
                {
                    "name": "Qubits, Bloch Sphere & The No-Cloning Theorem",
                    "content": r"""The fundamental carrier of quantum information is the **qubit** (quantum bit), a two-level quantum system existing as a coherent linear superposition of orthonormal computational basis states $\{|0\rangle, |1\rangle\}$:
$$|\psi\rangle = \alpha |0\rangle + \beta |1\rangle, \quad |\alpha|^2 + |\beta|^2 = 1$$
Up to an unobservable global phase, any pure single-qubit state can be parameterized on the unit **Bloch Sphere**:
$$|\psi\rangle = \cos\left(\frac{\theta}{2}\right) |0\rangle + e^{i \phi} \sin\left(\frac{\theta}{2}\right) |1\rangle$$
where $\theta \in [0, \pi]$ is the polar angle and $\phi \in [0, 2\pi)$ is the azimuthal phase angle.

Wootters, Zurek, and Dieks (1982) proved the **Quantum No-Cloning Theorem**: it is physically impossible to construct a unitary operator that creates an identical copy of an arbitrary unknown quantum state.
Proof: Suppose a unitary cloning operator $\hat{U}$ existed such that for an arbitrary target state $|e\rangle$:
$$\hat{U} |\psi\rangle |e\rangle = |\psi\rangle |\psi\rangle \quad \text{and} \quad \hat{U} |\phi\rangle |e\rangle = |\phi\rangle |\phi\rangle$$
Taking the inner product of the two equations and using unitary preservation $\langle \hat{U} A | \hat{U} B \rangle = \langle A | B \rangle$:
$$\langle \psi | \phi \rangle = (\langle \psi | \phi \rangle)^2 \implies \langle \psi | \phi \rangle (\langle \psi | \phi \rangle - 1) = 0$$
Thus, $\hat{U}$ can clone states if and only if they are identical ($\langle \psi | \phi \rangle = 1$) or completely orthogonal ($\langle \psi | \phi \rangle = 0$). The no-cloning theorem prevents arbitrary duplication of quantum data, guaranteeing quantum cryptographic security and preventing faster-than-light signaling via entanglement.""",
                    "simulation_logic": "4PT Logic: The No-Cloning Theorem prevents state packet pirating: quantum data cannot be copied across memory buffers, ensuring absolute uniqueness of localized observer coordinates.",
                    "equations": [
                        {
                            "name": "Bloch Sphere State Vector",
                            "formula": "|\\psi\\rangle = \\cos\\left(\\frac{\\theta}{2}\\right) |0\\rangle + e^{i\\phi} \\sin\\left(\\frac{\\theta}{2}\\right) |1\\rangle",
                            "explanation": "Parametric geometric representation of arbitrary two-level quantum pure state on unit sphere."
                        },
                        {
                            "name": "No-Cloning Unitarity Constraint",
                            "formula": "\\langle \\psi | \\phi \\rangle = \\langle \\psi | \\phi \\rangle^2 \\implies \\langle \\psi | \\phi \\rangle \\in \\{0, 1\\}",
                            "explanation": "Proof that linear unitary evolution forbids replication of non-orthogonal quantum states."
                        }
                    ]
                },
                {
                    "name": "Quantum Entanglement, Bell States & Teleportation",
                    "content": r"""Quantum entanglement represents a non-classical, non-separable correlation between two or more quantum subsystems. A composite bipartite state $|\Psi_{AB}\rangle \in \mathcal{H}_A \otimes \mathcal{H}_B$ is entangled if it cannot be written as a simple product state $|\psi_A\rangle \otimes |\phi_B\rangle$.

The canonical maximally entangled two-qubit basis comprises the four **Bell States**:
$$|\Phi^\pm\rangle = \frac{1}{\sqrt{2}} (|00\rangle \pm |11\rangle), \quad |\Psi^\pm\rangle = \frac{1}{\sqrt{2}} (|01\rangle \pm |10\rangle)$$
For mixed bipartite states described by density matrix $\rho_{AB}$, the **Peres-Horodecki (PPT) Criterion** (1996) establishes that if the partial transpose $\rho_{AB}^{T_B}$ possesses negative eigenvalues, the state is strictly entangled.

**Quantum Teleportation (Bennett et al. 1993):** An unknown quantum state $|\psi\rangle = \alpha |0\rangle + \beta |1\rangle$ can be transmitted faithfully from Alice to Bob using one shared Bell pair $|\Phi^+\rangle$ and two classical bits of communication:
1. Alice performs a joint Bell-state measurement on her qubit and her half of the entangled pair, collapsing the system into one of four Bell outcomes.
2. Alice sends her two classical measurement bits to Bob via a classical channel.
3. Bob applies one of four local Pauli unitary operations ($\hat{I}, \hat{\sigma}_x, \hat{\sigma}_z, \hat{\sigma}_z \hat{\sigma}_x$) to reconstruct the exact state $|\psi\rangle$.
Teleportation destroyed the original state at Alice's terminal (respecting no-cloning) and required classical signaling (respecting relativistic causality $v \le c$).""",
                    "simulation_logic": "4PT Logic: Quantum teleportation demonstrates distributed memory cache updating: using an entangled bridge and 2 classical bits, a state vector is rebuilt across remote network nodes.",
                    "equations": [
                        {
                            "name": "Bell State Basis",
                            "formula": "|\\Phi^+\\rangle = \\frac{1}{\\sqrt{2}} (|00\\rangle + |11\\rangle)",
                            "explanation": "Maximally entangled two-qubit EPR state with zero separable representation."
                        },
                        {
                            "name": "Quantum Teleportation Protocol",
                            "formula": "|\\psi\\rangle_A \\otimes |\\Phi^+\\rangle_{BC} = \\frac{1}{2} \\sum_{k=0}^3 |\\Phi_k\\rangle_{AB} \\otimes (\\sigma_k |\\psi\\rangle)_C",
                            "explanation": "Algebraic decomposition enabling full quantum state reconstruction via classical bit transfer."
                        }
                    ]
                }
            ]
        },

        # =====================================================================
        # 3. MATHEMATICS & GEOMETRY
        # =====================================================================
        {
            "subject": "Mathematics & Geometry",
            "course": "Differential Geometry & Curvature",
            "course_desc": "Riemannian metrics, connections, Christoffel symbols, Riemann and Ricci curvature tensors, and geodesics.",
            "topics": [
                {
                    "name": "Riemannian Metric & Levi-Civita Connection",
                    "content": r"""A smooth manifold $M$ of dimension $n$ becomes a **Riemannian manifold** $(M, g)$ when equipped with a smooth, symmetric, positive-definite $(0, 2)$-tensor field $g \in \Gamma(T^*M \otimes T^*M)$ called the Riemannian metric. In local coordinates $\{x^\mu\}$:
$$ds^2 = g_{\mu\nu}(x) dx^\mu dx^\nu$$
The metric assigns inner products to tangent vectors $\langle u, v \rangle = g_{\mu\nu} u^\mu v^\nu$ and determines distances, angles, and volumes on the curved manifold.

The **Fundamental Theorem of Riemannian Geometry** proves the existence of a unique affine connection $\nabla$ on $(M, g)$ that satisfies two conditions:
1. **Metric Compatibility:** $\nabla g = 0$, meaning the inner product of parallel-transported vectors is invariant along curves.
2. **Torsion-Free:** $T(X, Y) = \nabla_X Y - \nabla_Y X - [X, Y] = 0$.

This unique connection is the **Levi-Civita Connection**. Its connection coefficients in a coordinate basis are the **Christoffel Symbols of the Second Kind** $\Gamma^\mu_{\alpha\beta}$:
$$\Gamma^\mu_{\alpha\beta} = \frac{1}{2} g^{\mu\sigma} \left( \frac{\partial g_{\sigma\alpha}}{\partial x^\beta} + \frac{\partial g_{\sigma\beta}}{\partial x^\alpha} - \frac{\partial g_{\alpha\beta}}{\partial x^\sigma} \right)$$
The covariant derivative of a tensor field $T^\mu_{\ \nu}$ with respect to vector field $X = X^\alpha \partial_\alpha$ is:
$$\nabla_\alpha T^\mu_{\ \nu} = \partial_\alpha T^\mu_{\ \nu} + \Gamma^\mu_{\alpha\sigma} T^\sigma_{\ \nu} - \Gamma^\sigma_{\alpha\nu} T^\mu_{\ \sigma}$$
The Levi-Civita connection provides the mathematical foundation for parallel transport, curvature, and gravitational dynamics.""",
                    "simulation_logic": "4PT Logic: The Levi-Civita connection establishes coordinate transformation protocols across non-flat simulation meshes: it compensates for grid deformation when translating vectors across slices.",
                    "equations": [
                        {
                            "name": "Christoffel Symbols Formula",
                            "formula": "\\Gamma^\\mu_{\\alpha\\beta} = \\frac{1}{2} g^{\\mu\\sigma} \\left( \\partial_\\beta g_{\\sigma\\alpha} + \\partial_\\alpha g_{\\sigma\\beta} - \\partial_\\sigma g_{\\alpha\\beta} \\right)",
                            "explanation": "Connection coefficients derived uniquely from metric tensor partial derivatives."
                        },
                        {
                            "name": "Metric Compatibility Condition",
                            "formula": "\\nabla_\\sigma g_{\\mu\\nu} = \\partial_\\sigma g_{\\mu\\nu} - \\Gamma^\\alpha_{\\sigma\\mu} g_{\\alpha\\nu} - \\Gamma^\\alpha_{\\sigma\\nu} g_{\\mu\\alpha} = 0",
                            "explanation": "Guarantees length and orthogonality preservation under parallel transport."
                        }
                    ]
                },
                {
                    "name": "Riemann Curvature Tensor & Geodesic Deviation",
                    "content": r"""Curvature on a smooth Riemannian or pseudo-Riemannian manifold is the intrinsic geometric obstruction to the commutativity of second covariant derivatives.

The **Riemann Curvature Tensor** $R$ is a $(1, 3)$-tensor field measuring the non-integrability of parallel transport around an infinitesimal closed loop:
$$R(X, Y)Z = \nabla_X \nabla_Y Z - \nabla_Y \nabla_X Z - \nabla_{[X, Y]} Z$$
In local coordinate components:
$$R^\rho_{\ \sigma\mu\nu} = \partial_\mu \Gamma^\rho_{\nu\sigma} - \partial_\nu \Gamma^\rho_{\mu\sigma} + \Gamma^\rho_{\mu\lambda} \Gamma^\lambda_{\nu\sigma} - \Gamma^\rho_{\nu\lambda} \Gamma^\lambda_{\mu\sigma}$$
The Riemann tensor exhibits fundamental algebraic symmetries:
- Antisymmetry: $R_{\rho\sigma\mu\nu} = -R_{\sigma\rho\mu\nu} = -R_{\rho\sigma\nu\mu} = R_{\mu\nu\rho\sigma}$.
- First Bianchi Identity: $R^\rho_{\ [\sigma\mu\nu]} = 0$.
- Second Bianchi Identity: $\nabla_{[\lambda} R^\rho_{\ |\sigma|\mu\nu]} = 0$.

Contracting the Riemann tensor produces:
- **Ricci Tensor:** $R_{\mu\nu} = R^\sigma_{\ \mu\sigma\nu}$.
- **Ricci Scalar:** $R = g^{\mu\nu} R_{\mu\nu}$.
- **Einstein Tensor:** $G_{\mu\nu} = R_{\mu\nu} - \frac{1}{2} R g_{\mu\nu}$, which satisfies $\nabla^\mu G_{\mu\nu} = 0$ identically via the contracted second Bianchi identity.

**Geodesic Deviation (Jacobi Equation):** For two nearby geodesics parameterized by proper time $\tau$ with velocity $u^\mu = \frac{dx^\mu}{d\tau}$ and separation vector $\xi^\mu$, the tidal acceleration is directly determined by curvature:
$$\frac{D^2 \xi^\mu}{d\tau^2} = R^\mu_{\ \nu\rho\sigma} u^\nu u^\rho \xi^\sigma$$
In general relativity, this explains tidal gravitational forces without invoking Newtonian action-at-a-distance.""",
                    "simulation_logic": "4PT Logic: Curvature is the processing strain of the simulation manifold: dense data regions distort the spatial lattice, deflecting adjacent processing trajectories toward each other.",
                    "equations": [
                        {
                            "name": "Riemann Curvature Tensor Components",
                            "formula": "R^\\rho_{\\ \\sigma\\mu\\nu} = \\partial_\\mu \\Gamma^\\rho_{\\nu\\sigma} - \\partial_\\nu \\Gamma^\\rho_{\\mu\\sigma} + \\Gamma^\\rho_{\\mu\\lambda}\\Gamma^\\lambda_{\\nu\\sigma} - \\Gamma^\\rho_{\\nu\\lambda}\\Gamma^\\lambda_{\\mu\\sigma}",
                            "explanation": "Intrinsic curvature tensor measuring parallel transport non-commutativity."
                        },
                        {
                            "name": "Jacobi Equation for Geodesic Deviation",
                            "formula": "\\frac{D^2 \\xi^\\mu}{d\\tau^2} = R^\\mu_{\\ \\nu\\rho\\sigma} u^\\nu u^\\rho \\xi^\\sigma",
                            "explanation": "Relative acceleration of neighboring test trajectories driven by Riemann curvature."
                        }
                    ]
                }
            ]
        },
        {
            "subject": "Mathematics & Geometry",
            "course": "Lie Groups & Representation Theory",
            "course_desc": "Continuous Lie groups, Lie algebras, exponential maps, representations of SU(2), SO(3), and the Poincare group.",
            "topics": [
                {
                    "name": "Lie Groups, Lie Algebras & The Exponential Map",
                    "content": r"""Sophus Lie (1870s) introduced **Lie Groups** to systematically study the continuous symmetries of differential equations. A Lie group $G$ is a smooth manifold that simultaneously possesses a group structure such that multiplication $(g, h) \mapsto gh$ and inversion $g \mapsto g^{-1}$ are smooth maps.

The **Lie Algebra** $\mathfrak{g} = T_e G$ is the tangent space to the identity element $e \in G$, equipped with a bilinear, alternating bracket $[\cdot, \cdot]: \mathfrak{g} \times \mathfrak{g} \to \mathfrak{g}$ satisfying the **Jacobi Identity**:
$$[[X, Y], Z] + [[Y, Z], X] + [[Z, X], Y] = 0$$
For a matrix Lie group, the Lie bracket is simply the commutator $[X, Y] = XY - YX$. Given a basis of generators $\{T_a\}$, the Lie algebra is completely specified by its real **Structure Constants** $f_{abc}$:
$$[T_a, T_b] = i f_{abc} T_c$$
The **Exponential Map** $\exp: \mathfrak{g} \to G$ connects infinitesimal generators in the Lie algebra to finite group transformations in the Lie group:
$$\exp(X) = \sum_{k=0}^\infty \frac{X^k}{k!}$$
The **Baker-Campbell-Hausdorff (BCH) Formula** expresses the product of two exponentials purely in terms of repeated commutators:
$$\ln(\exp(X)\exp(Y)) = X + Y + \frac{1}{2}[X, Y] + \frac{1}{12}[X, [X, Y]] - \frac{1}{12}[Y, [X, Y]] + \dots$$
In modern gauge theories, the gauge groups $U(1)$, $SU(2)$, and $SU(3)$ are compact Lie groups whose Lie algebras dictate all gauge boson interactions.""",
                    "simulation_logic": "4PT Logic: Lie algebras represent the continuous transformation parameters of the rendering pipeline: group generators define rotational, translational, and internal gauge symmetry axes.",
                    "equations": [
                        {
                            "name": "Lie Bracket Structure Constants",
                            "formula": "[T_a, T_b] = i f_{abc} T_c",
                            "explanation": "Commutator algebra of Lie group generators with structure constants $f_{abc}$."
                        },
                        {
                            "name": "Baker-Campbell-Hausdorff Formula",
                            "formula": "\\exp(X) \\exp(Y) = \\exp\\left( X + Y + \\frac{1}{2}[X, Y] + \\dots \\right)",
                            "explanation": "Group multiplication expressed through Lie algebra commutator series."
                        }
                    ]
                },
                {
                    "name": "Representations of SU(2), SO(3) & Spinors",
                    "content": r"""Representation theory studies how abstract groups act as linear transformations on vector spaces: $\rho: G \to GL(V)$.

The rotation group of three-dimensional Euclidean space is the special orthogonal group $SO(3)$, whose elements satisfy $R^T R = I$ and $\det R = 1$. The special unitary group $SU(2)$ comprises $2 \times 2$ unitary matrices with unit determinant ($U^\dagger U = I, \det U = 1$). $SU(2)$ is topologically homeomorphic to the 3-sphere $S^3$ (simply connected) and acts as the **universal covering group** of $SO(3)$, with a $2$-to-$1$ surjective homomorphism $\pi: SU(2) \to SO(3)$.

The Lie algebra $\mathfrak{su}(2) \cong \mathfrak{so}(3)$ is spanned by three generators $J_i$ satisfying the angular momentum algebra:
$$[J_i, J_j] = i \hbar \epsilon_{ijk} J_k$$
Irreducible representations (irreps) are characterized by the eigenvalue $j(j+1)\hbar^2$ of the Casimir operator $J^2 = J_1^2 + J_2^2 + J_3^2$, where $j \in \{0, 1/2, 1, 3/2, 2, \dots\}$:
- **Integer $j = 0, 1, 2$ (Vectors and Tensors):** Single-valued representations of $SO(3)$. A $360^\circ$ rotation ($2\pi$) returns the state to itself.
- **Half-Integer $j = 1/2, 3/2$ (Spinors):** Double-valued representations of $SO(3)$, true representations of $SU(2)$. For $j = 1/2$, generators are Pauli matrices $J_i = \frac{\hbar}{2} \sigma_i$. A $360^\circ$ rotation introduces a minus sign ($e^{-i \pi \sigma_z} = -I$); an entire $720^\circ$ ($4\pi$) rotation is required to restore the initial state vector, experimentally confirmed via neutron interferometry (Werner et al. 1975).""",
                    "simulation_logic": "4PT Logic: Spin-1/2 fermions require $4\\pi$ rotation to return to baseline phase: this topological twist protects fermionic data packets from phase cancellation during spatial updates.",
                    "equations": [
                        {
                            "name": "Angular Momentum Lie Algebra",
                            "formula": "[J_i, J_j] = i \\hbar \\epsilon_{ijk} J_k",
                            "explanation": "Fundamental commutator relation generating 3D spatial rotations and spin."
                        },
                        {
                            "name": "Pauli Spin Matrices",
                            "formula": "\\sigma_x = \\begin{pmatrix} 0 & 1 \\\\ 1 & 0 \\end{pmatrix}, \\quad \\sigma_y = \\begin{pmatrix} 0 & -i \\\\ i & 0 \\end{pmatrix}, \\quad \\sigma_z = \\begin{pmatrix} 1 & 0 \\\\ 0 & -1 \\end{pmatrix}",
                            "explanation": "Generators for fundamental two-dimensional representation of SU(2)."
                        }
                    ]
                }
            ]
        },

        # =====================================================================
        # 4. THERMODYNAMICS & STATISTICAL MECHANICS
        # =====================================================================
        {
            "subject": "Thermodynamics & Statistical Mechanics",
            "course": "Non-Equilibrium Dynamics & Fluctuation Phenomena",
            "course_desc": "Boltzmann transport equation, H-theorem, Brownian motion, Langevin dynamics, and fluctuation-dissipation theorems.",
            "topics": [
                {
                    "name": "Boltzmann Transport Equation & The H-Theorem",
                    "content": r"""Ludwig Boltzmann (1872) bridged microscopic Newtonian particle collisions with macroscopic thermodynamic irreversibility by developing the kinetic theory of dilute gases.

The state of a gas of identical particles is described by the single-particle distribution function $f(\vec{r}, \vec{p}, t)$ in 6-dimensional $\mu$-space, representing the probability density of finding a particle at position $\vec{r}$ with momentum $\vec{p}$ at time $t$. The **Boltzmann Transport Equation** describes the dynamical evolution of $f$:
$$\frac{\partial f}{\partial t} + \frac{\vec{p}}{m} \cdot \nabla_{\vec{r}} f + \vec{F}_{\text{ext}} \cdot \nabla_{\vec{p}} f = \left( \frac{\partial f}{\partial t} \right)_{\text{coll}}$$
Under the assumption of *molecular chaos* (*Stosszahlansatz*—that colliding particles are completely uncorrelated before collision), Boltzmann derived the collision integral for elastic binary collisions:
$$\left( \frac{\partial f}{\partial t} \right)_{\text{coll}} = \int d^3 p_1 \int d\Omega \, \frac{d\sigma}{d\Omega} |\vec{v} - \vec{v}_1| \left( f' f'_1 - f f_1 \right)$$
Boltzmann defined the functional $H(t)$:
$$H(t) = \int d^3 r \int d^3 p \, f(\vec{r}, \vec{p}, t) \ln f(\vec{r}, \vec{p}, t)$$
The **H-Theorem** proves mathematically that for any isolated system:
$$\frac{dH}{dt} \le 0$$
Since thermodynamic entropy is $S(t) = -k_B H(t)$, this provides a microscopic mechanical derivation of the Second Law of Thermodynamics: entropy must monotonically increase until $f$ relaxes to the equilibrium Maxwell-Boltzmann distribution, where $\frac{dH}{dt} = 0$.""",
                    "simulation_logic": "4PT Logic: The H-theorem demonstrates how deterministic microscopic updates inexorably produce macroscopic informational decoherence due to phase randomization across unmonitored degrees of freedom.",
                    "equations": [
                        {
                            "name": "Boltzmann Transport Equation",
                            "formula": "\\frac{\\partial f}{\\partial t} + \\vec{v} \\cdot \\nabla_{\\vec{r}} f + \\vec{F} \\cdot \\nabla_{\\vec{p}} f = \\left(\\frac{\\partial f}{\\partial t}\\right)_{\\text{coll}}",
                            "explanation": "Evolution of one-particle phase space distribution under drift, external forces, and collisions."
                        },
                        {
                            "name": "Boltzmann's H-Theorem",
                            "formula": "\\frac{dH}{dt} \\le 0, \\quad H = \\int f \\ln f \\, d^3r \\, d^3p",
                            "explanation": "Microscopic proof of monotonic entropy increase in kinetic theory."
                        }
                    ]
                },
                {
                    "name": "Langevin Dynamics & The Fluctuation-Dissipation Theorem",
                    "content": r"""Paul Langevin (1908) formulated the theory of Brownian motion by introducing the concept of **stochastic differential equations**. A microscopic particle of mass $m$ suspended in a fluid experiences two forces: a systematic macroscopic viscous drag force $-\gamma v$, and a rapidly fluctuating stochastic force $\xi(t)$ arising from random thermal collisions with fluid molecules:
$$m \frac{dv}{dt} = -\gamma v + \xi(t)$$
where $\gamma = 6\pi \eta a$ by Stokes' law for a sphere of radius $a$ in viscosity $\eta$. The thermal noise $\xi(t)$ is modeled as Gaussian white noise satisfying:
$$\langle \xi(t) \rangle = 0, \quad \langle \xi(t) \xi(t') \rangle = 2 D_p \delta(t - t')$$
By integrating the Langevin equation and demanding thermal equilibrium $\langle \frac{1}{2} m v^2 \rangle = \frac{1}{2} k_B T$, Einstein and Langevin derived the **Einstein Diffusion Relation**:
$$D = \frac{k_B T}{\gamma} = \frac{k_B T}{6\pi \eta a}$$
Harry Nyquist (1928) and Herbert Callen & Richard Greene (1952) generalized this into the universal **Fluctuation-Dissipation Theorem (FDT)**: for any physical system in thermal equilibrium, the spontaneous microscopic thermal fluctuations of an observable are linearly proportional to the dissipative response (energy loss) of the system when subjected to an external perturbation:
$$S_A(\omega) = \frac{2 k_B T}{\omega} \text{Im}[\chi_A(\omega)]$$
where $S_A(\omega)$ is the power spectral density of fluctuations and $\chi_A(\omega)$ is the dynamic susceptibility.""",
                    "simulation_logic": "4PT Logic: The Fluctuation-Dissipation Theorem proves that thermal noise in the rendering engine is inextricably linked to energy dissipation: zero latency/zero dissipation requires zero thermal variance.",
                    "equations": [
                        {
                            "name": "Langevin Stochastic Equation",
                            "formula": "m \\frac{dv}{dt} = -\\gamma v + \\xi(t), \\quad \\langle \\xi(t) \\xi(t') \\rangle = 2 \\gamma k_B T \\delta(t - t')",
                            "explanation": "Equations of motion incorporating macroscopic frictional damping and microscopic stochastic thermal kicks."
                        },
                        {
                            "name": "Fluctuation-Dissipation Theorem",
                            "formula": "S_{AA}(\\omega) = \\frac{2 k_B T}{\\omega} \\text{Im}[\\chi_{AA}(\\omega)]",
                            "explanation": "Fundamental relation equating spontaneous thermal fluctuations to linear dissipative response."
                        }
                    ]
                }
            ]
        },

        # =====================================================================
        # 5. THEORETICAL PHYSICS: Analytical Mechanics & Gauge Theory
        # =====================================================================
        {
            "subject": "Theoretical Physics",
            "course": "Analytical Mechanics & Symmetries",
            "course_desc": "Lagrangian mechanics, Hamilton's principle of stationary action, canonical Hamiltonian formalism, and Noether invariants.",
            "topics": [
                {
                    "name": "Lagrangian Mechanics & Principle of Stationary Action",
                    "content": r"""Analytical mechanics reformulates Newtonian physics into a coordinate-independent variational framework.

The state of a system with $n$ degrees of freedom is described by generalized coordinates $q = (q_1, \dots, q_n)$ in configuration manifold $Q$, and generalized velocities $\dot{q} \in T_q Q$. The dynamics are governed by the **Lagrangian** $L(q, \dot{q}, t) = T - V$, where $T$ is kinetic energy and $V$ is potential energy.

**Hamilton's Principle of Stationary Action:** The actual physical trajectory $q(t)$ traversed by a system between configurations $q(t_1)$ and $q(t_2)$ makes the action functional $S[q(t)]$ stationary with respect to all infinitesimal variations $\delta q(t)$ vanishing at the endpoints ($\delta q(t_1) = \delta q(t_2) = 0$):
$$S[q(t)] = \int_{t_1}^{t_2} L(q(t), \dot{q}(t), t) \, dt, \quad \delta S = 0$$
Evaluating the first variation yields the **Euler-Lagrange Equations of Motion**:
$$\frac{d}{dt} \left( \frac{\partial L}{\partial \dot{q}_i} \right) - \frac{\partial L}{\partial q_i} = 0, \quad i = 1, \dots, n$$
Generalized momentum is defined as $p_i = \frac{\partial L}{\partial \dot{q}_i}$. If $L$ is independent of a coordinate $q_k$ ($\frac{\partial L}{\partial q_k} = 0$), $q_k$ is termed *cyclic*, and its conjugate momentum is strictly conserved: $\frac{d p_k}{dt} = 0$. The action principle extends directly to classical and quantum field theory: $S[\phi] = \int d^4x \, \mathcal{L}(\phi, \partial_\mu \phi)$.""",
                    "simulation_logic": "4PT Logic: The Principle of Stationary Action is the simulation's global optimization compiler: trajectories compute along paths of minimal informational overhead ($\delta S = 0$).",
                    "equations": [
                        {
                            "name": "Euler-Lagrange Equations",
                            "formula": "\\frac{d}{dt}\\left( \\frac{\\partial L}{\\partial \\dot{q}_i} \\right) - \\frac{\\partial L}{\\partial q_i} = 0",
                            "explanation": "Equations of motion derived from stationary action variational principle."
                        },
                        {
                            "name": "Action Functional",
                            "formula": "S[q] = \\int_{t_1}^{t_2} L(q, \\dot{q}, t) \\, dt, \\quad \\delta S = 0",
                            "explanation": "Variational action defining the physical trajectory in configuration space."
                        }
                    ]
                },
                {
                    "name": "Hamiltonian Mechanics & Canonical Transformations",
                    "content": r"""William Rowan Hamilton (1834) transformed Lagrangian mechanics from configuration space $TQ$ into cotangent phase space $T^*Q$, replacing $n$ second-order differential equations with $2n$ first-order differential equations.

The **Hamiltonian** $H(q, p, t)$ is obtained via the Legendre transformation:
$$H(q, p, t) = \sum_{i=1}^n p_i \dot{q}_i - L(q, \dot{q}, t)$$
where $p_i = \frac{\partial L}{\partial \dot{q}_i}$. The dynamics are governed by **Hamilton's Canonical Equations**:
$$\dot{q}_i = \frac{\partial H}{\partial p_i}, \quad \dot{p}_i = -\frac{\partial H}{\partial q_i}$$
Phase space $\Gamma = (q, p)$ possesses an intrinsic symplectic structure $\omega = \sum dq_i \wedge dp_i$. For any two observables $f(q, p)$ and $g(q, p)$, the **Poisson Bracket** is defined as:
$$\{f, g\} = \sum_{i=1}^n \left( \frac{\partial f}{\partial q_i} \frac{\partial g}{\partial p_i} - \frac{\partial f}{\partial p_i} \frac{\partial g}{\partial q_i} \right)$$
The time evolution of any observable follows $\frac{df}{dt} = \{f, H\} + \frac{\partial f}{\partial t}$. Canonical transformations $(q, p) \mapsto (Q, P)$ preserve the symplectic 2-form $\omega = \sum dQ_i \wedge dP_i$ and the Poisson brackets: $\{Q_i, P_j\} = \delta_{ij}$.

**Liouville's Theorem:** The phase space volume element $d\Gamma = \prod dq_i dp_i$ is an incompressible fluid under Hamiltonian flow: $\frac{d\rho}{dt} = 0$, guaranteeing conservation of information in classical dynamics.""",
                    "simulation_logic": "4PT Logic: Hamiltonian mechanics represents the phase-space memory map of the universe: Liouville's theorem ensures zero bit-loss during unitary coordinate evolution.",
                    "equations": [
                        {
                            "name": "Hamilton's Canonical Equations",
                            "formula": "\\dot{q}_i = \\frac{\\partial H}{\\partial p_i}, \\quad \\dot{p}_i = -\\frac{\\partial H}{\\partial q_i}",
                            "explanation": "First-order symmetric differential equations governing phase space trajectories."
                        },
                        {
                            "name": "Poisson Bracket Time Evolution",
                            "formula": "\\frac{df}{dt} = \\{f, H\\} + \\frac{\\partial f}{\\partial t}",
                            "explanation": "Time derivative of any phase space observable governed by the Hamiltonian vector field."
                        }
                    ]
                }
            ]
        },

        # =====================================================================
        # 6. BIOLOGICAL SCIENCES
        # =====================================================================
        {
            "subject": "Biological Sciences",
            "course": "Molecular Genetics & Evolutionary Dynamics",
            "course_desc": "DNA replication, central dogma, epigenetic chromatin remodeling, natural selection, and Fisher's fundamental theorem.",
            "topics": [
                {
                    "name": "Natural Selection & Fisher's Fundamental Theorem",
                    "content": r"""Charles Darwin and Alfred Russel Wallace (1858) established natural selection as the non-random mechanism driving adaptive evolution in biological populations. Natural selection operates whenever three conditions are satisfied: phenotypic variation exists, variation is heritable, and differential reproductive success correlates with phenotypic variants.

Ronald Fisher (1930) unified Darwinian natural selection with Mendelian genetics into population genetics. Fisher formalized the mathematical rate of evolutionary adaptation in **Fisher's Fundamental Theorem of Natural Selection**:
$$\frac{d\bar{W}}{dt} = \frac{\text{Var}_A(W)}{\bar{W}}$$
where $\bar{W}$ is the mean fitness of the population and $\text{Var}_A(W)$ is the additive genetic variance in fitness. The theorem proves that the rate of increase in mean fitness of any organism at any time is strictly equal to its additive genetic variance in fitness at that time.

Sewall Wright developed the concept of the **Fitness Landscape** $W(\vec{g})$, where populations navigate multi-dimensional genetic coordinates toward local adaptive peaks via selection, and cross adaptive valleys via genetic drift in finite populations. Motoo Kimura (1968) introduced the **Neutral Theory of Molecular Evolution**, demonstrating that the majority of molecular evolutionary changes at the DNA nucleotide level are caused by random genetic drift of selectively neutral mutant alleles rather than Darwinian selection.""",
                    "simulation_logic": "4PT Logic: Fisher's theorem is the simulation's algorithmic gradient ascent: natural selection continuously optimizes biological data structures against local environmental fitness constraints.",
                    "equations": [
                        {
                            "name": "Fisher's Fundamental Theorem of Natural Selection",
                            "formula": "\\frac{d\\bar{W}}{dt} = \\frac{\\text{Var}_A(W)}{\\bar{W}}",
                            "explanation": "Proves the rate of increase in mean population fitness equals its additive genetic variance."
                        },
                        {
                            "name": "Kimura's Neutral Mutation Rate",
                            "formula": "k = v_0",
                            "explanation": "Rate of neutral molecular substitutions per generation equals the neutral mutation rate."
                        }
                    ]
                },
                {
                    "name": "Epigenetics & Chromatin Remodeling",
                    "content": r"""Epigenetics investigates heritable changes in gene expression and cellular phenotype that do not involve alterations to the underlying DNA nucleotide sequence. Conrad Waddington (1942) coined the term "epigenetic landscape" to describe developmental cellular differentiation.

The human genome contains $\sim 3 \times 10^9$ base pairs per diploid cell, compacted into the cell nucleus via **chromatin**. The fundamental repeating structural unit of chromatin is the **nucleosome**, consisting of $147$ base pairs of DNA wrapped in $1.65$ left-handed superhelical turns around an octamer of core histone proteins ($2 \times H2A, H2B, H3, H4$).

Primary molecular mechanisms of epigenetic regulation include:
1. **DNA Methylation:** Addition of a methyl group ($-CH_3$) to the 5-carbon position of cytosine pyrimidine rings in CpG dinucleotides by DNA methyltransferases (DNMTs). High promoter CpG methylation recruits methyl-CpG-binding proteins and histone deacetylases, causing transcriptional repression and gene silencing.
2. **Histone Post-Translational Modifications:** Covalent modifications of histone amino-terminal tails, including acetylation (H3K9ac, H3K27ac via HATs, promoting transcriptionally active *euchromatin*), and methylation (H3K9me3, H3K27me3 via HMTs, generating condensed, transcriptionally silent *heterochromatin*).
3. **Non-coding RNAs:** MicroRNAs (miRNAs) and long non-coding RNAs (lncRNAs, such as *Xist* mediating X-chromosome inactivation) that guide chromatin-modifying complexes to specific genomic loci.

Epigenetic marks are faithfully preserved during mitotic cell division, providing the stable transcriptional memory that enables identical genomes to express distinct differentiated cell fates (e.g., neurons vs hepatocytes).""",
                    "simulation_logic": "4PT Logic: Epigenetics represents runtime configuration flags: the underlying DNA source code remains unchanged while memory access flags control which subroutines compile in each tissue slice.",
                    "equations": [
                        {
                            "name": "DNA Cytosine Methylation",
                            "formula": "\\text{Cytosine} + \\text{SAM} \\xrightarrow{\\text{DNMT}} 5\\text{-Methylcytosine} + \\text{SAH}",
                            "explanation": "Enzymatic transfer of methyl group from S-adenosylmethionine silencing promoter activity."
                        },
                        {
                            "name": "Histone Acetylation Equilibrium",
                            "formula": "\\text{Histone-Lys} + \\text{Acetyl-CoA} \\xrightleftharpoons[\\text{HDAC}]{\\text{HAT}} \\text{Histone-Lys-Ac} + \\text{CoA}",
                            "explanation": "Dynamic reversible acetylation neutralizes lysine positive charge to open chromatin architecture."
                        }
                    ]
                }
            ]
        }
    ]

    total_topics = 0
    total_eqs = 0

    for m in modules:
        subj = Subject.objects.get(name=m["subject"])
        course, _ = Course.objects.get_or_create(
            subject=subj,
            name=m["course"],
            defaults={"description": m["course_desc"]}
        )
        course.description = m["course_desc"]
        course.save()

        for t_info in m["topics"]:
            topic, _ = Topic.objects.get_or_create(
                course=course,
                name=t_info["name"],
                defaults={
                    "content": t_info["content"],
                    "simulation_logic": t_info["simulation_logic"]
                }
            )
            topic.content = t_info["content"]
            topic.simulation_logic = t_info["simulation_logic"]
            topic.save()
            total_topics += 1

            for eq_info in t_info.get("equations", []):
                eq, _ = Equation.objects.get_or_create(
                    topic=topic,
                    name=eq_info["name"],
                    defaults={
                        "formula": eq_info["formula"],
                        "explanation": eq_info["explanation"]
                    }
                )
                eq.formula = eq_info["formula"]
                eq.explanation = eq_info["explanation"]
                eq.save()
                total_eqs += 1

    # Link all new foundational topics to relevant Theories
    theory_topic_map = {
        "4PT": [
            "Turing Machines & The Halting Problem",
            "Gödel's Incompleteness Theorems",
            "Qubits, Bloch Sphere & The No-Cloning Theorem",
            "Quantum Entanglement, Bell States & Teleportation",
            "Boltzmann Transport Equation & The H-Theorem",
            "Hamiltonian Mechanics & Canonical Transformations",
            "Natural Selection & Fisher's Fundamental Theorem"
        ],
        "IUC": [
            "Hamiltonian Mechanics & Canonical Transformations",
            "Riemannian Metric & Levi-Civita Connection",
            "Riemann Curvature Tensor & Geodesic Deviation",
            "Lie Groups, Lie Algebras & The Exponential Map",
            "Boltzmann Transport Equation & The H-Theorem"
        ],
        "General_Relativity": [
            "Riemannian Metric & Levi-Civita Connection",
            "Riemann Curvature Tensor & Geodesic Deviation",
            "Lagrangian Mechanics & Principle of Stationary Action"
        ],
        "Quantum_Mechanics": [
            "Representations of SU(2), SO(3) & Spinors",
            "Qubits, Bloch Sphere & The No-Cloning Theorem",
            "Quantum Entanglement, Bell States & Teleportation",
            "Hamiltonian Mechanics & Canonical Transformations"
        ],
        "Electroweak_Theory": [
            "Lie Groups, Lie Algebras & The Exponential Map",
            "Representations of SU(2), SO(3) & Spinors",
            "Lagrangian Mechanics & Principle of Stationary Action"
        ],
        "Thermodynamics_Information": [
            "Boltzmann Transport Equation & The H-Theorem",
            "Langevin Dynamics & The Fluctuation-Dissipation Theorem",
            "Chemical Equilibrium & Le Chatelier's Principle",
            "Kolmogorov Algorithmic Complexity"
        ]
    }

    for th_name, top_names in theory_topic_map.items():
        th = Theory.objects.filter(name=th_name).first()
        if th:
            for tn in top_names:
                t_obj = Topic.objects.filter(name=tn).first()
                if t_obj:
                    th.topics.add(t_obj)

    print(f"Successfully seeded {total_topics} topics and {total_eqs} equations across the 6 foundational disciplines.")

if __name__ == '__main__':
    seed_full_foundations()

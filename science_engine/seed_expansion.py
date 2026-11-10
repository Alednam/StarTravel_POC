import os, sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'scicalc.settings')
django.setup()

from science_engine.models import Subject, Course, Topic, Equation, Theory

def seed_expansion():
    print("Beginning Deep Knowledge Base Expansion for Core Subjects...")

    modules = [
        # =====================================================================
        # 1. THERMODYNAMICS & STATISTICAL MECHANICS
        # =====================================================================
        {
            "subject": "Thermodynamics & Statistical Mechanics",
            "course": "Classical Thermodynamics & Potentials",
            "course_desc": "The four fundamental laws of thermodynamics, state functions, Carnot cycles, and thermodynamic potential relations.",
            "topics": [
                {
                    "name": "The Four Laws of Thermodynamics",
                    "content": r"""Classical thermodynamics is structured around four empirical and deductive laws governing heat, work, energy transfer, and entropy:

0. **Zeroth Law (Thermal Equilibrium):** If system $A$ is in thermal equilibrium with system $B$, and $B$ is in equilibrium with $C$, then $A$ is in equilibrium with $C$. This establishes the existence of empirical temperature $T$ as a state variable.
1. **First Law (Conservation of Energy):** The internal energy change $dU$ of a closed system equals the heat added minus work done by the system: $dU = \delta Q - \delta W = T dS - P dV$. Energy can neither be created nor destroyed.
2. **Second Law (Monotonicity of Entropy):** For any irreversible natural process in an isolated system, the total thermodynamic entropy strictly increases: $\Delta S_{\text{total}} > 0$. The Clausius inequality states that $\oint \frac{\delta Q}{T} \le 0$ for any closed cycle, vanishing exclusively for reversible processes.
3. **Third Law (Nernst Heat Theorem):** As absolute temperature approaches zero ($T \to 0\text{ K}$), the entropy of a pure crystalline substance approaches a universal constant: $\lim_{T \to 0} S = 0$. Absolute zero is dynamically unreachable in a finite number of thermodynamic operations.""",
                    "simulation_logic": "4PT Logic: The Second Law represents the mandatory processing dissipation of the simulation: without active 'Sealing' (anti-entropy maintenance), state vectors decay into thermal background noise.",
                    "equations": [
                        {
                            "name": "First Law Differential Form",
                            "formula": "dU = T dS - P dV + \\sum_i \\mu_i dN_i",
                            "explanation": "Fundamental thermodynamic relation combining energy conservation, entropy, pressure-volume work, and chemical potential."
                        },
                        {
                            "name": "Clausius Inequality",
                            "formula": "\\oint \\frac{\\delta Q}{T} \\le 0",
                            "explanation": "Second Law constraint establishing that cyclic entropy generation is non-negative."
                        }
                    ]
                },
                {
                    "name": "Thermodynamic Potentials & Maxwell Relations",
                    "content": r"""Thermodynamic potentials are state functions whose partial derivatives generate all macroscopic physical variables of a system. By performing Legendre transformations on internal energy $U(S, V, N)$, three additional primary potentials are derived:

- **Enthalpy:** $H(S, P, N) = U + PV$, with total differential $dH = T dS + V dP + \mu dN$.
- **Helmholtz Free Energy:** $F(T, V, N) = U - TS$, with total differential $dF = -S dT - P dV + \mu dN$. $F$ measures the maximum reversible work obtainable under isothermal, isochoric conditions.
- **Gibbs Free Energy:** $G(T, P, N) = H - TS$, with total differential $dG = -S dT + V dP + \mu dN$. $G$ governs systems at constant temperature and pressure.

Because the mixed second-order partial derivatives of exact differentials commute (Schwarz's theorem), each potential yields a fundamental **Maxwell Relation**:
1. $\left(\frac{\partial T}{\partial V}\right)_S = -\left(\frac{\partial P}{\partial S}\right)_V$
2. $\left(\frac{\partial T}{\partial P}\right)_S = \left(\frac{\partial V}{\partial S}\right)_P$
3. $\left(\frac{\partial S}{\partial V}\right)_T = \left(\frac{\partial P}{\partial T}\right)_V$
4. $\left(\frac{\partial S}{\partial P}\right)_T = -\left(\frac{\partial V}{\partial T}\right)_P$

These relations enable the experimental determination of unmeasurable quantities (such as entropy variations) via accessible measurements of pressure, volume, and temperature.""",
                    "simulation_logic": "4PT Logic: Legendre transformations represent canonical coordinate changes in the simulation engine, allowing the system state to be evaluated equivalently in terms of extensive variables ($S, V$) or intensive controls ($T, P$).",
                    "equations": [
                        {
                            "name": "Gibbs Free Energy Differential",
                            "formula": "dG = -S dT + V dP + \\sum_i \\mu_i dN_i",
                            "explanation": "Differential fundamental relation for systems under constant temperature and pressure."
                        },
                        {
                            "name": "Primary Maxwell Relation",
                            "formula": "\\left(\\frac{\\partial S}{\\partial V}\\right)_T = \\left(\\frac{\\partial P}{\\partial T}\\right)_V",
                            "explanation": "Relates isothermal entropy changes with volume to thermal pressure coefficients."
                        }
                    ]
                }
            ]
        },
        {
            "subject": "Thermodynamics & Statistical Mechanics",
            "course": "Statistical Mechanics & Ensembles",
            "course_desc": "Gibbs ensemble theory, partition functions, quantum statistics (Fermi-Dirac & Bose-Einstein), and Jaynes maximum entropy.",
            "topics": [
                {
                    "name": "Statistical Ensembles & The Partition Function",
                    "content": r"""Statistical mechanics connects microscopic mechanical trajectories in phase space $\Gamma = (q_i, p_i)$ with macroscopic thermodynamic observables. Josiah Willard Gibbs formalized this through three canonical ensembles:

1. **Microcanonical Ensemble:** Describes an isolated system with fixed energy $E$, volume $V$, and particle number $N$. The statistical weight is uniform across the energy shell, yielding Boltzmann's entropy: $S = k_B \ln \Omega(E, V, N)$.
2. **Canonical Ensemble:** Describes a system in thermal contact with a heat bath at inverse temperature $\beta = 1/(k_B T)$. The probability of microstate $i$ with energy $E_i$ follows the Boltzmann distribution: $P_i = \frac{1}{Z} e^{-\beta E_i}$. The canonical partition function is $Z = \sum_i e^{-\beta E_i} = \text{Tr}(e^{-\beta \hat{H}})$, from which the Helmholtz free energy is obtained directly via $F = -k_B T \ln Z$.
3. **Grand Canonical Ensemble:** Allows particle exchange with a chemical reservoir at potential $\mu$. The grand partition function $\Xi = \sum_i e^{-\beta(E_i - \mu N_i)}$ yields the grand potential $\Phi = -k_B T \ln \Xi$.

The partition function acts as the generating functional for all thermodynamic moments: the average energy is $\langle E \rangle = -\frac{\partial \ln Z}{\partial \beta}$, and energy fluctuations determine heat capacity: $\sigma_E^2 = \langle E^2 \rangle - \langle E \rangle^2 = k_B T^2 C_V$.""",
                    "simulation_logic": "4PT Logic: The partition function $Z$ is the universal compiling normalizer: summing over all allowable configuration states gives the total probability amplitude of the sector.",
                    "equations": [
                        {
                            "name": "Canonical Partition Function",
                            "formula": "Z = \\sum_i e^{-\\beta E_i} = \\text{Tr}\\left(e^{-\\beta \\hat{H}}\\right), \\quad \\beta = \\frac{1}{k_B T}",
                            "explanation": "Sum over states generating all equilibrium thermodynamic expectation values."
                        },
                        {
                            "name": "Boltzmann Entropy Formula",
                            "formula": "S = k_B \\ln \\Omega",
                            "explanation": "Logarithmic relation between thermodynamic entropy and phase space microstate volume $\\Omega$."
                        }
                    ]
                },
                {
                    "name": "Quantum Statistical Distributions (Fermi-Dirac & Bose-Einstein)",
                    "content": r"""Indistinguishability of identical quantum particles fundamentally alters their statistical counting, leading to two distinct quantum statistics based on intrinsic spin (the Spin-Statistics Theorem, Pauli 1940):

- **Fermions (Half-Integer Spin $s = 1/2, 3/2, \dots$):** Governed by the Pauli Exclusion Principle, which forbids more than one fermion from occupying the same single-particle quantum state. Fermion occupation numbers follow the **Fermi–Dirac Distribution**:
  $$\bar{n}_i = \frac{1}{e^{(\epsilon_i - \mu)/(k_B T)} + 1}$$
  At $T = 0\text{ K}$, fermions fill energy levels up to the Fermi energy $E_F$. This creates degeneracy pressure, supporting white dwarfs (electron degeneracy) and neutron stars against gravitational collapse.

- **Bosons (Integer Spin $s = 0, 1, 2, \dots$):** Symmetric wave functions allow unlimited particles to occupy the identical quantum state. Boson occupation numbers follow the **Bose–Einstein Distribution**:
  $$\bar{n}_i = \frac{1}{e^{(\epsilon_i - \mu)/(k_B T)} - 1}$$
  Below a critical temperature $T_c$, a macroscopic fraction of bosons condenses into the lowest single-particle ground state ($\epsilon_0 = 0$), forming a **Bose–Einstein Condensate (BEC)**. Predicted by Bose and Einstein in 1924, BEC was experimentally synthesized in 1995 by Cornell, Wieman, and Ketterle using rubidium and sodium atoms.""",
                    "simulation_logic": "4PT Logic: The Fermi-Dirac distribution prevents coordinate collision in the 3D rendering buffer; the Bose-Einstein distribution enables coherent multi-node synchronization (lasers and superfluids).",
                    "equations": [
                        {
                            "name": "Fermi-Dirac Distribution",
                            "formula": "\\bar{n}_i = \\frac{1}{e^{\\beta(\\epsilon_i - \\mu)} + 1}",
                            "explanation": "Average occupation number for fermions subject to the Pauli exclusion principle."
                        },
                        {
                            "name": "Bose-Einstein Distribution",
                            "formula": "\\bar{n}_i = \\frac{1}{e^{\\beta(\\epsilon_i - \\mu)} - 1}",
                            "explanation": "Average occupation number for bosons admitting Bose-Einstein condensation."
                        }
                    ]
                }
            ]
        },

        # =====================================================================
        # 2. MATHEMATICS & GEOMETRY: Functional Analysis & Differential Topology
        # =====================================================================
        {
            "subject": "Mathematics & Geometry",
            "course": "Functional Analysis & Operator Algebras",
            "course_desc": "Hilbert space spectral theory, bounded and unbounded self-adjoint operators, and Von Neumann algebras.",
            "topics": [
                {
                    "name": "Hilbert Spaces & Spectral Decomposition",
                    "content": r"""A Hilbert space $\mathcal{H}$ is an abstract vector space possessing the structure of an inner product $\langle x, y \rangle$ that is complete with respect to the induced norm $\|x\| = \sqrt{\langle x, x \rangle}$. Hilbert spaces serve as the universal mathematical arena for quantum mechanics, Fourier analysis, and linear partial differential equations.

The Riesz Representation Theorem establishes an isometric isomorphism between $\mathcal{H}$ and its continuous dual space $\mathcal{H}^*$: every continuous linear functional $f \in \mathcal{H}^*$ is uniquely represented by an inner product with a vector $y_f$: $f(x) = \langle y_f, x \rangle$.

For a densely defined, self-adjoint operator $\hat{A} = \hat{A}^\dagger$ on $\mathcal{H}$, the Spectral Theorem provides the ultimate generalization of matrix diagonalization. The operator decomposes into an integral over its spectrum $\sigma(\hat{A}) \subset \mathbb{R}$ against a Projection-Valued Measure (PVM) $E$:
$$\hat{A} = \int_{\sigma(\hat{A})} \lambda \, dE(\lambda)$$
In quantum mechanics, this theorem guarantees that physical measurement outcomes are real numbers and that measurement probabilities are obtained from the projection spectral measure $\langle \psi | E(\Delta) | \psi \rangle$.""",
                    "simulation_logic": "4PT Logic: The Spectral Theorem is the decompression algorithm of physical measurement: operator observables project infinite-dimensional Hilbert space amplitudes onto concrete real eigenvalues.",
                    "equations": [
                        {
                            "name": "Spectral Theorem for Self-Adjoint Operators",
                            "formula": "\\hat{A} = \\int_{\\sigma(\\hat{A})} \\lambda \\, dE(\\lambda)",
                            "explanation": "Decomposition of self-adjoint operator into real eigenvalues weighted by projection measure $E$."
                        },
                        {
                            "name": "Inner Product Norm Axiom",
                            "formula": "\\|x\\| = \\sqrt{\\langle x, x \\rangle}, \\quad \\langle x, y \\rangle = \\overline{\\langle y, x \\rangle}",
                            "explanation": "Inner product axioms ensuring completeness and geometric orthogonality in Hilbert space."
                        }
                    ]
                },
                {
                    "name": "Differential Forms & Generalized Stokes' Theorem",
                    "content": r"""Exterior calculus, formalized by Élie Cartan, provides a coordinate-independent formulation of multivariable calculus on smooth manifolds. A differential $k$-form $\omega \in \Omega^k(M)$ is a completely antisymmetric tensor field of rank $(0, k)$.

The exterior derivative $d: \Omega^k(M) \to \Omega^{k+1}(M)$ is the unique nilpotent linear differential operator satisfying:
1. $d(f) = \sum \frac{\partial f}{\partial x^i} dx^i$ for 0-forms.
2. $d(\alpha \wedge \beta) = d\alpha \wedge \beta + (-1)^p \alpha \wedge d\beta$ for $p$-form $\alpha$.
3. Nilpotency: $d^2 = d \circ d = 0$.

A form is **closed** if $d\omega = 0$, and **exact** if $\omega = d\alpha$. The de Rham cohomology group $H^k_{\text{dR}}(M) = \ker d_k / \text{im } d_{k-1}$ measures the topological holes of the manifold.

The **Generalized Stokes' Theorem** unifies the Fundamental Theorem of Calculus, Green's Theorem, the Divergence Theorem, and the classical Kelvin-Stokes Theorem into a single equation:
$$\int_{\partial M} \omega = \int_M d\omega$$
where $M$ is an oriented compact $(k+1)$-dimensional manifold with boundary $\partial M$, and $\omega$ is a smooth $k$-form. In Maxwellian electrodynamics, exterior calculus collapses all four Maxwell equations into two elegant geometric statements: $dF = 0$ (homogeneous) and $d *F = *J$ (inhomogeneous).""",
                    "simulation_logic": "4PT Logic: Stokes' Theorem proves that global boundary data on the simulation's outer horizon completely determines the interior field dynamics ($d^2 = 0$).",
                    "equations": [
                        {
                            "name": "Generalized Stokes' Theorem",
                            "formula": "\\int_{\\partial M} \\omega = \\int_M d\\omega",
                            "explanation": "Integrates differential form over manifold boundary relating topology to exterior derivative."
                        },
                        {
                            "name": "Geometric Maxwell Field Equations",
                            "formula": "dF = 0, \\quad d *F = *J",
                            "explanation": "Maxwell's equations expressed compactly via field strength 2-form $F = dA$ and Hodge star $*F$."
                        }
                    ]
                }
            ]
        },

        # =====================================================================
        # 3. CHEMICAL SCIENCES: Molecular Orbitals & Catalytic Kinetics
        # =====================================================================
        {
            "subject": "Chemical Sciences",
            "course": "Chemical Bonding & Molecular Dynamics",
            "course_desc": "Molecular orbital theory, covalent bonding, electronegativity, and reaction kinetics.",
            "topics": [
                {
                    "name": "Covalent Bonding & Molecular Orbital Theory",
                    "content": r"""Molecular Orbital (MO) Theory provides the quantum mechanical foundation for chemical bonding. When atoms approach, their atomic wave functions overlap, combining via the Linear Combination of Atomic Orbitals (LCAO) approximation:
$$\psi_{\text{MO}} = c_A \phi_A \pm c_B \phi_B$$

Constructive phase interference produces a **bonding molecular orbital** with increased electron probability density between nuclei, lowering the potential energy below that of isolated atoms. Destructive phase interference produces an **anti-bonding molecular orbital** ($\sigma^*, \pi^*$) with a nodal plane between nuclei, raising the energy.

Bond stability is quantified by the bond order: $\text{Bond Order} = \frac{N_{\text{bonding}} - N_{\text{antibonding}}}{2}$. Electrons occupy molecular orbitals according to the Aufbau principle, Hund's rule, and the Pauli exclusion principle, accurately explaining molecular magnetism (such as the paramagnetism of diatomic oxygen $O_2$).""",
                    "simulation_logic": "4PT Logic: Molecular orbitals represent shared distributed memory: individual atomic data structures merge their phase buffers into stable collective state packets.",
                    "equations": [
                        {
                            "name": "LCAO Wave Function Expansion",
                            "formula": "\\psi_{\\text{MO}} = \\sum_i c_i \\phi_i",
                            "explanation": "Linear combination of atomic orbitals generating molecular bonding and anti-bonding states."
                        },
                        {
                            "name": "Bond Order Definition",
                            "formula": "\\text{Bond Order} = \\frac{N_b - N_a}{2}",
                            "explanation": "Criterion for covalent bond stability based on net bonding electron pairs."
                        }
                    ]
                },
                {
                    "name": "Electronegativity & The Pauling Scale",
                    "content": r"""Electronegativity, formulated by Linus Pauling in 1932, is a fundamental chemical property measuring the tendency of an atom to attract a shared pair of electrons in a covalent chemical bond.

Pauling derived the electronegativity difference $(\chi_A - \chi_B)$ between elements $A$ and $B$ from empirical bond dissociation energies $E_d$:
$$\chi_A - \chi_B = (0.102 \\text{ eV}^{-1/2}) \\sqrt{E_d(AB) - \\frac{1}{2}[E_d(AA) + E_d(BB)]}$$
where the term inside the square root represents the extra ionic resonance energy stabilizing the polar bond.

Electronegativity values range from 0.7 (francium) to 4.0 (fluorine). Differences in electronegativity determine the character of chemical bonding across a continuous spectrum: non-polar covalent ($\Delta\chi < 0.4$), polar covalent ($0.4 \le \Delta\chi \le 1.7$), and ionic ($\Delta\chi > 1.7$). This asymmetry creates permanent molecular dipole moments $\mu = q \cdot r$, driving intermolecular hydrogen bonding, water's high dielectric constant, and biological macro-molecular folding.""",
                    "simulation_logic": "4PT Logic: Electronegativity represents the local informational pull of atomic nodes: uneven charge weighting generates polar bias across conductive simulation pathways.",
                    "equations": [
                        {
                            "name": "Pauling Electronegativity Relation",
                            "formula": "|\\chi_A - \\chi_B| = \\sqrt{E_d(AB) - \\sqrt{E_d(AA) \\cdot E_d(BB)}}",
                            "explanation": "Calculation of electronegativity difference from empirical bond dissociation energy excesses."
                        }
                    ]
                }
            ]
        }
    ]

    total_created_topics = 0
    total_created_eqs = 0

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
            total_created_topics += 1

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
                total_created_eqs += 1

    # Link new topics to Core Theories
    theory_links = {
        "Thermodynamics_Information": [
            "The Four Laws of Thermodynamics",
            "Thermodynamic Potentials & Maxwell Relations",
            "Statistical Ensembles & The Partition Function",
            "Quantum Statistical Distributions (Fermi-Dirac & Bose-Einstein)"
        ],
        "Quantum_Mechanics": [
            "Hilbert Spaces & Spectral Decomposition",
            "Quantum Statistical Distributions (Fermi-Dirac & Bose-Einstein)"
        ],
        "IUC": [
            "Differential Forms & Generalized Stokes' Theorem",
            "Statistical Ensembles & The Partition Function"
        ],
        "General_Relativity": [
            "Differential Forms & Generalized Stokes' Theorem"
        ]
    }

    for th_name, top_names in theory_links.items():
        th = Theory.objects.filter(name=th_name).first()
        if th:
            for tn in top_names:
                t_obj = Topic.objects.filter(name=tn).first()
                if t_obj:
                    th.topics.add(t_obj)

    print(f"Deep Expansion Complete: Added {total_created_topics} Topics and {total_created_eqs} Equations across foundational disciplines.")

if __name__ == '__main__':
    seed_expansion()

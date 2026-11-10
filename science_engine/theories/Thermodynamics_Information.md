# Statistical Mechanics, Thermodynamics & Information Theory

> **Core Premise:** Macroscopic thermodynamic laws and the arrow of time are statistical reflections of phase space volume and microstate counting; physical entropy is fundamentally equivalent to missing information content in microstate specification.

---

## 1. Mathematical Framework & State Space
* **Microstate Phase Space:** Symplectic phase space $\Gamma = \{ (q_i, p_i) \}_{i=1}^{3N}$ with Liouville measure $d\Gamma = \prod_{i=1}^{3N} \frac{dq_i dp_i}{(2\pi\hbar)^{3N}}$.
* **Density Distribution:** Probability measure $\rho(q, p, t)$ on $\Gamma$ satisfying the Liouville equation:
  $$\frac{\partial \rho}{\partial t} + \{\rho, H\} = 0$$
* **Quantum Density Operator:** Statistical operator $\hat{\rho}$ on Hilbert space $\mathcal{H}$ with $\hat{\rho} \ge 0$, $\text{Tr}(\hat{\rho}) = 1$.

---

## 2. Core Physical Mechanisms
- **Boltzmann & Gibbs Entropy:**
  $$S_B = k_B \ln \Omega(E), \quad S_{\text{Gibbs}} = -k_B \int d\Gamma \, \rho \ln \rho$$
- **Von Neumann Quantum Entropy:**
  $$S_{\text{vN}}(\hat{\rho}) = -k_B \text{Tr}(\hat{\rho} \ln \hat{\rho})$$
- **Shannon Information Theory & Equivalence:** For a discrete probability distribution $\{p_i\}$:
  $$H(X) = -\sum_{i} p_i \log_2 p_i \implies S = k_B \ln(2) H(X)$$
- **Landauer's Principle (1961):** Erasure of one bit of information in a thermal environment at temperature $T$ dissipates a minimum heat energy of:
  $$\Delta Q \ge k_B T \ln 2$$
- **Bekenstein–Hawking Black Hole Entropy (1973–1974):**
  $$S_{\text{BH}} = \frac{k_B c^3 A}{4 G \hbar} = \frac{k_B A}{4 \ell_P^2}$$
  connecting gravitation, quantum mechanics, and information geometry on event horizons.

---

## 3. Formal Axioms
1. **First Law (Conservation of Energy):** $dE = \delta Q - \delta W$.
2. **Second Law (Monotonicity of Entropy):** For any isolated macroscopic system, $\Delta S \ge 0$.
3. **Third Law (Nernst Heat Theorem):** As $T \to 0$, entropy approaches a universal constant independent of phase: $\lim_{T \to 0} S = 0$ for non-degenerate ground states.
4. **Jaynes Maximum Entropy Principle (1957):** The least biased probability distribution representing incomplete knowledge is the one that maximizes Shannon-Gibbs entropy subject to known macroscopic expectation values $\langle O_k \rangle$.

---

## 4. Symmetry Groups & Invariants
- **Phase Space Measure Invariance:** Canonical transformations preserve symplectic 2-form $\omega$ and phase space volume (Liouville's theorem).
- **Time-Reversal Asymmetry:** Microscopic equations of motion are time-reversal invariant ($T$-symmetry), while coarse-grained macroscopic entropy growth $dS/dt \ge 0$ defines the thermodynamic arrow of time.

---

## 5. Post-1984 Empirical Constraints & Benchmarks
- **Experimental Verification of Landauer's Principle (Bérut et al., Nature 2012):** Direct experimental measurement of dissipation during single-bit erasure in optical traps, confirming the $k_B T \ln 2$ bound.
- **Fluctuation Theorems (Jarzynski Equality 1997, Crooks 1999):** Exact relations for non-equilibrium work distributions $\langle e^{-\beta W} \rangle = e^{-\beta \Delta F}$, experimentally verified in single-molecule RNA unfolding.
- **Casimir Effect Precision Measurements (Lamoreaux 1997, Mohideen 1998):** Verified vacuum expectation energy shifts between conducting plates.

---

## 6. Identified Gaps & Incompatibilities
- **Loschmidt Paradox (Reversibility):** Deriving irreversible macroscopic dissipation ($dS/dt > 0$) strictly from time-reversible unitary quantum Hamiltonian evolution without ad-hoc coarse-graining.
- **Black Hole Information Retention:** Reconciling the thermal Bekenstein-Hawking entropy formula with quantum unitarity during late-stage black hole evaporation.

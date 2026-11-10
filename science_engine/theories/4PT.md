# The 4D Probability Tensor Field (4PT): Hypersurface Foliation & Quantum Decoherence

> **Core Premise:** Physical reality in $(3+1)$ spacetime is an induced Cauchy hypersurface foliation evolving within a higher-dimensional configuration space (superspace). Deterministic unitary evolution in superspace manifests on local spacelike slices as branching quantum probability amplitudes, with classicality enforced dynamically via environmental decoherence and pointer-state selection.

---

## 1. Foliation & Dimensional Architecture
* **3D Hypersurface $\Sigma_t$ (The Physical Spatial Slice):** Riemannian 3-manifold with induced metric $\gamma_{ij}$ and extrinsic curvature $K_{ij}$ within the ADM (Arnowitt–Deser–Misner, 1959) $(3+1)$ decomposition:
  $$ds^2 = -(N^2 - N_i N^i)dt^2 + 2N_i dx^i dt + \gamma_{ij} dx^i dx^j$$
* **4D Spacetime & Probability Branching (Everett–Wheeler Formalism):** The 4D spacetime history is an integral curve through Wheeler's superspace $\text{Riem}(\Sigma)/\text{Diff}(\Sigma)$. The universal state vector $|\Psi\rangle$ satisfies the Wheeler–DeWitt constraint (1967):
  $$\hat{\mathcal{H}} |\Psi\rangle = 0$$
  Branching corresponds to the decomposition of $|\Psi\rangle$ into orthogonal non-interfering decoherent histories.
* **Extended Dimensional Boundary Condition (Kaluza–Klein / Symplectic Geometry):** Ambient bundle space with connection 1-forms $A = A_\mu dx^\mu$ inducing gauge couplings. Global boundary conditions constrain the local Cauchy data on $\Sigma_0$.

---

## 2. Core Physical Mechanisms
- **ADM Foliation Dynamics:** Spatial evolution is governed by the Hamiltonian and momentum constraints:
  $$\mathcal{H} = \frac{1}{\sqrt{\gamma}} \left( K_{ij}K^{ij} - K^2 \right) - \sqrt{\gamma} \, {}^{(3)}R = 0, \quad \mathcal{M}^i = D_j (K^{ij} - \gamma^{ij}K) = 0$$
- **Lindblad Open System Decoherence (Zeh 1970, Lindblad 1976):** Subsystem density matrix $\rho_S = \text{Tr}_E(\rho_{\text{total}})$ evolves via the Lindblad master equation:
  $$\frac{\partial \rho_S}{\partial t} = -\frac{i}{\hbar} [\hat{H}_S, \rho_S] + \sum_k \left( \hat{L}_k \rho_S \hat{L}_k^\dagger - \frac{1}{2} \{ \hat{L}_k^\dagger \hat{L}_k, \rho_S \} \right)$$
  Off-diagonal elements decay exponentially at decoherence rate $\tau_{\text{dec}} \sim \tau_{\text{thermal}} \left(\frac{\lambda_{\text{thermal}}}{\Delta x}\right)^2$.
- **Einselection & Pointer State Invariance ("Sealing"):** Environment-Induced Superselection (Zurek, 1981) dynamically selects states $|\pi_i\rangle$ that are stable against entanglement with the environment:
  $$[\hat{H}_{SE}, |\pi_i\rangle\langle \pi_i|] \approx 0$$
  States that satisfy this commutation relation survive decoherence without information entropy loss into the reservoir.
- **Topological Boundary Injections (Instantons & Solitons):** Localized transitions between topologically distinct vacua are mediated by finite-action solutions in Euclidean spacetime (BPST instantons, 1975):
  $$S_E = \frac{1}{4g^2} \int d^4x \, F_{\mu\nu}^a F^{a\mu\nu} = \frac{8\pi^2 |q|}{g^2}$$
  Apparent discontinuities in local observables correspond to tunneling across topological winding sectors $q \in \pi_3(G) = \mathbb{Z}$.

---

## 3. Formal Axioms
1. **Axiom of Global Unitary Invariance:** The total state vector $|\Psi\rangle \in \mathcal{H}_{\text{total}}$ undergoes purely unitary time evolution under self-adjoint Hamiltonian $\hat{H}_{\text{total}} = \hat{H}_{\text{total}}^\dagger$.
2. **Axiom of Hypersurface Projection:** What a localized observer records as classical time $t$ is the parameter labeling the foliation $\Sigma_t$ along the normal vector $n^\mu = \frac{1}{N}(1, -N^i)$.
3. **Axiom of Decoherent Classicality:** Classical macroscopic trajectories emerge exclusively when the phase coherence between branches drops below the thermal threshold:
  $$\langle \psi_i(t) | \hat{\rho}_E(t) | \psi_j(t) \rangle \to \delta_{ij}$$
4. **Axiom of Gauge Redundancy:** Observable physical degrees of freedom are quotient invariants under the infinite-dimensional diffeomorphism group $\text{Diff}(\mathcal{M})$ and local gauge group $\mathcal{G}$.

---

## 4. Symmetry Groups & Mathematical Invariants
- **Diffeomorphism Group:** $\text{Diff}(\mathcal{M}_4)$ maintaining general covariance.
- **Symplectic Structure:** Non-degenerate closed 2-form $\Omega = \sum dp_i \wedge dq^i$ on the phase space of field configurations.
- **Casimir Invariants:** Mass-squared $P_\mu P^\mu = -m^2$ and relativistic spin $W_\mu W^\mu = m^2 s(s+1)$ from the Poincaré Lie algebra.

---

## 5. Post-1984 Empirical Constraints & Benchmarks
- **Experimental Cavity QED Decoherence (Brune et al., 1996; Haroche/Wineland, Nobel 2012):** Quantitative verification of decoherence dynamics using mesoscopic Schrödinger cat states of Rydberg atoms in microwave cavities.
- **Delayed-Choice Quantum Erasure (Kim et al., 1999):** Empirical proof that path information determination enforces complementarity collapse even when detection occurs after photon registration.
- **Neutrino Mass Splittings & Flavor Oscillations (Super-K 1998, SNO 2001):** Verified quantum mechanical flavor state superposition $\nu_\alpha = \sum U_{\alpha i} \nu_i$ evolving coherently over astronomical distances ($L/E$).
- **LIGO Gravitational Wave Polarizations (2017+):** Confirmation of two transverse-traceless tensor polarizations ($h_+, h_\times$) matching massless spin-2 Einstein gravitons without scalar or vector radiative modes.

---

## 6. Identified Gaps & Incompatibilities
- **Problem of Time in Quantum Gravity:** In canonical quantum gravity, the Wheeler–DeWitt equation $\hat{\mathcal{H}}|\Psi\rangle = 0$ contains no explicit time parameter $t$, requiring relational clock variables $\hat{\chi}$ to define internal evolution.
- **Black Hole Information Paradox:** The apparent conflict between Hawking radiation thermal evaporation ($S_{\text{Hawking}} = \frac{k_B c^3 A}{4G\hbar}$, 1974) and global S-matrix unitarity.
- **Quantum Decoherence Pointer Basis Selection:** Deriving the exact pointer basis purely from the total Hamiltonian without arbitrary system-environment splitting boundaries.

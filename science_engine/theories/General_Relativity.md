# General Relativity (GR)

> **Core Premise:** Gravitation is not an external physical force, but the manifestation of the curvature of a 4-dimensional pseudo-Riemannian spacetime manifold caused by the stress-energy-momentum distribution of matter and fields.

---

## 1. Mathematical Framework & State Space
* **Manifold:** 4-dimensional smooth Lorentzian manifold $(\mathcal{M}_4, g_{\mu\nu})$ with signature $(-, +, +, +)$.
* **Affine Connection:** Unique torsion-free Levi-Civita connection $\Gamma^\lambda_{\mu\nu} = \frac{1}{2}g^{\lambda\sigma}(\partial_\mu g_{\nu\sigma} + \partial_\nu g_{\mu\sigma} - \partial_\sigma g_{\mu\nu})$.
* **Curvature Tensors:** Riemann curvature tensor $R^\rho_{\ \sigma\mu\nu}$, Ricci tensor $R_{\mu\nu} = R^\lambda_{\ \mu\lambda\nu}$, and Ricci scalar $R = g^{\mu\nu} R_{\mu\nu}$.

---

## 2. Core Physical Mechanisms
- **Einstein Field Equations (EFE):** Derived from the Einstein–Hilbert action $S = \frac{c^4}{16\pi G} \int d^4x \sqrt{-g} (R - 2\Lambda) + S_{\text{matter}}$:
  $$G_{\mu\nu} + \Lambda g_{\mu\nu} = \frac{8\pi G}{c^4} T_{\mu\nu}$$
  where $G_{\mu\nu} \equiv R_{\mu\nu} - \frac{1}{2}R g_{\mu\nu}$ is the Einstein tensor.
- **Geodesic Motion:** Free-falling test particles follow timelike or null geodesics:
  $$\frac{d^2 x^\mu}{d\tau^2} + \Gamma^\mu_{\alpha\beta} \frac{dx^\alpha}{d\tau} \frac{dx^\beta}{d\tau} = 0$$
- **Gravitational Radiation:** Quadrupole formula for transverse-traceless metric perturbations $h_{ij}^{TT}$:
  $$\bar{h}_{ij}^{TT}(t, r) = \frac{2G}{c^4 r} \ddot{I}_{ij}\left(t - \frac{r}{c}\right)$$

---

## 3. Formal Axioms
1. **Equivalence Principle:** At any spacetime point, the gravitational field can be locally transformed away by transitioning to a locally inertial Cartesian coordinate frame.
2. **General Covariance:** Physical laws preserve form under arbitrary smooth coordinate transformations (Diffeomorphism invariance $\text{Diff}(\mathcal{M})$).
3. **Conservation Invariance:** Bianchi identities enforce exact covariant conservation of stress-energy:
  $$\nabla_\mu G^{\mu\nu} = 0 \implies \nabla_\mu T^{\mu\nu} = 0$$

---

## 4. Symmetry Groups & Invariants
- **Spacetime Symmetries:** Invariance under the diffeomorphism group $\text{Diff}(\mathcal{M})$.
- **Noether Invariants:** Killing vectors $\xi^\mu$ satisfying Killing's equation $\nabla_\mu \xi_\nu + \nabla_\nu \xi_\mu = 0$ generate constants of motion $C = g_{\mu\nu} \xi^\mu \frac{dx^\nu}{d\tau}$.

---

## 5. Post-1984 Empirical Constraints & Benchmarks
- **Binary Pulsar Orbital Decay (Hulse-Taylor PSR B1913+16, Nobel 1993):** Quadrupole gravitational wave damping verified to $<0.2\%$ precision.
- **Direct Gravitational Wave Detections (LIGO/Virgo, 2015+):** Transverse-traceless strain $h(t)$ matching numerical relativity waveforms for binary black hole mergers (GW150914).
- **Event Horizon Imaging (Event Horizon Telescope, 2019/2022):** Direct shadow imaging of supermassive black holes M87* and Sagittarius A* confirming Kerr metric shadow diameters.
- **Cosmic Microwave Background Flatness (Planck 2018):** Global spatial curvature $|\Omega_k| < 0.005$, confirming spatially flat Robertson-Walker metric.

---

## 6. Identified Gaps & Incompatibilities
- **Spacetime Singularities:** Penrose-Hawking singularity theorems prove incomplete geodesics at black hole interiors ($r=0$) and big bang, where curvature invariants diverge:
  $$R^{\mu\nu\rho\sigma} R_{\mu\nu\rho\sigma} \to \infty$$
- **Quantum Incompatibility:** Non-renormalizability of perturbative Einstein-Hilbert gravity when quantized as a quantum field theory with coupling $G \sim M_{\text{Planck}}^{-2}$.

# Electroweak Unified Gauge Theory ($SU(2)_L \times U(1)_Y$)

> **Core Premise:** Electromagnetic and weak nuclear interactions are unified within a non-Abelian Yang–Mills gauge theory with symmetry group $SU(2)_L \times U(1)_Y$, which undergoes spontaneous symmetry breaking via the Brout–Englert–Higgs mechanism down to electromagnetic $U(1)_{\text{EM}}$.

---

## 1. Mathematical Framework & State Space
* **Fiber Bundle:** Principal fiber bundle $P(\mathcal{M}_4, G)$ with structure group $G = SU(2)_L \times U(1)_Y$.
* **Connection 1-Forms (Gauge Fields):** $W_\mu = W_\mu^a \tau^a$ ($a=1,2,3$ with $\tau^a = \sigma^a/2$) and hypercharge gauge field $B_\mu$.
* **Curvature 2-Forms (Field Strengths):**
  $$W_{\mu\nu}^a = \partial_\mu W_\nu^a - \partial_\nu W_\mu^a + g \epsilon^{abc} W_\mu^b W_\nu^c, \quad B_{\mu\nu} = \partial_\mu B_\nu - \partial_\nu B_\mu$$

---

## 2. Core Physical Mechanisms
- **Yang–Mills Gauge Action:**
  $$\mathcal{L}_{\text{gauge}} = -\frac{1}{4} W_{\mu\nu}^a W^{a\mu\nu} - \frac{1}{4} B_{\mu\nu} B^{\mu\nu}$$
- **Spontaneous Symmetry Breaking (Higgs Mechanism):** Complex scalar doublet $\Phi = \begin{pmatrix} \phi^+ \\ \phi^0 \end{pmatrix}$ with Mexican-hat potential $V(\Phi) = \mu^2 \Phi^\dagger \Phi + \lambda (\Phi^\dagger \Phi)^2$ ($\mu^2 < 0$). Vacuum expectation value:
  $$\langle \Phi \rangle = \frac{1}{\sqrt{2}} \begin{pmatrix} 0 \\ v \end{pmatrix}, \quad v = \sqrt{-\frac{\mu^2}{\lambda}} \approx 246\text{ GeV}$$
- **Boson Mass Generation:** Gauge bosons acquire mass via covariant kinetic term $|D_\mu \Phi|^2$:
  $$M_W = \frac{1}{2} g v, \quad M_Z = \frac{1}{2} \sqrt{g^2 + g'^2} v, \quad M_\gamma = 0$$
  mixing angle: $\cos\theta_W = \frac{M_W}{M_Z} = \frac{g}{\sqrt{g^2 + g'^2}}$.

---

## 3. Formal Axioms
1. **Axiom of Chiral Gauge Invariance:** Left-handed fermions transform as $SU(2)_L$ doublets; right-handed fermions transform as $SU(2)_L$ singlets.
2. **Axiom of Renormalizability (t'Hooft 1971):** Spontaneously broken Yang–Mills gauge theories are rigorously renormalizable to all loop orders.
3. **Axiom of Anomaly Cancellation:** Triangle chiral anomalies vanish identically across generations due to exact charge assignments $\sum Q_f = 0$.

---

## 4. Symmetry Groups & Invariants
- **Gauge Group:** $SU(2)_L \times U(1)_Y \xrightarrow{\text{SSB}} U(1)_{\text{EM}}$.
- **Conserved Charges:** Electric charge $Q = T_3 + Y$, where $T_3$ is the third component of weak isospin and $Y$ is weak hypercharge.

---

## 5. Post-1984 Empirical Constraints & Benchmarks
- **Top Quark Mass (Fermilab CDF/D0, 1995):** $m_t = 172.69 \pm 0.30\text{ GeV}$, completing the three generations of quarks.
- **Precision Electroweak Measurements (LEP / SLC, 1990s):** Number of light neutrino families determined to be exactly $N_\nu = 2.984 \pm 0.008$.
- **Higgs Scalar Discovery (CERN LHC, 2012):** Neutral spin-0 CP-even scalar confirmed at $m_H = 125.09 \pm 0.24\text{ GeV}$ with coupling strengths matching SM predictions within $10\%$.
- **Absence of Low-Energy Supersymmetry (LHC Run 2/3, up to 2024):** Strict mass exclusion limits ($m_{\tilde{g}} > 2.3\text{ TeV}$, $m_{\tilde{q}} > 1.9\text{ TeV}$), falsifying minimal weak-scale SUSY literature.

---

## 6. Identified Gaps & Incompatibilities
- **Neutrino Mass Splittings:** Minimally constructed electroweak model requires exactly massless neutrinos, conflicting directly with post-1984 verified neutrino oscillation data.
- **Hierarchy Problem:** Quadratic divergence in the radiative corrections to the Higgs scalar mass: $\delta m_H^2 \sim \frac{\lambda}{16\pi^2} \Lambda_{\text{UV}}^2$.
- **Baryon Asymmetry:** Inability of the Standard Model CKM phase alone to explain the observed matter-antimatter cosmic asymmetry $\eta_B \approx 6 \times 10^{-10}$.

# Science Calculator Engine & StarTravel POC

[![Python](https://img.shields.io/badge/Python-3.12%20%7C%203.13%20%7C%203.14-3776AB?logo=python&logoColor=white)](https://python.org)
[![Django](https://img.shields.io/badge/Django-6.0+-092E20?logo=django&logoColor=white)](https://djangoproject.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Knowledge Base](https://img.shields.io/badge/Knowledge%20Base-416%20Topics%20%7C%201%2C330%20Equations-8A2BE2)](science_engine/fixtures/knowledge_base.json)
[![Theoretical Timeline](https://img.shields.io/badge/Chronological%20Lineage-1687%20--%202026+-orange)](https://github.com/Alednam/StarTravel_POC)

A rigorous mathematical physics and epistemic synthesis platform built on Django. The system bridges foundational theoretical physics (Analytical Mechanics, General Relativity, Gauge Field Theory, Operator Algebras) with empirical constraints, an interactive 340-year chronological connector graph, and deep-space mission architectures.

---

## Key Features

* **Oracle Chrono-Connector:**
  * **Interactive Chronological Timeline (1687 – 2026+):** Visualizes the historical evolution of physics from Classical Mechanics to Relativistic Geometrodynamics, Quantum Formalisms, Gauge Symmetries, and Modern Spaceflight.
  * **16 Directed Mathematical Bridges:** Bezier connector paths modeling exact formal derivations between theories with flowing transmission pulses.
  * **Interactive Lineage Breadcrumb:** Isolates upstream foundations and downstream derivations in real time with dynamic pedigree trees.
  * **Future Trajectory Projector:** Synthesizes multiple foundational theories to project future theoretical breakthroughs (c. 2045+) with computed coherence scores.
  * **Dual View Modes:** Smooth-panning horizontal timeline rail with minimap navigation and a compact vertical step-ladder cascade.
* **Epistemic Knowledge Base:**
  * Structured database hierarchy encompassing **7 Subjects, 62 Courses, 416 Topics, 1,330 Equations, and 8 Formal Theoretical Manuscripts**.
  * Complete, portable Django JSON fixture (`science_engine/fixtures/knowledge_base.json`) with auto-population on initialization.
* **StarTravel POC (Phases I–IV):** 18 technical interactive schematics covering deep-space spaceflight:
  * **Phase I: Propulsion:** Electrodynamic Tethers (EDT), Magnetic Sails (Magsails), Alfvén Wave MHD Coupling, Relativistic Radiative Drives.
  * **Phase II: Navigation:** Pulsar Timing Arrays (PTA), Barycentric Vector Tracking, Relativistic Shapiro Delays.
  * **Phase III: Evolution:** Closed-loop Artificial Gravity, Radiation Shielding, Bio-Resonance Conditioning.
  * **Phase IV: Architecture:** Superconducting Magnetic Shielding, Field Coils, and Habitat Structural Symmetries.
* **Cross-Discipline Gap Analysis:** Automated identification of theoretical boundaries, unproven axioms, and cross-theory synthesis opportunities.
* **Decoupled Architecture:** Secret keys, hostnames, and environments decoupled cleanly via `.env` and `python-dotenv`.

---

## Directory Structure

```text
├── documentation/               # Specifications, theoretical plans, and knowledge-base notes
│   ├── KB_implementation.md
│   ├── additional_topics.md
│   ├── err.md
│   ├── plan.md
│   └── topcs.md
├── test_scripts/                # Standalone generators & technical SVG art libraries
│   ├── assemble_poc.py
│   ├── generate_all_poc_schematics.py
│   └── poc_art_library.py
├── scicalc/                     # Django core settings and URL routing
├── science_engine/              # Physics engine app: views, models, templates, seeding
│   ├── theories/                # Formal theory definition manuscripts
│   ├── seed_*.py                # Database population scripts
│   └── logic.py                 # Epistemic analysis & graph inference
├── logic_bridge.json            # Semantic mappings between disciplines
├── manage.py                    # Django management CLI
├── requirements.txt             # Project Python dependencies
├── start_services.sh            # Service startup script (background process & logging)
├── stop_services.sh             # Graceful service shutdown script
├── .env.example                 # Template for environment configuration
└── .gitignore                   # Ignores secrets, database, virtualenv, and caches
```

---

## Quickstart & Installation

### 1. Prerequisites
* Python 3.12+ (tested on Python 3.13 / 3.14)
* `sqlite3`

### 2. Environment Setup

```bash
# Clone the repository
git clone git@github-scicalc:Alednam/StarTravel_POC.git
cd StarTravel_POC

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Configure environment variables
cp .env.example .env
```

Edit `.env` to customize your `DJANGO_SECRET_KEY`, `DEBUG`, or `ALLOWED_HOSTS`.

---

## Running the Application

### Using Service Scripts (Recommended)

Start the service in the background:
```bash
./start_services.sh
```
* Automatically runs database migrations.
* Starts the server at `http://127.0.0.1:8000/`.
* Stores runtime PID in `.server.pid` and logs to `server.log`.

Stop the service:
```bash
./stop_services.sh
```

### Manual Run

```bash
source venv/bin/activate
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
```

---

## Knowledge Base Management

The repository includes a complete Django fixture of the full knowledge base (**7 Subjects, 62 Courses, 416 Topics, and 1,330 Equations**) located at:
`science_engine/fixtures/knowledge_base.json`

### Restoring or Loading the Knowledge Base
`./start_services.sh` will automatically populate the database from the fixture if the database is clean. To manually reload or populate it:

```bash
python manage.py loaddata knowledge_base
```

### Seeding from Source Scripts
Alternatively, you can rebuild or update individual foundation modules using the seed scripts:

```bash
# Seed full foundations
./venv/bin/python science_engine/seed_full_foundations.py

# Seed deep knowledge expansion
./venv/bin/python science_engine/seed_expansion.py

# Seed spaceflight curriculum
./venv/bin/python science_engine/seed_spaceflight.py
```

---

## Rebuilding POC Schematics

The vector schematics and interactive diagrams can be regenerated at any time using the scripts in `test_scripts/`:

```bash
./venv/bin/python test_scripts/assemble_poc.py
```

---

## Scientific Domains & Research Topics

The platform models and formalizes canonical mathematical relationships across the following foundational fields:

* **Analytical Mechanics:** Variational principles ($\delta \int L \, dt = 0$), Hamilton-Jacobi dynamics, Poisson algebras, Liouville phase space measure invariance.
* **Classical & Modern Thermodynamics:** Boltzmann microstate counting ($S = k_B \ln \Omega$), Clausius entropy, Landauer's thermodynamic erasure limit ($\Delta Q \ge k_B T \ln 2$), Bekenstein-Hawking black hole area-entropy bounds.
* **General Relativity & Relativistic Astrophysics:** Einstein field equations ($G_{\mu\nu} = \kappa T_{\mu\nu}$), Schwarzschild metric, Kerr spinning metrics, gravitational Shapiro delay, ADM (3+1) hypersurface foliation ($ds^2 = -N^2 dt^2 + \gamma_{ij}(dx^i + N^i dt)(dx^j + N^j dt)$).
* **Quantum Formalism & Open Systems:** Complex Hilbert spaces, self-adjoint operator algebras, von Neumann density matrices, Lindblad master equation for environmental decoherence, Zurek einselection of pointer states.
* **Gauge Field Theory & Electroweak Symmetry:** Principal fiber bundles, Yang-Mills curvature 2-forms ($F_{\mu\nu}^a$), $SU(2)_L \times U(1)_Y$ electroweak unification, Brout-Englert-Higgs symmetry breaking, Ginzburg-Landau superconductivity.
* **Deep Space Magnetospheric Flight:** Lorentz force propulsion ($\vec{F} = I (\vec{L} \times \vec{B})$), motional induction ($\mathcal{E} = \int (\vec{v} \times \vec{B}) \cdot d\vec{\ell}$), supersonic solar wind plasma deflection ($P_{\text{dyn}} \approx B^2/2\mu_0$), shear Alfvén wings, and millisecond pulsar vector navigation.
* **Symplectic Invariants & Epistemic Synthesis:** Marsden-Weinstein reduction ($M_{\text{red}} = \mu^{-1}(0)/G$), Noether diffeomorphism invariants, 4PT probability tensor fields, and Invariant Universal Constraints (IUC).



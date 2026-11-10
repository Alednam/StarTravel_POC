# Science Calculator Engine & StarTravel POC

A rigorous mathematical physics and epistemic synthesis platform built on Django. The system bridges foundational theoretical physics (Analytical Mechanics, General Relativity, Gauge Field Theory, Operator Algebras) with empirical constraints and deep-space mission architectures.

---

## Key Features

* **Epistemic Knowledge Base:** Structured hierarchy of Subjects, Courses, Topics, Equations, and Theoretical Manuscripts.
* **StarTravel POC (Phases I–IV):** 18 technical interactive schematics covering deep-space spaceflight:
  * **Phase I: Propulsion:** Electrodynamic Tethers (EDT), Magnetic Sails, Alfvén Wave MHD Coupling, Relativistic Radiative Drives.
  * **Phase II: Navigation:** Pulsar Timing Arrays (PTA), Barycentric Vector Tracking, Relativistic Shapiro Delays.
  * **Phase III: Evolution:** Closed-loop Artificial Gravity, Radiation Shielding, Bio-Resonance Conditioning.
  * **Phase IV: Architecture:** Superconducting Magnetic Shielding, Field Coils, and Habitat Structural Symmetries.
* **Oracle & Cross-Discipline Gap Analysis:** Automated identification of theoretical boundaries and cross-theory synthesis.
* **Decoupled Architecture:** Secret keys, hostnames, and environments configured cleanly via `.env`.

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



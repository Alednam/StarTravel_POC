# Implementation Plan: High-Density Science Knowledge Base (KB)

## Objective
To transform the current skeleton Knowledge Base into a comprehensive, textbook-quality repository of scientific principles. Each entry will serve as a "Study Note" that connects fundamental science with the theoretical 4PT/IUC logic.

---

## Phase 1: Structural Scaffolding (The "Outline" Strategy)
*Current State:* Flattened list of laws.
*Target State:* Hierarchical Subject -> Course -> Topic mapping derived from established scientific curricula.

### 1.1 Outline-Aware Scraping
Update `ResearchEngine` to target Wikipedia "Outline" pages (e.g., *Outline of Physics*, *Outline of Chemistry*).
- **Mechanism:** Identify `<h2>` and `<h3>` as Courses, and `<li>` links as Topics.
- **Goal:** Build the full "tree" of science before filling in the leaves.

### 1.2 Multi-Disciplinary Seeding
Apply the outline strategy to the following core subjects:
- **Physics:** Classical, Quantum, Relativity, Thermodynamics.
- **Biology:** Genetics, Evolution, Cell Biology, Ecology.
- **Chemistry:** Organic, Inorganic, Physical, Biochemistry.
- **Information Theory:** Computation, Logic, Signal Processing, Entropy.

---

## Phase 2: Content Enrichment (The "Deep Note" Strategy)
*Current State:* Single-sentence definitions.
*Target State:* 3-5 paragraph introductory summaries for every topic.

### 2.1 Deep Extraction
For every topic discovered in Phase 1:
- Follow the Wikipedia URL.
- Extract the first 5 substantial paragraphs.
- Clean the text (remove citations like `[1]`, edit links, and metadata).
- Store as the `content` field in the `Topic` model.

---

## Phase 3: Mathematical Formalization
*Current State:* Simple text-based formulas.
*Target State:* Proper LaTeX/Sympy representations of core equations.

### 3.1 LaTeX Extraction
Identify `<span class="mwe-math-element">` tags during deep scraping.
- **Mechanism:** Extract the `alt` text (raw LaTeX) from the math images.
- **Goal:** Every topic should have at least 1-2 fundamental equations in the `Equation` model.

---

## Phase 4: The 4PT Synthesis Layer (The "Simulation" Perspective)
*Current State:* Scientific data and 4PT theories are separate.
*Target State:* Scientific topics include a "Simulation Logic" section.

### 4.1 Automated Synthesis
Develop a function in `Scientist` to "Synthesize" a topic:
- If Topic == "Uncertainty Principle" -> Append: *4PT Logic: Data compression for unobserved coordinates.*
- If Topic == "Entropy" -> Append: *4PT Logic: Systemic bit-rot and decoherence.*
- **Action:** Create a mapping file `logic_bridge.json` that defines these interpretations for core topics.

---

## Phase 5: UI/UX for Learning
*Current State:* Basic detail pages.
*Target State:* An educational interface that mimics a 5D "Archive."

### 5.1 Enhanced Topic View
- **Side Panel:** "Navigation Hierarchy" (Subject -> Course -> Topics list).
- **Interactive Equations:** Click to see variables explained.
- **Relationship Map:** Shows which 4PT Axioms depend on this specific scientific principle.

---

## Immediate Next Steps
1.  **Refactor `scraper.py`:** Finalize the `scrape_outline` and `fetch_page_content` methods.
2.  **Subject Mapping:** Run the `scrape_outline` for **Physics** and **Biology** to establish the foundation.
3.  **Bridge Creation:** Draft the `logic_bridge.json` to begin the 4PT Synthesis phase.

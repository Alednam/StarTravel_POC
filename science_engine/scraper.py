from .models import Subject, Course, Topic, Equation, Theory as TheoryModel
import requests
from bs4 import BeautifulSoup
import re
import os

class ResearchEngine:
    def __init__(self, theories_dir):
        self.theories_dir = theories_dir
        self.headers = {
            'User-Agent': 'ScienceCalculatorEngine/1.0 (https://github.com/scicalc; admin@scicalc.org) Python/requests'
        }
        self.logic_bridge = {}
        bridge_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'logic_bridge.json')
        if os.path.exists(bridge_path):
            try:
                import json
                with open(bridge_path, 'r', encoding='utf-8') as f:
                    self.logic_bridge = json.load(f)
            except Exception:
                pass

    def synthesize_topic(self, topic_name, content=""):
        """
        Synthesizes a topic into the 4PT Simulation Perspective.
        Checks exact matches, keyword heuristics, or generates axiomatic interpretations.
        """
        # 1. Exact match in logic bridge
        if topic_name in self.logic_bridge:
            return self.logic_bridge[topic_name]

        # 2. Case-insensitive or substring match
        name_lower = topic_name.lower()
        for k, v in self.logic_bridge.items():
            k_lower = k.lower()
            if k_lower in name_lower or name_lower in k_lower:
                return v

        # 3. Domain keyword heuristic synthesis
        combined = (topic_name + " " + (content[:300] if content else "")).lower()
        if any(w in combined for w in ["quantum", "uncertainty", "superposition", "wave-particle"]):
            return f"4PT Logic: Unitary state-vector superposition within the unobserved phase buffer prior to observer-triggered eigenstate collapse for {topic_name}."
        elif any(w in combined for w in ["entropy", "thermodynamic", "heat", "dissipation"]):
            return f"4PT Logic: Systemic metric of information decay and state degeneracy governing macro-state transitions in {topic_name}."
        elif any(w in combined for w in ["relativity", "spacetime", "gravity", "metric", "geodesic"]):
            return f"4PT Logic: Spacetime metric warping representing computational latency gradients and information density variations across mass-energy fields in {topic_name}."
        elif any(w in combined for w in ["dna", "gene", "evolution", "mutation", "selection", "cell"]):
            return f"4PT Logic: Automated biological optimization protocol updating genetic ROM configurations to preserve localized anti-entropic stability in {topic_name}."
        elif any(w in combined for w in ["electric", "magnetic", "lorentz", "tether", "plasma", "field"]):
            return f"4PT Logic: Informational gauge potential interactions coupling charged entities across ambient vector flux gradients in {topic_name}."
        elif any(w in combined for w in ["logic", "computation", "algorithm", "turing", "information"]):
            return f"4PT Logic: Fundamental axiomatic bit-processing grammar determining deterministic state evolution in {topic_name}."
        elif any(w in combined for w in ["math", "calculus", "algebra", "geometry", "manifold"]):
            return f"4PT Logic: Mathematical coordinate grammar formalizing boundary constraints and topological invariants in {topic_name}."
        else:
            return f"4PT Logic: Local metric configuration constraining state transitions and preserving conservation laws within the 3D projection of {topic_name}."

    def fetch_page_content(self, url):
        """Fetches and parses a specific Wikipedia page for full detailed content, formulas, and primary illustration."""
        try:
            response = requests.get(url, headers=self.headers, timeout=12)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Remove citations, edit links, navigation boxes, and metadata
            for tag in soup.find_all(['sup', 'span', 'table', 'div'], class_=['reference', 'mw-editsection', 'mw-empty-elt', 'infobox', 'navbox', 'reflist']):
                tag.decompose()
            
            content_div = soup.find(id="mw-content-text")
            if not content_div:
                return None, [], None
            parser_output = content_div.find(class_="mw-parser-output")
            if not parser_output:
                return None, [], None

            # Extract substantial paragraphs (first 3 to 5 substantial blocks)
            paragraphs = []
            for p in parser_output.find_all('p'):
                text = p.get_text().strip()
                # Remove citation brackets like [1], [2], [a]
                text = re.sub(r'\[\w+\]', '', text).strip()
                if len(text) > 40:
                    paragraphs.append(text)
                if len(paragraphs) >= 5:
                    break

            content_markdown = "\n\n".join(paragraphs)

            # Extract Equations
            equations = []
            for math in parser_output.find_all(['span', 'div'], class_="mwe-math-element"):
                img = math.find('img')
                if img and img.has_attr('alt'):
                    latex = img['alt'].strip()
                    # Clean {\displaystyle ...} wrapper if present
                    clean_latex = re.sub(r'^\{\\displaystyle\s*(.*)\}$', r'\1', latex, flags=re.DOTALL).strip()
                    if clean_latex and clean_latex not in [e['formula'] for e in equations]:
                        equations.append({'formula': clean_latex, 'explanation': "Mathematical expression from text."})
                if len(equations) >= 5:
                    break

            # Extract Primary Image
            image_url = None
            infobox = soup.find(class_="infobox")
            if infobox:
                img_tag = infobox.find('img')
                if img_tag and img_tag.get('src'):
                    src = img_tag['src']
                    image_url = "https:" + src if src.startswith('//') else src
            
            if not image_url:
                thumb = soup.find(class_="thumbimage")
                if thumb and thumb.get('src'):
                    src = thumb['src']
                    image_url = "https:" + src if src.startswith('//') else src

            return content_markdown, equations, image_url
        except Exception:
            return None, [], None

    def scrape_outline(self, subject_name, outline_url, max_topics_per_course=12):
        """
        Target a Wikipedia 'Outline' page to build a full subject/course/topic hierarchy.
        e.g. https://en.wikipedia.org/wiki/Outline_of_physics
        """
        try:
            response = requests.get(outline_url, headers=self.headers, timeout=15)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            
            subject_obj, _ = Subject.objects.get_or_create(
                name=subject_name,
                defaults={'description': f"Comprehensive repository of {subject_name} knowledge."}
            )

            current_course = None
            processed_topics = 0
            
            # Find all headings (mw-heading or direct h2/h3)
            elements = soup.find_all(['div', 'h2', 'h3'])
            for el in elements:
                is_heading = False
                header_text = ""
                
                if el.name == 'div' and any(c in el.get('class', []) for c in ['mw-heading2', 'mw-heading3']):
                    is_heading = True
                    header_text = el.get_text().strip().replace('[edit]', '')
                elif el.name in ['h2', 'h3'] and el.parent and not ('mw-heading' in el.parent.get('class', [])):
                    is_heading = True
                    header_text = el.get_text().strip().replace('[edit]', '')

                if is_heading:
                    # Skip administrative/meta sections
                    if any(x in header_text.lower() for x in ['history', 'lists', 'organizations', 'see also', 'external links', 'further reading', 'references', 'notes', 'what type']):
                        current_course = None
                        continue
                    current_course, _ = Course.objects.get_or_create(subject=subject_obj, name=header_text)
                    
                    # Look ahead for following sibling lists
                    target_parent = el.parent if el.name in ['h2', 'h3'] and 'mw-heading' in el.parent.get('class', []) else el
                    sib = target_parent.find_next_sibling()
                    course_topic_count = 0
                    
                    while sib and not ('mw-heading' in (sib.get('class') or [])) and sib.name not in ['h2', 'h3']:
                        if sib.name in ['ul', 'ol']:
                            for li in sib.find_all('li', recursive=False):
                                if course_topic_count >= max_topics_per_course:
                                    break
                                link = li.find('a', href=True)
                                if link:
                                    href = link['href']
                                    wiki_path = href.replace('https://en.wikipedia.org', '')
                                    if wiki_path.startswith('/wiki/'):
                                        slug = wiki_path[6:]
                                        # Filter namespaces
                                        if any(slug.startswith(ns + ':') for ns in ['Wikipedia', 'Help', 'File', 'Category', 'Portal', 'Special', 'Talk']):
                                            continue
                                        topic_name = link.get_text().strip()
                                        if any(x in topic_name.lower() for x in ['outline of', 'index of', 'list of', 'glossary of', 'timeline of']):
                                            continue
                                        if len(topic_name) < 3:
                                            continue
                                        
                                        topic_url = f"https://en.wikipedia.org{wiki_path}"
                                        topic_obj, created = Topic.objects.get_or_create(course=current_course, name=topic_name)
                                        
                                        if created or not topic_obj.content or len(topic_obj.content) < 80:
                                            detail_text, formulas, image_url = self.fetch_page_content(topic_url)
                                            if detail_text:
                                                topic_obj.content = detail_text
                                                topic_obj.image_url = image_url
                                                topic_obj.simulation_logic = self.synthesize_topic(topic_name, detail_text)
                                                topic_obj.save()
                                                
                                                for eq in formulas:
                                                    Equation.objects.get_or_create(
                                                        topic=topic_obj,
                                                        formula=eq['formula'],
                                                        defaults={'name': f"{topic_name} Formula", 'explanation': eq['explanation']}
                                                    )
                                                processed_topics += 1
                                                course_topic_count += 1
                        sib = sib.find_next_sibling()
            
            return True, f"Successfully built {subject_name} hierarchy with {processed_topics} detailed topics."

        except Exception as e:
            return False, f"Outline scrape failed: {str(e)}"

    def enrich_topic_by_name(self, topic_obj):
        """Fetches detailed content and formulas for an existing topic using its name."""
        try:
            slug = topic_obj.name.strip().replace(' ', '_')
            topic_url = f"https://en.wikipedia.org/wiki/{slug}"
            detail_text, formulas, image_url = self.fetch_page_content(topic_url)
            
            if detail_text:
                topic_obj.content = detail_text
                if image_url:
                    topic_obj.image_url = image_url
                if not topic_obj.simulation_logic:
                    topic_obj.simulation_logic = self.synthesize_topic(topic_obj.name, detail_text)
                topic_obj.save()
                
                for eq in formulas:
                    Equation.objects.get_or_create(
                        topic=topic_obj,
                        formula=eq['formula'],
                        defaults={'name': f"{topic_obj.name} Formulation", 'explanation': eq['explanation']}
                    )
                return True
        except Exception:
            pass
        return False

    def enrich_all_sparse_topics(self):
        """Enriches all topics in the database that currently lack content or simulation logic."""
        sparse_topics = Topic.objects.filter(content='') | Topic.objects.filter(simulation_logic='')
        enriched_count = 0
        for topic in sparse_topics.distinct():
            if not topic.simulation_logic:
                topic.simulation_logic = self.synthesize_topic(topic.name, topic.content)
                topic.save()
            if not topic.content or len(topic.content) < 50:
                success = self.enrich_topic_by_name(topic)
                if success:
                    enriched_count += 1
        return enriched_count

    def scrape_scientific_laws(self, sync_to_db=True):
        """
        Scrapes a list of scientific laws and optionally saves them to the DB.
        """
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }
            response = requests.get(self.source_url, headers=headers)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            extracted_laws = []
            content_div = soup.find(id="mw-content-text")
            if not content_div:
                return False, "Could not find content on page."

            # We'll try to find categories (headers) to group into Subjects
            current_subject_name = "General Science"
            subject_obj, _ = Subject.objects.get_or_create(name=current_subject_name)
            
            # Find all list items and headers
            elements = content_div.find_all(['h2', 'h3', 'li'])
            
            for el in elements:
                if el.name in ['h2', 'h3']:
                    # Update current subject if it looks like a field of science
                    header_text = el.get_text().strip().replace('[edit]', '')
                    if any(x in header_text.lower() for x in ['physics', 'biology', 'chemistry', 'math', 'economics', 'social']):
                        current_subject_name = header_text
                        subject_obj, _ = Subject.objects.get_or_create(name=current_subject_name)
                    continue

                if el.name == 'li':
                    text = el.get_text().strip()
                    if ':' in text and len(text) > 20:
                        parts = text.split(':', 1)
                        name = parts[0].strip()
                        definition = parts[1].strip()
                        
                        name = re.sub(r'[\[\]\d+]', '', name)
                        definition = re.sub(r'[\[\]\d+]', '', definition)
                        
                        if len(name) < 100:
                            extracted_laws.append(f"- **{name}**: {definition}")
                            
                            if sync_to_db:
                                # Create a Topic for each law
                                course_name = f"Notable Laws in {current_subject_name}"
                                course_obj, _ = Course.objects.get_or_create(subject=subject_obj, name=course_name)
                                topic_obj, _ = Topic.objects.get_or_create(course=course_obj, name=name, defaults={'content': definition})
                                
                                # Check if definition has a formula-like string (e.g. F = ma)
                                formula_match = re.search(r'([A-Za-z0-9_]+\s*=\s*[^.!?]+)', definition)
                                if formula_match:
                                    Equation.objects.get_or_create(
                                        topic=topic_obj, 
                                        name=f"{name} Formula", 
                                        defaults={'formula': formula_match.group(1), 'explanation': f"Derived from {name}"}
                                    )

            if not extracted_laws:
                return False, "No laws extracted."

            # Save to file (backward compatibility)
            filename = "scraped_scientific_laws.md"
            file_path = os.path.join(self.theories_dir, filename)
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write("# Compendium of Scraped Scientific Laws\n\n")
                f.write(f"## Laws and Rules\n")
                for law in extracted_laws:
                    f.write(f"{law}\n")
            
            return True, f"Successfully harvested {len(extracted_laws)} laws into DB and {filename}."

        except Exception as e:
            return False, f"Scraping failed: {str(e)}"

class KnowledgeSeeder:
    """Provides initial structured knowledge if the database is empty."""
    
    @staticmethod
    def seed_from_markdown(file_path):
        """Parses a markdown file to seed the knowledge base."""
        if not os.path.exists(file_path):
            return f"Error: {file_path} not found."
            
        with open(file_path, 'r') as f:
            content = f.read()
            
        lines = content.split('\n')
        current_course = None
        current_topic = None
        current_subject_obj = None
        
        for line in lines:
            stripped = line.strip()
            
            # Course Detection (### Headers)
            if stripped.startswith('###'):
                course_name = re.sub(r'^[#\s.IVX]+', '', stripped).strip()
                
                # Dynamic Subject Detection based on course name
                lower_course = course_name.lower()
                subj_name = "General Science"
                if any(x in lower_course for x in ['quantum', 'source code', 'network', 'rendering', 'architecture']):
                    subj_name = "Quantum Physics"
                elif any(x in lower_course for x in ['biology', 'evolution', 'replication']):
                    subj_name = "Biology"
                elif any(x in lower_course for x in ['chemistry', 'elements', 'material']):
                    subj_name = "Chemistry"
                elif any(x in lower_course for x in ['information', 'logic', 'protocol', 'signal']):
                    subj_name = "Information Theory"
                
                current_subject_obj, _ = Subject.objects.get_or_create(
                    name=subj_name,
                    defaults={'description': f"Principles and studies related to {subj_name}."}
                )
                
                current_course, _ = Course.objects.get_or_create(subject=current_subject_obj, name=course_name)
                continue
                
            # Topic Detection (* **Topic Name:** Description)
            if (stripped.startswith('* **') or stripped.startswith('- **')) and current_course:
                match = re.search(r'[*+-]\s+\*\*([^*]+)\*\*:\s*(.*)', stripped)
                if match:
                    topic_name = match.group(1).strip()
                    topic_desc = match.group(2).strip()
                    current_topic, _ = Topic.objects.get_or_create(
                        course=current_course, 
                        name=topic_name,
                        defaults={'content': topic_desc}
                    )
                continue
            
            # Additional content (like 4PT Logic)
            if stripped.startswith('* *') and current_topic:
                current_topic.content += "\n\n" + stripped.replace('*', '').strip()
                current_topic.save()
            elif stripped and not stripped.startswith('#') and current_topic:
                # Append other lines to current topic content if they aren't headers
                if not any(stripped.startswith(x) for x in ['*', '-', '###']):
                    current_topic.content += " " + stripped
                    current_topic.save()

        return f"Successfully processed {file_path}."

    @staticmethod
    def seed_basics():
        physics, _ = Subject.objects.get_or_create(
            name="Physics", 
            defaults={'description': "The study of matter, energy, and the fundamental forces of nature."}
        )
        
        classical, _ = Course.objects.get_or_create(subject=physics, name="Classical Mechanics")
        topics = [
            ("Newton's First Law", "An object at rest remains at rest, and an object in motion remains in motion at constant speed and in a straight line unless acted on by an unbalanced force."),
            ("Newton's Second Law", "The acceleration of an object depends on the mass of the object and the amount of force applied."),
            ("Newton's Third Law", "Whenever one object exerts a force on a second object, the second object exerts an equal and opposite force on the first.")
        ]
        for name, content in topics:
            t, _ = Topic.objects.get_or_create(course=classical, name=name, defaults={'content': content})
            if "Second Law" in name:
                Equation.objects.get_or_create(topic=t, name="Force Formula", defaults={'formula': "F = m * a", 'explanation': "Force equals mass times acceleration."})

                quantum, _ = Course.objects.get_or_create(subject=physics, name="Quantum Mechanics")

                qt_topics = [

                    ("Wave-Particle Duality", "The realization that everything exists as both a wave (probability) and a particle (rendered matter)."),

                    ("The Uncertainty Principle", "Formulated by Heisenberg; states that you cannot know both the position and momentum of a particle with perfect precision. 4PT Logic: This is the simulation’s Data Compression—it doesn't calculate what it doesn't need to render."),

                    ("Superposition", "The ability of a system to exist in multiple states simultaneously (The 'Probability Soup')."),

                    ("Quantum Tunneling", "Particles passing through barriers they shouldn't be able to. 4PT Logic: A 'Logic Clip' through the simulation's collision boundaries.")

                ]

                for name, content in qt_topics:

                    t, _ = Topic.objects.get_or_create(course=quantum, name=name, defaults={'content': content})

                    if "Uncertainty" in name:

                        Equation.objects.get_or_create(topic=t, name="Heisenberg Relation", defaults={'formula': "Δx * Δp ≥ ħ / 2", 'explanation': "The product of the uncertainties in position and momentum is at least h-bar over two."})

                    if "Duality" in name:

                        Equation.objects.get_or_create(topic=t, name="De Broglie Wavelength", defaults={'formula': "λ = h / p", 'explanation': "Wavelength equals Planck's constant divided by momentum."})

        

                return "Basics seeding complete."

        
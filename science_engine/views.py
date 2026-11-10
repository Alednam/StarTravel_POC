from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .logic import Scientist
from .scraper import ResearchEngine
from .forms import QueryForm, UploadTheoryForm
from .models import Subject, Course, Topic, Equation, Theory as TheoryModel
import os
import json
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import ensure_csrf_cookie
from django.core.paginator import Paginator
from django.db.models import Q

# Initialize the Scientist globally
bot = Scientist(name="Dr. Gemini")

# Pre-load theories on startup
module_dir = os.path.dirname(__file__)
theories_dir = os.path.join(module_dir, 'theories')

# Ensure theories dir exists
if not os.path.exists(theories_dir):
    os.makedirs(theories_dir)

def load_all_theories():
    """Helper to reload all theories from disk and sync to DB"""
    # Note:bot.load_from_db() is called in Scientist constructor
    for filename in os.listdir(theories_dir):
        if filename.endswith(".md"):
            bot.load_theory(os.path.join(theories_dir, filename), save_to_db=True)

# Initial load/sync (safely catch if migrations are pending)
try:
    load_all_theories()
except Exception:
    pass

def network_data(request):
    """
    API endpoint for the neuro-map visualization.
    """
    try:
        limit = int(request.GET.get('limit', 50))
    except ValueError:
        limit = 50
        
    data = bot.generate_knowledge_graph(limit=limit)
    return JsonResponse(data)

def gap_analysis(request):
    """
    Displays a dashboard of identified gaps across all theories and proposes solutions.
    """
    gaps_report = []
    
    # Iterate through all theories
    for name, theory in bot.known_theories.items():
        for gap in theory.gaps:
            # Find solutions in *other* theories
            solutions = bot.find_solutions_for_gap(gap)
            gaps_report.append({
                'source_theory': name,
                'gap_text': gap,
                'solutions': solutions
            })
    
    context = {
        'gaps_report': gaps_report
    }
    return render(request, 'science_engine/gap_analysis.html', context)

def theory_list(request, theory_name=None):
    """
    Displays a list of theories with a sidebar and a main content area for the selected theory.
    """
    # Get all theories sorted alphabetically
    all_theories = sorted(list(bot.known_theories.keys()))
    
    # Pagination for sidebar
    paginator = Paginator(all_theories, 20) # Show 20 theories per page in sidebar
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    selected_theory = None
    comparison_analysis = None
    related_topics = []
    
    if theory_name:
        if theory_name in bot.known_theories:
            selected_theory = bot.known_theories[theory_name]
            # Compare with IUC (or user choice, default IUC)
            comparison_analysis = bot.compare_theories(theory_name, "IUC")
            
            # Fetch related topics from DB if they exist
            if selected_theory.db_instance:
                related_topics = selected_theory.db_instance.topics.all().prefetch_related('equations')
        else:
            comparison_analysis = "Theory not found."
    elif all_theories:
        # Default to first theory if none selected
        selected_theory = bot.known_theories[all_theories[0]]
        comparison_analysis = bot.compare_theories(all_theories[0], "IUC")
        if selected_theory.db_instance:
            related_topics = selected_theory.db_instance.topics.all().prefetch_related('equations')

    context = {
        'page_obj': page_obj,
        'selected_theory': selected_theory,
        'comparison_analysis': comparison_analysis,
        'related_topics': related_topics,
    }
    return render(request, 'science_engine/theory_list.html', context)

def index(request):
    # Retrieve chat history from session or initialize
    chat_history = request.session.get('chat_history', [])
    
    # Analysis of current loaded theories (summary)
    loaded_theories = list(bot.known_theories.keys())
    analysis_summary = f"Loaded Theories: {', '.join(loaded_theories)}"

    query_form = QueryForm()
    upload_form = UploadTheoryForm()

    if request.method == 'POST':
        if 'query_submit' in request.POST:
            query_form = QueryForm(request.POST)
            if query_form.is_valid():
                user_query = query_form.cleaned_data['query']
                
                # Get bot response
                response = bot.think(user_query)
                
                # Update history
                chat_history.append({'role': 'user', 'text': user_query})
                chat_history.append({'role': 'bot', 'text': response})
                request.session['chat_history'] = chat_history
                
                return redirect('index')

        elif 'upload_submit' in request.POST:
            upload_form = UploadTheoryForm(request.POST, request.FILES)
            if upload_form.is_valid():
                uploaded_file = request.FILES['file']
                fs = FileSystemStorage(location=theories_dir)
                filename = fs.save(uploaded_file.name, uploaded_file)
                
                load_all_theories()
                
                chat_history.append({'role': 'system', 'text': f"Successfully uploaded and studied: {filename}"})
                request.session['chat_history'] = chat_history
                return redirect('index')

        elif 'scrape_submit' in request.POST:
            researcher = ResearchEngine(theories_dir)
            success, message = researcher.scrape_scientific_laws()
            
            if success:
                load_all_theories()
                chat_history.append({'role': 'system', 'text': f"Research Complete: {message}"})
            else:
                chat_history.append({'role': 'system', 'text': f"Research Failed: {message}"})
            
            request.session['chat_history'] = chat_history
            return redirect('index')
    
    context = {
        'analysis_summary': analysis_summary,
        'chat_history': chat_history,
        'query_form': query_form,
        'upload_form': upload_form,
        'loaded_theories': loaded_theories, 
    }
    
    return render(request, 'science_engine/index.html', context)

def oracle_engine_view(request):
    """
    Renders the Oracle Engine interface for probability calculation.
    """
    anchors = bot.oracle.anchors
    result = None
    current_hypothesis = ""
    selected_anchors = []

    if request.method == 'POST':
        current_hypothesis = request.POST.get('hypothesis', '')
        selected_anchors = request.POST.getlist('anchors')
        
        result = bot.oracle.calculate_resonance(current_hypothesis, selected_anchors)

    context = {
        'anchors': anchors,
        'result': result,
        'current_hypothesis': current_hypothesis,
        'selected_anchors': selected_anchors,
    }
    return render(request, 'science_engine/oracle.html', context)

def knowledge_base(request):
    """
    Displays the organized scientific knowledge base as a Library of Books.
    Includes both scientific Subjects and theoretical Manuscripts with search and filtering.
    """
    query = request.GET.get('q', '').strip()
    active_tab = request.GET.get('tab', 'all')
    
    # Search Mode
    if query:
        search_theories = TheoryModel.objects.filter(
            Q(name__icontains=query) |
            Q(premise__icontains=query) |
            Q(content__icontains=query)
        )
        search_subjects = Subject.objects.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query)
        )
        search_courses = Course.objects.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query)
        ).select_related('subject')[:20]
        search_topics = Topic.objects.filter(
            Q(name__icontains=query) |
            Q(content__icontains=query) |
            Q(simulation_logic__icontains=query)
        ).select_related('course__subject')[:30]
        
        context = {
            'query': query,
            'active_tab': 'search',
            'search_theories': search_theories,
            'search_subjects': search_subjects,
            'search_courses': search_courses,
            'search_topics': search_topics,
            'total_results': search_theories.count() + search_subjects.count() + search_courses.count() + search_topics.count(),
        }
        return render(request, 'science_engine/knowledge_base.html', context)

    # 1. Get all Subjects (Scientific Foundations) with pre-aggregated counts
    raw_subjects = list(Subject.objects.prefetch_related('courses__topics__equations').all().order_by('name'))
    subjects_data = []
    
    color_map = {
        'Theoretical Physics': {'color': 'emerald', 'accent': '#059669', 'bg': 'bg-emerald-50', 'border': 'border-emerald-200'},
        'Mathematics & Geometry': {'color': 'violet', 'accent': '#7c3aed', 'bg': 'bg-violet-50', 'border': 'border-violet-200'},
        'Thermodynamics & Statistical Mechanics': {'color': 'teal', 'accent': '#0d9488', 'bg': 'bg-teal-50', 'border': 'border-teal-200'},
        'Information Theory & Logic': {'color': 'blue', 'accent': '#2563eb', 'bg': 'bg-blue-50', 'border': 'border-blue-200'},
        'Chemical Sciences': {'color': 'amber', 'accent': '#d97706', 'bg': 'bg-amber-50', 'border': 'border-amber-200'},
        'Biological Sciences': {'color': 'rose', 'accent': '#e11d48', 'bg': 'bg-rose-50', 'border': 'border-rose-200'},
        'Planetary & Solar Magnetospheric Spaceflight': {'color': 'cyan', 'accent': '#06b6d4', 'bg': 'bg-cyan-50', 'border': 'border-cyan-200'},
    }

    for s in raw_subjects:
        courses = list(s.courses.all())
        courses_count = len(courses)
        topics_count = sum(c.topics.count() for c in courses)
        equations_count = sum(sum(t.equations.count() for t in c.topics.all()) for c in courses)
        theme = color_map.get(s.name, {'color': 'slate', 'accent': '#475569', 'bg': 'bg-slate-50', 'border': 'border-slate-200'})
        
        subjects_data.append({
            'type': 'subject',
            'id': s.id,
            'title': s.name,
            'author': 'Scientific Archive',
            'description': s.description,
            'courses': courses,
            'courses_count': courses_count,
            'topics_count': topics_count,
            'equations_count': equations_count,
            'preview_courses': [c.name for c in courses[:4]],
            'relation_tag': 'Scientific Foundation',
            'color': theme['color'],
            'accent': theme['accent'],
        })

    # 2. Get all Theories (Research Manuscripts)
    raw_theories = list(TheoryModel.objects.prefetch_related('topics').all())
    theories_data = []

    for t in raw_theories:
        display_title = t.name.replace('_', ' ')
        is_core = t.name in ['4PT', 'IUC']
        is_spaceflight = 'Spaceflight' in t.name
        is_archive = t.name == 'scraped_scientific_laws'
        
        if is_spaceflight:
            relation_tag = 'Spaceflight Traversal Theory'
            color = 'cyan'
        elif is_core:
            relation_tag = 'Core Axiomatic Theory'
            color = 'indigo'
        elif is_archive:
            relation_tag = 'Historical Scrape Archive'
            color = 'slate'
        else:
            relation_tag = 'Foundational Physics Manuscript'
            color = 'indigo'
            
        theories_data.append({
            'type': 'theory',
            'id': t.name,
            'title': display_title,
            'raw_name': t.name,
            'author': 'Theoretical Researcher',
            'description': t.premise or "Axiomatic mathematical physics manuscript.",
            'relation_tag': relation_tag,
            'is_sealed': t.is_sealed,
            'seal_hash': t.content_hash,
            'topics_count': t.topics.count(),
            'equations_count': len(t.equations_list) if t.equations_list else 0,
            'domains': t.domains,
            'color': color,
        })

    # Sort theories: Spaceflight & Core first, then foundational manuscripts, then archive
    theories_data.sort(key=lambda x: (
        0 if 'Spaceflight' in x['relation_tag'] else (1 if 'Core' in x['relation_tag'] else 2),
        x['title']
    ))

    context = {
        'query': query,
        'active_tab': active_tab,
        'subjects': subjects_data,
        'theories': theories_data,
        'total_disciplines': len(subjects_data),
        'total_manuscripts': len(theories_data),
        'total_topics': sum(s['topics_count'] for s in subjects_data),
        'total_equations': sum(s['equations_count'] for s in subjects_data),
    }
    return render(request, 'science_engine/knowledge_base.html', context)

def subject_detail(request, subject_id):
    """Detail view for a specific scientific subject with paginated courses."""
    subject = get_object_or_404(Subject, pk=subject_id)
    course_list = subject.courses.all().order_by('name')
    paginator = Paginator(course_list, 10) # 10 courses per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'science_engine/subject_detail.html', {
        'subject': subject,
        'page_obj': page_obj
    })

def course_detail(request, course_id):
    """Detail view for a specific course within a subject with paginated topics."""
    course = get_object_or_404(Course.objects.select_related('subject'), pk=course_id)
    topic_list = course.topics.all().order_by('id')
    paginator = Paginator(topic_list, 20) # 20 topics per page (chapters)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'science_engine/course_detail.html', {
        'course': course,
        'page_obj': page_obj
    })

def topic_detail(request, topic_id):
    """Detail view for a specific scientific topic and its equations."""
    topic = get_object_or_404(Topic.objects.select_related('course__subject').prefetch_related('equations', 'theories'), pk=topic_id)
    
    # Get navigation context (book-like flow)
    all_topics = list(topic.course.topics.all().order_by('id'))
    topic_index = all_topics.index(topic)
    
    prev_topic = all_topics[topic_index - 1] if topic_index > 0 else None
    next_topic = all_topics[topic_index + 1] if topic_index < len(all_topics) - 1 else None
    
    # Check if this topic belongs to the Space Flight curriculum
    is_spaceflight = "Spaceflight" in topic.course.subject.name
    poc_diagram_type = "propulsion"
    if is_spaceflight:
        course_name = topic.course.name.lower()
        topic_name = topic.name.lower()
        if "propulsion" in course_name or "tether" in topic_name or "sail" in topic_name or "alfvén" in topic_name or "lorentz" in topic_name:
            poc_diagram_type = "propulsion"
        elif "navigation" in course_name or "orbit" in topic_name or "pulsar" in topic_name or "harmonic" in topic_name or "mcilwain" in topic_name or "magnetopause" in topic_name:
            poc_diagram_type = "navigation"
        elif "evolution" in course_name or "bio" in topic_name or "crypto" in topic_name or "schumann" in topic_name or "speciation" in topic_name or "hypomagnetic" in topic_name:
            poc_diagram_type = "evolution"
        elif "architecture" in course_name or "superconducting" in topic_name or "contactor" in topic_name or "shield" in topic_name or "libration" in topic_name or "cryogenic" in topic_name:
            poc_diagram_type = "architecture"
        else:
            poc_diagram_type = "propulsion"

    context = {
        'topic': topic,
        'prev_topic': prev_topic,
        'next_topic': next_topic,
        'is_spaceflight': is_spaceflight,
        'poc_diagram_type': poc_diagram_type,
    }
    return render(request, 'science_engine/topic_detail.html', context)

def space_flight(request):
    """
    Space Flight & Magnetospheric Traversal Portal.
    Covers the 3 core pillars:
    1. Propulsion: Utilizing planetary & solar magnetic fields and plasma waves.
    2. Navigation: Magnetometry, spherical harmonics, L-shells, and pulsar clocks.
    3. Human Evolution: Bioelectromagnetics, quantum magnetoreception, active radiation shielding, and deep-space speciation.
    """
    subject = Subject.objects.filter(name="Planetary & Solar Magnetospheric Spaceflight").prefetch_related('courses__topics__equations').first()
    
    courses = list(subject.courses.all()) if subject else []
    
    # Categorize courses by pillar
    propulsion_course = next((c for c in courses if "Propulsion" in c.name), None)
    navigation_course = next((c for c in courses if "Navigation" in c.name), None)
    evolution_course = next((c for c in courses if "Evolution" in c.name or "Bioelectromagnetics" in c.name), None)
    architecture_course = next((c for c in courses if "Architecture" in c.name or "Engineering" in c.name), None)

    # Spacecraft Subsystems Architecture Data (Phase IV)
    spacecraft_subsystems = [
        {
            'name': 'Primary Electrodynamic Tether Assembly',
            'subsystem_code': 'SYS-EDT-01',
            'material': 'Carbon Nanotube / Al-Clad Ultra-High Molecular Weight Polyethylene (UHMWPE)',
            'dimensions': 'Length: 25.0 km | Thickness: 0.12 mm tape | Width: 25.0 mm',
            'operating_rating': 'Max Tension: 15.0 kN | Electrical Current: 10 - 25 A DC',
            'libration_control': 'Phase-locked active current throttling I(t) at in-plane natural frequency',
            'role': 'Propellantless orbital altitude shifting, inclination precessions, and geomagnetic energy harvesting.'
        },
        {
            'name': 'High-Temperature Superconducting (HTS) Magnet Ring',
            'subsystem_code': 'SYS-MAG-02',
            'material': 'REBCO (GdBa2Cu3O7) Coated Superconducting Tape',
            'dimensions': 'Coil Diameter: 12.0 m | Turns: 2,400 | Inductance: 4.8 H',
            'operating_rating': 'Peak Field: 5.5 T on-axis | Stored Energy: 48.0 MJ | Cryogenic Temp: 30 K',
            'libration_control': 'Closed-cycle Stirling/Brayton cryocoolers with multi-layer vacuum insulation',
            'role': 'Drives the Magsail solar-wind deflection bubble and establishes exterior active radiation deflection.'
        },
        {
            'name': 'Ionospheric Hollow Cathode Plasma Contactors',
            'subsystem_code': 'SYS-HCPC-03',
            'material': 'Lanthanum Hexaboride (LaB6) Thermionic Insert with Tantalum Anode Orifice',
            'dimensions': 'Dual redundant fore/aft pod assemblies with active gas feed',
            'operating_rating': 'Discharge Current: 25.0 A | Xenon Mass Flow: 1.2 mg/s | Sheath Voltage: < 22 V',
            'libration_control': 'Autonomous micro-valve flow controllers linked to Langmuir probe impedance feedback',
            'role': 'Closes orbital electrical circuit with ambient ionospheric plasma, eliminating spacecraft charging.'
        },
        {
            'name': 'Active Multipole Habitat Magnetic Shield',
            'subsystem_code': 'SYS-SHLD-04',
            'material': 'Coaxial Opposing Toroidal Superconducting Coils (Halbach Configuration)',
            'dimensions': 'Habitat Radius: 3.5 m | Toroid Major Radius: 5.0 m | Minor Radius: 0.8 m',
            'operating_rating': 'External Deflection Field: 3.5 - 5.0 T | Habitat Internal Field: < 0.05 mT (Zero-Leakage)',
            'libration_control': 'Carbon-fiber composite tensile tie-rods rated for 10 MPa magnetic virial pressure',
            'role': 'Deflects GCR and SPE energetic protons while maintaining terrestrial magnetic baseline inside living quarters.'
        },
        {
            'name': 'Bio-Resonance Environmental Generator Matrix',
            'subsystem_code': 'SYS-BIO-05',
            'material': '3-Axis Orthogonal Helmholtz Coil Lattice integrated into Habitat Bulkheads',
            'dimensions': 'Spatial Coverage: 100% of crew habitable volume (Sleep pods, cockpit, exercise bay)',
            'operating_rating': 'Static Field: 50.0 µT DC (Earth Equivalent) | Dynamic ELF: 7.83 Hz / 14.3 Hz Schumann Pulse',
            'libration_control': 'Microprocessor-controlled crystal oscillator with phase-locked loop modulation',
            'role': 'Prevents hypomagnetic biological degradation, neuro-cognitive impairment, and circadian desynchronization.'
        }
    ]

    # Detailed CAD Engineering Blueprints (Phase IV Hardware Schematics)
    cad_blueprints = [
        {
            'id': 'cad-edt',
            'subsystem_code': 'SYS-EDT-01',
            'drawing_no': 'DWG-EDT-2026-A1',
            'title': 'Electrodynamic Tether Deployer & Commutator Assembly',
            'scale': '1:15',
            'units': 'Millimeters [mm]',
            'tolerance': 'ISO 2768-mK (+/- 0.1 mm)',
            'material_spec': 'Ti-6Al-4V Grade 5 Casing / UHMWPE-Al Conductive Tape / Ag-C Slip Rings',
            'description': 'Motorized deployment reel mechanism with high-voltage commutator slip rings, active eddy-current braking governor, and ceramic guide nozzle for 25 km orbital conductive tether.',
            'bom': [
                {'item': '01', 'part': 'Spool Drum Core', 'qty': 1, 'mat': 'Ti-6Al-4V Forged', 'desc': 'Lightweight flanged hub accommodating 25 km folded flat tape.'},
                {'item': '02', 'part': 'Planetary Gear Reduction Drive', 'qty': 1, 'mat': 'AISI 9310 Steel', 'desc': '120:1 torque multiplier for controlled tension deployment.'},
                {'item': '03', 'part': 'Dual Ag-Graphite Slip Ring Assembly', 'qty': 2, 'mat': 'Silver-Graphite / BeCu', 'desc': 'Low-noise rotary electrical commutator rated for 30 A continuous.'},
                {'item': '04', 'part': 'Electromagnetic Hysteresis Brake', 'qty': 1, 'mat': 'Alnico / Armco Iron', 'desc': 'Non-contact friction-free tension regulation against libration shock.'},
                {'item': '05', 'part': 'Capstan Pinch Roller Array', 'qty': 4, 'mat': 'Vespel SP-1 Polymer', 'desc': 'Maintains tether drive grip and measures extraction velocity.'},
                {'item': '06', 'part': 'Ceramic Egress Guide Nozzle', 'qty': 1, 'mat': '99.5% Al2O3 Alumina', 'desc': 'Dielectric throat preventing arcing to vehicle chassis.'},
                {'item': '07', 'part': 'End-Mass Ejection Cradle', 'qty': 1, 'mat': 'Al 7075-T6 anodized', 'desc': 'Houses 85 kg tip sub-satellite with pyrotechnic separation bolt.'}
            ],
            'specs': {
                'Drum Outer Diameter': '850 mm',
                'Drum Core Diameter': '320 mm',
                'Overall Assembly Height': '1,240 mm',
                'Total Subsystem Dry Mass': '118.5 kg',
                'Peak Operating Voltage': '5,000 V DC',
                'Max Tether Line Speed': '2.5 m/s'
            }
        },
        {
            'id': 'cad-mag',
            'subsystem_code': 'SYS-MAG-02',
            'drawing_no': 'DWG-MAG-2026-B2',
            'title': 'REBCO HTS Toroidal Magnet Ring & Cryostat',
            'scale': '1:50',
            'units': 'Millimeters [mm]',
            'tolerance': 'ISO 2768-fH (+/- 0.05 mm on seal faces)',
            'material_spec': 'REBCO YBa2Cu3O7 Tape / Hastelloy C-276 / SS 316LN Cryostat / 40-Layer MLI',
            'description': '12-meter high-temperature superconducting magnet ring generating 5.5 Tesla on-axis field, enclosed in dual-wall high-vacuum cryostat with closed-cycle Stirling cold-head interface.',
            'bom': [
                {'item': '01', 'part': 'HTS Double Pancake Coils', 'qty': 24, 'mat': 'REBCO / Cu stabilizer', 'desc': 'Layer-wound superconducting tape pack, 2,400 total turns.'},
                {'item': '02', 'part': 'Cryostat Vacuum Vessel (Outer)', 'qty': 1, 'mat': 'SS 316LN Annealed', 'desc': 'Double-welded toroidal vessel sustaining 10^-5 Pa high vacuum.'},
                {'item': '03', 'part': 'Liquid Neon Thermal Shield', 'qty': 1, 'mat': 'OFHC High-Purity Copper', 'desc': 'Conductive thermal barrier intercepted by first cryocooler stage.'},
                {'item': '04', 'part': 'Multi-Layer Insulation (MLI)', 'qty': 40, 'mat': 'Aluminized Mylar / Dacron', 'desc': 'Reflective radiation barrier reducing radiative heat ingress < 15 W.'},
                {'item': '05', 'part': 'G-10 Fiberglass Thermal Stand-offs', 'qty': 16, 'mat': 'G-10 CR Cryogenic Grade', 'desc': 'Low thermal-conductivity support struts reacting magnetic loads.'},
                {'item': '06', 'part': 'Persistent Current Switch (PCS)', 'qty': 1, 'mat': 'Thermal Superconducting Gate', 'desc': 'Superconducting-to-resistive transition switch for closed-loop persistence.'},
                {'item': '07', 'part': 'Dual Pulse-Tube Cold Head Coupler', 'qty': 2, 'mat': 'Oxygen-Free Copper Bus', 'desc': 'Interface to redundant closed-cycle Stirling/Brayton refrigerators.'}
            ],
            'specs': {
                'Major Toroid Diameter': '12,000 mm',
                'Coil Cross-Section Width': '450 mm',
                'Coil Cross-Section Height': '600 mm',
                'Stored Magnetic Energy': '48.0 Megajoules',
                'Cryostat Cold-Mass': '1,420 kg',
                'Operating Temperature': '30.0 Kelvin'
            }
        },
        {
            'id': 'cad-hcpc',
            'subsystem_code': 'SYS-HCPC-03',
            'drawing_no': 'DWG-HCPC-2026-C1',
            'title': 'Hollow Cathode Plasma Contactor Pod',
            'scale': '1:5',
            'units': 'Millimeters [mm]',
            'tolerance': 'ISO 2768-fH (+/- 0.02 mm)',
            'material_spec': 'LaB6 Single Crystal / Pure Tantalum / Tungsten / Al2O3 Isolators',
            'description': 'Thermionic hollow cathode electron collector and emitter pod for ionospheric circuit closure, with xenon micro-feed plenum, keeper electrode, and swaged tantalum heater.',
            'bom': [
                {'item': '01', 'part': 'LaB6 Hollow Thermionic Insert', 'qty': 1, 'mat': 'Lanthanum Hexaboride', 'desc': 'Low work-function (2.67 eV) polycrystalline thermionic emitter tube.'},
                {'item': '02', 'part': 'Tungsten Orifice Throat Plate', 'qty': 1, 'mat': 'Sintered Tungsten W-99.9%', 'desc': 'Precision 0.5 mm discharge aperture accelerating internal plasma.'},
                {'item': '03', 'part': 'Coaxial Swaged Heater Coil', 'qty': 1, 'mat': 'Tantalum / MgO Insulated', 'desc': 'Preheats LaB6 insert to 1,450 C for electron emission ignition.'},
                {'item': '04', 'part': 'Molybdenum Keeper Electrode', 'qty': 1, 'mat': 'Molybdenum TZM Alloy', 'desc': 'Maintains self-sustaining discharge arc at low keeper voltage.'},
                {'item': '05', 'part': 'High-Purity Alumina Isolator Body', 'qty': 2, 'mat': 'Al2O3 99.8% Ceramic', 'desc': 'Dielectric high-temperature electrical isolation barrier.'},
                {'item': '06', 'part': 'Micro-Porous Gas Diffuser Plenum', 'qty': 1, 'mat': 'Porous Stainless Steel 316L', 'desc': 'Ensures laminar Xenon propellant dispersal at 1.2 mg/s.'},
                {'item': '07', 'part': 'Anodic Plasma Plume Expansion Nozzle', 'qty': 1, 'mat': 'Pyrolytic Graphite', 'desc': 'Divergent magnetic boundary shaping the contactor plasma bridge.'}
            ],
            'specs': {
                'Outer Body Diameter': '110 mm',
                'Overall Pod Length': '285 mm',
                'Emitter Orifice Diameter': '0.50 mm',
                'Total Subsystem Mass': '4.8 kg',
                'Discharge Current Range': '5.0 - 25.0 Amperes',
                'Ignition Strike Voltage': '1,200 Volts'
            }
        },
        {
            'id': 'cad-shld',
            'subsystem_code': 'SYS-SHLD-04',
            'drawing_no': 'DWG-SHLD-2026-D1',
            'title': 'Active Multipole Habitat Magnetic Shield Assembly',
            'scale': '1:40',
            'units': 'Millimeters [mm]',
            'tolerance': 'ISO 2768-mK (+/- 0.2 mm)',
            'material_spec': 'Toray T1000 Carbon Fiber / REBCO Superconducting Tape / Ti-6Al-4V Bulkheads',
            'description': 'Coaxial dual-toroid magnetic shield creating 4.5 Tesla external radiation deflection barrier while maintaining zero-field (< 0.05 mT) inside the human living module via reverse-wound trim coils.',
            'bom': [
                {'item': '01', 'part': 'Outer Deflector Toroid Coil', 'qty': 1, 'mat': 'REBCO HTS Cable-in-Conduit', 'desc': 'Generates primary 4.5 T external particle deflection envelope.'},
                {'item': '02', 'part': 'Inner Bucking/Trim Coil Set', 'qty': 2, 'mat': 'Opposing REBCO HTS Windings', 'desc': 'Active magnetic cancellation nulling interior field < 50 uT.'},
                {'item': '03', 'part': 'High-Modulus Carbon Tensile Spokes', 'qty': 32, 'mat': 'Toray T1000 Composite', 'desc': 'Pre-stressed radial ties reacting 10 MPa magnetic bursting forces.'},
                {'item': '04', 'part': 'Cylindrical Habitat Pressure Hull', 'qty': 1, 'mat': 'Al-Li 2195 / Carbon Sandwich', 'desc': 'Sealed 7.0 m diameter living compartment for crew of 6.'},
                {'item': '05', 'part': 'Kevlar/Nextel Whipple Meteorite Shield', 'qty': 1, 'mat': 'Nextel / Kevlar 29 multi-layer', 'desc': 'Hypervelocity impact protection surrounding coils and habitat.'},
                {'item': '06', 'part': 'Cryogenic Ring Distribution Manifold', 'qty': 4, 'mat': 'Vacuum-Jacketed SS304', 'desc': 'Circulates supercritical neon coolant across deflector coils.'}
            ],
            'specs': {
                'Outer Shield Diameter': '10,000 mm',
                'Habitat Hull Diameter': '7,000 mm',
                'Habitat Module Length': '8,200 mm',
                'Peak Deflection Field': '4.8 Tesla',
                'Internal Residual Field': '< 0.045 milli-Tesla',
                'Total Structural Mass': '6,850 kg'
            }
        },
        {
            'id': 'cad-bio',
            'subsystem_code': 'SYS-BIO-05',
            'drawing_no': 'DWG-BIO-2026-E1',
            'title': '3-Axis Helmholtz Bio-Resonance Habitat Conditioning Matrix',
            'scale': '1:30',
            'units': 'Millimeters [mm]',
            'tolerance': 'ISO 2768-mK (+/- 0.5 mm)',
            'material_spec': 'Oxygen-Free Copper Litz Wire / Polyimide Insulation / Carbon Composite Ribs',
            'description': 'Three nested orthogonal Helmholtz coil pairs embedded flush into habitat ribs, synthesizing an isotropic 50 uT geomagnetic field with 7.83 Hz Schumann resonance ELF modulation.',
            'bom': [
                {'item': '01', 'part': 'X-Axis Circular Helmholtz Pair', 'qty': 2, 'mat': 'OFHC Litz Wire 12 AWG', 'desc': 'Transverse horizontal static and ULF field synthesis.'},
                {'item': '02', 'part': 'Y-Axis Circular Helmholtz Pair', 'qty': 2, 'mat': 'OFHC Litz Wire 12 AWG', 'desc': 'Transverse vertical static and ULF field synthesis.'},
                {'item': '03', 'part': 'Z-Axis Longitudinal Helmholtz Pair', 'qty': 2, 'mat': 'OFHC Litz Wire 12 AWG', 'desc': 'Axial longitudinal static and ULF field synthesis.'},
                {'item': '04', 'part': 'DSP Schumann Waveform Synthesizer', 'qty': 2, 'mat': 'Radiation-Hardened FPGA', 'desc': 'Generates ultra-low noise 7.83 Hz fundamental and harmonic sine pulses.'},
                {'item': '05', 'part': 'Precision Linear Current Drivers', 'qty': 3, 'mat': 'Ultra-stable Power Op-Amps', 'desc': 'Maintains 50 uT field vector with < 0.1% spatial ripple.'},
                {'item': '06', 'part': '3-Axis Fluxgate Feedback Magnetometer', 'qty': 4, 'mat': 'Permalloy Core Sensors', 'desc': 'Monitors habitat interior field in closed-loop compensation mode.'}
            ],
            'specs': {
                'Coil Cage Diameter': '7,400 mm',
                'Coil Pair Separation Distance': '3,700 mm',
                'Synthesized Static Field': '50.0 micro-Tesla',
                'ELF Modulation Frequency': '7.83 Hz (Schumann fundamental)',
                'Total System Power Draw': '185 Watts',
                'Total System Mass': '142 kg'
            }
        }
    ]
    
    # Celestial Magnetospheres Reference Table
    celestial_bodies = [
        {
            'name': 'Earth (Terra)',
            'code': 'TER-01',
            'b_eq': '31.2 µT (0.312 G)',
            'dipole_moment': '7.94 × 10²² A·m²',
            'standoff_rmp': '10 - 12 R_E (~65,000 km)',
            'bow_shock': '~14 R_E',
            'plasma_density': '1 - 10 cm⁻³ (magnetosphere) / 10³ - 10⁶ cm⁻³ (plasmasphere)',
            'alfven_speed': '200 - 1,500 km/s',
            'propulsion_utility': 'Ideal for Electrodynamic Tethers (EDT), L-shell orbital boosting, and low-Earth de-orbiting.',
            'nav_features': 'High-precision IGRF/WMM Gauss coefficients (degrees up to 13), Schumann resonance (7.83 Hz).',
            'bio_hazards': 'Van Allen inner belt (protons > 100 MeV), outer belt (relativistic electrons > 1 MeV). Requires active shielding.',
        },
        {
            'name': 'Jupiter (Jovian)',
            'code': 'JUP-02',
            'b_eq': '428 µT (4.28 G, 14× Earth)',
            'dipole_moment': '1.55 × 10²⁷ A·m² (~20,000× Earth)',
            'standoff_rmp': '50 - 100 R_J (~3.5 - 7 million km)',
            'bow_shock': '~100 - 120 R_J',
            'plasma_density': 'Io Plasma Torus: ~1,000 - 3,000 cm⁻³ (SO₂⁺, S⁺, O⁺)',
            'alfven_speed': '300 - 4,000 km/s (Mega-Alfvén Wings)',
            'propulsion_utility': 'Immense tether Lorentz forces (kilonewtons achievable), massive Alfvén wing momentum extraction from planetary rotation.',
            'nav_features': 'Sub-millisecond Jovian decametric radio bursts (DAM) and Io flux tube alignment coordinates.',
            'bio_hazards': 'Lethal radiation belts (100–1000× human lethal dose in hours); mandates 5-Tesla active superconducting deflectors.',
        },
        {
            'name': 'Saturn (Cronus)',
            'code': 'SAT-03',
            'b_eq': '21.0 µT (0.210 G)',
            'dipole_moment': '4.6 × 10²⁵ A·m²',
            'standoff_rmp': '20 - 25 R_S (~1.2 - 1.5 million km)',
            'bow_shock': '~30 R_S',
            'plasma_density': 'Enceladus water plume torus: 10 - 100 cm⁻³ (H₂O⁺)',
            'alfven_speed': '100 - 800 km/s',
            'propulsion_utility': 'Symmetric dipole allows smooth equatorial tether orbit adjustments and ring-plane plasma coupling.',
            'nav_features': 'Nearly perfect axial symmetry (< 1° dipole tilt), Saturn Kilometric Radiation (SKR) periodicities.',
            'bio_hazards': 'Moderate radiation belts partially absorbed by the E-ring and main rings; lower shielding mass budget than Jupiter.',
        },
        {
            'name': 'The Sun (Heliosphere)',
            'code': 'SOL-00',
            'b_eq': '100 - 200 µT (surface) / 5 - 10 nT (at 1 AU)',
            'dipole_moment': 'Variable 11-year solar cycle magnetic polarity reversal',
            'standoff_rmp': 'Heliopause: ~120 AU (~1.8 × 10¹⁰ km)',
            'bow_shock': 'Heliospheric boundary layer',
            'plasma_density': 'Solar wind: ~5 - 10 cm⁻³ at 1 AU, speed: 400 - 800 km/s',
            'alfven_speed': '40 - 100 km/s at 1 AU',
            'propulsion_utility': 'High-dynamic-pressure Magsail and M2P2 propulsion; continuous outward acceleration across entire solar system.',
            'nav_features': 'Parker spiral interplanetary magnetic field (IMF) sector boundary crossings, Solar System Barycenter coordinates.',
            'bio_hazards': 'Solar Particle Events (SPEs), Coronal Mass Ejections (CMEs), and Galactic Cosmic Rays (GCRs).',
        },
    ]

    context = {
        'subject': subject,
        'propulsion_course': propulsion_course,
        'navigation_course': navigation_course,
        'evolution_course': evolution_course,
        'architecture_course': architecture_course,
        'spacecraft_subsystems': spacecraft_subsystems,
        'cad_blueprints': cad_blueprints,
        'celestial_bodies': celestial_bodies,
        'total_topics': sum(c.topics.count() for c in courses) if courses else 0,
        'total_equations': sum(sum(t.equations.count() for t in c.topics.all()) for c in courses) if courses else 0,
    }
    return render(request, 'science_engine/space_flight.html', context)

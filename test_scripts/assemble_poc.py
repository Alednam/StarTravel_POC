import json
import sys
from pathlib import Path

# Ensure local test_scripts folder is accessible for imports
sys.path.insert(0, str(Path(__file__).resolve().parent))

from poc_art_library import (
    art_579, art_580, art_581, art_582, art_583, art_584,
    art_585, art_586, art_587, art_588, art_589, art_590,
    art_591, art_592, art_593, art_594, art_595, art_596
)
from generate_all_poc_schematics import topics_data

art_map = {
    579: art_579, 580: art_580, 581: art_581, 582: art_582,
    583: art_583, 584: art_584, 585: art_585, 586: art_586,
    587: art_587, 588: art_588, 589: art_589, 590: art_590,
    591: art_591, 592: art_592, 593: art_593, 594: art_594,
    595: art_595, 596: art_596
}

def build_svg_defs():
    return """
        <defs>
            <pattern id="poc-grid" width="25" height="25" patternUnits="userSpaceOnUse">
                <path d="M 25 0 L 0 0 0 25" fill="none" stroke="#0f274a" stroke-width="0.5" />
            </pattern>
            <marker id="arrow-cyan" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                <path d="M 0 2 L 10 5 L 0 8 z" fill="#38bdf8" />
            </marker>
            <marker id="arrow-amber" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                <path d="M 0 2 L 10 5 L 0 8 z" fill="#f59e0b" />
            </marker>
            <marker id="arrow-green" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                <path d="M 0 2 L 10 5 L 0 8 z" fill="#34d399" />
            </marker>
            <marker id="arrow-red" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                <path d="M 0 2 L 10 5 L 0 8 z" fill="#f43f5e" />
            </marker>
            <marker id="arrow-purple" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                <path d="M 0 2 L 10 5 L 0 8 z" fill="#c084fc" />
            </marker>
            <marker id="arrow-indigo" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                <path d="M 0 2 L 10 5 L 0 8 z" fill="#818cf8" />
            </marker>
        </defs>
    """

def build_single_svg(t):
    tid = t["id"]
    code = t["code"]
    name = t["name"]
    accent = t["accent"]
    art_html = art_map[tid]()

    col1_title, col1_val, col1_sub = t["col1_title"], t["col1_val"], t["col1_sub"]
    col2_title, col2_val, col2_sub = t["col2_title"], t["col2_val"], t["col2_sub"]
    col3_title, col3_val, col3_sub = t["col3_title"], t["col3_val"], t["col3_sub"]
    col4_title, col4_val, col4_sub = t["col4_title"], t["col4_val"], t["col4_sub"]

    is_first = (tid == 579)
    display_class = "block" if is_first else "hidden"
    svg_display_title = name if len(name) <= 44 else name[:42] + "..."

    return f"""
        <!-- TOPIC {tid}: {code} - {name} -->
        <svg id="svg-poc-{tid}" viewBox="0 0 1000 620" class="w-full h-full poc-sheet {display_class} select-none">
            {build_svg_defs()}

            <!-- Background Blueprint Grid -->
            <rect width="1000" height="620" fill="url(#poc-grid)" />

            <!-- Outer Blueprint Borders -->
            <rect x="12" y="12" width="976" height="596" fill="none" stroke="{accent}" stroke-width="1.2" opacity="0.6" />
            <rect x="16" y="16" width="968" height="588" fill="none" stroke="{accent}" stroke-width="0.6" opacity="0.3" />

            <!-- Corner Alignment Targets -->
            <g stroke="{accent}" stroke-width="0.8" opacity="0.6">
                <path d="M 12 30 L 30 30 L 30 12" fill="none" />
                <path d="M 988 30 L 970 30 L 970 12" fill="none" />
                <path d="M 12 590 L 30 590 L 30 608" fill="none" />
                <path d="M 988 590 L 970 590 L 970 608" fill="none" />
            </g>

            <!-- Top Left Title Plate -->
            <g transform="translate(30, 32)">
                <rect x="0" y="0" width="370" height="52" rx="4" fill="#040e24" stroke="{accent}" stroke-width="1" />
                <text x="12" y="18" font-family="monospace" font-size="10" font-weight="bold" fill="{accent}">EXPERIMENT: {code}</text>
                <text x="12" y="34" font-family="monospace" font-size="9" font-weight="bold" fill="#f8fafc">{svg_display_title}</text>
                <text x="12" y="46" font-family="monospace" font-size="8" fill="#94a3b8">{t['phase_name']}</text>
            </g>

            <!-- Top Right HUD Status -->
            <g transform="translate(710, 32)">
                <rect x="0" y="0" width="260" height="42" rx="4" fill="#040e24" stroke="{accent}" stroke-width="0.8" />
                <text x="12" y="16" font-family="monospace" font-size="8" fill="#94a3b8">VALIDATION PROTOCOL: TRL-6</text>
                <text x="12" y="32" font-family="monospace" font-size="9" font-weight="bold" fill="#34d399">STATUS: FLIGHT VERIFIED</text>
            </g>

            <!-- Custom Topic Artwork -->
            {art_html}

            <!-- Bottom Integrated Telemetry Bar (4 Columns) -->
            <g transform="translate(30, 532)">
                <rect x="0" y="0" width="940" height="68" rx="4" fill="#040e24" stroke="{accent}" stroke-width="1" opacity="0.95" />
                <line x1="235" y1="0" x2="235" y2="68" stroke="{accent}" stroke-width="0.5" opacity="0.4" />
                <line x1="470" y1="0" x2="470" y2="68" stroke="{accent}" stroke-width="0.5" opacity="0.4" />
                <line x1="705" y1="0" x2="705" y2="68" stroke="{accent}" stroke-width="0.5" opacity="0.4" />

                <!-- Col 1 -->
                <text x="15" y="20" font-family="monospace" font-size="8" fill="#94a3b8">{col1_title}</text>
                <text x="15" y="40" font-family="monospace" font-size="13" font-weight="bold" fill="#38bdf8">{col1_val}</text>
                <text x="15" y="56" font-family="monospace" font-size="8" fill="#64748b">{col1_sub}</text>

                <!-- Col 2 -->
                <text x="250" y="20" font-family="monospace" font-size="8" fill="#94a3b8">{col2_title}</text>
                <text x="250" y="40" font-family="monospace" font-size="13" font-weight="bold" fill="#34d399">{col2_val}</text>
                <text x="250" y="56" font-family="monospace" font-size="8" fill="#64748b">{col2_sub}</text>

                <!-- Col 3 -->
                <text x="485" y="20" font-family="monospace" font-size="8" fill="#94a3b8">{col3_title}</text>
                <text x="485" y="40" font-family="monospace" font-size="13" font-weight="bold" fill="#f59e0b">{col3_val}</text>
                <text x="485" y="56" font-family="monospace" font-size="8" fill="#64748b">{col3_sub}</text>

                <!-- Col 4 -->
                <text x="720" y="20" font-family="monospace" font-size="8" fill="#94a3b8">{col4_title}</text>
                <text x="720" y="40" font-family="monospace" font-size="13" font-weight="bold" fill="#c084fc">{col4_val}</text>
                <text x="720" y="56" font-family="monospace" font-size="8" fill="#64748b">{col4_sub}</text>
            </g>
        </svg>
    """

def assemble():
    svgs_list = [build_single_svg(t) for t in topics_data]
    svgs_combined = "\n".join(svgs_list)

    phases = [
        {"key": "propulsion", "label": "Phase I: Propulsion", "color": "cyan"},
        {"key": "navigation", "label": "Phase II: Navigation", "color": "indigo"},
        {"key": "evolution", "label": "Phase III: Evolution", "color": "purple"},
        {"key": "architecture", "label": "Phase IV: Architecture", "color": "emerald"},
    ]

    phase_tabs_html = ""
    for p in phases:
        is_p1 = (p["key"] == "propulsion")
        active_cls = "bg-cyan-600 text-white border-cyan-500 shadow-sm" if is_p1 else "bg-slate-900/80 text-slate-300 border-slate-700 hover:border-slate-500"
        phase_tabs_html += f"""
            <button onclick="switchPocPhase('{p['key']}')" id="btn-phase-{p['key']}" class="px-3 py-1.5 rounded-lg border font-bold transition font-mono text-xs {active_cls}">
                {p['label']}
            </button>
        """

    topic_pills_html = ""
    for p in phases:
        p_topics = [t for t in topics_data if t["phase"] == p["key"]]
        hidden_cls = "" if p["key"] == "propulsion" else "hidden"
        topic_pills_html += f"""
        <div id="pills-phase-{p['key']}" class="flex flex-wrap items-center gap-1.5 {hidden_cls}">
        """
        for t in p_topics:
            tid = t["id"]
            is_active = (tid == 579)
            btn_cls = "bg-cyan-950 text-cyan-300 border-cyan-500 shadow-sm font-bold" if is_active else "bg-slate-950 text-slate-400 border-slate-800 hover:border-slate-600 hover:text-slate-200"
            topic_pills_html += f"""
                <button onclick="switchPocTopic({tid})" id="btn-topic-{tid}" class="topic-pill px-2.5 py-1 rounded border text-[11px] font-mono transition {btn_cls}">
                    {t['short_name']}
                </button>
            """
        topic_pills_html += "</div>\n"

    meta_dict = {t["id"]: t for t in topics_data}
    meta_json = json.dumps(meta_dict)

    template_content = f"""<!-- Space Flight Proof of Concept (POC) Physics Schematics -->
<!-- Comprehensive 18-Topic Physics Demonstrator for Space Flight Portal and Topic Detail Pages -->

<div class="poc-container w-full rounded-2xl bg-gradient-to-br from-[#050b18] via-[#091428] to-[#040814] border border-cyan-800/40 p-5 lg:p-8 shadow-2xl font-sans text-slate-200 relative overflow-hidden my-8">

    <!-- Top Status Bar & POC Selector Header -->
    <div class="flex flex-col lg:flex-row lg:items-center justify-between gap-4 border-b border-cyan-900/40 pb-5 mb-5">
        <div>
            <div class="flex flex-wrap items-center gap-2 mb-1.5">
                <span class="px-2 py-0.5 rounded bg-cyan-950/80 border border-cyan-500/40 text-cyan-300 font-mono text-[10px] font-bold uppercase tracking-widest">
                    Proof of Concept Demonstration
                </span>
                <span class="text-slate-500 text-xs font-mono">|</span>
                <span class="text-slate-400 font-mono text-xs font-bold" id="poc-system-id">POC-579-EDT</span>
                <span class="text-slate-500 text-xs font-mono">|</span>
                <span class="px-2 py-0.5 rounded bg-slate-900 border border-slate-700 text-slate-300 font-mono text-[10px] font-bold" id="poc-phase-badge">Phase I: Propulsion</span>
            </div>
            <h3 class="text-xl lg:text-2xl font-bold text-white tracking-tight" id="poc-heading-title">
                Electrodynamic Tethers (EDTs) & Motional EMF
            </h3>
            <p class="text-slate-400 text-xs mt-1 max-w-3xl" id="poc-heading-desc">
                Propellantless Lorentz thrust and motional induction across a 25 km conductive tether in planetary magnetic flux.
            </p>
            <div class="mt-2 text-cyan-400 font-mono text-xs overflow-x-auto" id="poc-heading-formula">
                $$\\vec{{F}} = I (\\vec{{L}} \\times \\vec{{B}}), \\quad \\mathcal{{E}} = \\int (\\vec{{v}}_{{rel}} \\times \\vec{{B}}) \\cdot d\\vec{{\\ell}}$$
            </div>
        </div>

        <!-- Phase Navigation Tabs -->
        <div class="flex flex-wrap items-center gap-2">
            {phase_tabs_html}
        </div>
    </div>

    <!-- Topic Selector Pills (Sub-navigation for all 18 topics) -->
    <div class="mb-4 bg-slate-950/60 p-2.5 rounded-xl border border-slate-800/80">
        <div class="text-[10px] font-mono text-slate-500 uppercase tracking-wider mb-2 font-bold">Select Proof of Concept Topic:</div>
        {topic_pills_html}
    </div>

    <!-- Main Canvas Area (18 Interactive Blueprint SVGs) -->
    <div class="relative w-full aspect-[16/10] bg-[#020617] rounded-xl border border-cyan-900/30 overflow-hidden shadow-inner flex items-center justify-center">
        {svgs_combined}
    </div>

    <!-- Bottom Responsive Telemetry Grid Cards (Mirroring SVG parameters for mobile readability) -->
    <div class="grid grid-cols-2 md:grid-cols-4 gap-3 mt-4">
        <div class="bg-slate-950/70 border border-slate-800 rounded-lg p-3">
            <div class="text-[9px] font-mono text-slate-400 uppercase" id="card-col1-title">MOTIONAL INDUCED EMF</div>
            <div class="text-lg font-mono font-bold text-cyan-400 mt-0.5" id="card-col1-val">5,380 V DC</div>
            <div class="text-[10px] font-mono text-slate-500 truncate" id="card-col1-sub">E = (v_rel x B) · L</div>
        </div>
        <div class="bg-slate-950/70 border border-slate-800 rounded-lg p-3">
            <div class="text-[9px] font-mono text-slate-400 uppercase" id="card-col2-title">LORENTZ THRUST</div>
            <div class="text-lg font-mono font-bold text-emerald-400 mt-0.5" id="card-col2-val">10.68 N</div>
            <div class="text-[10px] font-mono text-slate-500 truncate" id="card-col2-sub">F = I · (L x B) Continuous</div>
        </div>
        <div class="bg-slate-950/70 border border-slate-800 rounded-lg p-3">
            <div class="text-[9px] font-mono text-slate-400 uppercase" id="card-col3-title">SPECIFIC IMPULSE (I_sp)</div>
            <div class="text-lg font-mono font-bold text-amber-400 mt-0.5" id="card-col3-val">INFINITE (∞)</div>
            <div class="text-[10px] font-mono text-slate-500 truncate" id="card-col3-sub">Zero reaction mass</div>
        </div>
        <div class="bg-slate-950/70 border border-slate-800 rounded-lg p-3">
            <div class="text-[9px] font-mono text-slate-400 uppercase" id="card-col4-title">ORBITAL DELTA-V</div>
            <div class="text-lg font-mono font-bold text-purple-400 mt-0.5" id="card-col4-val">86.4 km/s / yr</div>
            <div class="text-[10px] font-mono text-slate-500 truncate" id="card-col4-sub">Continuous Semi-Major Boost</div>
        </div>
    </div>

    <!-- Bottom Caption & Physics Bridge -->
    <div class="mt-4 flex flex-col md:flex-row md:items-center justify-between text-xs font-mono text-slate-400 border-t border-slate-800/80 pt-3">
        <div id="poc-footer-notes">
            <span class="text-cyan-400 font-bold">PHYSICAL PROOF:</span> Motional induction verified by NASA TSS-1R flight test (3.5 kV generated) and JAXA KITE orbital tests.
        </div>
        <div class="text-[10px] text-slate-500 uppercase mt-1 md:mt-0">
            Hardware Validation Standard: ISO 14644 &bull; NASA TRL-6
        </div>
    </div>
</div>

<script>
    const pocTopicsMeta = {meta_json};

    let currentPhase = 'propulsion';
    let currentTopicId = 579;

    function switchPocPhase(phaseKey) {{
        currentPhase = phaseKey;

        // Update Phase Tab Buttons
        const phases = ['propulsion', 'navigation', 'evolution', 'architecture'];
        phases.forEach(p => {{
            const btn = document.getElementById('btn-phase-' + p);
            if (btn) {{
                btn.className = "px-3 py-1.5 rounded-lg border font-bold transition font-mono text-xs bg-slate-900/80 text-slate-300 border-slate-700 hover:border-slate-500";
            }}
            const pillsDiv = document.getElementById('pills-phase-' + p);
            if (pillsDiv) {{
                pillsDiv.classList.add('hidden');
            }}
        }});

        const activeBtn = document.getElementById('btn-phase-' + phaseKey);
        if (activeBtn) {{
            const colorMap = {{
                'propulsion': 'bg-cyan-600 text-white border-cyan-500 shadow-sm',
                'navigation': 'bg-indigo-600 text-white border-indigo-500 shadow-sm',
                'evolution': 'bg-purple-600 text-white border-purple-500 shadow-sm',
                'architecture': 'bg-emerald-600 text-white border-emerald-500 shadow-sm'
            }};
            activeBtn.className = "px-3 py-1.5 rounded-lg border font-bold transition font-mono text-xs " + (colorMap[phaseKey] || 'bg-cyan-600 text-white');
        }}

        const activePillsDiv = document.getElementById('pills-phase-' + phaseKey);
        if (activePillsDiv) {{
            activePillsDiv.classList.remove('hidden');
        }}

        // Switch to the first topic in this phase if the currently active topic is not in this phase
        const activeTopic = pocTopicsMeta[currentTopicId];
        if (!activeTopic || activeTopic.phase !== phaseKey) {{
            const firstTopicInPhase = Object.values(pocTopicsMeta).find(t => t.phase === phaseKey);
            if (firstTopicInPhase) {{
                switchPocTopic(firstTopicInPhase.id);
            }}
        }}
    }}

    function switchPocTopic(topicId) {{
        topicId = parseInt(topicId);
        const meta = pocTopicsMeta[topicId];
        if (!meta) return;

        currentTopicId = topicId;

        // If the topic belongs to another phase, ensure that phase's sub-pill bar is visible
        if (meta.phase !== currentPhase) {{
            currentPhase = meta.phase;
            const phases = ['propulsion', 'navigation', 'evolution', 'architecture'];
            phases.forEach(p => {{
                const btn = document.getElementById('btn-phase-' + p);
                if (btn) {{
                    btn.className = "px-3 py-1.5 rounded-lg border font-bold transition font-mono text-xs bg-slate-900/80 text-slate-300 border-slate-700 hover:border-slate-500";
                }}
                const pillsDiv = document.getElementById('pills-phase-' + p);
                if (pillsDiv) {{
                    pillsDiv.classList.add('hidden');
                }}
            }});
            const activePhaseBtn = document.getElementById('btn-phase-' + meta.phase);
            if (activePhaseBtn) {{
                const colorMap = {{
                    'propulsion': 'bg-cyan-600 text-white border-cyan-500 shadow-sm',
                    'navigation': 'bg-indigo-600 text-white border-indigo-500 shadow-sm',
                    'evolution': 'bg-purple-600 text-white border-purple-500 shadow-sm',
                    'architecture': 'bg-emerald-600 text-white border-emerald-500 shadow-sm'
                }};
                activePhaseBtn.className = "px-3 py-1.5 rounded-lg border font-bold transition font-mono text-xs " + (colorMap[meta.phase] || 'bg-cyan-600 text-white');
            }}
            const activePillsDiv = document.getElementById('pills-phase-' + meta.phase);
            if (activePillsDiv) {{
                activePillsDiv.classList.remove('hidden');
            }}
        }}

        // Hide all SVGs and show the selected SVG
        for (let id = 579; id <= 596; id++) {{
            const svgEl = document.getElementById('svg-poc-' + id);
            if (svgEl) {{
                svgEl.classList.add('hidden');
                svgEl.classList.remove('block');
            }}
        }}
        const targetSvg = document.getElementById('svg-poc-' + topicId);
        if (targetSvg) {{
            targetSvg.classList.remove('hidden');
            targetSvg.classList.add('block');
        }}

        // Update Topic Pill Button active styles
        const allPills = document.querySelectorAll('.topic-pill');
        allPills.forEach(pill => {{
            pill.className = "topic-pill px-2.5 py-1 rounded border text-[11px] font-mono transition bg-slate-950 text-slate-400 border-slate-800 hover:border-slate-600 hover:text-slate-200";
        }});
        const activePill = document.getElementById('btn-topic-' + topicId);
        if (activePill) {{
            const pillColorMap = {{
                'propulsion': 'bg-cyan-950 text-cyan-300 border-cyan-500 shadow-sm font-bold',
                'navigation': 'bg-indigo-950 text-indigo-300 border-indigo-500 shadow-sm font-bold',
                'evolution': 'bg-purple-950 text-purple-300 border-purple-500 shadow-sm font-bold',
                'architecture': 'bg-emerald-950 text-emerald-300 border-emerald-500 shadow-sm font-bold'
            }};
            activePill.className = "topic-pill px-2.5 py-1 rounded border text-[11px] font-mono transition " + (pillColorMap[meta.phase] || 'bg-cyan-950 text-cyan-300 border-cyan-500');
        }}

        // Update Header Text & Metadata
        document.getElementById('poc-system-id').innerText = meta.code;
        document.getElementById('poc-phase-badge').innerText = meta.phase_name;
        document.getElementById('poc-heading-title').innerText = meta.name;
        document.getElementById('poc-heading-desc').innerText = meta.desc;

        // Update Formula Block
        const formulaEl = document.getElementById('poc-heading-formula');
        if (formulaEl) {{
            formulaEl.innerHTML = '$$' + meta.formula + '$$';
            if (window.renderMathInElement) {{
                renderMathInElement(formulaEl, {{
                    delimiters: [
                        {{left: '$$', right: '$$', display: true}},
                        {{left: '$', right: '$', display: false}}
                    ]
                }});
            }} else if (window.MathJax && window.MathJax.typesetPromise) {{
                MathJax.typesetPromise([formulaEl]);
            }}
        }}

        // Update Bottom Responsive Parameter Cards
        document.getElementById('card-col1-title').innerText = meta.col1_title;
        document.getElementById('card-col1-val').innerText = meta.col1_val;
        document.getElementById('card-col1-sub').innerText = meta.col1_sub;

        document.getElementById('card-col2-title').innerText = meta.col2_title;
        document.getElementById('card-col2-val').innerText = meta.col2_val;
        document.getElementById('card-col2-sub').innerText = meta.col2_sub;

        document.getElementById('card-col3-title').innerText = meta.col3_title;
        document.getElementById('card-col3-val').innerText = meta.col3_val;
        document.getElementById('card-col3-sub').innerText = meta.col3_sub;

        document.getElementById('card-col4-title').innerText = meta.col4_title;
        document.getElementById('card-col4-val').innerText = meta.col4_val;
        document.getElementById('card-col4-sub').innerText = meta.col4_sub;

        // Update Footer Physical Proof Citation
        const noteParts = meta.notes.split(':');
        document.getElementById('poc-footer-notes').innerHTML =
            `<span class="text-cyan-400 font-bold">${{noteParts[0]}}:</span> ${{noteParts.slice(1).join(':')}}`;
    }}

    // Backwards compatibility alias for older 4-phase callers
    function switchPocDiagram(mode) {{
        if (typeof mode === 'number' || (!isNaN(parseInt(mode)) && parseInt(mode) >= 579)) {{
            switchPocTopic(parseInt(mode));
        }} else if (['propulsion', 'navigation', 'evolution', 'architecture'].includes(mode)) {{
            switchPocPhase(mode);
        }}
    }}

    // Auto-initialize when the DOM is ready
    document.addEventListener('DOMContentLoaded', function() {{
        {{% if topic and topic.id >= 579 and topic.id <= 596 %}}
        switchPocTopic({{{{ topic.id }}}});
        {{% else %}}
        switchPocTopic(579);
        {{% endif %}}
    }});
</script>
"""

    output_path = Path(__file__).resolve().parent.parent / "science_engine" / "templates" / "science_engine" / "poc_diagrams.html"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(template_content)
    print(f"Successfully generated {output_path} ({len(template_content)} bytes).")

if __name__ == "__main__":
    assemble()

# 18 Technical SVG Artworks for Space Flight Topics

def art_579():
    """Electrodynamic Tethers (EDTs) & Motional EMF"""
    return """
        <!-- Planet Earth Dipole Sphere (Left side) -->
        <g transform="translate(150, 310)">
            <circle cx="0" cy="0" r="145" fill="#0284c7" fill-opacity="0.05" stroke="#0284c7" stroke-width="1" stroke-dasharray="4,4" />
            <circle cx="0" cy="0" r="130" fill="#0369a1" fill-opacity="0.1" stroke="#38bdf8" stroke-width="1.2" />
            <circle cx="0" cy="0" r="115" fill="#0b1e3b" stroke="#0ea5e9" stroke-width="2" />
            <path d="M -70 -40 Q 0 -90 70 -40 Q 40 40 -70 -40 Z" fill="#064e3b" fill-opacity="0.6" />
            <path d="M -40 30 Q 30 20 60 70 Q -20 90 -40 30 Z" fill="#064e3b" fill-opacity="0.6" />
            <line x1="0" y1="-140" x2="0" y2="140" stroke="#f43f5e" stroke-width="1.5" stroke-dasharray="8,4" />
            <text x="0" y="-148" font-family="monospace" font-size="9" font-weight="bold" fill="#f43f5e" text-anchor="middle">MAG NORTH (S POLE)</text>
            <text x="0" y="158" font-family="monospace" font-size="9" font-weight="bold" fill="#38bdf8" text-anchor="middle">MAG SOUTH (N POLE)</text>
            <text x="0" y="5" font-family="monospace" font-size="11" font-weight="bold" fill="#e2e8f0" text-anchor="middle">TERRA CORE</text>
            <text x="0" y="20" font-family="monospace" font-size="8" fill="#64748b" text-anchor="middle">B0 = 31.2 µT</text>
        </g>

        <!-- Magnetic Field Lines (B-Field Flow) -->
        <g stroke="#38bdf8" stroke-width="1.2" fill="none" opacity="0.6">
            <path d="M 150 435 C 320 460 380 380 380 310 C 380 240 320 160 150 185" marker-mid="url(#arrow-cyan)" />
            <path d="M 150 445 C 480 490 560 380 560 310 C 560 240 480 130 150 175" marker-mid="url(#arrow-cyan)" />
            <path d="M 150 455 C 650 520 740 380 740 310 C 740 240 650 100 150 165" marker-mid="url(#arrow-cyan)" />
        </g>

        <!-- Orbit Trajectory Arc -->
        <path d="M 500 120 C 680 170 760 310 770 480" fill="none" stroke="#64748b" stroke-width="1" stroke-dasharray="6,4" />

        <!-- 25 km Electrodynamic Tether Assembly -->
        <!-- Upper Main Spacecraft (Anode / Collector) -->
        <g transform="translate(680, 160)">
            <rect x="-35" y="-14" width="70" height="28" rx="3" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5" />
            <line x1="-35" y1="0" x2="-65" y2="0" stroke="#38bdf8" stroke-width="2" />
            <rect x="-85" y="-12" width="20" height="24" fill="#0284c7" stroke="#38bdf8" stroke-width="0.8" />
            <line x1="35" y1="0" x2="65" y2="0" stroke="#38bdf8" stroke-width="2" />
            <rect x="65" y="-12" width="20" height="24" fill="#0284c7" stroke="#38bdf8" stroke-width="0.8" />
            <text x="0" y="4" font-family="monospace" font-size="8" font-weight="bold" fill="#38bdf8" text-anchor="middle">MAIN BUS (ANODE)</text>
            <!-- Plasma Contactor plume -->
            <path d="M 0 -14 Q -15 -35 0 -45 Q 15 -35 0 -14 Z" fill="#38bdf8" fill-opacity="0.3" stroke="#38bdf8" stroke-width="0.8" />
            <text x="0" y="-48" font-family="monospace" font-size="7" fill="#a5f3fc" text-anchor="middle">e- COLLECTION</text>
        </g>

        <!-- Conductive Tether Wire (25 km scaled) -->
        <line x1="680" y1="174" x2="680" y2="440" stroke="#f59e0b" stroke-width="2.5" />
        <!-- Glowing Current Direction Indicators along Tether -->
        <g fill="#f59e0b">
            <polygon points="680,210 676,200 684,200" />
            <polygon points="680,260 676,250 684,250" />
            <polygon points="680,310 676,300 684,300" />
            <polygon points="680,360 676,350 684,350" />
            <polygon points="680,410 676,400 684,400" />
        </g>

        <!-- Lower Sub-Satellite / Hollow Cathode (Cathode / Emitter) -->
        <g transform="translate(680, 440)">
            <circle cx="0" cy="12" r="14" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5" />
            <text x="0" y="15" font-family="monospace" font-size="7" font-weight="bold" fill="#f59e0b" text-anchor="middle">CATHODE</text>
            <!-- Electron emitter plume -->
            <path d="M 0 26 Q -20 50 0 60 Q 20 50 0 26 Z" fill="#f59e0b" fill-opacity="0.3" stroke="#f59e0b" stroke-width="0.8" />
            <text x="0" y="70" font-family="monospace" font-size="7" fill="#fde68a" text-anchor="middle">LaB6 e- EJECTION</text>
        </g>

        <!-- Ionospheric Closing Current Path (Plasma circuit) -->
        <path d="M 680 495 C 800 480 840 320 840 240 C 840 180 770 140 680 135" fill="none" stroke="#a855f7" stroke-width="1.2" stroke-dasharray="4,4" />
        <text x="850" y="270" font-family="monospace" font-size="8" fill="#c084fc">IONOSPHERIC CLOSURE (O+ PLASMA)</text>

        <!-- Physics Vector Triad Callout -->
        <g transform="translate(530, 240)">
            <rect x="0" y="0" width="130" height="90" rx="3" fill="#040d1a" stroke="#0ea5e9" stroke-width="0.8" />
            <text x="10" y="16" font-family="monospace" font-size="8" font-weight="bold" fill="#38bdf8">VECTOR DYNAMICS</text>
            <!-- v_orb vector -->
            <line x1="20" y1="40" x2="60" y2="40" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrow-cyan)" />
            <text x="65" y="43" font-family="monospace" font-size="8" fill="#38bdf8">v_orb (7.67 km/s)</text>
            <!-- B vector -->
            <line x1="20" y1="40" x2="20" y2="75" stroke="#a855f7" stroke-width="2" marker-end="url(#arrow-purple)" />
            <text x="25" y="73" font-family="monospace" font-size="8" fill="#a855f7">B_geo (31 µT)</text>
            <!-- F_L Lorentz force vector -->
            <line x1="20" y1="40" x2="50" y2="25" stroke="#34d399" stroke-width="2.2" marker-end="url(#arrow-green)" />
            <text x="55" y="25" font-family="monospace" font-size="8" font-weight="bold" fill="#34d399">F_L (10.68 N)</text>
        </g>

        <!-- Motional EMF Formula Tag -->
        <g transform="translate(710, 310)">
            <rect x="0" y="0" width="135" height="40" rx="3" fill="#091428" stroke="#f59e0b" stroke-width="0.8" />
            <text x="8" y="16" font-family="monospace" font-size="8" font-weight="bold" fill="#fbbf24">MOTIONAL EMF INDUCED</text>
            <text x="8" y="30" font-family="monospace" font-size="10" font-weight="bold" fill="#ffffff">E = 5,380 V DC</text>
        </g>
    """

def art_580():
    """Magnetic Sails (Magsails) & Plasma Magnetospheres"""
    return """
        <!-- Supersonic Solar Wind Incoming Protons (Left to Right) -->
        <g stroke="#38bdf8" stroke-width="1.2" opacity="0.6">
            <line x1="40" y1="120" x2="280" y2="120" marker-end="url(#arrow-cyan)" />
            <line x1="40" y1="180" x2="310" y2="180" marker-end="url(#arrow-cyan)" />
            <line x1="40" y1="240" x2="330" y2="240" marker-end="url(#arrow-cyan)" />
            <line x1="40" y1="300" x2="340" y2="300" marker-end="url(#arrow-cyan)" />
            <line x1="40" y1="360" x2="330" y2="360" marker-end="url(#arrow-cyan)" />
            <line x1="40" y1="420" x2="310" y2="420" marker-end="url(#arrow-cyan)" />
            <line x1="40" y1="480" x2="280" y2="480" marker-end="url(#arrow-cyan)" />
        </g>
        <g transform="translate(60, 200)">
            <rect x="0" y="0" width="140" height="48" rx="3" fill="#040e24" stroke="#0ea5e9" stroke-width="0.8" />
            <text x="8" y="16" font-family="monospace" font-size="8" font-weight="bold" fill="#38bdf8">SUPERSONIC SOLAR WIND</text>
            <text x="8" y="30" font-family="monospace" font-size="8" fill="#94a3b8">v_sw = 500 km/s (Mach 8.5)</text>
            <text x="8" y="42" font-family="monospace" font-size="8" fill="#94a3b8">n_p = 7 protons / cm^3</text>
        </g>

        <!-- Parabolic Bow Shock Discontinuity -->
        <path d="M 320 80 Q 220 300 320 520" fill="none" stroke="#f43f5e" stroke-width="2.5" stroke-dasharray="6,3" />
        <text x="210" y="305" font-family="monospace" font-size="9" font-weight="bold" fill="#f43f5e" transform="rotate(-90 210 305)">BOW SHOCK FRONT</text>

        <!-- Magnetopause Boundary Standoff Surface -->
        <path d="M 410 100 Q 340 300 410 500" fill="#0284c7" fill-opacity="0.08" stroke="#38bdf8" stroke-width="2" />
        <text x="350" y="160" font-family="monospace" font-size="8" font-weight="bold" fill="#38bdf8">MAGNETOPAUSE (R_mp = 48.5 km)</text>

        <!-- Deflected Streamlines around Magnetopause -->
        <g stroke="#38bdf8" stroke-width="1.2" fill="none" opacity="0.7">
            <path d="M 310 180 C 370 170 430 130 580 120 C 720 110 880 100 950 95" marker-mid="url(#arrow-cyan)" />
            <path d="M 330 240 C 380 230 430 200 580 180 C 720 170 880 170 950 170" marker-mid="url(#arrow-cyan)" />
            <path d="M 330 360 C 380 370 430 400 580 420 C 720 430 880 430 950 430" marker-mid="url(#arrow-cyan)" />
            <path d="M 310 420 C 370 430 430 470 580 480 C 720 490 880 500 950 505" marker-mid="url(#arrow-cyan)" />
        </g>

        <!-- Superconducting Coil Magsail Core (Center-Right) -->
        <g transform="translate(560, 300)">
            <!-- Dipole Field Loops -->
            <ellipse cx="0" cy="0" rx="90" ry="140" fill="none" stroke="#6366f1" stroke-width="1.5" opacity="0.6" />
            <ellipse cx="0" cy="0" rx="140" ry="190" fill="none" stroke="#6366f1" stroke-width="1" opacity="0.4" />
            <!-- Spacecraft Bus & HTS Ring -->
            <circle cx="0" cy="0" r="32" fill="#0b1b36" stroke="#38bdf8" stroke-width="2" />
            <ellipse cx="0" cy="0" rx="26" ry="10" fill="none" stroke="#34d399" stroke-width="3" />
            <text x="0" y="4" font-family="monospace" font-size="7" font-weight="bold" fill="#34d399" text-anchor="middle">HTS COIL (3.5 kA)</text>
            <text x="0" y="-38" font-family="monospace" font-size="8" fill="#e2e8f0" text-anchor="middle">SPACECRAFT CORE</text>
        </g>

        <!-- Pressure Balance Callout Box -->
        <g transform="translate(680, 200)">
            <rect x="0" y="0" width="160" height="60" rx="3" fill="#040e24" stroke="#34d399" stroke-width="0.8" />
            <text x="8" y="16" font-family="monospace" font-size="8" font-weight="bold" fill="#34d399">PRESSURE EQUILIBRIUM</text>
            <text x="8" y="32" font-family="monospace" font-size="8" fill="#94a3b8">P_dyn (Solar Wind) = B^2 / 2u0</text>
            <text x="8" y="48" font-family="monospace" font-size="9" font-weight="bold" fill="#ffffff">F_drag = +11.47 N (PROGRADE)</text>
        </g>

        <!-- Momentum Transfer Vector -->
        <line x1="592" y1="300" x2="720" y2="300" stroke="#34d399" stroke-width="3" marker-end="url(#arrow-green)" />
        <text x="650" y="292" font-family="monospace" font-size="9" font-weight="bold" fill="#34d399">F_LORENTZ DRAG</text>
    """

def art_581():
    """Alfvén Wave Propulsion & MHD Coupling"""
    return """
        <!-- Ambient Background Magnetic Flux (Planetary B0 Lines, Vertical) -->
        <g stroke="#38bdf8" stroke-width="1" opacity="0.35">
            <line x1="120" y1="80" x2="120" y2="520" />
            <line x1="220" y1="80" x2="220" y2="520" />
            <line x1="320" y1="80" x2="320" y2="520" />
            <line x1="420" y1="80" x2="420" y2="520" />
            <line x1="520" y1="80" x2="520" y2="520" />
            <line x1="620" y1="80" x2="620" y2="520" />
            <line x1="720" y1="80" x2="720" y2="520" />
            <line x1="820" y1="80" x2="820" y2="520" />
        </g>
        <text x="125" y="110" font-family="monospace" font-size="8" fill="#38bdf8">BACKGROUND B0 (PLANETARY DIPOLE FLUX)</text>

        <!-- Electrodynamic Craft (Moving horizontally at v0) -->
        <g transform="translate(420, 300)">
            <!-- Spacecraft Body -->
            <rect x="-30" y="-14" width="60" height="28" rx="3" fill="#0f172a" stroke="#0ea5e9" stroke-width="1.8" />
            <text x="0" y="4" font-family="monospace" font-size="8" font-weight="bold" fill="#38bdf8" text-anchor="middle">MHD CRAFT</text>
            <!-- Velocity Vector v0 -->
            <line x1="30" y1="0" x2="90" y2="0" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#arrow-cyan)" />
            <text x="95" y="4" font-family="monospace" font-size="8" font-weight="bold" fill="#38bdf8">v0 = 7.5 km/s</text>
        </g>

        <!-- Shear Alfvén Wave Wings (Mach Cones propagating up & down along B0) -->
        <!-- Upper Alfvén Wing -->
        <polygon points="420,286 280,100 320,100 440,286" fill="#6366f1" fill-opacity="0.25" stroke="#818cf8" stroke-width="1.5" />
        <!-- Birkeland Current Loops in Wing -->
        <line x1="425" y1="286" x2="295" y2="105" stroke="#f59e0b" stroke-width="2" stroke-dasharray="6,3" />
        <line x1="435" y1="286" x2="310" y2="105" stroke="#34d399" stroke-width="2" stroke-dasharray="6,3" />
        <text x="240" y="160" font-family="monospace" font-size="8" font-weight="bold" fill="#818cf8">NORTHERN ALFVÉN WING</text>
        <text x="240" y="172" font-family="monospace" font-size="7" fill="#fbbf24">I_A = Birkeland Current</text>

        <!-- Lower Alfvén Wing -->
        <polygon points="420,314 280,500 320,500 440,314" fill="#6366f1" fill-opacity="0.25" stroke="#818cf8" stroke-width="1.5" />
        <!-- Birkeland Current Loops in Wing -->
        <line x1="425" y1="314" x2="295" y2="495" stroke="#f59e0b" stroke-width="2" stroke-dasharray="6,3" />
        <line x1="435" y1="314" x2="310" y2="495" stroke="#34d399" stroke-width="2" stroke-dasharray="6,3" />
        <text x="240" y="450" font-family="monospace" font-size="8" font-weight="bold" fill="#818cf8">SOUTHERN ALFVÉN WING</text>
        <text x="240" y="462" font-family="monospace" font-size="7" fill="#34d399">Coupling to Ionosphere</text>

        <!-- Mach Angle Indicator -->
        <path d="M 420 230 A 70 70 0 0 0 370 238" fill="none" stroke="#f43f5e" stroke-width="1.2" />
        <text x="350" y="215" font-family="monospace" font-size="8" font-weight="bold" fill="#f43f5e">θ = tan^-1(v0/vA) = 0.89°</text>

        <!-- Impedance & Momentum Transfer Callout Block -->
        <g transform="translate(640, 220)">
            <rect x="0" y="0" width="185" height="110" rx="3" fill="#040e24" stroke="#818cf8" stroke-width="1" />
            <text x="10" y="18" font-family="monospace" font-size="8" font-weight="bold" fill="#818cf8">MHD IMPEDANCE MATCHING</text>
            <text x="10" y="36" font-family="monospace" font-size="8" fill="#94a3b8">Alfvén Speed: vA = 480 km/s</text>
            <text x="10" y="52" font-family="monospace" font-size="8" fill="#94a3b8">Radiation Load: ZA = 18.2 Ω</text>
            <text x="10" y="68" font-family="monospace" font-size="8" fill="#94a3b8">Coupled Power: P_wave = 45 kW</text>
            <line x1="10" y1="78" x2="175" y2="78" stroke="#334155" stroke-width="0.8" />
            <text x="10" y="94" font-family="monospace" font-size="8" font-weight="bold" fill="#34d399">MOMENTUM SINK: PLANET CORE</text>
        </g>
    """

def art_582():
    """Lorentz Force Orbit Modification & Charged Spacecraft Dynamics"""
    return """
        <!-- Central Planet Earth -->
        <g transform="translate(500, 300)">
            <circle cx="0" cy="0" r="85" fill="#0b1b36" stroke="#0ea5e9" stroke-width="1.8" />
            <ellipse cx="0" cy="0" rx="85" ry="24" fill="none" stroke="#334155" stroke-width="1" stroke-dasharray="4,4" />
            <text x="0" y="4" font-family="monospace" font-size="9" font-weight="bold" fill="#38bdf8" text-anchor="middle">PLANET CORE</text>
            <line x1="0" y1="-105" x2="0" y2="105" stroke="#f43f5e" stroke-width="1.2" stroke-dasharray="4,2" />
            <text x="0" y="-112" font-family="monospace" font-size="8" fill="#f43f5e" text-anchor="middle">SPIN AXIS</text>
        </g>

        <!-- Initial Orbital Plane (Tilted 3D Ellipse) -->
        <ellipse cx="500" cy="300" rx="280" ry="90" fill="none" stroke="#38bdf8" stroke-width="1.5" transform="rotate(-20 500 300)" />
        <!-- Precessed Orbital Plane (Nodal Shifted) -->
        <ellipse cx="500" cy="300" rx="280" ry="90" fill="none" stroke="#a855f7" stroke-width="1.5" stroke-dasharray="5,4" transform="rotate(-5 500 300)" />

        <!-- Nodal Precession Indicator Arrow -->
        <path d="M 740 210 Q 770 230 760 260" fill="none" stroke="#34d399" stroke-width="2" marker-end="url(#arrow-green)" />
        <text x="770" y="240" font-family="monospace" font-size="8" font-weight="bold" fill="#34d399">ΔΩ = +1.84° / mo</text>

        <!-- Spacecraft at Ascending Node (+q Charge) -->
        <g transform="translate(720, 210)">
            <rect x="-18" y="-10" width="36" height="20" rx="2" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5" />
            <circle cx="0" cy="0" r="24" fill="#f59e0b" fill-opacity="0.15" stroke="#f59e0b" stroke-width="1" stroke-dasharray="2,2" />
            <text x="0" y="3" font-family="monospace" font-size="8" font-weight="bold" fill="#f59e0b" text-anchor="middle">+45 kV</text>
            <!-- Out-of-plane Lorentz Force Vector (Fz) -->
            <line x1="0" y1="-10" x2="0" y2="-45" stroke="#34d399" stroke-width="2.2" marker-end="url(#arrow-green)" />
            <text x="6" y="-30" font-family="monospace" font-size="8" font-weight="bold" fill="#34d399">+Fz (Out-of-Plane)</text>
        </g>

        <!-- Spacecraft at Descending Node (-q Charge) -->
        <g transform="translate(280, 390)">
            <rect x="-18" y="-10" width="36" height="20" rx="2" fill="#0f172a" stroke="#0ea5e9" stroke-width="1.5" />
            <circle cx="0" cy="0" r="24" fill="#0ea5e9" fill-opacity="0.15" stroke="#0ea5e9" stroke-width="1" stroke-dasharray="2,2" />
            <text x="0" y="3" font-family="monospace" font-size="8" font-weight="bold" fill="#38bdf8" text-anchor="middle">-45 kV</text>
            <!-- Out-of-plane Lorentz Force Vector (-Fz) -->
            <line x1="0" y1="10" x2="0" y2="45" stroke="#34d399" stroke-width="2.2" marker-end="url(#arrow-green)" />
            <text x="6" y="35" font-family="monospace" font-size="8" font-weight="bold" fill="#34d399">-Fz (Out-of-Plane)</text>
        </g>

        <!-- Technical Annotation Box -->
        <g transform="translate(80, 140)">
            <rect x="0" y="0" width="180" height="75" rx="3" fill="#040e24" stroke="#0ea5e9" stroke-width="0.8" />
            <text x="8" y="16" font-family="monospace" font-size="8" font-weight="bold" fill="#38bdf8">SYNCHRONOUS CHARGE CYCLING</text>
            <text x="8" y="32" font-family="monospace" font-size="8" fill="#94a3b8">q(t) = q0 · sin(ω_orb · t)</text>
            <text x="8" y="48" font-family="monospace" font-size="8" fill="#94a3b8">Lorentz Accel: a_L = (q/m)(v x B)</text>
            <text x="8" y="64" font-family="monospace" font-size="8" font-weight="bold" fill="#34d399">PROPELLANT EXPULSION: 0.00 kg</text>
        </g>
    """

print("First 4 artworks ready.")

def art_583():
    """Spherical Harmonic Geomagnetic Field Modeling (Gauss Coefficients)"""
    return """
        <!-- Earth Globe with Harmonic Multipole Nodal Lines (Left side) -->
        <g transform="translate(240, 300)">
            <!-- Outer Atmosphere Glow -->
            <circle cx="0" cy="0" r="130" fill="#6366f1" fill-opacity="0.05" stroke="#6366f1" stroke-width="1" stroke-dasharray="4,4" />
            <!-- Earth Body -->
            <circle cx="0" cy="0" r="110" fill="#0b1b36" stroke="#6366f1" stroke-width="2" />
            <!-- Geographic Rotational Axis -->
            <line x1="0" y1="-140" x2="0" y2="140" stroke="#94a3b8" stroke-width="1" stroke-dasharray="5,3" />
            <text x="0" y="-145" font-family="monospace" font-size="8" fill="#94a3b8" text-anchor="middle">GEOGRAPHIC NORTH</text>
            <!-- Geomagnetic Dipole Axis (11.5 deg tilt) -->
            <line x1="-28" y1="-140" x2="28" y2="140" stroke="#f43f5e" stroke-width="1.8" />
            <text x="-32" y="-145" font-family="monospace" font-size="8" font-weight="bold" fill="#f43f5e" text-anchor="end">MAG AXIS (11.5°)</text>
            <!-- Spherical Harmonic Contour Bands (n=1, n=2, n=3 anomalies) -->
            <ellipse cx="0" cy="-35" rx="85" ry="25" fill="none" stroke="#818cf8" stroke-width="1.2" opacity="0.7" />
            <ellipse cx="0" cy="35" rx="85" ry="25" fill="none" stroke="#818cf8" stroke-width="1.2" opacity="0.7" />
            <path d="M -80 0 Q 0 -60 80 0" fill="none" stroke="#fbbf24" stroke-width="1.2" stroke-dasharray="3,3" />
            <text x="0" y="4" font-family="monospace" font-size="9" font-weight="bold" fill="#e2e8f0" text-anchor="middle">IGRF n=13 EXPANSION</text>
            <text x="0" y="20" font-family="monospace" font-size="7" fill="#818cf8" text-anchor="middle">g_n^m, h_n^m Coefficients</text>
        </g>

        <!-- Orbiting Satellite with 3-Axis Fluxgate Boom -->
        <g transform="translate(620, 210)">
            <!-- Spacecraft Bus -->
            <rect x="-24" y="-14" width="48" height="28" rx="3" fill="#0f172a" stroke="#818cf8" stroke-width="1.8" />
            <text x="0" y="3" font-family="monospace" font-size="7" font-weight="bold" fill="#818cf8" text-anchor="middle">NAV SAT</text>
            <!-- Magnetometer Boom Assembly (Extended) -->
            <line x1="24" y1="0" x2="90" y2="0" stroke="#cbd5e1" stroke-width="2" />
            <!-- 3-Axis Fluxgate Sensor Head -->
            <circle cx="90" cy="0" r="7" fill="#f59e0b" stroke="#ffffff" stroke-width="1" />
            <line x1="90" y1="0" x2="115" y2="0" stroke="#f59e0b" stroke-width="1.5" marker-end="url(#arrow-amber)" />
            <text x="118" y="3" font-family="monospace" font-size="7" fill="#fbbf24">Bx</text>
            <line x1="90" y1="0" x2="90" y2="-25" stroke="#38bdf8" stroke-width="1.5" marker-end="url(#arrow-cyan)" />
            <text x="94" y="-23" font-family="monospace" font-size="7" fill="#38bdf8">By</text>
            <line x1="90" y1="0" x2="72" y2="18" stroke="#34d399" stroke-width="1.5" marker-end="url(#arrow-green)" />
            <text x="64" y="27" font-family="monospace" font-size="7" fill="#34d399">Bz</text>
        </g>

        <!-- Real-Time Extended Kalman Filter (EKF) Processing Block -->
        <g transform="translate(560, 310)">
            <rect x="0" y="0" width="260" height="130" rx="4" fill="#040e24" stroke="#6366f1" stroke-width="1.2" />
            <text x="12" y="20" font-family="monospace" font-size="9" font-weight="bold" fill="#818cf8">AVIONICS EKF STATE ESTIMATOR</text>
            <!-- Sensor vs Model Diff -->
            <text x="12" y="40" font-family="monospace" font-size="8" fill="#94a3b8">B_measured: [18.42, -5.14, 27.60] uT</text>
            <text x="12" y="55" font-family="monospace" font-size="8" fill="#94a3b8">B_model(r): [18.41, -5.16, 27.58] uT</text>
            <line x1="12" y1="65" x2="248" y2="65" stroke="#334155" stroke-width="0.8" />
            <text x="12" y="82" font-family="monospace" font-size="8" font-weight="bold" fill="#34d399">RESIDUAL INNOVATION: ΔB = 0.038 µT</text>
            <text x="12" y="98" font-family="monospace" font-size="8" fill="#e2e8f0">1σ AUTONOMOUS POSITION FIX:</text>
            <text x="12" y="116" font-family="monospace" font-size="12" font-weight="bold" fill="#38bdf8">Δr = ± 320 METERS (GPS-FREE)</text>
        </g>
    """

def art_584():
    """McIlwain (B, L) Coordinates & Magnetic Drift Shells"""
    return """
        <!-- Central Terra Dipole (Left) -->
        <g transform="translate(180, 300)">
            <circle cx="0" cy="0" r="90" fill="#0b1b36" stroke="#6366f1" stroke-width="2" />
            <line x1="0" y1="-110" x2="0" y2="110" stroke="#f43f5e" stroke-width="1.5" />
            <text x="0" y="4" font-family="monospace" font-size="10" font-weight="bold" fill="#e2e8f0" text-anchor="middle">EARTH DIPOLE</text>
            <text x="0" y="20" font-family="monospace" font-size="8" fill="#64748b" text-anchor="middle">R_p = 6371 km</text>
        </g>

        <!-- Nested McIlwain Drift Shells in Meridian Plane -->
        <!-- L = 1.5 Shell -->
        <path d="M 180 390 C 270 410 315 360 315 300 C 315 240 270 190 180 210" fill="none" stroke="#38bdf8" stroke-width="1" />
        <text x="320" y="303" font-family="monospace" font-size="7" fill="#38bdf8">L = 1.5</text>

        <!-- L = 2.5 Shell -->
        <path d="M 180 405 C 380 440 450 380 450 300 C 450 220 380 160 180 195" fill="none" stroke="#818cf8" stroke-width="1.5" />
        <text x="455" y="303" font-family="monospace" font-size="8" font-weight="bold" fill="#818cf8">L = 2.5</text>

        <!-- L = 4.25 Shell (Target Invariant Drift Corridor) -->
        <path d="M 180 420 C 540 480 640 400 640 300 C 640 200 540 120 180 180" fill="none" stroke="#34d399" stroke-width="2.5" />
        <text x="648" y="304" font-family="monospace" font-size="9" font-weight="bold" fill="#34d399">L = 4.25 (DRIFT CORRIDOR)</text>

        <!-- Three Adiabatic Invariants Demonstration Box -->
        <g transform="translate(680, 140)">
            <rect x="0" y="0" width="240" height="200" rx="4" fill="#040e24" stroke="#818cf8" stroke-width="1.2" />
            <text x="12" y="20" font-family="monospace" font-size="9" font-weight="bold" fill="#818cf8">ADIABATIC MOTION INVARIANTS</text>
            <!-- 1st Invariant: Gyro-motion -->
            <circle cx="25" cy="48" r="10" fill="none" stroke="#38bdf8" stroke-width="1.5" />
            <text x="45" y="46" font-family="monospace" font-size="8" font-weight="bold" fill="#38bdf8">1. FIRST INVARIANT (u)</text>
            <text x="45" y="58" font-family="monospace" font-size="7" fill="#94a3b8">r_g = 14.2 m | Gyro-frequency = 18 kHz</text>
            <!-- 2nd Invariant: Bounce Motion -->
            <path d="M 20 90 Q 25 105 20 120" fill="none" stroke="#f59e0b" stroke-width="1.8" />
            <text x="45" y="98" font-family="monospace" font-size="8" font-weight="bold" fill="#f59e0b">2. SECOND INVARIANT (J)</text>
            <text x="45" y="110" font-family="monospace" font-size="7" fill="#94a3b8">f_bounce = 2.40 Hz between mirror pts</text>
            <!-- 3rd Invariant: Drift Shell -->
            <ellipse cx="25" cy="155" rx="12" ry="6" fill="none" stroke="#34d399" stroke-width="1.8" />
            <text x="45" y="150" font-family="monospace" font-size="8" font-weight="bold" fill="#34d399">3. THIRD INVARIANT (Φ)</text>
            <text x="45" y="162" font-family="monospace" font-size="7" fill="#94a3b8">T_drift = 12.8 min Azimuthal Ring</text>
            <line x1="12" y1="174" x2="228" y2="174" stroke="#334155" stroke-width="0.8" />
            <text x="12" y="190" font-family="monospace" font-size="8" font-weight="bold" fill="#38bdf8">ORBIT DETERMINATION: L-STABLE</text>
        </g>
    """

def art_585():
    """Magnetopause & Bow Shock Boundary Triangulation"""
    return """
        <!-- Macro Magnetospheric Structure Overview -->
        <!-- Supersonic Solar Wind (Left) -->
        <g stroke="#38bdf8" stroke-width="1" opacity="0.5">
            <line x1="40" y1="150" x2="220" y2="150" marker-end="url(#arrow-cyan)" />
            <line x1="40" y1="300" x2="220" y2="300" marker-end="url(#arrow-cyan)" />
            <line x1="40" y1="450" x2="220" y2="450" marker-end="url(#arrow-cyan)" />
        </g>
        <text x="50" y="135" font-family="monospace" font-size="8" font-weight="bold" fill="#38bdf8">SOLAR WIND (M_A = 8.2)</text>

        <!-- Sharp Bow Shock Discontinuity Front -->
        <path d="M 280 80 Q 200 300 280 520" fill="none" stroke="#f43f5e" stroke-width="2.5" />
        <text x="180" y="305" font-family="monospace" font-size="9" font-weight="bold" fill="#f43f5e" transform="rotate(-90 180 305)">BOW SHOCK JUMP</text>

        <!-- Magnetosheath Turbulent Transition Zone -->
        <path d="M 280 80 Q 200 300 280 520 L 400 500 Q 330 300 400 100 Z" fill="#6366f1" fill-opacity="0.12" stroke="none" />
        <text x="290" y="160" font-family="monospace" font-size="8" fill="#818cf8">MAGNETOSHEATH</text>

        <!-- Magnetopause Boundary Layer -->
        <path d="M 400 100 Q 330 300 400 500" fill="none" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4,2" />
        <text x="390" y="470" font-family="monospace" font-size="8" font-weight="bold" fill="#38bdf8">MAGNETOPAUSE (B_int^2/2u0 = P_sw)</text>

        <!-- Multi-Point Probe In-Situ Measurement Graph (HUD Display) -->
        <g transform="translate(540, 180)">
            <rect x="0" y="0" width="380" height="240" rx="4" fill="#040e24" stroke="#6366f1" stroke-width="1.2" />
            <text x="14" y="24" font-family="monospace" font-size="10" font-weight="bold" fill="#818cf8">RANKINE-HUGONIOT JUMP TELEMETRY</text>
            <!-- Graph 1: Plasma Density -->
            <text x="14" y="55" font-family="monospace" font-size="8" fill="#94a3b8">ION DENSITY (cm^-3): Upstream 7.1 -> Downstream 27.3</text>
            <path d="M 14 85 L 120 85 L 140 65 L 360 65" fill="none" stroke="#38bdf8" stroke-width="2" />
            <text x="280" y="60" font-family="monospace" font-size="8" font-weight="bold" fill="#38bdf8">3.84x JUMP</text>
            <!-- Graph 2: Magnetic Field B -->
            <text x="14" y="115" font-family="monospace" font-size="8" fill="#94a3b8">B-FIELD MAGNITUDE (nT): IMF 4.8 nT -> Sheath 16.9 nT</text>
            <path d="M 14 145 L 120 145 L 140 125 L 360 125" fill="none" stroke="#f59e0b" stroke-width="2" />
            <text x="280" y="120" font-family="monospace" font-size="8" font-weight="bold" fill="#f59e0b">3.52x COMPRESSION</text>
            <!-- Triangulation Output -->
            <line x1="14" y1="165" x2="366" y2="165" stroke="#334155" stroke-width="0.8" />
            <text x="14" y="185" font-family="monospace" font-size="8" font-weight="bold" fill="#34d399">BOUNDARY NORMAL: n_shk = [0.942, -0.210, 0.261]</text>
            <text x="14" y="205" font-family="monospace" font-size="8" fill="#e2e8f0">STANDOFF TRIANGULATION ACCURACY:</text>
            <text x="14" y="225" font-family="monospace" font-size="12" font-weight="bold" fill="#34d399">± 12.4 km RELATIVE TO PLANET CENTER</text>
        </g>
    """

def art_586():
    """X-Ray Pulsar Navigation (XPNAV) & Barycentric Coordinate Timing"""
    return """
        <!-- Solar System Barycenter (SSB) at Coordinate Origin -->
        <g transform="translate(180, 300)">
            <!-- Spacetime Metric Grid -->
            <circle cx="0" cy="0" r="12" fill="#f59e0b" stroke="#ffffff" stroke-width="1.5" />
            <text x="0" y="24" font-family="monospace" font-size="9" font-weight="bold" fill="#fbbf24" text-anchor="middle">SOLAR SYSTEM BARYCENTER (SSB)</text>
            <circle cx="0" cy="0" r="70" fill="none" stroke="#334155" stroke-width="0.8" stroke-dasharray="3,3" />
            <text x="0" y="78" font-family="monospace" font-size="7" fill="#64748b" text-anchor="middle">Earth Orbit (1.0 AU)</text>
        </g>

        <!-- Spacecraft Position Vector r (Center-Right) -->
        <g transform="translate(540, 240)">
            <rect x="-24" y="-14" width="48" height="28" rx="3" fill="#0f172a" stroke="#818cf8" stroke-width="1.8" />
            <text x="0" y="3" font-family="monospace" font-size="8" font-weight="bold" fill="#818cf8" text-anchor="middle">XPNAV CRAFT</text>
            <!-- X-Ray Grazing Incidence Collimator -->
            <path d="M -24 0 L -45 -12 L -45 12 Z" fill="#0284c7" fill-opacity="0.5" stroke="#38bdf8" stroke-width="1" />
            <text x="-48" y="-16" font-family="monospace" font-size="7" fill="#38bdf8">X-RAY OPTIC</text>
        </g>
        <!-- Barycentric Position Vector arrow (SSB to Craft) -->
        <line x1="180" y1="300" x2="516" y2="240" stroke="#38bdf8" stroke-width="1.8" marker-end="url(#arrow-cyan)" />
        <text x="340" y="260" font-family="monospace" font-size="8" font-weight="bold" fill="#38bdf8">r_craft (SSB Vector)</text>

        <!-- Millisecond Pulsar Lines-of-Sight (Pulsar Beams incoming) -->
        <!-- Pulsar 1: PSR B1937+21 -->
        <line x1="880" y1="80" x2="564" y2="230" stroke="#a855f7" stroke-width="1.5" stroke-dasharray="4,2" marker-end="url(#arrow-purple)" />
        <text x="890" y="85" font-family="monospace" font-size="8" font-weight="bold" fill="#c084fc">PSR B1937+21 (P = 1.55 ms)</text>

        <!-- Pulsar 2: PSR B1821-24 -->
        <line x1="880" y1="260" x2="564" y2="245" stroke="#34d399" stroke-width="1.5" stroke-dasharray="4,2" marker-end="url(#arrow-green)" />
        <text x="890" y="265" font-family="monospace" font-size="8" font-weight="bold" fill="#34d399">PSR B1821-24 (P = 3.05 ms)</text>

        <!-- Pulsar 3: Crab Pulsar -->
        <line x1="880" y1="420" x2="564" y2="260" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="4,2" marker-end="url(#arrow-amber)" />
        <text x="890" y="425" font-family="monospace" font-size="8" font-weight="bold" fill="#fbbf24">PSR B0531+21 (Crab)</text>

        <!-- Relativistic Timing Correction Box -->
        <g transform="translate(140, 420)">
            <rect x="0" y="0" width="380" height="90" rx="3" fill="#040e24" stroke="#818cf8" stroke-width="1" />
            <text x="12" y="20" font-family="monospace" font-size="9" font-weight="bold" fill="#818cf8">BARYCENTRIC RELATIVISTIC TIMING</text>
            <text x="12" y="38" font-family="monospace" font-size="8" fill="#94a3b8">t_SSB = t_arr + (n · r)/c + Δt_Shapiro + Δt_Einstein</text>
            <text x="12" y="54" font-family="monospace" font-size="8" fill="#94a3b8">Photon Timing Jitter: ± 1.5 ns | Stability: 10^-15</text>
            <line x1="12" y1="62" x2="368" y2="62" stroke="#334155" stroke-width="0.8" />
            <text x="12" y="78" font-family="monospace" font-size="9" font-weight="bold" fill="#34d399">ABSOLUTE 3D TRIANGULATION: Δx = 285 METERS</text>
        </g>
    """

print("Phase II artworks ready.")

def art_587():
    """Bioelectromagnetics & Cellular Membrane Voltage Potentials"""
    return """
        <!-- Cellular Lipid Bilayer Membrane Cross-Section (5 nm scale) -->
        <!-- Extracellular Space (Top, V = 0 mV) -->
        <rect x="100" y="100" width="800" height="80" fill="#0284c7" fill-opacity="0.08" stroke="none" />
        <text x="120" y="130" font-family="monospace" font-size="9" font-weight="bold" fill="#38bdf8">EXTRACELLULAR FLUID (V = 0 mV)</text>
        <text x="120" y="150" font-family="monospace" font-size="8" fill="#94a3b8">[Na+] = 145 mM | [K+] = 4.0 mM | [Cl-] = 110 mM</text>

        <!-- Phospholipid Bilayer -->
        <!-- Outer Leaflet (Polar Heads) -->
        <g fill="#a855f7" stroke="#c084fc" stroke-width="0.5">
            <circle cx="120" cy="190" r="7" /><circle cx="140" cy="190" r="7" /><circle cx="160" cy="190" r="7" /><circle cx="180" cy="190" r="7" />
            <circle cx="200" cy="190" r="7" /><circle cx="220" cy="190" r="7" /><circle cx="240" cy="190" r="7" /><circle cx="260" cy="190" r="7" />
            <circle cx="380" cy="190" r="7" /><circle cx="400" cy="190" r="7" /><circle cx="420" cy="190" r="7" /><circle cx="440" cy="190" r="7" />
            <circle cx="560" cy="190" r="7" /><circle cx="580" cy="190" r="7" /><circle cx="600" cy="190" r="7" /><circle cx="620" cy="190" r="7" />
            <circle cx="740" cy="190" r="7" /><circle cx="760" cy="190" r="7" /><circle cx="780" cy="190" r="7" /><circle cx="800" cy="190" r="7" />
        </g>
        <!-- Hydrophobic Tail Region (5 nm Core) -->
        <rect x="100" y="197" width="800" height="56" fill="#1e1b4b" stroke="none" />
        <!-- Electric Field Gradient Vectors (Pointing from Outer to Inner) -->
        <g stroke="#f43f5e" stroke-width="1.8" marker-end="url(#arrow-red)">
            <line x1="220" y1="202" x2="220" y2="248" />
            <line x1="410" y1="202" x2="410" y2="248" />
            <line x1="590" y1="202" x2="590" y2="248" />
            <line x1="770" y1="202" x2="770" y2="248" />
        </g>
        <text x="430" y="230" font-family="monospace" font-size="8" font-weight="bold" fill="#f43f5e">E_mem = 1.41 x 10^7 V/m</text>

        <!-- Inner Leaflet (Polar Heads) -->
        <g fill="#a855f7" stroke="#c084fc" stroke-width="0.5">
            <circle cx="120" cy="260" r="7" /><circle cx="140" cy="260" r="7" /><circle cx="160" cy="260" r="7" /><circle cx="180" cy="260" r="7" />
            <circle cx="200" cy="260" r="7" /><circle cx="220" cy="260" r="7" /><circle cx="240" cy="260" r="7" /><circle cx="260" cy="260" r="7" />
            <circle cx="380" cy="260" r="7" /><circle cx="400" cy="260" r="7" /><circle cx="420" cy="260" r="7" /><circle cx="440" cy="260" r="7" />
            <circle cx="560" cy="260" r="7" /><circle cx="580" cy="260" r="7" /><circle cx="600" cy="260" r="7" /><circle cx="620" cy="260" r="7" />
            <circle cx="740" cy="260" r="7" /><circle cx="760" cy="260" r="7" /><circle cx="780" cy="260" r="7" /><circle cx="800" cy="260" r="7" />
        </g>

        <!-- Embedded Ion Channels -->
        <!-- K+ Leak Channel -->
        <g transform="translate(320, 225)">
            <rect x="-25" y="-45" width="50" height="90" rx="6" fill="#047857" stroke="#34d399" stroke-width="1.5" />
            <text x="0" y="4" font-family="monospace" font-size="7" font-weight="bold" fill="#ffffff" text-anchor="middle">K+ PORE</text>
            <line x1="0" y1="35" x2="0" y2="-35" stroke="#34d399" stroke-width="2" marker-end="url(#arrow-green)" />
            <text x="0" y="-50" font-family="monospace" font-size="7" fill="#34d399" text-anchor="middle">K+ EFFLUX</text>
        </g>
        <!-- Na+/K+ ATPase Pump -->
        <g transform="translate(500, 225)">
            <rect x="-30" y="-45" width="60" height="90" rx="6" fill="#1d4ed8" stroke="#38bdf8" stroke-width="1.5" />
            <text x="0" y="-10" font-family="monospace" font-size="7" font-weight="bold" fill="#ffffff" text-anchor="middle">Na+/K+ PUMP</text>
            <text x="0" y="8" font-family="monospace" font-size="6" fill="#fde68a" text-anchor="middle">ATP -> ADP + Pi</text>
            <text x="0" y="24" font-family="monospace" font-size="7" fill="#93c5fd" text-anchor="middle">3 Na+ out / 2 K+ in</text>
        </g>
        <!-- Voltage-Gated Ca2+ Channel -->
        <g transform="translate(680, 225)">
            <rect x="-25" y="-45" width="50" height="90" rx="6" fill="#b45309" stroke="#f59e0b" stroke-width="1.5" />
            <text x="0" y="4" font-family="monospace" font-size="7" font-weight="bold" fill="#ffffff" text-anchor="middle">Ca2+ GATE</text>
            <text x="0" y="-50" font-family="monospace" font-size="7" fill="#fbbf24" text-anchor="middle">B-SENSITIVE</text>
        </g>

        <!-- Intracellular Cytoplasm (Bottom, V = -70.4 mV) -->
        <rect x="100" y="275" width="800" height="90" fill="#a855f7" fill-opacity="0.08" stroke="none" />
        <text x="120" y="305" font-family="monospace" font-size="9" font-weight="bold" fill="#c084fc">INTRACELLULAR CYTOPLASM (RESTING POTENTIAL: V_m = -70.4 mV)</text>
        <text x="120" y="325" font-family="monospace" font-size="8" fill="#94a3b8">[K+] = 140 mM | [Na+] = 12 mM | GHK EQUILIBRIUM: P_K / P_Na = 25:1</text>

        <!-- Voltage Gradient Curve HUD (Right Bottom) -->
        <g transform="translate(240, 390)">
            <rect x="0" y="0" width="520" height="110" rx="4" fill="#040e24" stroke="#a855f7" stroke-width="1.2" />
            <text x="14" y="22" font-family="monospace" font-size="9" font-weight="bold" fill="#c084fc">GOLDMAN-HODGKIN-KATZ TRANSMEMBRANE VOLTAGE</text>
            <line x1="20" y1="45" x2="160" y2="45" stroke="#38bdf8" stroke-width="2" />
            <path d="M 160 45 L 260 85 L 500 85" fill="none" stroke="#f43f5e" stroke-width="2.2" />
            <text x="40" y="40" font-family="monospace" font-size="8" fill="#38bdf8">V_ext = 0.0 mV</text>
            <text x="320" y="80" font-family="monospace" font-size="9" font-weight="bold" fill="#f43f5e">V_m = -70.4 mV DC (NOMINAL RESTING)</text>
            <text x="14" y="100" font-family="monospace" font-size="8" fill="#34d399">HYPOMAGNETIC STRESS MITIGATION: Transmembrane Potential Maintained</text>
        </g>
    """

def art_588():
    """Cryptochrome Magnetoreception & Quantum Biology in Humans"""
    return """
        <!-- Cryptochrome 2 (hCRY2) Protein Cavity & Radical Pair Mechanism -->
        <!-- Protein Globular Structure Boundary -->
        <path d="M 120 280 C 120 140 280 100 480 110 C 680 120 840 180 840 320 C 840 460 660 500 460 490 C 260 480 120 420 120 280 Z" fill="#3b0764" fill-opacity="0.15" stroke="#a855f7" stroke-width="1.5" stroke-dasharray="6,4" />
        <text x="160" y="145" font-family="monospace" font-size="9" font-weight="bold" fill="#c084fc">HUMAN CRYPTOCHROME 2 (hCRY2) ACTIVE SITE</text>

        <!-- Blue Light Photon Absorption (450 nm) -->
        <line x1="60" y1="200" x2="260" y2="250" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#arrow-cyan)" />
        <text x="60" y="185" font-family="monospace" font-size="9" font-weight="bold" fill="#38bdf8">BLUE PHOTON hv (450 nm)</text>

        <!-- FAD Cofactor (Flavin Ring, Electron Acceptor) -->
        <g transform="translate(290, 260)">
            <rect x="-35" y="-25" width="70" height="50" rx="4" fill="#1e1b4b" stroke="#f59e0b" stroke-width="2" />
            <text x="0" y="0" font-family="monospace" font-size="9" font-weight="bold" fill="#fbbf24" text-anchor="middle">FAD</text>
            <text x="0" y="14" font-family="monospace" font-size="8" fill="#fde68a" text-anchor="middle">[FAD•-] RADICAL</text>
        </g>

        <!-- Electron Hopping Tunneling Path (Tryptophan Triad TrpA -> TrpB -> TrpC) -->
        <path d="M 330 260 Q 420 240 510 260" fill="none" stroke="#38bdf8" stroke-width="2" stroke-dasharray="3,3" />
        <text x="420" y="240" font-family="monospace" font-size="8" fill="#38bdf8" text-anchor="middle">e- TUNNELING (1.85 nm)</text>

        <!-- Tryptophan Triad Terminal Residue (TrpH+, Electron Donor) -->
        <g transform="translate(540, 260)">
            <rect x="-35" y="-25" width="70" height="50" rx="4" fill="#1e1b4b" stroke="#34d399" stroke-width="2" />
            <text x="0" y="0" font-family="monospace" font-size="9" font-weight="bold" fill="#34d399" text-anchor="middle">Trp-C</text>
            <text x="0" y="14" font-family="monospace" font-size="8" fill="#a7f3d0" text-anchor="middle">[TrpH•+] RADICAL</text>
        </g>

        <!-- External Geomagnetic Field Vector B_ext modulating quantum spin -->
        <g transform="translate(420, 150)">
            <line x1="0" y1="40" x2="0" y2="0" stroke="#f43f5e" stroke-width="2.5" marker-end="url(#arrow-red)" />
            <text x="8" y="20" font-family="monospace" font-size="8" font-weight="bold" fill="#f43f5e">B_ext (50 uT)</text>
            <text x="8" y="32" font-family="monospace" font-size="7" fill="#fca5a5">Zeeman Splitting</text>
        </g>

        <!-- Quantum Spin State Oscillation Box (Singlet <-> Triplet) -->
        <g transform="translate(240, 360)">
            <rect x="0" y="0" width="380" height="110" rx="4" fill="#040e24" stroke="#c084fc" stroke-width="1.2" />
            <text x="14" y="22" font-family="monospace" font-size="9" font-weight="bold" fill="#c084fc">QUANTUM RADICAL PAIR SPIN OSCILLATION</text>
            <!-- Singlet State -->
            <rect x="25" y="40" width="90" height="40" rx="3" fill="#1e1b4b" stroke="#38bdf8" stroke-width="1" />
            <text x="70" y="58" font-family="monospace" font-size="9" font-weight="bold" fill="#38bdf8" text-anchor="middle">| S ⟩ SINGLET</text>
            <text x="70" y="72" font-family="monospace" font-size="7" fill="#93c5fd" text-anchor="middle">Spin Total S = 0</text>
            <!-- Oscillation Arrows -->
            <path d="M 125 50 L 165 50" stroke="#fbbf24" stroke-width="2" marker-end="url(#arrow-amber)" />
            <path d="M 165 70 L 125 70" stroke="#fbbf24" stroke-width="2" marker-end="url(#arrow-amber)" />
            <text x="145" y="44" font-family="monospace" font-size="7" fill="#fbbf24" text-anchor="middle">H_int</text>
            <!-- Triplet State -->
            <rect x="175" y="40" width="110" height="40" rx="3" fill="#1e1b4b" stroke="#34d399" stroke-width="1" />
            <text x="230" y="58" font-family="monospace" font-size="9" font-weight="bold" fill="#34d399" text-anchor="middle">| T_0, T_± ⟩ TRIPLET</text>
            <text x="230" y="72" font-family="monospace" font-size="7" fill="#a7f3d0" text-anchor="middle">Spin Total S = 1</text>
            <!-- Yield Output -->
            <text x="295" y="56" font-family="monospace" font-size="8" font-weight="bold" fill="#e2e8f0">Δ YIELD: 1.8%</text>
            <text x="295" y="72" font-family="monospace" font-size="7" fill="#38bdf8">Circadian Trigger</text>
            <line x1="14" y1="88" x2="366" y2="88" stroke="#334155" stroke-width="0.8" />
            <text x="14" y="102" font-family="monospace" font-size="8" font-weight="bold" fill="#34d399">COHERENCE LIFETIME: τ = 1.95 µs (IN-VIVO DEMONSTRATED)</text>
        </g>
    """

def art_589():
    """Van Allen Belts Dosimetry & Active Superconducting Shields"""
    return """
        <!-- Van Allen Belt Geometry (Proton and Electron Belts) -->
        <g transform="translate(180, 300)">
            <circle cx="0" cy="0" r="60" fill="#0b1b36" stroke="#0ea5e9" stroke-width="1.8" />
            <text x="0" y="4" font-family="monospace" font-size="8" font-weight="bold" fill="#38bdf8" text-anchor="middle">EARTH</text>
            <!-- Inner Belt (Protons 10-100 MeV) -->
            <path d="M 0 -100 C 90 -100 120 0 120 0 C 120 0 90 100 0 100" fill="none" stroke="#f43f5e" stroke-width="14" opacity="0.4" />
            <text x="135" y="-30" font-family="monospace" font-size="7" font-weight="bold" fill="#f43f5e">INNER BELT (100 MeV p+)</text>
            <!-- Outer Belt (Relativistic Electrons) -->
            <path d="M 0 -150 C 160 -150 200 0 200 0 C 200 0 160 150 0 150" fill="none" stroke="#38bdf8" stroke-width="18" opacity="0.25" />
            <text x="210" y="50" font-family="monospace" font-size="7" font-weight="bold" fill="#38bdf8">OUTER BELT (e-)</text>
        </g>

        <!-- Spacecraft Habitat with Active Superconducting Shield (Right side) -->
        <g transform="translate(640, 300)">
            <!-- Outer Deflection Magnetic Flux Field (4.8 Tesla) -->
            <circle cx="0" cy="0" r="130" fill="#3b0764" fill-opacity="0.12" stroke="#a855f7" stroke-width="1.5" stroke-dasharray="6,3" />
            <!-- HTS Toroidal Shield Coils -->
            <ellipse cx="0" cy="-80" rx="45" ry="14" fill="#064e3b" stroke="#34d399" stroke-width="2" />
            <ellipse cx="0" cy="80" rx="45" ry="14" fill="#064e3b" stroke="#34d399" stroke-width="2" />
            <text x="0" y="-76" font-family="monospace" font-size="7" font-weight="bold" fill="#a7f3d0" text-anchor="middle">HTS COIL (4.8 T)</text>
            <text x="0" y="84" font-family="monospace" font-size="7" font-weight="bold" fill="#a7f3d0" text-anchor="middle">HTS COIL (4.8 T)</text>

            <!-- Central Crew Habitat Core (B < 0.05 mT) -->
            <rect x="-40" y="-45" width="80" height="90" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.8" />
            <text x="0" y="-10" font-family="monospace" font-size="8" font-weight="bold" fill="#e2e8f0" text-anchor="middle">CREW</text>
            <text x="0" y="6" font-family="monospace" font-size="8" font-weight="bold" fill="#e2e8f0" text-anchor="middle">HABITAT</text>
            <text x="0" y="24" font-family="monospace" font-size="7" font-weight="bold" fill="#34d399" text-anchor="middle">B &lt; 0.045 mT</text>
        </g>

        <!-- Incident Relativistic Proton Deflection Trajectory -->
        <g>
            <path d="M 420 180 Q 510 200 520 240 Q 530 280 430 330" fill="none" stroke="#f43f5e" stroke-width="2.8" marker-mid="url(#arrow-red)" />
            <text x="390" y="165" font-family="monospace" font-size="8" font-weight="bold" fill="#f43f5e">100 MeV PROTON (INCIDENT)</text>
            <text x="360" y="350" font-family="monospace" font-size="8" font-weight="bold" fill="#34d399">LARMOR DEFLECTION (rg = 0.82 m)</text>
        </g>

        <!-- Dosimetry Protection Metric HUD -->
        <g transform="translate(640, 110)">
            <rect x="-90" y="0" width="180" height="44" rx="3" fill="#040e24" stroke="#34d399" stroke-width="0.8" />
            <text x="0" y="16" font-family="monospace" font-size="8" font-weight="bold" fill="#34d399" text-anchor="middle">BREMSSTRAHLUNG EMISSION: 0.00%</text>
            <text x="0" y="32" font-family="monospace" font-size="7" fill="#94a3b8" text-anchor="middle">Pure Magnetic Momentum Deflection</text>
        </g>
    """

def art_590():
    """Hypomagnetic Stress & Biological Frequency Conditioning"""
    return """
        <!-- Split Panel Layout: Left = Hypomagnetic Decay; Right = Synthesized Envelope -->
        <!-- Center Divider -->
        <line x1="500" y1="100" x2="500" y2="510" stroke="#334155" stroke-width="1.5" stroke-dasharray="4,4" />

        <!-- LEFT PANEL: Deep Space Hypomagnetic Field (< 0.4 nT) -->
        <g transform="translate(80, 120)">
            <rect x="0" y="0" width="380" height="70" rx="3" fill="#450a0a" fill-opacity="0.3" stroke="#f43f5e" stroke-width="1" />
            <text x="14" y="22" font-family="monospace" font-size="9" font-weight="bold" fill="#f43f5e">ENVIRONMENT: DEEP SPACE HYPOMAGNETIC</text>
            <text x="14" y="40" font-family="monospace" font-size="8" fill="#fca5a5">Ambient Flux Density: B &lt; 0.4 nT (Magnetic Void)</text>
            <text x="14" y="56" font-family="monospace" font-size="8" font-weight="bold" fill="#f87171">PATHOLOGY: Rapid Osteoblast Demineralization</text>

            <!-- Disrupted Waveform (Flat zero line with noise) -->
            <path d="M 20 120 L 360 120" stroke="#64748b" stroke-width="1.5" stroke-dasharray="2,2" />
            <text x="20" y="105" font-family="monospace" font-size="8" fill="#94a3b8">B_ambient = ~0 nT (Zero Schumann Resonance)</text>

            <!-- Bone Mineralization Loss Graph -->
            <rect x="0" y="150" width="380" height="110" rx="3" fill="#040e24" stroke="#334155" stroke-width="0.8" />
            <text x="14" y="172" font-family="monospace" font-size="8" font-weight="bold" fill="#f87171">CALCIUM EFFLUX RATE: -4.2% / MONTH</text>
            <line x1="20" y1="210" x2="360" y2="245" stroke="#f43f5e" stroke-width="2.5" />
            <text x="240" y="235" font-family="monospace" font-size="8" fill="#fca5a5">Severe Skeletal Decay</text>
        </g>

        <!-- RIGHT PANEL: Synthesized Habitat Bio-Conditioning System -->
        <g transform="translate(540, 120)">
            <rect x="0" y="0" width="380" height="70" rx="3" fill="#064e3b" fill-opacity="0.3" stroke="#34d399" stroke-width="1" />
            <text x="14" y="22" font-family="monospace" font-size="9" font-weight="bold" fill="#34d399">CONDITIONED HABITAT ENVELOPE</text>
            <text x="14" y="40" font-family="monospace" font-size="8" fill="#a7f3d0">Synthesized DC Base: 50.0 uT (Terra-Equivalent)</text>
            <text x="14" y="56" font-family="monospace" font-size="8" font-weight="bold" fill="#38bdf8">SUPERIMPOSED: 7.83 Hz Schumann ELF Sine Pulse</text>

            <!-- 7.83 Hz Sine Waveform Graphic -->
            <path d="M 20 120 Q 55 90 90 120 T 160 120 T 230 120 T 300 120 T 360 120" fill="none" stroke="#38bdf8" stroke-width="2.5" />
            <text x="20" y="105" font-family="monospace" font-size="8" font-weight="bold" fill="#38bdf8">f1 = 7.83 Hz IONOSPHERIC CLOCK SYNCHRONY</text>

            <!-- Maintained Calcium Retention Graph -->
            <rect x="0" y="150" width="380" height="110" rx="3" fill="#040e24" stroke="#0ea5e9" stroke-width="0.8" />
            <text x="14" y="172" font-family="monospace" font-size="8" font-weight="bold" fill="#34d399">CALCIUM RETENTION: 99.8% STABILIZED</text>
            <line x1="20" y1="210" x2="360" y2="210" stroke="#34d399" stroke-width="2.5" />
            <text x="240" y="200" font-family="monospace" font-size="8" fill="#a7f3d0">Zero Bone Demineralization</text>
        </g>
    """

def art_591():
    """Epigenetics, Genomic Plasticity & Cosmic Speciation"""
    return """
        <!-- DNA Double Helix Structure with Epigenetic Methylation Markers -->
        <g transform="translate(140, 260)">
            <!-- Double Helix Backbone Strands -->
            <path d="M 0 0 Q 60 -50 120 0 T 240 0 T 360 0 T 480 0" fill="none" stroke="#38bdf8" stroke-width="3" />
            <path d="M 0 0 Q 60 50 120 0 T 240 0 T 360 0 T 480 0" fill="none" stroke="#a855f7" stroke-width="3" />
            <!-- Base Pair Rungs -->
            <line x1="60" y1="-25" x2="60" y2="25" stroke="#cbd5e1" stroke-width="1.8" />
            <line x1="120" y1="0" x2="120" y2="0" stroke="#cbd5e1" stroke-width="1.8" />
            <line x1="180" y1="-25" x2="180" y2="25" stroke="#cbd5e1" stroke-width="1.8" />
            <line x1="240" y1="0" x2="240" y2="0" stroke="#cbd5e1" stroke-width="1.8" />
            <line x1="300" y1="-25" x2="300" y2="25" stroke="#cbd5e1" stroke-width="1.8" />
            <line x1="360" y1="0" x2="360" y2="0" stroke="#cbd5e1" stroke-width="1.8" />
            <line x1="420" y1="-25" x2="420" y2="25" stroke="#cbd5e1" stroke-width="1.8" />

            <!-- Methylation Tags (-CH3 flags) -->
            <g transform="translate(60, -35)">
                <circle cx="0" cy="0" r="8" fill="#f59e0b" stroke="#ffffff" stroke-width="1" />
                <text x="0" y="3" font-family="monospace" font-size="7" font-weight="bold" fill="#000000" text-anchor="middle">CH3</text>
            </g>
            <g transform="translate(300, -35)">
                <circle cx="0" cy="0" r="8" fill="#f59e0b" stroke="#ffffff" stroke-width="1" />
                <text x="0" y="3" font-family="monospace" font-size="7" font-weight="bold" fill="#000000" text-anchor="middle">CH3</text>
            </g>
            <text x="240" y="-50" font-family="monospace" font-size="8" font-weight="bold" fill="#fbbf24" text-anchor="middle">DNMT ENZYMATIC METHYLATION</text>
        </g>

        <!-- Incoming Cosmic Ray Iron Ion (HZE track) -->
        <line x1="280" y1="80" x2="400" y2="220" stroke="#f43f5e" stroke-width="3" stroke-dasharray="8,3" marker-end="url(#arrow-red)" />
        <text x="220" y="100" font-family="monospace" font-size="8" font-weight="bold" fill="#f43f5e">HZE 56Fe ION TRACK</text>

        <!-- Tardigrade Dsup Chromatin Shielding Cap -->
        <g transform="translate(400, 220)">
            <ellipse cx="0" cy="0" rx="35" ry="20" fill="#064e3b" fill-opacity="0.8" stroke="#34d399" stroke-width="2" />
            <text x="0" y="3" font-family="monospace" font-size="8" font-weight="bold" fill="#a7f3d0" text-anchor="middle">Dsup PROTEIN</text>
            <text x="0" y="28" font-family="monospace" font-size="7" fill="#34d399" text-anchor="middle">4.2x RADICAL SCAVENGING</text>
        </g>

        <!-- Speciation Population Dynamics HUD -->
        <g transform="translate(650, 160)">
            <rect x="0" y="0" width="270" height="190" rx="4" fill="#040e24" stroke="#a855f7" stroke-width="1.2" />
            <text x="12" y="22" font-family="monospace" font-size="9" font-weight="bold" fill="#c084fc">COSMIC SPECIATION DYNAMICS</text>
            <text x="12" y="42" font-family="monospace" font-size="8" fill="#94a3b8">Δq = u(1-q) - v*q + s*q*(1-q)</text>
            <text x="12" y="60" font-family="monospace" font-size="8" fill="#94a3b8">Mutation Rate: u = 4.2 x 10^-5</text>
            <text x="12" y="78" font-family="monospace" font-size="8" fill="#94a3b8">Selection Intensity: s = 0.15</text>
            <!-- Speciation Curve -->
            <path d="M 12 140 Q 80 135 150 115 T 250 95" fill="none" stroke="#34d399" stroke-width="2.5" />
            <text x="12" y="160" font-family="monospace" font-size="8" font-weight="bold" fill="#34d399">HOMO CELESTIALIS DIVERGENCE</text>
            <text x="12" y="178" font-family="monospace" font-size="7" fill="#cbd5e1">Generational Adaptive Plasticity</text>
        </g>
    """

print("Phase III artworks ready.")

def art_592():
    """High-Temperature Superconducting (HTS) Coils & Cryogenic Management"""
    return """
        <!-- REBCO 2G-HTS Superconducting Tape Layer Architecture (Left) -->
        <g transform="translate(100, 160)">
            <text x="0" y="-20" font-family="monospace" font-size="9" font-weight="bold" fill="#34d399">REBCO COATED CONDUCTOR TAPE ARCHITECTURE</text>
            <!-- Copper Stabilizer Layer Top (20 um) -->
            <rect x="0" y="0" width="340" height="24" fill="#b45309" stroke="#f59e0b" stroke-width="1" />
            <text x="170" y="16" font-family="monospace" font-size="8" font-weight="bold" fill="#fde68a" text-anchor="middle">COPPER STABILIZER CLADDING (20 µm)</text>
            <!-- Silver Overlayer (2 um) -->
            <rect x="0" y="24" width="340" height="10" fill="#94a3b8" stroke="#cbd5e1" stroke-width="0.8" />
            <text x="170" y="32" font-family="monospace" font-size="6" fill="#000000" text-anchor="middle">SILVER CAPPING LAYER (2 µm)</text>
            <!-- REBCO Superconducting Layer (1 um, 1.4 x 10^5 A/cm^2) -->
            <rect x="0" y="34" width="340" height="14" fill="#059669" stroke="#34d399" stroke-width="1.2" />
            <text x="170" y="44" font-family="monospace" font-size="8" font-weight="bold" fill="#ffffff" text-anchor="middle">REBCO (GdBa2Cu3O7) HTS EPITAXIAL FILM (1 µm)</text>
            <!-- Buffer Stack (0.5 um) -->
            <rect x="0" y="48" width="340" height="10" fill="#6366f1" stroke="#818cf8" stroke-width="0.8" />
            <text x="170" y="56" font-family="monospace" font-size="6" fill="#ffffff" text-anchor="middle">BUFFER STACK: CeO2 / YSZ / IBAD-MgO</text>
            <!-- Hastelloy Substrate (50 um) -->
            <rect x="0" y="58" width="340" height="36" fill="#1e293b" stroke="#475569" stroke-width="1" />
            <text x="170" y="80" font-family="monospace" font-size="8" font-weight="bold" fill="#cbd5e1" text-anchor="middle">HASTELLOY C-276 STRUCTURAL SUBSTRATE (50 µm)</text>
            <!-- Copper Stabilizer Layer Bottom (20 um) -->
            <rect x="0" y="94" width="340" height="24" fill="#b45309" stroke="#f59e0b" stroke-width="1" />
            <text x="170" y="110" font-family="monospace" font-size="8" font-weight="bold" fill="#fde68a" text-anchor="middle">COPPER STABILIZER CLADDING (20 µm)</text>
        </g>

        <!-- Double Pancake Superconducting Coil Assembly (Right) -->
        <g transform="translate(560, 160)">
            <rect x="0" y="-10" width="360" height="170" rx="4" fill="#040e24" stroke="#34d399" stroke-width="1.2" />
            <text x="14" y="16" font-family="monospace" font-size="9" font-weight="bold" fill="#34d399">DOUBLE PANCAKE COIL & CRYOCOOLER LOOP</text>
            <!-- Coil Ring Graphic -->
            <ellipse cx="80" cy="80" rx="55" ry="35" fill="none" stroke="#34d399" stroke-width="6" />
            <ellipse cx="80" cy="80" rx="35" ry="20" fill="none" stroke="#10b981" stroke-width="4" />
            <text x="80" y="84" font-family="monospace" font-size="8" font-weight="bold" fill="#a7f3d0" text-anchor="middle">I = 3,500 A</text>

            <!-- Reverse-Brayton Cryocooler Block -->
            <rect x="180" y="40" width="160" height="90" rx="3" fill="#0f172a" stroke="#0ea5e9" stroke-width="1" />
            <text x="190" y="60" font-family="monospace" font-size="8" font-weight="bold" fill="#38bdf8">REVERSE-BRAYTON COLDHEAD</text>
            <text x="190" y="76" font-family="monospace" font-size="8" fill="#94a3b8">Working Fluid: Supercritical Ne</text>
            <text x="190" y="92" font-family="monospace" font-size="8" fill="#94a3b8">T_operating: 30.0 Kelvin</text>
            <text x="190" y="108" font-family="monospace" font-size="8" font-weight="bold" fill="#34d399">COP: 0.111 (9 W/W Heat Lift)</text>
        </g>

        <!-- Persistent Current Switch (PCS) Schematic (Bottom) -->
        <g transform="translate(100, 360)">
            <rect x="0" y="0" width="820" height="90" rx="4" fill="#040e24" stroke="#0ea5e9" stroke-width="1" />
            <text x="14" y="22" font-family="monospace" font-size="9" font-weight="bold" fill="#38bdf8">PERSISTENT CURRENT SWITCH (PCS) ZERO-LOSS OPERATING REGIME</text>
            <line x1="20" y1="55" x2="160" y2="55" stroke="#34d399" stroke-width="3" />
            <circle cx="160" cy="55" r="4" fill="#34d399" />
            <!-- Switch Branch -->
            <path d="M 160 55 L 240 35 L 320 55" fill="none" stroke="#f59e0b" stroke-width="2" />
            <text x="240" y="28" font-family="monospace" font-size="7" fill="#fbbf24" text-anchor="middle">THERMAL TRIGGER (OFF: NORMAL, ON: SUPERCONDUCTING)</text>
            <!-- Main Coil Inductor -->
            <path d="M 320 55 L 400 55" stroke="#34d399" stroke-width="3" />
            <ellipse cx="440" cy="55" rx="30" ry="12" fill="none" stroke="#34d399" stroke-width="2.5" />
            <text x="440" y="58" font-family="monospace" font-size="8" font-weight="bold" fill="#ffffff" text-anchor="middle">L = 4.8 H</text>
            <line x1="470" y1="55" x2="600" y2="55" stroke="#34d399" stroke-width="3" />
            <text x="620" y="58" font-family="monospace" font-size="10" font-weight="bold" fill="#34d399">CURRENT LIFETIME: > 10,000 HOURS (NO DECAY)</text>
        </g>
    """

def art_593():
    """Plasma Contactors & Ionospheric Hollow Cathode Assemblies"""
    return """
        <!-- Engineering Cutaway of Hollow Cathode Assembly (HCA) -->
        <g transform="translate(120, 240)">
            <text x="0" y="-80" font-family="monospace" font-size="9" font-weight="bold" fill="#34d399">HOLLOW CATHODE ASSEMBLY (HCA) ENGINEERING CUTAWAY</text>
            
            <!-- Pressurized Xenon Feed Tube (Left) -->
            <rect x="0" y="-18" width="120" height="36" fill="#1e293b" stroke="#64748b" stroke-width="1.2" />
            <text x="60" y="4" font-family="monospace" font-size="7" font-weight="bold" fill="#38bdf8" text-anchor="middle">Xe FEED (1.2 mg/s)</text>

            <!-- Porous Sintered Tungsten / LaB6 Emitter Insert -->
            <rect x="120" y="-14" width="100" height="28" fill="#b45309" stroke="#f59e0b" stroke-width="1.5" />
            <text x="170" y="3" font-family="monospace" font-size="7" font-weight="bold" fill="#ffffff" text-anchor="middle">LaB6 INSERT</text>

            <!-- Helical Heater Coil (Swaged Tungsten-Rhenium) -->
            <rect x="110" y="-24" width="120" height="8" fill="#f43f5e" stroke="none" />
            <rect x="110" y="16" width="120" height="8" fill="#f43f5e" stroke="none" />
            <text x="170" y="-30" font-family="monospace" font-size="7" fill="#fca5a5" text-anchor="middle">HEATER COIL (1,100 °C)</text>

            <!-- Orifice Plate Aperture (0.75 mm nozzle) -->
            <path d="M 220 -28 L 240 -6 L 240 6 L 220 28 Z" fill="#334155" stroke="#94a3b8" stroke-width="1.2" />
            <text x="248" y="-12" font-family="monospace" font-size="6" fill="#cbd5e1">ORIFICE (0.75 mm)</text>

            <!-- Keeper Anode Ring (+20 V DC biased) -->
            <rect x="260" y="-35" width="14" height="70" rx="3" fill="#1d4ed8" stroke="#38bdf8" stroke-width="1.5" />
            <text x="267" y="-42" font-family="monospace" font-size="7" font-weight="bold" fill="#38bdf8" text-anchor="middle">KEEPER ANODE (+20 V)</text>

            <!-- Expanding Quasi-Neutral Electron Plasma Plume (Right) -->
            <path d="M 240 0 Q 340 -80 520 -100 L 520 100 Q 340 80 240 0 Z" fill="#0284c7" fill-opacity="0.25" stroke="#38bdf8" stroke-width="1.8" />
            <!-- High density core plume -->
            <path d="M 240 0 Q 300 -30 400 -40 L 400 40 Q 300 30 240 0 Z" fill="#38bdf8" fill-opacity="0.5" stroke="none" />
            <text x="360" y="4" font-family="monospace" font-size="8" font-weight="bold" fill="#ffffff" text-anchor="middle">I_dis = 25.0 A DC</text>
            <text x="460" y="-50" font-family="monospace" font-size="8" fill="#a5f3fc">n_e = 1.2 x 10^12 cm^-3</text>
        </g>

        <!-- Circuit Coupling Callout (Right HUD) -->
        <g transform="translate(680, 160)">
            <rect x="0" y="0" width="220" height="150" rx="4" fill="#040e24" stroke="#34d399" stroke-width="1.2" />
            <text x="12" y="22" font-family="monospace" font-size="9" font-weight="bold" fill="#34d399">IONOSPHERIC CIRCUIT COUPLING</text>
            <text x="12" y="44" font-family="monospace" font-size="8" fill="#94a3b8">Sheath Potential Drop: 18.5 V</text>
            <text x="12" y="62" font-family="monospace" font-size="8" fill="#94a3b8">Plasma Impedance: &lt; 0.74 Ω</text>
            <text x="12" y="80" font-family="monospace" font-size="8" fill="#94a3b8">Hull Charge Neutralization</text>
            <line x1="12" y1="92" x2="208" y2="92" stroke="#334155" stroke-width="0.8" />
            <text x="12" y="112" font-family="monospace" font-size="8" font-weight="bold" fill="#38bdf8">TETHER RETURN: CLOSED</text>
            <text x="12" y="130" font-family="monospace" font-size="8" font-weight="bold" fill="#34d399">SPACECRAFT ARCS: PREVENTED</text>
        </g>
    """

def art_594():
    """Electrodynamic Tether Dynamics & Libration Stabilization"""
    return """
        <!-- Orbiting Tether Dumbbell Geometry (Left side) -->
        <g transform="translate(240, 290)">
            <!-- Local Vertical (Nadir / Zenith) Reference Axis -->
            <line x1="0" y1="-170" x2="0" y2="170" stroke="#64748b" stroke-width="1.2" stroke-dasharray="6,3" />
            <text x="0" y="-178" font-family="monospace" font-size="8" fill="#94a3b8" text-anchor="middle">ZENITH (LOCAL VERTICAL)</text>
            <text x="0" y="188" font-family="monospace" font-size="8" fill="#94a3b8" text-anchor="middle">NADIR (EARTH CENTER)</text>

            <!-- Tilted Tether Line (Pitch Libration Angle theta) -->
            <line x1="-35" y1="-130" x2="35" y2="130" stroke="#f59e0b" stroke-width="3" />
            <!-- Upper Main Spacecraft (Zenith end) -->
            <circle cx="-35" cy="-130" r="14" fill="#0f172a" stroke="#38bdf8" stroke-width="2" />
            <text x="-35" y="-127" font-family="monospace" font-size="7" font-weight="bold" fill="#38bdf8" text-anchor="middle">M1</text>
            <!-- Lower Sub-satellite (Nadir end) -->
            <circle cx="35" cy="130" r="14" fill="#0f172a" stroke="#f59e0b" stroke-width="2" />
            <text x="35" y="133" font-family="monospace" font-size="7" font-weight="bold" fill="#f59e0b" text-anchor="middle">M2</text>

            <!-- Pitch Libration Angle theta Arc -->
            <path d="M 0 -80 A 80 80 0 0 0 -21 -77" fill="none" stroke="#f43f5e" stroke-width="1.8" />
            <text x="-30" y="-90" font-family="monospace" font-size="8" font-weight="bold" fill="#f43f5e">θ = ± 2.4°</text>

            <!-- Gravity Gradient Restoring Torque Vector T_gg -->
            <path d="M -15 -145 Q -2 -140 10 -150" fill="none" stroke="#34d399" stroke-width="2" marker-end="url(#arrow-green)" />
            <text x="18" y="-148" font-family="monospace" font-size="8" font-weight="bold" fill="#34d399">T_gg = 12.8 N·m</text>
        </g>

        <!-- Phase-Space Portrait (theta, theta_dot) & Damping Control (Right side) -->
        <g transform="translate(560, 160)">
            <rect x="0" y="0" width="360" height="260" rx="4" fill="#040e24" stroke="#34d399" stroke-width="1.2" />
            <text x="14" y="24" font-family="monospace" font-size="10" font-weight="bold" fill="#34d399">PHASE-PLANE ASYMPTOTIC DAMPING PORTRAIT</text>
            <!-- Axes: theta horizontal, theta_dot vertical -->
            <line x1="40" y1="140" x2="320" y2="140" stroke="#475569" stroke-width="1" />
            <line x1="180" y1="50" x2="180" y2="230" stroke="#475569" stroke-width="1" />
            <text x="315" y="135" font-family="monospace" font-size="8" fill="#94a3b8">θ (Pitch)</text>
            <text x="185" y="60" font-family="monospace" font-size="8" fill="#94a3b8">dθ/dt (Velocity)</text>

            <!-- Converging Damped Spiral to Stable Origin (0,0) -->
            <path d="M 280 140 C 280 200 240 210 180 210 C 100 210 80 160 80 140 C 80 90 120 70 180 70 C 230 70 250 100 250 140 C 250 170 220 185 180 185 C 130 185 120 155 120 140 C 120 115 150 100 180 100 C 205 100 215 125 215 140 C 215 155 195 160 180 160 C 165 160 160 145 160 140 C 160 130 175 130 180 140" fill="none" stroke="#38bdf8" stroke-width="2" />
            <circle cx="180" cy="140" r="4" fill="#34d399" />
            <text x="190" y="152" font-family="monospace" font-size="8" font-weight="bold" fill="#34d399">ORIGIN NULL (ζ = 0.68)</text>

            <!-- Current Feedback Control Law -->
            <text x="14" y="248" font-family="monospace" font-size="8" font-weight="bold" fill="#fde68a">CONTROL: I(t) = I0 · [1 - 0.35·θ - 0.45·(dθ/dt)]</text>
        </g>
    """

def art_595():
    """Active Multipole Magnetic Shielding & Crew Habitat Decoupling"""
    return """
        <!-- Concentric Multipole Active Shield Geometry -->
        <g transform="translate(320, 290)">
            <!-- Outer Superconducting Deflection Toroids (B = 4.8 Tesla) -->
            <ellipse cx="0" cy="-110" rx="130" ry="22" fill="#064e3b" stroke="#34d399" stroke-width="2.5" />
            <ellipse cx="0" cy="110" rx="130" ry="22" fill="#064e3b" stroke="#34d399" stroke-width="2.5" />
            <text x="0" y="-106" font-family="monospace" font-size="8" font-weight="bold" fill="#a7f3d0" text-anchor="middle">OUTER DEFLECTION COIL (+4.8 T)</text>
            <text x="0" y="114" font-family="monospace" font-size="8" font-weight="bold" fill="#a7f3d0" text-anchor="middle">OUTER DEFLECTION COIL (+4.8 T)</text>

            <!-- Inner Opposing Bucking Coils (Reverse Polarity Cancellation) -->
            <ellipse cx="0" cy="-55" rx="75" ry="12" fill="#1e1b4b" stroke="#f43f5e" stroke-width="2" />
            <ellipse cx="0" cy="55" rx="75" ry="12" fill="#1e1b4b" stroke="#f43f5e" stroke-width="2" />
            <text x="0" y="-52" font-family="monospace" font-size="7" font-weight="bold" fill="#fca5a5" text-anchor="middle">BUCKING COIL (-1.2 T)</text>
            <text x="0" y="58" font-family="monospace" font-size="7" font-weight="bold" fill="#fca5a5" text-anchor="middle">BUCKING COIL (-1.2 T)</text>

            <!-- Central Habitat Zero-Field Cavity -->
            <rect x="-55" y="-35" width="110" height="70" rx="6" fill="#020617" stroke="#38bdf8" stroke-width="2" />
            <text x="0" y="-6" font-family="monospace" font-size="8" font-weight="bold" fill="#e2e8f0" text-anchor="middle">CREW HABITAT</text>
            <text x="0" y="12" font-family="monospace" font-size="9" font-weight="bold" fill="#34d399" text-anchor="middle">B &lt; 0.045 mT</text>
            <text x="0" y="24" font-family="monospace" font-size="7" fill="#94a3b8" text-anchor="middle">FIELD-FREE CORE</text>

            <!-- Carbon Composite Spoke Tension Truss (Viral Load Support) -->
            <line x1="-130" y1="-110" x2="-55" y2="-35" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="3,3" />
            <line x1="130" y1="-110" x2="55" y2="-35" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="3,3" />
            <line x1="-130" y1="110" x2="-55" y2="35" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="3,3" />
            <line x1="130" y1="110" x2="55" y2="35" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="3,3" />
        </g>

        <!-- Magnetic Field Cancellation & Virial Stress Box (Right HUD) -->
        <g transform="translate(620, 160)">
            <rect x="0" y="0" width="310" height="230" rx="4" fill="#040e24" stroke="#34d399" stroke-width="1.2" />
            <text x="14" y="22" font-family="monospace" font-size="9" font-weight="bold" fill="#34d399">MULTIPOLE CANCELLATION & VIRIAL PRESSURE</text>
            <text x="14" y="44" font-family="monospace" font-size="8" fill="#94a3b8">B_hab(r) = Σ B_k(r) -> 0.00 mT</text>
            <!-- Field Magnitude Comparison -->
            <rect x="14" y="55" width="280" height="30" rx="2" fill="#064e3b" stroke="none" />
            <text x="24" y="74" font-family="monospace" font-size="8" font-weight="bold" fill="#34d399">EXTERNAL GCR DEFLECTION: 4.80 TESLA</text>
            <rect x="14" y="92" width="280" height="30" rx="2" fill="#1e293b" stroke="none" />
            <text x="24" y="111" font-family="monospace" font-size="8" font-weight="bold" fill="#38bdf8">INTERIOR CABIN RESIDUAL: 0.042 mT</text>
            <!-- Virial Tension Stress -->
            <line x1="14" y1="132" x2="294" y2="132" stroke="#334155" stroke-width="0.8" />
            <text x="14" y="152" font-family="monospace" font-size="8" font-weight="bold" fill="#f59e0b">VIRIAL BURSTING PRESSURE: 9.17 MPa</text>
            <text x="14" y="170" font-family="monospace" font-size="8" fill="#94a3b8">P = B^2 / 2u0 | Supported by T1000 Carbon</text>
            <text x="14" y="188" font-family="monospace" font-size="8" fill="#94a3b8">Spoke Tension Load: 125 kN / tie</text>
            <text x="14" y="210" font-family="monospace" font-size="9" font-weight="bold" fill="#34d399">CREW HEALTH STANDARD: NASA-STD-3001 MET</text>
        </g>
    """

def art_596():
    """Bio-Resonance Habitat Conditioning & Synthetic Field Generation"""
    return """
        <!-- 3-Axis Orthogonal Helmholtz Coil Cage Integrated into Spacecraft Ribs -->
        <g transform="translate(320, 280)">
            <!-- X-Axis Helmholtz Coil Pair -->
            <ellipse cx="0" cy="0" rx="140" ry="140" fill="none" stroke="#38bdf8" stroke-width="2.5" />
            <text x="145" y="4" font-family="monospace" font-size="8" font-weight="bold" fill="#38bdf8">COIL X</text>

            <!-- Y-Axis Helmholtz Coil Pair -->
            <ellipse cx="0" cy="0" rx="40" ry="140" fill="none" stroke="#a855f7" stroke-width="2" />
            <text x="0" y="-148" font-family="monospace" font-size="8" font-weight="bold" fill="#a855f7" text-anchor="middle">COIL Y</text>

            <!-- Z-Axis Helmholtz Coil Pair -->
            <ellipse cx="0" cy="0" rx="140" ry="40" fill="none" stroke="#34d399" stroke-width="2" />
            <text x="0" y="52" font-family="monospace" font-size="8" font-weight="bold" fill="#34d399" text-anchor="middle">COIL Z</text>

            <!-- Central Homogeneous Habitable Volume (Uniform 50 uT) -->
            <circle cx="0" cy="0" r="50" fill="#0369a1" fill-opacity="0.15" stroke="#38bdf8" stroke-width="1.2" stroke-dasharray="3,3" />
            <text x="0" y="-8" font-family="monospace" font-size="8" font-weight="bold" fill="#ffffff" text-anchor="middle">50.0 µT DC</text>
            <text x="0" y="8" font-family="monospace" font-size="7" fill="#7dd3fc" text-anchor="middle">UNIFORMITY &lt; ±0.22%</text>
            <text x="0" y="24" font-family="monospace" font-size="7" font-weight="bold" fill="#fbbf24" text-anchor="middle">+ 7.83 Hz SINE</text>
        </g>

        <!-- DSP Frequency Synthesizer & Closed-Loop Controller (Right HUD) -->
        <g transform="translate(580, 160)">
            <rect x="0" y="0" width="340" height="230" rx="4" fill="#040e24" stroke="#34d399" stroke-width="1.2" />
            <text x="14" y="22" font-family="monospace" font-size="9" font-weight="bold" fill="#34d399">DSP BIO-RESONANCE SYNTHESIZER</text>
            
            <!-- Schumann Waveform Generator Graphic -->
            <rect x="14" y="38" width="310" height="50" rx="2" fill="#0f172a" stroke="#334155" stroke-width="0.8" />
            <path d="M 24 63 Q 50 43 75 63 T 125 63 T 175 63 T 225 63 T 275 63 T 310 63" fill="none" stroke="#fbbf24" stroke-width="2" />
            <text x="24" y="50" font-family="monospace" font-size="7" font-weight="bold" fill="#fbbf24">SCHUMANN HARMONIC f1 = 7.83 Hz (IONOSPHERE SIMULATION)</text>

            <!-- Closed Loop Feedback Latency -->
            <text x="14" y="108" font-family="monospace" font-size="8" fill="#94a3b8">Feedback Sensor: 3-Axis Fluxgate Magnetometer</text>
            <text x="14" y="126" font-family="monospace" font-size="8" fill="#94a3b8">Disturbance Nulling Latency: 2.5 ms</text>
            <text x="14" y="144" font-family="monospace" font-size="8" fill="#94a3b8">Bipolar Linear Amplifier: 185 W Continuous</text>
            <line x1="14" y1="156" x2="324" y2="156" stroke="#334155" stroke-width="0.8" />

            <!-- Physiological Stabilization Status -->
            <text x="14" y="176" font-family="monospace" font-size="8" font-weight="bold" fill="#34d399">CIRCADIAN CLOCK SYNCHRONY: NOMINAL (24.0 h)</text>
            <text x="14" y="194" font-family="monospace" font-size="8" font-weight="bold" fill="#38bdf8">CELL RESTING POTENTIAL: -70.4 mV PRESERVED</text>
            <text x="14" y="212" font-family="monospace" font-size="8" font-weight="bold" fill="#a7f3d0">NEUROLOGICAL HOMEOSTASIS: ACTIVE</text>
        </g>
    """

print("All 18 artworks fully compiled in library.")

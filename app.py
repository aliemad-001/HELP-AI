import streamlit as st
import time

# ==============================================================================
# COLOR SYSTEM & MODERN UI CONFIGURATION (Pure Native Engine)
# ==============================================================================
st.set_page_config(
    page_title="PathPilot AI",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

custom_css = """
<style>
    .stApp {
        background-color: #0F172A;
        color: #F8FAFC;
    }
    [data-testid="stMetricBorderDiv"], .stElementContainer div[data-style="border"] {
        background-color: #1E293B !important;
        border: 1px solid #334155 !important;
        border-radius: 16px !important;
        padding: 20px !important;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3) !important;
    }
    [data-testid="stMetricValue"] {
        font-size: 32px;
        font-weight: 800;
        color: #8B5CF6;
    }
</style>
"""
st.html(custom_css)

# ==============================================================================
# MASTER KNOWLEDGE DICTIONARIES (All 16 Personalities Core Matrix Data)
# ==============================================================================
PERSONALITY_REGISTRY = {
    "INTJ": {
        "title": "Architect", "strengths": ["Strategic", "Logical", "Independent", "Determined"], "growth": ["Arrogant", "Overthinker", "Dismissive of Emotions"],
        "questions": [
            "Do you prioritize macro long-term strategy planning over short-term execution?",
            "Do you vastly prefer working strictly independently over group collaborations?",
            "Do logic and optimization strategy games deeply interest you?",
            "Is process efficiency your ultimate standard metric for success?",
            "Would you rather design the structural layout of a system than manage its people?"
        ],
        "universities": ["MIT", "Stanford", "ETH Zurich", "Carnegie Mellon"],
        "diversity_map": {
            "Technology": {
                "bonus": {"AI Engineer": 10, "Software Engineer": 8, "Data Scientist": 9, "Cybersecurity Specialist": 7},
                "roadmap": ["Phase 1: Deep-dive into Discrete Math & Compiler Design Foundations", "Phase 2: Construct isolated scalable microservice backends", "Phase 3: Architect robust zero-trust security layers", "Phase 4: Deploy enterprise-tier autonomous cloud clusters"],
                "projects": ["Distributed Neural Network Architecture", "Cryptographic Consensus Core Simulation"]
            },
            "Business": {
                "bonus": {"Business Analyst": 10, "Product Manager": 8, "Entrepreneur": 6},
                "roadmap": ["Phase 1: Analyze advanced market volatility datasets", "Phase 2: Build quantitative predictive econometric tracking sandboxes", "Phase 3: Structure structural risk optimization audits", "Phase 4: Design macro-scale operational corporate strategies"],
                "projects": ["Automated Algorithmic Arbitrage Engine", "Predictive Corporate Competitor Analysis Core"]
            },
            "Healthcare": {
                "bonus": {"Medical Researcher": 10, "Doctor": 7, "Pharmacist": 6},
                "roadmap": ["Phase 1: Master complex quantitative genomic parsing rules", "Phase 2: Run clinical trial data simulation pipelines", "Phase 3: Build diagnostic optimization tools for laboratories", "Phase 4: Publish predictive pathological structural models"],
                "projects": ["Genomic Sequencing Variant Mapping Pipeline", "Computational Molecular Interaction Sandbox"]
            },
            "Education": {
                "bonus": {"Education Consultant": 10, "Professor": 8, "Teacher": 5},
                "roadmap": ["Phase 1: Deconstruct structural learning analytics frameworks", "Phase 2: Standardize adaptive instructional assessment rules", "Phase 3: Architect scalable multi-district curriculum metrics", "Phase 4: Launch systemic educational optimization consultancies"],
                "projects": ["Data-Driven Adaptive Learning System Engine", "Institutional Curricular Alignment Sandbox"]
            },
            "Engineering": {
                "bonus": {"Electrical Engineer": 10, "Mechanical Engineer": 8, "Civil Engineer": 7},
                "roadmap": ["Phase 1: Analyze high-level finite element structural models", "Phase 2: Program hardware register-level industrial routing steps", "Phase 3: Optimize automated load tolerances under systemic strain", "Phase 4: Direct macro-scale smart infrastructure setups"],
                "projects": ["Smart Traffic Grid Infrastructure Simulator", "Finite Element Structural Stress Analyzer"]
            },
            "Creative Arts": {
                "bonus": {"Graphic Designer": 10, "Animator": 7, "Content Creator": 5},
                "roadmap": ["Phase 1: Study underlying design systems & geometric layout laws", "Phase 2: Systematize programmatic visual vector patterns", "Phase 3: Architect comprehensive interactive digital UI guidelines", "Phase 4: Launch technical spatial design framework agencies"],
                "projects": ["Scalable Dynamic UI Design Token System", "Procedural Vector Geometry Blueprint Engine"]
            }
        }
    },
    "INTP": {
        "title": "Logician", "strengths": ["Analytical", "Original", "Open-Minded", "Objective"], "growth": ["Disconnected", "Condescending", "Loathe Rules"],
        "questions": [
            "Do you find yourself constantly analyzing abstract theoretical frameworks?",
            "Do you value conceptual originality more than structural convention?",
            "Are you comfortable pivoting projects mid-way if a more interesting problem appears?",
            "Do you look for underlying logical fallacies during routine debates?",
            "Would you prefer discovering a new principle over building a commercial application?"
        ],
        "universities": ["MIT", "Stanford", "ETH Zurich", "ETH Zurich"],
        "diversity_map": {
            "Technology": {
                "bonus": {"AI Engineer": 10, "Data Scientist": 9, "Software Engineer": 7, "Cybersecurity Specialist": 6},
                "roadmap": ["Phase 1: Study functional programming languages & lambda calculus", "Phase 2: Build custom memory-safe compiler architectures", "Phase 3: Train alternative generative deep learning algorithms", "Phase 4: Author open-source abstract framework paradigms"],
                "projects": ["Custom Memory-Safe Functional Language Compiler", "Autonomous Neural Hyperparameter Tuning Core"]
            },
            "Business": {
                "bonus": {"Business Analyst": 10, "Product Manager": 7, "Entrepreneur": 5},
                "roadmap": ["Phase 1: Deconstruct macroeconomic game theory models", "Phase 2: Develop independent market structural simulators", "Phase 3: Audit complex decentralized micro-transaction ledger formats", "Phase 4: Formulate innovative algorithmic business optimization metrics"],
                "projects": ["Algorithmic Game Theory Market Matrix", "Decentralized Token Economic Flow Sandbox"]
            },
            "Healthcare": {
                "bonus": {"Medical Researcher": 10, "Pharmacist": 8, "Doctor": 5},
                "roadmap": ["Phase 1: Audit massive cellular data correlation matrices", "Phase 2: Simulate theoretical biochemical compounding dynamics", "Phase 3: Code advanced epidemiological mutation tracking loops", "Phase 4: Deliver first-principles scientific breakthroughs"],
                "projects": ["Biochemical Compounding Affinity Core Simulator", "Epidemiological Mutation Spread Blueprint"]
            },
            "Education": {
                "bonus": {"Professor": 10, "Education Consultant": 8, "Teacher": 5},
                "roadmap": ["Phase 1: Research underlying cognitive processing theories", "Phase 2: Analyze algorithmic knowledge gap detection models", "Phase 3: Formulate abstract pedagogical tracking taxonomies", "Phase 4: Direct alternative logic training institutions"],
                "projects": ["Algorithmic Student Knowledge Gap Mapper", "Cognitive Taxonomical Framework Tracker"]
            },
            "Engineering": {
                "bonus": {"Electrical Engineer": 10, "Mechanical Engineer": 8, "Civil Engineer": 6},
                "roadmap": ["Phase 1: Deconstruct thermodynamics and fundamental field theories", "Phase 2: Code low-level physical micro-sensor firmware array maps", "Phase 3: Simulate unconventional experimental layout models", "Phase 4: Pioneer foundational material engineering mechanics"],
                "projects": ["Bare-Metal Sensor Array Firmware Controller", "Thermodynamic Flow Simulation Array Engine"]
            },
            "Creative Arts": {
                "bonus": {"Animator": 10, "Graphic Designer": 7, "Content Creator": 6},
                "roadmap": ["Phase 1: Study mathematical fractals and procedural generation laws", "Phase 2: Build automated physics engines for interactive media", "Phase 3: Script custom shading pipelines for graphics engines", "Phase 4: Consult on technical visual generation software stacks"],
                "projects": ["Procedural Graphic Generation Canvas Sandbox", "Custom Physics-Driven Motion Shader Module"]
            }
        }
    },
    "ENTJ": {
        "title": "Commander", "strengths": ["Efficient", "Energetic", "Confident", "Strong-Willed"], "growth": ["Stubborn", "Dominant", "Intolerant"],
        "questions": [
            "Do you effortlessly take command of team structures when bottlenecks occur?",
            "Are you motivated by maximizing competitive market efficiency?",
            "Do you find managing human capital and deadlines highly rewarding?",
            "Is execution velocity more important to you than absolute perfection?",
            "Do you actively design optimization roadmaps for your career daily?"
        ],
        "universities": ["Stanford", "Wharton", "LUMS", "IBA"],
        "diversity_map": {
            "Technology": {
                "bonus": {"Product Manager": 10, "Cybersecurity Specialist": 8, "Software Engineer": 7, "AI Engineer": 6},
                "roadmap": ["Phase 1: Direct multi-engineer tech workspace agile sprints", "Phase 2: Standardize global enterprise software deployment SLAs", "Phase 3: Supervise cross-platform systems scaling audits", "Phase 4: Command enterprise-tier engineering organizations globally"],
                "projects": ["Multi-Tenant Scalable Operations Orchestrator", "Enterprise Tech Infrastructure Performance Deck"]
            },
            "Business": {
                "bonus": {"Entrepreneur": 10, "Product Manager": 9, "Business Analyst": 8, "Marketing Manager": 7},
                "roadmap": ["Phase 1: Evaluate tech startup seed capitalization runways", "Phase 2: Negotiate enterprise strategic vendor agreements", "Phase 3: Execute target user acquisition market offensives", "Phase 4: Scale full corporate enterprise frameworks toward market dominance"],
                "projects": ["Venture Seed Capital Runway Optimization Deck", "Strategic Market Penetration Deployment Matrix"]
            },
            "Healthcare": {
                "bonus": {"Doctor": 10, "Medical Researcher": 8, "Pharmacist": 6},
                "roadmap": ["Phase 1: Supervise hospital resource distribution logistics", "Phase 2: Enforce clinical compliance and output standards", "Phase 3: Lead multi-disciplinary specialized surgical cohorts", "Phase 4: Direct regional healthcare delivery infrastructure networks"],
                "projects": ["Integrated Healthcare Operations Routing Core", "Clinical Compliance Risk Mitigation Architecture"]
            },
            "Education": {
                "bonus": {"Education Consultant": 10, "Professor": 8, "Teacher": 6},
                "roadmap": ["Phase 1: Direct institutional educational budget frameworks", "Phase 2: Enforce systemic performance tracking standard criteria", "Phase 3: Command regional university administrative operations networks", "Phase 4: Restructure national educational system deployment models"],
                "projects": ["Regional Institutional Educational Budget Manager", "Systemic Academic Performance Metric Grid"]
            },
            "Engineering": {
                "bonus": {"Civil Engineer": 10, "Mechanical Engineer": 8, "Electrical Engineer": 7},
                "roadmap": ["Phase 1: Manage multi-million scale physical construction frameworks", "Phase 2: Enforce industrial factory manufacturing efficiency metrics", "Phase 3: Lead large-scale field engineering deployment teams", "Phase 4: Command international civil or mechanical infrastructure consortia"],
                "projects": ["Industrial Manufacturing Efficiency Router Core", "Macro Civil Infrastructure Lifecycle Tracking Suite"]
            },
            "Creative Arts": {
                "bonus": {"Content Creator": 10, "Marketing Manager": 9, "Graphic Designer": 6},
                "roadmap": ["Phase 1: Establish large-scale creative content production studios", "Phase 2: Direct major corporate marketing campaign frameworks", "Phase 3: Manage comprehensive studio brand ecosystem portfolios", "Phase 4: Dominate global media agency monetization networks"],
                "projects": ["Scalable Creative Studio Asset Pipeline Tracker", "Corporate Content Campaign Monetization Blueprint"]
            }
        }
    },
    "ENTP": {
        "title": "Debater", "strengths": ["Innovative", "Curious", "Fast Learner", "Entrepreneurial"], "growth": ["Inconsistent", "Dislikes Routine", "Argumentative"],
        "questions": [
            "Do you enjoy challenging conventional wisdom and debating radical concepts?",
            "Would you rather assume the risk of building a startup than joining an established firm?",
            "How deep is your intrinsic interest in artificial intelligence ecosystem evolution?",
            "Do you enjoy dissecting highly complex, ambiguous problems?",
            "Do you struggle with standard routine operational tasks once conceptual loops are closed?"
        ],
        "universities": ["Stanford", "Wharton", "LUMS", "IBA"],
        "diversity_map": {
            "Technology": {
                "bonus": {"Entrepreneur": 10, "AI Engineer": 9, "Software Engineer": 7, "Data Scientist": 6},
                "roadmap": ["Phase 1: Rapidly deploy dynamic front-to-back Python prototypes", "Phase 2: Build 5 intersecting functional AI product wrappers", "Phase 3: Pitches disruptive technology concepts in hackathons", "Phase 4: Incubate cross-platform autonomous product SaaS labs"],
                "projects": ["AI Automated Startup Idea Validator Node", "Real-Time Gamified Student Planner Network"]
            },
            "Business": {
                "bonus": {"Entrepreneur": 10, "Marketing Manager": 9, "Product Manager": 8, "Business Analyst": 6},
                "roadmap": ["Phase 1: Draft growth hack loops using alternative channels", "Phase 2: Build interactive continuous business model builders", "Phase 3: Validate unique value monetization structures fast", "Phase 4: Scale modular, automated micro-venture ecosystems online"],
                "projects": ["Alternative Growth Hack Loop Validator Engine", "Interactive Business Model Canvas Prototyper"]
            },
            "Healthcare": {
                "bonus": {"Medical Researcher": 10, "Doctor": 7, "Pharmacist": 5},
                "roadmap": ["Phase 1: Ideate computational medical delivery software paths", "Phase 2: Launch digital alternative medical awareness applications", "Phase 3: Prototype user-friendly telehealth tracking portals", "Phase 4: Disrupt legacy diagnostic workflows with smart tech toolsets"],
                "projects": ["Telehealth Application UI Wireframe Network", "Legacy Diagnostic Workflow Software Disrupter"]
            },
            "Education": {
                "bonus": {"Education Consultant": 10, "Teacher": 8, "Professor": 6},
                "roadmap": ["Phase 1: Build gamified digital learning interaction modules", "Phase 2: Host interactive global conceptual student panels", "Phase 3: Launch alternative educational content properties", "Phase 4: Scale alternative online micro-school tracking models"],
                "projects": ["Gamified Quiz Application Software Blueprint", "Decentralized Micro-School Enrollment Portal"]
            },
            "Engineering": {
                "bonus": {"Mechanical Engineer": 10, "Electrical Engineer": 8, "Civil Engineer": 5},
                "roadmap": ["Phase 1: Prototype rapid mechanical proof-of-concept models", "Phase 2: Integrate cheap microcontrollers into smart arrays", "Phase 3: Pitch innovative green renewable energy inventions", "Phase 4: Scale agile component manufacturing tech operations"],
                "projects": ["Agile 3D Component Prototyping System", "Smart Microcontroller Environmental Collector"]
            },
            "Creative Arts": {
                "bonus": {"Content Creator": 10, "Graphic Designer": 8, "Animator": 7},
                "roadmap": ["Phase 1: Launch multiple visual experimentation digital spaces", "Phase 2: Mix interactive generative script formats with media", "Phase 3: Coordinate modern immersive performance events online", "Phase 4: Consult on dynamic branding systems for startup tracks"],
                "projects": ["Generative Media Scripting Sandbox Engine", "Immersive Startup Branding Design Token Suite"]
            }
        }
    },
    "INFJ": {
        "title": "Advocate", "strengths": ["Creative", "Insightful", "Principled", "Passionate"], "growth": ["Sensitive", "Extremely Private", "Perfectionist"],
        "questions": [
            "Does the positive social impact of your work matter significantly more than compensation?",
            "Do you find yourself deeply attuned to the long-term motivations of others?",
            "Do you possess an absolute core set of principles you refuse to compromise?",
            "Do you prefer deep, singular mentorship interactions over broad crowds?",
            "Are you driven to resolve structural human inequalities via systemic design?"
        ],
        "universities": ["Harvard", "Johns Hopkins", "Oxford", "Aga Khan University"],
        "diversity_map": {
            "Technology": {
                "bonus": {"Software Engineer": 10, "Data Scientist": 8, "AI Engineer": 7, "Cybersecurity Specialist": 6},
                "roadmap": ["Phase 1: Code ethical alternative open-source privacy frameworks", "Phase 2: Construct non-profit data tracking aggregation models", "Phase 3: Optimize user interface design paths for accessibility", "Phase 4: Manage engineering tracks at global human-centric platforms"],
                "projects": ["Ethical Open-Source Privacy Guard Node", "Accessible Human-Centric UI Tracker Template"]
            },
            "Business": {
                "bonus": {"Business Analyst": 10, "Product Manager": 7, "Marketing Manager": 6},
                "roadmap": ["Phase 1: Formulate social enterprise corporate charter rules", "Phase 2: Audit alternative sustainable fair-trade supply models", "Phase 3: Write comprehensive ethical organizational growth specs", "Phase 4: Direct impact investments networks globally"],
                "projects": ["Social Enterprise Sustainability Flow Audit", "Ethical Capital Allocation Matrix Engine"]
            },
            "Healthcare": {
                "bonus": {"Doctor": 10, "Medical Researcher": 9, "Pharmacist": 6},
                "roadmap": ["Phase 1: Train in holistic patient mental support methodologies", "Phase 2: Champion community-level disease prevention metrics", "Phase 3: Write comprehensive diagnostic empathy delivery systems", "Phase 4: Direct specialized care counseling institutions"],
                "projects": ["Holistic Community Welfare Database Tracker", "Pathological Empathy-Driven Interaction Protocol"]
            },
            "Education": {
                "bonus": {"Teacher": 10, "Education Consultant": 9, "Professor": 8},
                "roadmap": ["Phase 1: Deploy individualized custom remedial tracking nodes", "Phase 2: Manage vulnerable student special education support frameworks", "Phase 3: Lead deep humanistic peer mentoring networks", "Phase 4: Author foundational educational equity reform papers"],
                "projects": ["Remedial Student Progress Tracking Portal", "Humanistic Peer Mentoring System Framework"]
            },
            "Engineering": {
                "bonus": {"Civil Engineer": 10, "Mechanical Engineer": 7, "Electrical Engineer": 6},
                "roadmap": ["Phase 1: Study eco-friendly sustainable green engineering codes", "Phase 2: Structural design layouts for clean water networks", "Phase 3: Audit rural public utility deployment safety metrics", "Phase 4: Oversee global structural infrastructure aid initiatives"],
                "projects": ["Rural Clean Water Distribution Grid Mockup", "Eco-Friendly Structural Material Strain Auditor"]
            },
            "Creative Arts": {
                "bonus": {"Graphic Designer": 10, "Content Creator": 8, "Animator": 7},
                "roadmap": ["Phase 1: Create intentional visual assets for advocacy groups", "Phase 2: Write thoughtful story treatments highlighting human conditions", "Phase 3: Build high-empathy UI user experience layouts", "Phase 4: Establish meaningful design consultancies supporting causes"],
                "projects": ["Advocacy Visual Asset System Layout", "High-Empathy User Experience UI Wireframe"]
            }
        }
    },
    "INFP": {
        "title": "Mediator", "strengths": ["Empathetic", "Generous", "Imaginative", "Open-Minded"], "growth": ["Unrealistic", "Self-Isolating", "Vulnerable"],
        "questions": [
            "Do you evaluate career tracks based on how closely they mirror your personal ideals?",
            "Do you find creative writing or visual imagery highly therapeutic?",
            "Do you require extensive solo deep-focus windows to recharge your output?",
            "Are you highly sensitive to disharmony or aggressive competition?",
            "Do you view raw technical tools as instruments for self-expression?"
        ],
        "universities": ["RISD", "CalArts", "NCA", "Harvard"],
        "diversity_map": {
            "Technology": {
                "bonus": {"Software Engineer": 10, "AI Engineer": 7, "Data Scientist": 6},
                "roadmap": ["Phase 1: Learn markdown scripting & indie design framework setups", "Phase 2: Build indie creative applications for alternative learning", "Phase 3: Develop localized community content-sharing tools", "Phase 4: Direct independent product interfaces focusing on user health"],
                "projects": ["Indie Alternative Learning Application Mock", "Localized Community Story Sharing Tool Node"]
            },
            "Business": {
                "bonus": {"Business Analyst": 10, "Marketing Manager": 7, "Product Manager": 6},
                "roadmap": ["Phase 1: Research human-centric organizational work rules", "Phase 2: Strategy paths for small artisanal commerce clusters", "Phase 3: Implement authentic identity marketing metrics", "Phase 4: Counsel startup founders on mental safety systems"],
                "projects": ["Artisanal Small Business Commerce Tracker", "Human-Centric Organizational Workplace Audit"]
            },
            "Healthcare": {
                "bonus": {"Medical Researcher": 10, "Doctor": 6, "Pharmacist": 5},
                "roadmap": ["Phase 1: Study alternative holistic wellness therapy data", "Phase 2: Build simple narrative art therapy tool maps", "Phase 3: Analyze healthcare delivery accessibility in rural spots", "Phase 4: Advocate for humanitarian mental support network setups"],
                "projects": ["Narrative Art Therapy Progress Log Matrix", "Rural Healthcare Access Data Disparity Map"]
            },
            "Education": {
                "bonus": {"Teacher": 10, "Education Consultant": 8, "Professor": 6},
                "roadmap": ["Phase 1: Author creative storytelling instructional materials", "Phase 2: Instruct alternative creative writing workshops online", "Phase 3: Model customized progress tracking maps for remote kids", "Phase 4: Build niche emotional intelligence training paths"],
                "projects": ["Creative Storytelling Instructional Module Deck", "Emotional Intelligence Student Progress Tracker"]
            },
            "Engineering": {
                "bonus": {"Mechanical Engineer": 10, "Electrical Engineer": 7, "Civil Engineer": 5},
                "roadmap": ["Phase 1: Design biomimetic mechanical kinetic structural concepts", "Phase 2: Prototype low-cost alternative prosthetics layout models", "Phase 3: Evaluate eco-conscious passive solar heating systems", "Phase 4: Consult on localized, alternative material engineering setups"],
                "projects": ["Biomimetic Kinetic Component Mechanism Rig", "Low-Cost Prosthetic Joint Mechanical Sandbox"]
            },
            "Creative Arts": {
                "bonus": {"Graphic Designer": 10, "Content Creator": 9, "Animator": 8},
                "roadmap": ["Phase 1: Build deep personal artistic portfolio concept sets", "Phase 2: Code interactive storytelling multimedia apps", "Phase 3: Illustrate distinct indie character system libraries", "Phase 4: Run independent digital creative design consultancies"],
                "projects": ["Interactive Story Visual Novel Framework", "Bespoke Digital Character Design Library Node"]
            }
        }
    },
    "ENFJ": {
        "title": "Protagonist", "strengths": ["Charismatic", "Inspiring", "Altruistic", "Natural Leaders"], "growth": ["Overly Idealistic", "Too Selfless", "Fluctuating Self-Esteem"],
        "questions": [
            "Do you genuinely love guiding others to unlock their ultimate capability potentials?",
            "Are you naturally elected to lead collaborative groups or panels?",
            "Do you prioritize team morale and harmony over cold technical efficiency?",
            "Can you easily communicate complex conceptual paradigms to varied crowds?",
            "Do you thrive on receiving direct, authentic validation from communities?"
        ],
        "universities": ["Stanford", "Harvard", "LUMS", "Oxford"],
        "diversity_map": {
            "Technology": {
                "bonus": {"Product Manager": 10, "Software Engineer": 7, "AI Engineer": 6},
                "roadmap": ["Phase 1: Run cross-team tech community developer meetups", "Phase 2: Manage collaborative open-source tool contributions", "Phase 3: Interface directly between technical teams and client panels", "Phase 4: Direct technology transformation consulting firms"],
                "projects": ["Open Developer Community Collaboration Portal", "Cross-Team Tech Project Sync Dashboard"]
            },
            "Business": {
                "bonus": {"Marketing Manager": 10, "Product Manager": 9, "Entrepreneur": 7, "Business Analyst": 6},
                "roadmap": ["Phase 1: Direct corporate human resources training pathways", "Phase 2: Structure public relations outreach framework plans", "Phase 3: Orchestrate corporate social responsibility campaigns", "Phase 4: Executive direction of major consumer brand systems"],
                "projects": ["Corporate HR Onboarding & Training Manual", "CSR Campaign Stakeholder Impact Tracker Matrix"]
            },
            "Healthcare": {
                "bonus": {"Doctor": 10, "Pharmacist": 7, "Medical Researcher": 6},
                "roadmap": ["Phase 1: Coordinate complex public health awareness drives", "Phase 2: Direct patient advocacy representative networks", "Phase 3: Manage inter-disciplinary mental health response modules", "Phase 4: Executive direction of public healthcare networks"],
                "projects": ["Public Health Campaign Activation Playbook", "Patient Advocacy Network Tracking System"]
            },
            "Education": {
                "bonus": {"Teacher": 10, "Education Consultant": 9, "Professor": 8},
                "roadmap": ["Phase 1: Lead regional student speech and panel activities", "Phase 2: Establish institutional student mentorship system templates", "Phase 3: Manage staff developmental training workshops", "Phase 4: Preside over major alternative educational institutions"],
                "projects": ["Institutional Student Mentorship Mapping Matrix", "Educational Professional Development Tracker"]
            },
            "Engineering": {
                "bonus": {"Civil Engineer": 10, "Mechanical Engineer": 7, "Electrical Engineer": 6},
                "roadmap": ["Phase 1: Run cross-functional field engineer work cohorts", "Phase 2: Facilitate public engineering project impact hearings", "Phase 3: Negotiate safety framework consensus across stakeholders", "Phase 4: Direct international engineering client relation nodes"],
                "projects": ["Public Infrastructure Hearing Feedback Matrix", "Cross-Functional Field Engineer Sync Hub"]
            },
            "Creative Arts": {
                "bonus": {"Content Creator": 10, "Marketing Manager": 9, "Graphic Designer": 6},
                "roadmap": ["Phase 1: Direct multi-artist visual performance groups", "Phase 2: Run major collaborative community design workshops", "Phase 3: Anchor client presentation pitches for design firms", "Phase 4: Lead global media team activation operations networks"],
                "projects": ["Collaborative Community Art Workshop Blueprint", "Creative Design Pitch Presentation Interface"]
            }
        }
    },
    "ENFP": {
        "title": "Campaigner", "strengths": ["Enthusiastic", "Creative", "Excellent Communicators", "Festive"], "growth": ["Disorganized", "Overly Accommodating", "Restless"],
        "questions": [
            "Do you find your mind constantly ideating vast webs of creative opportunities?",
            "Are you energized by working dynamically across multiple distinct focus areas at once?",
            "Do you enjoy cultivating broad networks of unique creative individuals?",
            "Do you get bored quickly once a project enters standard execution routines?",
            "Do you value deep personal freedom over standard structured corporate hierarchy?"
        ],
        "universities": ["RISD", "CalArts", "LUMS", "IBA"],
        "diversity_map": {
            "Technology": {
                "bonus": {"Entrepreneur": 10, "Software Engineer": 7, "AI Engineer": 6},
                "roadmap": ["Phase 1: Create interactive frontend app user journeys fast", "Phase 2: Launch emerging tech social sandbox interfaces", "Phase 3: Build gamified digital developer hackathon spaces", "Phase 4: Consult on dynamic UI user onboarding strategies"],
                "projects": ["Emerging Tech Social UI Sandbox Concept", "Gamified Developer Onboarding User Journey"]
            },
            "Business": {
                "bonus": {"Marketing Manager": 10, "Entrepreneur": 9, "Product Manager": 7, "Business Analyst": 5},
                "roadmap": ["Phase 1: Run multi-channel viral branding experiments", "Phase 2: Deploy agile, creative startup validation pitches", "Phase 3: Invent alternative direct-to-consumer sales pipelines", "Phase 4: Direct hyper-growth startup incubator ecosystems"],
                "projects": ["Multi-Channel Viral Brand Growth Sandbox", "Agile Direct-To-Consumer Sales Pipeline Model"]
            },
            "Healthcare": {
                "bonus": {"Medical Researcher": 10, "Doctor": 6, "Pharmacist": 5},
                "roadmap": ["Phase 1: Build creative health awareness media properties", "Phase 2: Launch mobile fitness engagement app prototypes", "Phase 3: Create alternative patient community network models", "Phase 4: Direct creative strategy for healthcare platforms"],
                "projects": ["Mobile Fitness Gamified Engagement Prototype", "Patient Community Network Connection Model"]
            },
            "Education": {
                "bonus": {"Teacher": 10, "Education Consultant": 9, "Professor": 6},
                "roadmap": ["Phase 1: Design highly animated dynamic learning games", "Phase 2: Host collaborative online student growth spaces", "Phase 3: Launch innovative non-traditional study communities", "Phase 4: Scale alternative virtual edutainment platform grids"],
                "projects": ["Animated Interactive Educational Mini-Game", "Virtual Edutainment Student Activation Interface"]
            },
            "Engineering": {
                "bonus": {"Mechanical Engineer": 10, "Electrical Engineer": 7, "Civil Engineer": 5},
                "roadmap": ["Phase 1: Ideate bold futuristic consumer product concepts", "Phase 2: Incorporate recycled alternative elements into devices", "Phase 3: Pitch human-centric ergonomic structure improvements", "Phase 4: Direct rapid innovation squads at manufacturing firms"],
                "projects": ["Ergonomic Consumer Product Layout Model", "Rapid-Innovation Hardware Device Sandbox Node"]
            },
            "Creative Arts": {
                "bonus": {"Content Creator": 10, "Graphic Designer": 9, "Animator": 8},
                "roadmap": ["Phase 1: Build cross-platform experimental digital channels", "Phase 2: Publish highly animated interactive video series", "Phase 3: Coordinate global independent creative asset networks", "Phase 4: Manage complete independent creative visual studio networks"],
                "projects": ["Cross-Platform Interactive Video Interface", "Independent Creative Asset Network Framework"]
            }
        }
    },
    "ISTJ": {
        "title": "Logistician", "strengths": ["Responsible", "Dutiful", "Orderly", "Reliable"], "growth": ["Stubborn", "By-the-Book", "Judgmental"],
        "questions": [
            "Do you value structural order, proven traditions, and clear regulatory guidelines?",
            "Do you take immense pride in absolute accuracy, attention to detail, and punctuality?",
            "Do you prefer dealing with observable facts over abstract speculative theories?",
            "Are you highly comfortable managing deterministic, repeatable, and logical processes?",
            "Do you consider yourself exceptionally dependable when deadlines are critical?"
        ],
        "universities": ["MIT", "Carnegie Mellon", "NUST", "FAST"],
        "diversity_map": {
            "Technology": {
                "bonus": {"Cybersecurity Specialist": 10, "Software Engineer": 8, "Data Scientist": 7, "AI Engineer": 5},
                "roadmap": ["Phase 1: Acquire professional systems compliance certifications", "Phase 2: Implement continuous integration automated test maps", "Phase 3: Conduct deep security vulnerability database parsing", "Phase 4: Oversee infrastructure compliance engineering centers"],
                "projects": ["Automated CI/CD Test Coverage Regression Engine", "Database Access Log Vulnerability Audit Shell"]
            },
            "Business": {
                "bonus": {"Business Analyst": 10, "Product Manager": 6, "Entrepreneur": 4},
                "roadmap": ["Phase 1: Learn operational accounting & corporate law rules", "Phase 2: Audit multi-tier inventory corporate supply charts", "Phase 3: Maintain structured financial risk ledger matrix grids", "Phase 4: Direct enterprise risk compliance divisions"],
                "projects": ["Enterprise Corporate Inventory Flow Auditor", "Structured Financial Risk Ledger Matrix Grid"]
            },
            "Healthcare": {
                "bonus": {"Pharmacist": 10, "Doctor": 7, "Medical Researcher": 6},
                "roadmap": ["Phase 1: Study rigorous medical safety regulation criteria", "Phase 2: Implement auditable pharmacy distribution pipelines", "Phase 3: Audit institutional laboratory testing safety logs", "Phase 4: Direct health system data records operations networks"],
                "projects": ["Auditable Pharmacy Distribution Tracker Core", "Laboratory Safety Compliance Log Analyzer"]
            },
            "Education": {
                "bonus": {"Education Consultant": 10, "Professor": 7, "Teacher": 6},
                "roadmap": ["Phase 1: Standardize school testing evaluation data sets", "Phase 2: Implement auditable student progress metric files", "Phase 3: Manage academic transcript archiving security structures", "Phase 4: Direct institutional school board accreditation audits"],
                "projects": ["Standardized Testing Evaluation Analytics Hub", "Secure Academic Transcript Archiving System"]
            },
            "Engineering": {
                "bonus": {"Civil Engineer": 10, "Electrical Engineer": 8, "Mechanical Engineer": 7},
                "roadmap": ["Phase 1: Master regional civil construction building codes", "Phase 2: Execute rigorous hardware wiring component validation steps", "Phase 3: Audit safety load balance records for structures", "Phase 4: Direct industrial engineering quality assurance sectors"],
                "projects": ["Civil Building Code Stress Tolerance Verifier", "Electrical Wiring Hardware Validation Matrix"]
            },
            "Creative Arts": {
                "bonus": {"Graphic Designer": 10, "Animator": 6, "Content Creator": 4},
                "roadmap": ["Phase 1: Organize high-volume asset production library catalogs", "Phase 2: Implement strict version control systems across files", "Phase 3: Verify exact printing and media scaling color outputs", "Phase 4: Manage technical production pipelines inside large design studios"],
                "projects": ["High-Volume Asset Version Control Matrix", "Technical Media Output Resolution Verifier"]
            }
        }
    },
    "ISFJ": {
        "title": "Defender", "strengths": ["Supportive", "Reliable", "Observant", "Hardworking"], "growth": ["Humble to a Fault", "Overload Themselves", "Resistant to Change"],
        "questions": [
            "Do you prefer working behind the scenes to ensure stability and care?",
            "Do you have a strong memory for specific personal details about people?",
            "Do you struggle to say no when peers look to load tasks onto your schedule?",
            "Are you highly motivated by direct loyalty and concrete helpfulness?",
            "Do you prefer predictable schedules over volatile environments?"
        ],
        "universities": ["Harvard", "Johns Hopkins", "Aga Khan University", "King Edward"],
        "diversity_map": {
            "Technology": {
                "bonus": {"Software Engineer": 10, "Cybersecurity Specialist": 7, "Data Scientist": 6},
                "roadmap": ["Phase 1: Learn interface configuration standards & usability", "Phase 2: Manage inner-office software bug tracking lists", "Phase 3: Build helpful internal company guide interfaces", "Phase 4: Manage secure user data access control registries"],
                "projects": ["Internal Corporate IT Bug Ticket Interface", "Secure User Data Access Log Registry Tracker"]
            },
            "Business": {
                "bonus": {"Business Analyst": 10, "Marketing Manager": 6, "Product Manager": 5},
                "roadmap": ["Phase 1: Coordinate team administrative support framework assets", "Phase 2: Maintain systematic client record archives neatly", "Phase 3: Monitor inner-office resource usage metric grids", "Phase 4: Direct customer satisfaction monitoring divisions"],
                "projects": ["Systematic Client Archive & Record Hub", "Inner-Office Resource Metric Monitor Base"]
            },
            "Healthcare": {
                "bonus": {"Doctor": 10, "Pharmacist": 9, "Medical Researcher": 6},
                "roadmap": ["Phase 1: Master practical bedside patient monitoring care", "Phase 2: Manage institutional medicine inventory ledger logs", "Phase 3: Keep detailed medical case history logs cleanly", "Phase 4: Direct patient welfare and support clinics networks"],
                "projects": ["Patient Case History Information Log Hub", "Medicine Inventory Ledger Access System"]
            },
            "Education": {
                "bonus": {"Teacher": 10, "Education Consultant": 8, "Professor": 5},
                "roadmap": ["Phase 1: Setup classroom homework grading organization maps", "Phase 2: Design supportive secondary tutoring materials packs", "Phase 3: Monitor individual student attendance anomaly tracks", "Phase 4: Manage local school pastoral support framework setups"],
                "projects": ["Classroom Homework Grading Management Tool", "Student Attendance Anomaly Monitor Array"]
            },
            "Engineering": {
                "bonus": {"Civil Engineer": 10, "Electrical Engineer": 7, "Mechanical Engineer": 6},
                "roadmap": ["Phase 1: Draft blueprint documentation formatting charts", "Phase 2: Verify structural maintenance checklist parameters grids", "Phase 3: Monitor hardware stress fatigue warning records", "Phase 4: Supervise facility engineering maintenance work divisions"],
                "projects": ["Engineering Blueprint File Registry Tracker", "Facility Maintenance Schedule Verification Grid"]
            },
            "Creative Arts": {
                "bonus": {"Graphic Designer": 10, "Animator": 6, "Content Creator": 5},
                "roadmap": ["Phase 1: Deliver customized layout adjustments for client briefs", "Phase 2: Maintain extensive corporate design templates sets", "Phase 3: Archive production artwork legacy libraries cleanly", "Phase 4: Manage internal asset quality checks at creative labs"],
                "projects": ["Corporate Brand Design Template Archive", "Creative Asset Quality Verification Checklist"]
            }
        }
    },
    "ESTJ": {
        "title": "Executive", "strengths": ["Dedicated", "Direct", "Organized", "Excellent Administrators"], "growth": ["Inflexible", "Uncomfortable with Unconventionality", "Too Focused on Status"],
        "questions": [
            "Do you actively create clear frameworks, rules, and structures inside unstructured groups?",
            "Is objective truth and direct truthfulness your core baseline for professional debate?",
            "Do you find chaotic, disorganized environments incredibly frustrating to operate within?",
            "Do you excel at organizing logistics, parameters, and structural deployment grids?",
            "Do you evaluate task execution strictly based on historical performance metrics?"
        ],
        "universities": ["Stanford", "Wharton", "LUMS", "IBA"],
        "diversity_map": {
            "Technology": {
                "bonus": {"Software Engineer": 10, "Cybersecurity Specialist": 9, "Data Scientist": 7},
                "roadmap": ["Phase 1: Implement strict project issue hierarchy maps", "Phase 2: Enforce precise code merge governance metrics", "Phase 3: Supervise internal engineering operations sprint tracking", "Phase 4: Command corporate enterprise IT infrastructure sectors"],
                "projects": ["Git Merge Request Governance Guard Shell", "Engineering Workspace Sprint Allocation Tool"]
            },
            "Business": {
                "bonus": {"Business Analyst": 10, "Product Manager": 8, "Marketing Manager": 7, "Entrepreneur": 6},
                "roadmap": ["Phase 1: Systematize sales operations funnel analytics steps", "Phase 2: Execute clear performance evaluation team benchmarks", "Phase 3: Manage comprehensive corporate supply procurement loops", "Phase 4: Preside as Chief Operations Officer inside target markets"],
                "projects": ["Sales Operations Funnel Analytics Manager", "Corporate Procurement Lifecycle Tracker Deck"]
            },
            "Healthcare": {
                "bonus": {"Doctor": 10, "Pharmacist": 8, "Medical Researcher": 5},
                "roadmap": ["Phase 1: Enforce clinical hygiene and protocol safety codes", "Phase 2: Manage hospital inventory supply-chain routing grids", "Phase 3: Supervise emergency medical shifts shift rosters", "Phase 4: Direct regional public hospital operations networks"],
                "projects": ["Clinical Protocol Safety Verification Shell", "Hospital Shift Roster Optimization Engine"]
            },
            "Education": {
                "bonus": {"Education Consultant": 10, "Teacher": 7, "Professor": 6},
                "roadmap": ["Phase 1: Implement rigorous school behavioral policy models", "Phase 2: Direct school examination process safety plans", "Phase 3: Enforce strict faculty reporting metrics requirements", "Phase 4: Preside as Superintendent across school network systems"],
                "projects": ["School Examination Security Procedure Matrix", "Faculty Reporting Lifecycle Metric Tracker"]
            },
            "Engineering": {
                "bonus": {"Civil Engineer": 10, "Mechanical Engineer": 8, "Electrical Engineer": 7},
                "roadmap": ["Phase 1: Supervise field site construction safety protocol charts", "Phase 2: Enforce assembly-line manufacturing volume targets", "Phase 3: Monitor engineering equipment operational longevity logs", "Phase 4: Direct major manufacturing plant engineering divisions"],
                "projects": ["Assembly-Line Manufacturing Volume Monitor", "Field Site Safety Protocol Compliance Matrix"]
            },
            "Creative Arts": {
                "bonus": {"Marketing Manager": 10, "Graphic Designer": 7, "Content Creator": 5},
                "roadmap": ["Phase 1: Enforce creative commercial client delivery deadline codes", "Phase 2: Manage complex design production vendor arrays", "Phase 3: Direct operational billing metrics across studio accounts", "Phase 4: Direct project management offices at major advertising labs"],
                "projects": ["Creative Studio Client Billing Metric Interface", "Design Production Vendor Alignment Tracker"]
            }
        }
    },
    "ESFJ": {
        "title": "Consul", "strengths": ["Loyal", "Social", "Warm", "Connecting"], "growth": ["Worried About Social Status", "Inflexible", "Vulnerable to Criticism"],
        "questions": [
            "Do you enjoy organizing interactive social activities for your peers?",
            "Do you consider the direct practical needs of your community your personal mandate?",
            "Do you feel highly motivated when group settings feel genuinely unified?",
            "Do you value active community recognition and visible social status indicators?",
            "Are you highly skilled at managing conflict resolutions gracefully?"
        ],
        "universities": ["LUMS", "IBA", "Stanford", "Harvard"],
        "diversity_map": {
            "Technology": {
                "bonus": {"Software Engineer": 10, "Product Manager": 8, "Cybersecurity Specialist": 5},
                "roadmap": ["Phase 1: Coordinate regional developer community outreach tracks", "Phase 2: Manage internal product beta testing feedback loops", "Phase 3: Oversee user-facing technology support response groups", "Phase 4: Direct customer onboarding modules for software groups"],
                "projects": ["Product Beta Feedback User Loop Sync", "User Technical Support Response Interface"]
            },
            "Business": {
                "bonus": {"Marketing Manager": 10, "Product Manager": 8, "Business Analyst": 6, "Entrepreneur": 5},
                "roadmap": ["Phase 1: Run comprehensive corporate event schedule frameworks", "Phase 2: Manage local client relations support communication portals", "Phase 3: Orchestrate brand community engagement program charts", "Phase 4: Direct customer experience networks at consumer firms"],
                "projects": ["Corporate Event Scheduling Framework Manual", "Client Relations Communication Sync Portal"]
            },
            "Healthcare": {
                "bonus": {"Doctor": 10, "Pharmacist": 8, "Medical Researcher": 5},
                "roadmap": ["Phase 1: Direct public outpatient greeting care structures", "Phase 2: Manage local community clinic outreach activities", "Phase 3: Run healthcare event coordination program grids", "Phase 4: Oversee regional patient relations network facilities"],
                "projects": ["Community Clinic Outreach Activation Portal", "Patient Experience Feedback Collection Hub"]
            },
            "Education": {
                "bonus": {"Teacher": 10, "Education Consultant": 9, "Professor": 6},
                "roadmap": ["Phase 1: Direct parent-teacher association dialogue setups", "Phase 2: Organize institutional student celebrations & panels", "Phase 3: Manage local school counseling communication files", "Phase 4: Run regional student enrichment program networks"],
                "projects": ["Parent-Teacher Association Communication Matrix", "Student Enrichment Program Registration Portal"]
            },
            "Engineering": {
                "bonus": {"Civil Engineer": 10, "Mechanical Engineer": 7, "Electrical Engineer": 6},
                "roadmap": ["Phase 1: Coordinate safety briefing programs for field crews", "Phase 2: Manage community land usage feedback panels", "Phase 3: Maintain inter-office technical crew deployment schedules", "Phase 4: Oversee public engineering infrastructure relation networks"],
                "projects": ["Field Crew Safety Briefing Program Schedule", "Community Infrastructure Impact Survey Sync"]
            },
            "Creative Arts": {
                "bonus": {"Marketing Manager": 10, "Graphic Designer": 7, "Content Creator": 6},
                "roadmap": ["Phase 1: Direct multi-client creative pitch account loops", "Phase 2: Organize design exhibition community events", "Phase 3: Maintain cross-departmental creative studio calendars", "Phase 4: Direct visual project onboarding operations sets"],
                "projects": ["Design Exhibition Event Management Tracker", "Creative Studio Account Sync Onboarding Interface"]
            }
        }
    },
    "ISTP": {
        "title": "Virtuoso", "strengths": ["Practical", "Optimistic", "Spontaneous", "Great in Crises"], "growth": ["Private", "Insensitive", "Easily Bored"],
        "questions": [
            "Do you learn best by modifying, constructing, and testing physical or software assets directly?",
            "Do you thrive during real-time systems failures or high-pressure emergencies?",
            "Do you hate restrictive micro-management and rigid bureaucratic rules?",
            "Do you look to understand how systems operate fundamentally under the hood?",
            "Do you value practical utility far more than aesthetic design?"
        ],
        "universities": ["MIT", "ETH Zurich", "NUST", "UET"],
        "diversity_map": {
            "Technology": {
                "bonus": {"Cybersecurity Specialist": 10, "Software Engineer": 9, "AI Engineer": 6, "Data Scientist": 5},
                "roadmap": ["Phase 1: Master raw hardware debugging & network routing commands", "Phase 2: Build high-performance terminal utility applications", "Phase 3: Script automated threat response server tools", "Phase 4: Direct incident response technical recovery teams"],
                "projects": ["Bare-Metal Terminal Utility Script Core", "Real-Time Server Threat Response Script Tool"]
            },
            "Business": {
                "bonus": {"Business Analyst": 10, "Product Manager": 6, "Entrepreneur": 5},
                "roadmap": ["Phase 1: Learn relational data modeling commands & SQL scripts", "Phase 2: Build custom transaction tracing dashboard systems", "Phase 3: Extract transactional bottleneck anomalies manually", "Phase 4: Direct data infrastructure diagnostic operations sectors"],
                "projects": ["SQL Transaction Tracing Data Dashboard", "Transactional Bottleneck Anomaly Extractor"]
            },
            "Healthcare": {
                "bonus": {"Pharmacist": 10, "Doctor": 7, "Medical Researcher": 6},
                "roadmap": ["Phase 1: Study bio-telemetry micro-sensor tracking hardware", "Phase 2: Calibrate specialized laboratory diagnostics machinery", "Phase 3: Maintain real-time medical device network connections", "Phase 4: Manage technical support networks inside trauma fields"],
                "projects": ["Bio-Telemetry Sensor Calibration System", "Medical Device Local Network Sync Core"]
            },
            "Education": {
                "bonus": {"Professor": 10, "Teacher": 7, "Education Consultant": 5},
                "roadmap": ["Phase 1: Prototype practical hardware learning logic blocks", "Phase 2: Script simple code evaluation automation shells", "Phase 3: Run interactive computing training lab rooms", "Phase 4: Oversee applied technical engineering trade tracks"],
                "projects": ["Automated Code Homework Evaluation Shell", "Applied Tech Logic Block Circuit Mockup"]
            },
            "Engineering": {
                "bonus": {"Mechanical Engineer": 10, "Electrical Engineer": 9, "Civil Engineer": 7},
                "roadmap": ["Phase 1: Code embedded engine diagnostic firmware files", "Phase 2: Wire real-world micro-sensor component arrays manually", "Phase 3: Stress-test structural metal stress failure limits", "Phase 4: Direct immediate on-site hardware emergency engineering centers"],
                "projects": ["Embedded Engine Diagnostic Firmware Module", "Micro-Sensor Hardware Array Wiring Grid"]
            },
            "Creative Arts": {
                "bonus": {"Animator": 10, "Graphic Designer": 7, "Content Creator": 5},
                "roadmap": ["Phase 1: Master complex 3D tracking software and rig controllers", "Phase 2: Code alternative digital visual video editing tools", "Phase 3: Construct bespoke custom camera rigging systems manually", "Phase 4: Manage engineering layout operations inside media houses"],
                "projects": ["3D Animation Rig Skeleton Bone Matrix", "Custom Video Filter Processing Pipeline Node"]
            }
        }
    },
    "ISFP": {
        "title": "Adventurer", "strengths": ["Artistic", "Imaginative", "Passionate", "Curious"], "growth": ["Fiercely Independent", "Unpredictable", "Easily Stressed"],
        "questions": [
            "Do you view your workspace as an open canvas for artistic expression?",
            "Do you follow spontaneous creative tangents rather than structured plans?",
            "Do you feel intensely restricted when locked into repetitive analytical processes?",
            "Is sensory design harmony a crucial metric for your creations?",
            "Do you require complete independence over your artistic production cycles?"
        ],
        "universities": ["RISD", "CalArts", "NCA", "AIVA"],
        "diversity_map": {
            "Technology": {
                "bonus": {"Software Engineer": 10, "AI Engineer": 6, "Data Scientist": 5},
                "roadmap": ["Phase 1: Study modern dynamic CSS frameworks & style tags", "Phase 2: Build high-fidelity web mockup interface pages", "Phase 3: Design alternative visual asset icons portfolios", "Phase 4: Run frontend asset design system architecture tracks"],
                "projects": ["Modern CSS Framework Theme System Deck", "High-Fidelity UI Presentation Web Mockup"]
            },
            "Business": {
                "bonus": {"Marketing Manager": 10, "Product Manager": 6, "Business Analyst": 4},
                "roadmap": ["Phase 1: Learn boutique brand system creation rules", "Phase 2: Craft beautiful custom commercial box packaging files", "Phase 3: Setup bespoke point-of-sale product showroom layouts", "Phase 4: Consult on experiential corporate image assets"],
                "projects": ["Boutique Brand System Visual Identity Deck", "Commercial Product Box Packaging File System"]
            },
            "Healthcare": {
                "bonus": {"Medical Researcher": 10, "Doctor": 6, "Pharmacist": 4},
                "roadmap": ["Phase 1: Research medical illustration formatting frameworks", "Phase 2: Design soothing pediatric care interior color mockups", "Phase 3: Build human anatomy visual study layout cards", "Phase 4: Consult on spatial layout design inside recovery spaces"],
                "projects": ["Anatomy Visual Identification Flashcard Deck", "Pediatric Care Room Spatial Color Palette Mock"]
            },
            "Education": {
                "bonus": {"Teacher": 10, "Education Consultant": 7, "Professor": 5},
                "roadmap": ["Phase 1: Illustrate engaging primary school book page systems", "Phase 2: Setup virtual whiteboard presentation layouts", "Phase 3: Create alternative sensory tactile craft project tutorials", "Phase 4: Manage aesthetic visual choices at ed-tech platform teams"],
                "projects": ["Primary School Textbook Page Layout Matrix", "Tactile Craft Project Sensory Guide Book"]
            },
            "Engineering": {
                "bonus": {"Mechanical Engineer": 10, "Civil Engineer": 7, "Electrical Engineer": 6},
                "roadmap": ["Phase 1: Draft organic aesthetic product enclosure geometry", "Phase 2: Model detailed 3D spatial architectural concepts", "Phase 3: Construct beautiful ergonomic physical device mockups", "Phase 4: Oversee styling decisions inside commercial tech divisions"],
                "projects": ["Organic Product Enclosure Shell Geometry CAD", "3D Spatial Architectural Layout Concept Rig"]
            },
            "Creative Arts": {
                "bonus": {"Graphic Designer": 10, "Animator": 9, "Content Creator": 8},
                "roadmap": ["Phase 1: Create beautiful original digital painting canvas layers", "Phase 2: Build immersive hand-drawn vector scene layouts", "Phase 3: Author distinct alternative typography style books", "Phase 4: Launch premium independent digital fine arts studio brands"],
                "projects": ["Immersive Hand-Drawn Scene Canvas Layout", "Custom Visual Typography System Style Book"]
            }
        }
    },
    "ESTP": {
        "title": "Entrepreneur", "strengths": ["Bold", "Direct", "Rational", "Action-Oriented"], "growth": ["Impatient", "Risk-Prone", "Misses Big Picture"],
        "questions": [
            "Do you enjoy taking direct calculation risks to capture market wins?",
            "Do you operate best in hyper-fast, dynamic, non-linear environments?",
            "Do you favor immediate real-world testing over exhaustive planning documentation?",
            "Are you highly persuasive when managing real-time human negotiations?",
            "Do you lose motivation quickly when locked into theoretical whiteboard setups?"
        ],
        "universities": ["Stanford", "Wharton", "LUMS", "IBA"],
        "diversity_map": {
            "Technology": {
                "bonus": {"Software Engineer": 10, "Cybersecurity Specialist": 8, "AI Engineer": 7},
                "roadmap": ["Phase 1: Run crash server deployment load testing matrices", "Phase 2: Deploy agile network firewall block overrides manually", "Phase 3: Build quick cross-platform field tracking app modules", "Phase 4: Command technical systems live restoration units"],
                "projects": ["Server Traffic Crash Load Generator Matrix", "Agile Cross-Platform Field Tracker Application"]
            },
            "Business": {
                "bonus": {"Entrepreneur": 10, "Marketing Manager": 9, "Product Manager": 8, "Business Analyst": 6},
                "roadmap": ["Phase 1: Close time-sensitive strategic sales pipelines", "Phase 2: Negotiate direct live seed round capitalization terms", "Phase 3: Execute fast pivot user conversion campaigns", "Phase 4: Run disruptive corporate venture creation spaces"],
                "projects": ["Live Strategic Sales Pipeline Tracker Node", "Disruptive Venture Pivot Conversion Tracker"]
            },
            "Healthcare": {
                "bonus": {"Doctor": 10, "Pharmacist": 7, "Medical Researcher": 5},
                "roadmap": ["Phase 1: Train in high-velocity trauma care operations", "Phase 2: Direct emergency triage sorting coordination systems", "Phase 3: Optimize medical response helicopter equipment setups", "Phase 4: Command urgent clinical response operations networks"],
                "projects": ["Trauma Field Triage Logic Routing Manual", "Urgent Response Helicopter Equipment Matrix"]
            },
            "Education": {
                "bonus": {"Education Consultant": 10, "Teacher": 7, "Professor": 5},
                "roadmap": ["Phase 1: Build immersive alternative outdoor logic bootcamps", "Phase 2: Direct action-oriented vocational training modules", "Phase 3: Host fast experimental competitive panel formats", "Phase 4: Lead corporate fast-track professional training systems"],
                "projects": ["Vocational Action-Oriented Course Module App", "Outdoor Tactical Logic Bootcamp Program Schedule"]
            },
            "Engineering": {
                "bonus": {"Mechanical Engineer": 10, "Electrical Engineer": 8, "Civil Engineer": 7},
                "roadmap": ["Phase 1: Calibrate extreme racing mechanical motor layouts", "Phase 2: Field repair heavy operational machinery faults fast", "Phase 3: Run immediate high-voltage circuit power connections", "Phase 4: Command immediate field engineering rescue systems"],
                "projects": ["Mechanical Racing Motor Performance Tuner", "High-Voltage Circuit Power Connection Board"]
            },
            "Creative Arts": {
                "bonus": {"Content Creator": 10, "Marketing Manager": 9, "Graphic Designer": 6},
                "roadmap": ["Phase 1: Direct fast immersive public experiential media stunts", "Phase 2: Script dynamic gorilla marketing activation events", "Phase 3: Run live high-stakes video media production arrays", "Phase 4: Lead hyper-growth media project activation taskforces"],
                "projects": ["Gorilla Marketing Stunt Activation Blueprint", "Live High-Stakes Media Production System Console"]
            }
        }
    },
    "ESFP": {
        "title": "Entertainer", "strengths": ["Bold", "Original", "Practical", "Excellent Social Skills"], "growth": ["Easily Bored", "Poor Long-Term Planner", "Unfocused"],
        "questions": [
            "Do you naturally command the energy and excitement of social settings?",
            "Do you find collaborative creative workshops highly empowering?",
            "Do you view the entire world as an open stage for interactive experiences?",
            "Do you prioritize immediate sensory excitement over long-term tracking routines?",
            "Are you exceptionally skilled at styling presentation aesthetics for high user engagement?"
        ],
        "universities": ["CalArts", "RISD", "LUMS", "IBA"],
        "diversity_map": {
            "Technology": {
                "bonus": {"Software Engineer": 10, "Product Manager": 7, "AI Engineer": 6},
                "roadmap": ["Phase 1: Learn rich multimedia canvas render animations", "Phase 2: Design highly interactive consumer gaming apps frontend", "Phase 3: Run tech conference product feature launch presentations", "Phase 4: Consult on consumer viral game mechanics design arrays"],
                "projects": ["Multimedia Canvas Render Animation Module", "Interactive Consumer Game UI Frontend Layout"]
            },
            "Business": {
                "bonus": {"Marketing Manager": 10, "Entrepreneur": 8, "Product Manager": 8, "Business Analyst": 5},
                "roadmap": ["Phase 1: Orchestrate major brand activation launch galas", "Phase 2: Create high-impact video advertising assets decks", "Phase 3: Direct social media celebrity promotion strategies", "Phase 4: Lead comprehensive creative lifestyle brand system offices"],
                "projects": ["Brand Activation Gala Launch Playbook", "High-Impact Video Ad Campaign Storyboard Deck"]
            },
            "Healthcare": {
                "bonus": {"Doctor": 10, "Pharmacist": 6, "Medical Researcher": 5},
                "roadmap": ["Phase 1: Direct youth hospital entertainment activity schedules", "Phase 2: Launch interactive digital medical awareness campaigns", "Phase 3: Coordinate high-energy rehabilitation group sessions", "Phase 4: Manage public relations for healthcare network alliances"],
                "projects": ["Youth Hospital Entertainment Activity Tracker", "Digital Health Awareness Campaign Asset Layout"]
            },
            "Education": {
                "bonus": {"Teacher": 10, "Education Consultant": 9, "Professor": 6},
                "roadmap": ["Phase 1: Author active dramatic classroom interaction scripts", "Phase 2: Host major regional student competition award nights", "Phase 3: Deploy animated video study guides globally online", "Phase 4: Lead modern educational entertainment content platforms"],
                "projects": ["Dramatic Classroom Interaction Script Playbook", "Animated Online Study Video Content Segment"]
            },
            "Engineering": {
                "bonus": {"Mechanical Engineer": 10, "Civil Engineer": 6, "Electrical Engineer": 6},
                "roadmap": ["Phase 1: Design interactive electronic consumer device exterior shells", "Phase 2: Plan immersive theme park structural attraction concepts", "Phase 3: Present bold conceptual car design presentations layouts", "Phase 4: Direct industrial design product demonstration groups"],
                "projects": ["Theme Park Structural Attraction Attraction Concept Rig", "Electronic Consumer Device Enclosure CAD Design"]
            },
            "Creative Arts": {
                "bonus": {"Content Creator": 10, "Graphic Designer": 9, "Animator": 8},
                "roadmap": ["Phase 1: Produce high-fidelity interactive media channel grids", "Phase 2: Orchestrate spectacular dynamic lighting visual sets", "Phase 3: Direct large-scale digital video cast production sets", "Phase 4: Command major contemporary digital entertainment studio houses"],
                "projects": ["Interactive Media Grid Video Production Array", "Dynamic Lighting Stage Visual Set Architecture"]
            }
        }
    }
}

# Static Academic-Career Knowledge Graphs
PATHWAYS = {
    "Technology": {
        "careers": {"AI Engineer": 82, "Software Engineer": 78, "Data Scientist": 75, "Cybersecurity Specialist": 72},
        "dream": ["MIT", "Stanford"], "strong": ["NUST", "FAST"], "affordable": ["COMSATS", "Air University"],
        "skills": ["Python", "Git", "Data Structures", "Machine Learning"],
        "resources": ["CS50", "freeCodeCamp", "Kaggle", "Andrew Ng"],
        "projects": ["AI Career Mentor", "Expense Tracker", "Study Planner"],
        "opportunities": ["Hackathons", "Coding Competitions"]
    },
    "Business": {
        "careers": {"Entrepreneur": 85, "Product Manager": 80, "Business Analyst": 74, "Marketing Manager": 70},
        "dream": ["Stanford", "Wharton"], "strong": ["LUMS", "IBA"], "affordable": ["COMSATS", "IQRA"],
        "skills": ["Leadership", "Marketing", "Communication", "Finance"],
        "resources": ["Y Combinator School", "HubSpot Academy", "Coursera"],
        "projects": ["Startup Idea Validator", "Business Planner"],
        "opportunities": ["Startup Weekends", "Business Challenges"]
    },
    "Healthcare": {
        "careers": {"Doctor": 88, "Medical Researcher": 82, "Pharmacist": 71},
        "dream": ["Harvard", "Johns Hopkins"], "strong": ["Aga Khan University", "King Edward"], "affordable": ["Public Medical Colleges"],
        "skills": ["Biology", "Research", "Clinical Communication"],
        "resources": ["Khan Academy", "PubMed", "Coursera Health"],
        "projects": ["Nutrition Tracker", "Medical Info Portal"],
        "opportunities": ["Science Olympiads", "Medical Campaigns"]
    },
    "Education": {
        "careers": {"Teacher": 80, "Professor": 78, "Education Consultant": 71},
        "dream": ["Harvard", "Oxford"], "strong": ["LUMS", "NUST"], "affordable": ["Public Universities"],
        "skills": ["Teaching", "Communication", "Curriculum Design"],
        "resources": ["Coursera", "edX", "Teaching Channel"],
        "projects": ["Quiz Gamified App", "Learning Management System"],
        "opportunities": ["Teaching Workshops", "Community Tutoring"]
    },
    "Engineering": {
        "careers": {"Mechanical Engineer": 80, "Electrical Engineer": 82, "Civil Engineer": 73},
        "dream": ["MIT", "Stanford"], "strong": ["NUST", "UET"], "affordable": ["COMSATS", "Air University"],
        "skills": ["Physics", "Mathematics", "CAD Modeling", "Design Thinking"],
        "resources": ["MIT OpenCourseWare", "Khan Academy", "Engineering Explained"],
        "projects": ["Smart Traffic System", "IoT Micro-grid Tracker"],
        "opportunities": ["Robotics Competitions", "Science Exhibitions"]
    },
    "Creative Arts": {
        "careers": {"Graphic Designer": 85, "Animator": 80, "Content Creator": 78},
        "dream": ["RISD", "CalArts"], "strong": ["NCA", "AIVA"], "affordable": ["Local Design Institutes"],
        "skills": ["UI/UX Design", "Visual Storytelling", "Adobe Creative Suite"],
        "resources": ["Canva Design School", "Figma Learn", "Behance Showcase"],
        "projects": ["Interactive Portfolio Website", "3D Motion Design Deck"],
        "opportunities": ["Design Competitions", "Art Exhibitions"]
    }
}

# ==============================================================================
# LAYOUT STRUCTURING: APPLICATION HEADER
# ==============================================================================
col_logo, col_title = st.columns([1, 11])
with col_title:
    st.title("🎓 PathPilot AI")
    st.caption("⚡ Your Intelligent AI Career Success Mentor • Built for GenZ Builders")
st.markdown("---")

# ==============================================================================
# CORE WORKFLOW ROUTING ENGINE
# ==============================================================================
if "step" not in st.session_state:
    st.session_state.step = 1
if "report_generated" not in st.session_state:
    st.session_state.report_generated = False

# ONBOARDING SURVEY WIZARD
if not st.session_state.report_generated:
    st.markdown(f"### 🚀 Step {st.session_state.step} of 4")
    progress_percent = int((st.session_state.step / 4) * 100)
    st.progress(st.session_state.step / 4, text=f"Profile Setup Tracker: {progress_percent}%")

    # Step 1: Base Core Metrics
    if st.session_state.step == 1:
        with st.container(border=True):
            st.markdown("#### 🧠 Academic Foundations")
            grade = st.selectbox("Current Academic Tier", ["O-Level", "A-Level", "FSc", "Matric", "Other"], index=0)
            interest = st.selectbox("Main Interest Core Focus Area", list(PATHWAYS.keys()), index=0)
            goal = st.text_input("What is your North Star Dream Career or Goal? (e.g., Build an AI SaaS, Eradicate Disease)")
        
        if st.button("Continue ➡️", use_container_width=True):
            if goal.strip() == "":
                st.warning("Please outline your target North Star Dream Career or Goal to initialize routing.")
            else:
                st.session_state.grade = grade
                st.session_state.interest = interest
                st.session_state.goal = goal
                st.session_state.step = 2
                st.rerun()

    # Step 2: Traits & Multi-Select Matrices
    elif st.session_state.step == 2:
        with st.container(border=True):
            st.markdown("#### 🛠 Skills & Core Competencies Matrix")
            subjects = st.multiselect("Favorite Subjects", ["Computer Science", "Mathematics", "Physics", "Chemistry", "Biology", "Business", "Economics", "Art"], default=["Computer Science", "Mathematics"])
            strengths = st.multiselect("Superpowers (Your Top Strengths)", ["Problem Solving", "Creativity", "Leadership", "Communication", "Analytical Thinking", "Teamwork"], default=["Problem Solving"])
            weaknesses = st.multiselect("Growth Areas (Skills to Level Up)", ["Programming", "Public Speaking", "Mathematics", "Time Management", "Confidence", "Writing"], default=["Time Management"])
            activities = st.multiselect("High-Energy Activities You Vibe With", ["Coding", "Building Projects", "Research", "Reading", "Business", "Teaching", "Designing"], default=["Building Projects"])
            
            leadership_raw = st.radio("Do You Vibe With Leading Teams?", ["😀 Love It", "🙂 Down for it sometimes", "😐 Prefer execution over coordination"])
            st.session_state.leadership = "Yes" if "Love" in leadership_raw else ("Sometimes" if "Down" in leadership_raw else "No")
        
        col_back, col_next = st.columns(2)
        with col_back:
            if st.button("⬅️ Back", use_container_width=True):
                st.session_state.step = 1
                st.rerun()
        with col_next:
            if st.button("Continue ➡️", use_container_width=True):
                st.session_state.subjects = subjects
                st.session_state.strengths = strengths
                st.session_state.weaknesses = weaknesses
                st.session_state.activities = activities
                st.session_state.step = 3
                st.rerun()

    # Step 3: EXTENSION MODULE - Personality Mode Route Selection
    elif st.session_state.step == 3:
        with st.container(border=True):
            st.markdown("#### 🧩 Personality Intelligence Engine Activation")
            st.write("Unlock dynamic archetype behavioral profiling to refine your mentoring metrics.")
            
            p_route = st.radio("Choose onboarding method:", [
                "Option A: I already know my personality type.",
                "Option B: I don't know my personality (Take Mini Diagnostics Assessment)."
            ])
            st.session_state.p_route = "A" if "Option A" in p_route else "B"
            
        col_back, col_next = st.columns(2)
        with col_back:
            if st.button("⬅️ Back", use_container_width=True):
                st.session_state.step = 2
                st.rerun()
        with col_next:
            if st.button("Initialize Module ➡️", use_container_width=True):
                st.session_state.step = 4
                st.rerun()

    # Step 4: EXTENSION MODULE - Personality Intelligence Engine Evaluation Execution
    elif st.session_state.step == 4:
        # ----------------------------------------------------------------------
        # OPTION A: DIRECT ARCHETYPE DISCOVERY WITH SPECIFIC CONTEXT DEEP-DIVE
        # ----------------------------------------------------------------------
        if st.session_state.p_route == "A":
            with st.container(border=True):
                st.markdown("#### Archetype Verification Tracking Pipeline")
                selected_type = st.selectbox("Select explicit structural personality signature:", list(PERSONALITY_REGISTRY.keys()))
                
                st.markdown(f"##### 🎯 Context Verification Diagnostics for **{selected_type}** Profile")
                st.caption("Fine-tune your parameter scales below:")
                
                q_list = PERSONALITY_REGISTRY[selected_type]["questions"]
                
                st.slider(f"1. {q_list[0]}", 1, 10, 5, key="p_q1")
                st.slider(f"2. {q_list[1]}", 1, 10, 5, key="p_q2")
                st.slider(f"3. {q_list[2]}", 1, 10, 5, key="p_q3")
                st.slider(f"4. {q_list[3]}", 1, 10, 5, key="p_q4")
                st.slider(f"5. {q_list[4]}", 1, 10, 5, key="p_q5")
                
            col_back, col_submit = st.columns(2)
            with col_back:
                if st.button("⬅️ Change Route", use_container_width=True):
                    st.session_state.step = 3
                    st.rerun()
            with col_submit:
                if st.button("🔥 Compile Integrated Report", type="primary", use_container_width=True):
                    st.session_state.selected_personality = selected_type
                    st.session_state.p_confidence = 100
                    st.session_state.p_rationale = "Self-reported profile validated via contextual metric verification parameters tracking grids."
                    st.session_state.report_generated = True
                    st.rerun()

        # ----------------------------------------------------------------------
        # OPTION B: 12-QUESTION VECTOR PERSONALITY DIAGNOSTIC TEST (No MBTI naming)
        # ----------------------------------------------------------------------
        else:
            with st.container(border=True):
                st.markdown("#### 🧠 Cognitive Distribution Analysis Portal")
                st.caption("Answer cleanly based on authentic operational defaults to map traits.")
                
                st.markdown("**Section 1: Energy Recharge Configurations**")
                ie1 = st.radio("Q1: After processing a highly intense week, your default method to refresh is:", ["Spend time alone in focus windows", "Sync with peer networks / group interactions"])
                ie2 = st.radio("Q2: In active design workspace sprints, you prefer:", ["Reflecting deeply in solo design periods", "Expressing concepts in open group circles"])
                ie3 = st.radio("Q3: When introduced to unvetted large networks, you typically:", ["Observe from a safe distance first", "Engage instantly with multiple nodes"])
                
                st.markdown("**Section 2: Data Processing Defaults**")
                sn1 = st.radio("Q4: When processing clean information assets, you are instinctively drawn to:", ["Observable real-world metrics & facts", "Vast abstract future concepts & macro systems"])
                sn2 = st.radio("Q5: If learning an advanced technology infrastructure track, you favor:", ["Clear real-world execution code recipes", "First-principles engineering architecture books"])
                sn3 = st.radio("Q6: Your peers value your output vectors primarily due to your:", ["Grounded functional reliability", "Unconventional innovative vision options"])
                
                st.markdown("**Section 3: Evaluation Engine Priorities**")
                tf1 = st.radio("Q7: When resolving critical strategic bottlenecks, your primary anchor metric is:", ["Cold objective tracking logic structures", "Human collaborative alignment variables"])
                tf2 = st.radio("Q8: If delivering a high-impact course critique, you emphasize:", ["Strict unvarnished error diagnosis truth", "Constructive empathetic coaching loops"])
                tf3 = st.radio("Q9: You are driven to complete assignments based on a desire for:", ["Systemic elite technical performance", "Deep personal authenticity and validation"])
                
                st.markdown("**Section 4: Project Lifecycle Execution Styles**")
                jp1 = st.radio("Q10: Your operational calendars are typically handled via:", ["Strict predictive block planning schedules", "Dynamic fluid real-time priority adaptations"])
                jp2 = st.radio("Q11: When starting long-term technical deployments, you:", ["Map all modular sub-components beforehand", "Jump straight into implementation code blocks layout"])
                jp3 = st.radio("Q12: Deadlines make you feel most optimized when they are:", ["Vetted milestones tracked well ahead", "Urgent catalysts triggering fast output at the end"])

            col_back, col_submit = st.columns(2)
            with col_back:
                if st.button("⬅️ Change Route", use_container_width=True):
                    st.session_state.step = 3
                    st.rerun()
            with col_submit:
                if st.button("🔥 Compile Cognitive Vector Profile", type="primary", use_container_width=True):
                    i_score = sum([1 for x in [ie1, ie2, ie3] if "alone" in x or "solo" in x or "Observe" in x])
                    n_score = sum([1 for x in [sn1, sn2, sn3] if "abstract" in x or "architecture" in x or "innovative" in x])
                    t_score = sum([1 for x in [tf1, tf2, tf3] if "logic" in x or "unvarnished" in x or "performance" in x])
                    j_score = sum([1 for x in [jp1, jp2, jp3] if "predictive" in x or "Map" in x or "Vetted" in x])
                    
                    computed_type = f"{'I' if i_score >= 2 else 'E'}{'N' if n_score >= 2 else 'S'}{'T' if t_score >= 2 else 'F'}{'J' if j_score >= 2 else 'P'}"
                    
                    vec_max = max(i_score, 3-i_score) + max(n_score, 3-n_score) + max(t_score, 3-t_score) + max(j_score, 3-j_score)
                    st.session_state.p_confidence = int((vec_max / 12) * 100)
                    st.session_state.selected_personality = computed_type
                    st.session_state.p_rationale = f"Profile mapped via consistent processing nodes tracking. Metrics indicate alignment with {'Introverted' if 'I' in computed_type else 'Extraverted'} {'Intuitive' if 'N' in computed_type else 'Observant'} processing paradigms."
                    st.session_state.report_generated = True
                    st.rerun()

# ==============================================================================
# ONLINE DASHBOARD EXECUTION MODE
# ==============================================================================
if st.session_state.report_generated:
    interest_data = PATHWAYS[st.session_state.interest]
    career_base_scores = interest_data["careers"].copy()
    p_code = st.session_state.selected_personality
    p_meta = PERSONALITY_REGISTRY[p_code]
    
    # FETCH UNIQUE DIVERSIFIED SUBSYSTEM PROFILE RULES
    p_diverse = p_meta["diversity_map"][st.session_state.interest]

    # INTEGRATED SCORING ENGINE (Natively Modifying Weights)
    integrated_scores = {}
    for c, base in career_base_scores.items():
        integrated_scores[c] = base

    if "Problem Solving" in st.session_state.strengths:
        for c in integrated_scores: integrated_scores[c] += 5
    if "Analytical Thinking" in st.session_state.strengths:
        for c in integrated_scores: integrated_scores[c] += 4
    if st.session_state.leadership == "Yes":
        for c in integrated_scores: integrated_scores[c] += 6

    # Inject the multi-tier personality area bonus allocation matrix rules safely
    p_bonus_map = p_diverse["bonus"]
    for c in integrated_scores:
        if c in p_bonus_map:
            integrated_scores[c] += p_bonus_map[c]

    final_ranked_careers = sorted(integrated_scores.items(), key=lambda x: x[1], reverse=True)
    top_career, top_score = final_ranked_careers[0][0], final_ranked_careers[0][1]

    # UNIVERSITY LIST BALANCING MATRIX INTERSECTION
    raw_dream_unis = interest_data["dream"]
    raw_strong_unis = interest_data["strong"]
    p_preferred_unis = p_meta["universities"]

    modified_dream = list(dict.fromkeys(p_preferred_unis + raw_dream_unis))
    modified_strong = list(dict.fromkeys(raw_strong_unis))

    readiness_score = min(40 + (len(st.session_state.strengths) * 8) + (len(st.session_state.activities) * 5), 100)
    workspace_tier = "Explorer Level 1" if readiness_score < 60 else ("Builder Level 2" if readiness_score < 80 else "Specialist Level 3")

    st.info(f"⚡ Active Workspace Platform: {workspace_tier} | Archetype Signature Matrix Key: {p_code} - {p_meta['title']}")

    # ==========================================================================
    # VISUAL RENDER NODES: 3-TAB BENTO SYSTEM LAYOUT
    # ==========================================================================
    tab_insights, tab_personality, tab_system_map = st.tabs([
        "📊 Unified Career Matrix Insights", 
        "🧩 Personality Intelligence Engine", 
        "🏛 System Execution Roadmap Maps"
    ])

    with tab_insights:
        col_c1, col_c2 = st.columns([1, 1])
        with col_c1:
            with st.container(border=True):
                st.markdown("🎯 #### Primary Vector Match Resolution")
                st.metric(label="Calculated Profile Match Index", value=f"{top_score}% Confidence")
                st.markdown(f"**Top Recommended Target Path:** `{top_career}`")
                st.markdown(f"**North Star Mission Alignment Tag:** *\"{st.session_state.goal}\"*")
            
            with st.container(border=True):
                st.markdown("##### Target Technical Skills Baseline Repositories")
                for skill in interest_data["skills"]:
                    st.markdown(f"- `🛠 {skill}`")
        
        with col_c2:
            with st.container(border=True):
                st.markdown("🚀 #### Top Integrated Competitive Match Vectors")
                st.caption("Baseline metrics altered dynamically by deep-dive personality weights maps")
                for career, score in final_ranked_careers[:3]:
                    st.markdown(f"**{career}** • Evaluation Score: `{score}`")
                    st.progress(min(score, 100) / 100)

            with st.container(border=True):
                st.markdown("🏆 #### Profile Milestone Credentials Status")
                col_m1, col_m2 = st.columns(2)
                with col_m1: st.markdown("🏅 **AI Pioneer Match**\n\n`ACTIVE`")
                with col_m2: st.markdown(f"🔥 **{p_meta['title']} Badge**\n\n`UNLOCKED`")

    with tab_personality:
        col_p1, col_p2 = st.columns([1, 1])
        with col_p1:
            with st.container(border=True):
                st.markdown(f"### 🎯 Archetype Profile: {p_code} — {p_meta['title']}")
                st.metric(label="Archetype Detection Alignment Confidence", value=f"{st.session_state.p_confidence}%")
                st.write(f"**Diagnostic Pipeline Log:** *{st.session_state.p_rationale}*")
            
            with st.container(border=True):
                st.markdown("#### 🧠 Cognitive Superpowers Mapping Tracker")
                for strength in p_meta["strengths"]:
                    st.markdown(f"✅ `✓ {strength}`")
                    
            with st.container(border=True):
                st.markdown("#### ⚠️ Growth Vectors & Mitigation Flags")
                for growth in p_meta["growth"]:
                    st.markdown(f"🚨 `• {growth}`")

        with col_p2:
            with st.container(border=True):
                st.markdown(f"#### 💡 Archetype Bonus Metrics Mapped to **{st.session_state.interest}**")
                st.caption("Points explicitly appended directly into this core interest vertical focus area:")
                for b_career, b_val in p_bonus_map.items():
                    st.markdown(f"📈 *{b_career}:* **+{b_val} Weight Target Modifier**")

            with st.container(border=True):
                st.markdown("🎨 #### Targeted Portfolio Project Directives")
                st.caption(f"Bespoke validation prompts explicitly customized for a **{p_code}** tracking **{st.session_state.interest}** paths:")
                for project in p_diverse["projects"]:
                    st.markdown(f"🚀 **{project}**")

    with tab_system_map:
        col_r1, col_r2 = st.columns([1, 1])
        with col_r1:
            with st.container(border=True):
                st.markdown(f"### 🗺 Custom Timeline Roadmap Architecture for **{p_code}** inside **{st.session_state.interest}**")
                for step in p_diverse["roadmap"]:
                    with st.status(step, state="complete"):
                        st.write("Milestone metrics verified and updated natively.")

        with col_r2:
            with st.container(border=True):
                st.markdown("### 🏛 Adaptive Institutional Systems Alignment Placement")
                st.markdown("**Tier 1 Placement Matrix (Dream Focus Systems)**")
                for uni in modified_dream: st.markdown(f"⭐ `{uni}`")
                
                st.markdown("**Tier 2 Competitive Options (High Match Foundations)**")
                for uni in modified_strong: st.markdown(f"🎯 `{uni}`")
                
                st.markdown("**Tier 3 Operational Value Matrices**")
                for uni in interest_data["affordable"]: st.markdown(f"💡 `{uni}`")

            with st.container(border=True):
                st.markdown("🌐 #### Curated Open Learning Resource Vectors")
                for res in interest_data["resources"]:
                    st.markdown(f"🔗 *[{res} Portal Connection Link](https://www.google.com/search?q={res.replace(' ', '+')}+course)*")

    # ==========================================================================
    # 4. ADVANCED MENTOR COGNITIVE INFERENCE GENERATION ENGINE
    # ==========================================================================
    st.markdown("---")
    with st.container(border=True):
        st.markdown("### 🧠 Master AI Success Mentor Counsel & Operational Directives")
        
        weaknesses_joined = ", ".join(st.session_state.weaknesses) if st.session_state.weaknesses else "None identified"
        subjects_joined = ", ".join(st.session_state.subjects) if st.session_state.subjects else "General Syllabus Core"
        strengths_joined = ", ".join(st.session_state.strengths) if st.session_state.strengths else "General Adaptability"
        
        paragraph_1 = f"""
        Greetings, Pilot. Looking closely at your validated academic configuration track framework tracking across `{st.session_state.grade}`, 
        your primary interest profile orientation toward **{st.session_state.interest}** matches seamlessly with your mapped 
        behavioral footprint signature token **{p_code} ({p_meta['title']})**. The core diagnostic execution engine indicates that your clear baseline strength markers 
        in `{strengths_joined}` provide an excellent infrastructure advantage to drive execution loops toward your explicit goal milestone destination: *\"{st.session_state.goal}\"*. 
        However, to prevent standard optimization execution failures, your identified growth tracking gaps in `{weaknesses_joined}` must be addressed through targeted technical resource allocations.
        """
        
        paragraph_2 = f"""
        To achieve high proficiency conversion status, execute your customized **{p_code}** timeline deployment pipeline meticulously. Your personality's focus 
        profile suggests that your top strategic target path matching **{top_career}** with an integrated match index metric of `{top_score}` is highly accurate. 
        Focus your upcoming developmental sprints on executing high-value portfolio frameworks such as *\"{p_diverse['projects'][0]}\"*. This method ensures you establish distinct 
        portfolio verification weight configurations when applying for admission allocations across top-tier institutional networks like **{", ".join(modified_dream[:2])}**.
        """
        
        paragraph_3 = f"""
        **AI Operational Directive Notes:** Leverage your inherent cognitive traits while reinforcing your core academic foundation pillars in `{subjects_joined}`. 
        Do not let structural constraints or operational tasks stall your forward velocity. Initialize Phase 1 of your personalized roadmap strategy track today, 
        maintain strict discipline throughout validation cycles, and focus your efforts on the highest-priority targets. You have the structural blueprints; now, go build.
        """
        
        st.markdown(f"> *{paragraph_1}*")
        st.markdown(f"> *{paragraph_2}*")
        st.markdown(f"> *{paragraph_3}*")

    # GLOBAL STATE CLEAR RESET RE-ENTRY POINT TOOL PIPELINE
    st.markdown("---")
    if st.button("🔄 Clear Profile Cache Engine & Initialize State Reset", use_container_width=True):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()

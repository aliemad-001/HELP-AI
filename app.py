import streamlit as st
import time

# ==============================================================================
# 11. COLOR SYSTEM & MODERN UI THEMING
# ==============================================================================
st.set_page_config(
    page_title="PathPilot AI",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for GenZ "Modern SaaS / Dark Mode" Aesthetic (#0F172A, #6366F1, #8B5CF6)
st.markdown("""
<style>
    /* Main app layout adjustments */
    .stApp {
        background-color: #0F172A;
        color: #F8FAFC;
    }
    
    /* Bento Box style card container */
    .bento-card {
        background-color: #1E293B;
        border: 1px solid #334155;
        border-radius: 16px;
        padding: 24px;
        margin-bottom: 20px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
        transition: transform 0.3s ease, border-color 0.3s ease;
    }
    .bento-card:hover {
        transform: translateY(-2px);
        border-color: #6366F1;
    }
    
    /* Chip element simulation */
    .chip {
        background-color: #312E81;
        color: #E0E7FF;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 14px;
        display: inline-block;
        margin-right: 8px;
        margin-bottom: 8px;
        border: 1px solid #4338CA;
    }
    
    /* Timeline style tracking */
    .timeline-node {
        border-left: 3px dashed #8B5CF6;
        padding-left: 20px;
        margin-left: 10px;
        position: relative;
        padding-bottom: 20px;
    }
    .timeline-node::before {
        content: '●';
        color: #22C55E;
        position: absolute;
        left: -8px;
        top: 0;
        font-size: 16px;
    }
    
    /* Global metric styling overrides */
    [data-testid="stMetricValue"] {
        font-size: 32px;
        font-weight: 800;
        color: #8B5CF6;
    }
</style>
""", unsafe_with_html=True)

# ==============================================================================
# SESSION STATE MANAGEMENT (Deep Component Integration)
# ==============================================================================
if "step" not in st.session_state:
    st.session_state.step = 1
if "report_generated" not in st.session_state:
    st.session_state.report_generated = False

# Static Data Pathways Repository
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
# HEADER COMPONENT (Modern SaaS Styling)
# ==============================================================================
col_logo, col_title = st.columns([1, 11])
with col_title:
    st.title("🎓 PathPilot AI")
    st.caption("⚡ Your Intelligent AI Career Success Mentor • Built for GenZ Builders")
st.markdown("---")

# ==============================================================================
# LEFT SIDE / SURVEY EXPANSION: STEP-BASED INTERACTIVE FORM
# ==============================================================================
if not st.session_state.report_generated:
    # 5. Modern Progressive Loading/Forms UI Flow
    st.markdown(f"### 🚀 Step {st.session_state.step} of 3")
    progress_val = int((st.session_state.step / 3) * 100)
    st.progress(st.session_state.step / 3, text=f"Profile Completion Status: {progress_val}%")

    # Step 1: Persona Foundations
    if st.session_state.step == 1:
        st.markdown('<div class="bento-card"><h4>🧠 Tell Us About Yourself</h4>', unsafe_with_html=True)
        
        grade = st.selectbox("Current Academic Tier", ["O-Level", "A-Level", "FSc", "Matric", "Other"])
        interest = st.selectbox("Main Interest Core Focus Area", list(PATHWAYS.keys()))
        goal = st.text_input("What is your North Star Dream Career or Goal? (e.g. Build an AI SaaS, Eradicate Disease)")
        
        st.markdown('</div>', unsafe_with_html=True)
        
        if st.button("Continue ➡️", use_container_width=True):
            st.session_state.grade = grade
            st.session_state.interest = interest
            st.session_state.goal = goal
            st.session_state.step = 2
            st.rerun()

    # Step 2: Traits & Skills

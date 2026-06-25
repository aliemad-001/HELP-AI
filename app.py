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

# Global style injection using st.html (Strictly CSS definitions only, no text layouts)
custom_css = """
<style>
    /* Main application background theme */
    .stApp {
        background-color: #0F172A;
        color: #F8FAFC;
    }
    
    /* Style Streamlit's native border container to look like our custom Bento Cards */
    [data-testid="stMetricBorderDiv"], .stElementContainer div[data-style="border"] {
        background-color: #1E293B !important;
        border: 1px solid #334155 !important;
        border-radius: 16px !important;
        padding: 20px !important;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3) !important;
    }
    
    /* Metric styling configurations */
    [data-testid="stMetricValue"] {
        font-size: 32px;
        font-weight: 800;
        color: #8B5CF6;
    }
</style>
"""
st.html(custom_css)

# ==============================================================================
# CENTRAL STATE ENGINE (Deep Integration Architecture)
# ==============================================================================
if "step" not in st.session_state:
    st.session_state.step = 1
if "report_generated" not in st.session_state:
    st.session_state.report_generated = False

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
# SURVEY MODE: USER INTERACTION STEP SYSTEM (No HTML Variant)
# ==============================================================================
if not st.session_state.report_generated:
    st.markdown(f"### 🚀 Step {st.session_state.step} of 3")
    progress_percent = int((st.session_state.step / 3) * 100)
    st.progress(st.session_state.step / 3, text=f"Profile Onboarding Status: {progress_percent}%")

    # Step 1: Base Foundations
    if st.session_state.step == 1:
        with st.container(border=True):
            st.markdown("#### 🧠 Academic Foundations")
            grade = st.selectbox("Current Academic Tier", ["O-Level", "A-Level", "FSc", "Matric", "Other"])
            interest = st.selectbox("Main Interest Core Focus Area", list(PATHWAYS.keys()))
            goal = st.text_input("What is your North Star Dream Career or Goal? (e.g., Build an AI SaaS, Eradicate Disease)")
        
        if st.button("Continue ➡️", use_container_width=True):
            st.session_state.grade = grade
            st.session_state.interest = interest
            st.session_state.goal = goal
            st.session_state.step = 2
            st.rerun()

    # Step 2: Superpowers & Traits
    elif st.session_state.step == 2:
        with st.container(border=True):
            st.markdown("#### 🛠 Skills & Core Competencies Matrix")
            subjects = st.multiselect("Favorite Subjects", ["Computer Science", "Mathematics", "Physics", "Chemistry", "Biology", "Business", "Economics", "Art"])
            strengths = st.multiselect("Superpowers (Your Top Strengths)", ["Problem Solving", "Creativity", "Leadership", "Communication", "Analytical Thinking", "Teamwork"])
            weaknesses = st.multiselect("Growth Areas (Skills to Level Up)", ["Programming", "Public Speaking", "Mathematics", "Time Management", "Confidence", "Writing"])
            activities = st.multiselect("High-Energy Activities You Vibe With", ["Coding", "Building Projects", "Research", "Reading", "Business", "Teaching", "Designing"])
            
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

    # Step 3: Psychology Layer (MBTI Integration)
    elif st.session_state.step == 3:
        with st.container(border=True):
            st.markdown("#### 🧩 Psychological Alignment Blueprint (Optional)")
            use_personality = st.toggle("Activate MBTI Personality Intelligence Matching Pipeline")
            
            personality = None
            if use_personality:
                personality = st.selectbox("Select Your Explicit MBTI Personality Signature Profile", ["ENTP", "INTJ", "INFJ", "ESTP"])
                st.markdown("##### Fine-Tune Your Dynamic Drivers")
                if personality == "ENTP":
                    st.slider("Interest in Moonshot Startups", 1, 10, 5, key="startup_interest")
                    st.slider("Interest in Deep AI Architectures", 1, 10, 5, key="ai_interest")
                elif personality == "INTJ":
                    st.slider("Inclination Towards Macro Long-Term Architecture Planning", 1, 10, 5, key="planning_interest")
                elif personality == "INFJ":
                    st.slider("Drive for High Social Impact Projects", 1, 10, 5, key="social_impact")
                elif personality == "ESTP":
                    st.slider("Risk Tolerance Status Blueprint", 1, 10, 5, key="risk_taking")
        
        col_back, col_submit = st.columns(2)
        with col_back:
            if st.button("⬅️ Back", use_container_width=True):
                st.session_state.step = 2
                st.rerun()
        with col_submit:
            if st.button("🔥 Compile My Personalized Identity Platform", type="primary", use_container_width=True):
                st.session_state.personality = personality
                
                # Dynamic Loader Interaction Feedback
                status_box = st.empty()
                with status_box.container():
                    with st.container(border=True):
                        with st.spinner("🤖 Triggering Core Matrix Engines..."):
                            time.sleep(0.5)
                        st.toast("⚡ Parsing Intersecting Data Matrices... Completed", icon="✅")
                        time.sleep(0.4)
                        st.toast("🔮 Injecting Gamification Framework Parameters... Completed", icon="🏆")
                        time.sleep(0.4)
                        st.toast("🎯 Formulating Interactive Mentorship Pathways... Ready", icon="💡")
                
                status_box.empty()
                st.session_state.report_generated = True
                st.rerun()

# ==============================================================================
# DASHBOARD MODE: REAL-TIME INTERACTIVE STUDENT INSIGHTS PORTAL
# ==============================================================================
if st.session_state.report_generated:
    data = PATHWAYS[st.session_state.interest]
    career_scores = data["careers"].copy()
    
    # Algorithmic Scoring Intersect Engine Execution
    if "Problem Solving" in st.session_state.strengths:
        for c in career_scores: career_scores[c] += 5
    if "Analytical Thinking" in st.session_state.strengths:
        for c in career_scores: career_scores[c] += 4
    if st.session_state.leadership == "Yes":
        for c in career_scores: career_scores[c] += 6
        
    ranked_careers = sorted(career_scores.items(), key=lambda x: x[1], reverse=True)
    top_career, top_score = ranked_careers[0][0], ranked_careers[0][1]
    
    # Live Readiness Computations
    readiness_score = min(40 + (len(st.session_state.strengths) * 8) + (len(st.session_state.activities) * 5), 100)
    user_level = "Explorer Level 1" if readiness_score < 60 else ("Builder Level 2" if readiness_score < 80 else "Specialist Level 3")

    # Global Live Notification Banner Strip (Parser-safe native component)
    target_goal = st.session_state.goal if st.session_state.goal else 'General Premium Track'
    st.info(f"⚡ Active Workspace: {user_level} | 🎯 North Star Goal: {target_goal}")
    
    # Modern App Tabs Structure
    tab_dashboard, tab_university, tab_roadmap = st.tabs(["📊 Career Insights Matrix", "🏛 University Systems Map", "🗺 Interactive Execution Timeline"])
    
    with tab_dashboard:
        col_left_panel, col_right_panel = st.columns([1, 1])
        
        with col_left_panel:
            with st.container(border=True):
                st.subheader("🎯 Primary Matched Target Profile")
                st.metric(label="Career Readiness Quotient Index", value=f"{readiness_score}/100")
                
                st.markdown("##### Operational Competency Profile Flags")
                # Completely safe, text-only tag style layout using clear markdown
                for strength in st.session_state.strengths:
                    st.write(f"✨ **{strength}**")
            
            with st.container(border=True):
                st.markdown("### 🧠 Autonomous AI Mentor Recommendation Advice")
                st.markdown(f"""
                > *"Based on your clear technical proficiency markers, and matching high affinity metrics towards **{st.session_state.interest}**, 
                the pipeline has validated **{top_career}** as your absolute highest conversion career track. Your core mastery index 
                suggests that shifting resources towards optimizing growth weaknesses like `{', '.join(st.session_state.weaknesses)}` will amplify 
                your portfolio authority indexes globally across target top-tier ecosystems."*
                """)

        with col_right_panel:
            with st.container(border=True):
                st.subheader("🚀 Top High-Match Career Vector Metrics")
                for career, score in ranked_careers[:3]:
                    norm_score = min(score, 100)
                    st.markdown(f"**{career}** • Match Confidence Index: `{norm_score}%`")
                    st.progress(norm_score / 100)
            
            with st.container(border=True):
                st.subheader("🏆 Earned Profile Badges & Milestones")
                col_b1, col_b2, col_b3 = st.columns(3)
                with col_b1: st.markdown("🏅 **AI Explorer**\n\n`UNLOCKED`")
                with col_b2: st.markdown("🔥 **High Bio-Affinity**\n\n`LOCKED`" if "Biology" not in st.session_state.subjects else "🔥 **Bio Pioneer**\n\n`UNLOCKED`")
                with col_b3: st.markdown("🚀 **Founder Track**\n\n`UNLOCKED`" if st.session_state.leadership == "Yes" else "📋 **Strategist**\n\n`UNLOCKED`")

    with tab_university:
        with st.container(border=True):
            st.markdown("### 🎓 Global & Regional Institutional Alignment Target Tiers")
            col_u1, col_u2, col_u3 = st.columns(3)
            with col_u1:
                st.markdown("🏆 **Tier 1 Alpha (Dream Global)**")
                for uni in data["dream"]: st.markdown(f"⭐ `{uni}`")
            with col_u2:
                st.markdown("🎯 **Tier 2 High Affinity (Competitive Match)**")
                for uni in data["strong"]: st.markdown(f"⚡ `{uni}`")
            with col_u3:
                st.markdown("💡 **Tier 3 Value Optimized Target Matrix**")
                for uni in data["affordable"]: st.markdown(f"✅ `{uni}`")

    with tab_roadmap:
        with st.container(border=True):
            st.markdown("### 🗺 Linear Strategic Learning Roadmap Timeline Generation")
            
            # Using clean, cloud-native status wrappers
            with st.status("📅 Phase 1: Present Foundation Build Phase (Next 90 Days)", state="complete"):
                st.write("Master base core fundamentals directly connected with your choice preferences.")
            with st.status("🚀 Phase 2: Portfolio Aggregation Optimization (Months 3 - 6)", state="complete"):
                st.write("Construct 2-3 production scale modular verified build projects.")
            with st.status("🏆 Phase 3: Network Authority Leverage Scaling (Months 6 - 12)", state="complete"):
                st.write("Compete directly across massive technical hackathons and target external regional ecosystem opportunities.")
            
            st.markdown("#### 🛠 Focused Target Hard Skills Repositories To Build")
            for skill in data["skills"]:
                st.markdown(f"- **`{skill}`**")
                
            st.markdown("#### 🌐 Curated Open-Source Open Learning Platform Pathways")
            for res in data["resources"]:
                st.markdown(f"🔗 *[{res} Global Training Portal Link](https://www.google.com/search?q={res.replace(' ', '+')}+course)*")

    # Cache reset button
    if st.button("🔄 Clear Profile Cache Engine & Initialize State Reset", use_container_width=True):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()

import streamlit as st
import time

# ==============================================================================
# COLOR SYSTEM & MODERN UI CONFIGURATION (Parser-Safe Architecture)
# ==============================================================================
st.set_page_config(
    page_title="PathPilot AI",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Using st.html to safely apply dark-mode bento aesthetics without breaking the markdown parser
custom_css = """
<style>
    /* Main application background theme */
    .stApp {
        background-color: #0F172A;
        color: #F8FAFC;
    }
    
    /* Bento Box UI containers */
    .bento-card {
        background-color: #1E293B;
        border: 1px solid #334155;
        border-radius: 16px;
        padding: 24px;
        margin-bottom: 20px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
    }
    
    /* GenZ-style tag chips */
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
    
    /* Interactive success timeline track */
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
# SURVEY MODE: USER INTERACTION STEP SYSTEM
# ==============================================================================
if not st.session_state.report_generated:
    st.markdown(f"### 🚀 Step {st.session_state.step} of 3")
    progress_percent = int((st.session_state.step / 3) * 100)
    st.progress(st.session_state.step / 3, text=f"Profile Onboarding Status: {progress_percent}%")

    # Step 1: Base Foundations
    if st.session_state.step == 1:
        st.markdown('<div class="bento-card"><h4>🧠 Academic Foundations</h4>', unsafe_with_html=True)
        grade = st.selectbox("Current Academic Tier", ["O-Level", "A-Level", "FSc", "Matric", "Other"])
        interest = st.selectbox("Main Interest Core Focus Area", list(PATHWAYS.keys()))
        goal = st.text_input("What is your North Star Dream Career or Goal? (e.g., Build an AI SaaS, Eradicate Disease)")
        st.markdown('</div>', unsafe_with_html=True)
        
        if st.button("Continue ➡️", use_container_width=True):
            st.session_state.grade = grade
            st.session_state.interest = interest
            st.session_state.goal = goal
            st.session_state.step = 2
            st.rerun()

    # Step 2: Superpowers & Traits
    elif st.session_state.step == 2:
        st.markdown('<div class="bento-card"><h4>🛠 Skills & Core Competencies Matrix</h4>', unsafe_with_html=True)
        subjects = st.multiselect("Favorite Subjects", ["Computer Science", "Mathematics", "Physics", "Chemistry", "Biology", "Business", "Economics", "Art"])
        strengths = st.multiselect("Superpowers (Your Top Strengths)", ["Problem Solving", "Creativity", "Leadership", "Communication", "Analytical Thinking", "Teamwork"])
        weaknesses = st.multiselect("Growth Areas (Skills to Level Up)", ["Programming", "Public Speaking", "Mathematics", "Time Management", "Confidence", "Writing"])
        activities = st.multiselect("High-Energy Activities You Vibe With", ["Coding", "Building Projects", "Research", "Reading", "Business", "Teaching", "Designing"])
        
        leadership_raw = st.radio("Do You Vibe With Leading Teams?", ["😀 Love It", "🙂 Down for it sometimes", "😐 Prefer execution over coordination"])
        st.session_state.leadership = "Yes" if "Love" in leadership_raw else ("Sometimes" if "Down" in leadership_raw else "No")
        st.markdown('</div>', unsafe_with_html=True)
        
        col_back, col_next = st.columns(2)
        with col_back:
            if st.button("⬅️ Back"):
                st.session_state.step = 1
                st.rerun()
        with col_next:
            if st.button("Continue ➡️"):
                st.session_state.subjects = subjects
                st.session_state.strengths = strengths
                st.session_state.weaknesses = weaknesses
                st.session_state.activities = activities
                st.session_state.step = 3
                st.rerun()

    # Step 3: Psychology Layer (MBTI Integration)
    elif st.session_state.step == 3:
        st.markdown('<div class="bento-card"><h4>🧩 Psychological Alignment Blueprint (Optional)</h4>', unsafe_with_html=True)
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
        st.markdown('</div>', unsafe_with_html=True)
        
        col_back, col_submit = st.columns(2)
        with col_back:
            if st.button("⬅️ Back"):
                st.session_state.step = 2
                st.rerun()
        with col_submit:
            if st.button("🔥 Compile My Personalized Identity Ecosystem Platform", type="primary", use_container_width=True):
                st.session_state.personality = personality
                
                # Dynamic Loader Interaction Feedback
                status_box = st.empty()
                with status_box.container():
                    st.markdown('<div class="bento-card">', unsafe_with_html=True)
                    with st.spinner("🤖 Triggering Core Matrix Engines..."):
                        time.sleep(0.5)
                    st.toast("⚡ Parsing Intersecting Data Matrices... Completed", icon="✅")
                    time.sleep(0.4)
                    st.toast("🔮 Injecting Gamification Framework Parameters... Completed", icon="🏆")
                    time.sleep(0.4)
                    st.toast("🎯 Formulating Interactive Mentorship Pathways... Ready", icon="💡")
                    st.markdown('</div>', unsafe_with_html=True)
                
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

    # Global Live Notification Banner Strip
    st.markdown(f"""
    <div style="background: linear-gradient(90deg, #6366F1, #8B5CF6); border-radius:12px; padding:16px; margin-bottom:25px;">
        <h4 style="margin:0; color:white;">⚡ Active Session Hub Profile Workspace: {user_level}</h4>
        <p style="margin:0; color:#E0E7FF; font-size:14px;">Target Goal Destination Flag: "{st.session_state.goal if st.session_state.goal else 'General Premium Track'}"</p>
    </div>
    """, unsafe_with_html=True)
    
    # Modern App Tabs Structure
    tab_dashboard, tab_university, tab_roadmap = st.tabs(["📊 Career Insights Matrix", "🏛 University Systems Map", "🗺 Interactive Execution Timeline"])
    
    with tab_dashboard:
        col_left_panel, col_right_panel = st.columns([1, 1])
        
        with col_left_panel:
            st.markdown('<div class="bento-card">', unsafe_with_html=True)
            st.subheader("🎯 Primary Matched Target Profile")
            st.metric(label="Career Readiness Quotient Index", value=f"{readiness_score}/100")
            
            st.markdown("##### Operational Competency Profile Flags")
            for strength in st.session_state.strengths:
                st.markdown(f'<span class="chip">✨ {strength}</span>', unsafe_with_html=True)
            st.markdown('</div>', unsafe_with_html=True)
            
            st.markdown('<div class="bento-card">', unsafe_with_html=True)
            st.markdown("### 🧠 Autonomous AI Mentor Recommendation Advice")
            st.markdown(f"""
            > *"Based on your clear technical proficiency markers, and matching high affinity metrics towards **{st.session_state.interest}**, 
            the pipeline has validated **{top_career}** as your absolute highest conversion career track. Your core mastery index 
            suggests that shifting resources towards optimizing growth weaknesses like `{', '.join(st.session_state.weaknesses)}` will amplify 
            your portfolio authority indexes globally across target top-tier ecosystems."*
            """)
            st.markdown('</div>', unsafe_with_html=True)

        with col_right_panel:
            st.markdown('<div class="bento-card">', unsafe_with_html=True)
            st.subheader("🚀 Top High-Match Career Vector Metrics")
            for career, score in ranked_careers[:3]:
                norm_score = min(score, 100)
                st.markdown(f"**{career}** • Match Confidence Index: `{norm_score}%`")
                st.progress(norm_score / 100)
            st.markdown('</div>', unsafe_with_html=True)
            
            st.markdown('<div class="bento-card">', unsafe_with_html=True)
            st.subheader("🏆 Earned Profile Badges & Milestones")
            col_b1, col_b2, col_b3 = st.columns(3)
            with col_b1: st.markdown("🏅 **AI Explorer**\n\n`UNLOCKED`")
            with col_b2: st.markdown("🔥 **High Bio-Affinity**\n\n`LOCKED`" if "Biology" not in st.session_state.subjects else "🔥 **Bio Pioneer**\n\n`UNLOCKED`")
            with col_b3: st.markdown("🚀 **Founder Track**\n\n`UNLOCKED`" if st.session_state.leadership == "Yes" else "📋 **Strategist**\n\n`UNLOCKED`")
            st.markdown('</div>', unsafe_with_html=True)

    with tab_university:
        st.markdown('<div class="bento-card">', unsafe_with_html=True)
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
        st.markdown('</div>', unsafe_with_html=True)

    with tab_roadmap:
        st.markdown('<div class="bento-card">', unsafe_with_html=True)
        st.markdown("### 🗺 Linear Strategic Learning Roadmap Timeline Generation")
        st.markdown("""
        <div class="timeline-node">
            <h5 style='margin:0; color:#8B5CF6;'>Phase 1: Present Foundation Build Phase (Next 90 Days)</h5>
            <p style='margin:0; font-size:14px; color:#94A3B8;'>Master base core fundamentals directly connected with your choice preferences.</p>
        </div>
        <div class="timeline-node">
            <h5 style='margin:0; color:#8B5CF6;'>Phase 2: Portfolio Aggregation Optimization (Months 3 - 6)</h5>
            <p style='margin:0; font-size:14px; color:#94A3B8;'>Construct 2-3 production scale modular verified build projects.</p>
        </div>
        <div class="timeline-node">
            <h5 style='margin:0; color:#8B5CF6;'>Phase 3: Network Authority Leverage Scaling (Months 6 - 12)</h5>
            <p style='margin:0; font-size:14px; color:#94A3B8;'>Compete directly across massive technical hackathons and target external regional ecosystem opportunities.</p>
        </div>
        """, unsafe_with_html=True)
        
        st.markdown("#### 🛠 Focused Target Hard Skills Repositories To Build")
        for skill in data["skills"]:
            st.markdown(f"- **`{skill}`**")
            
        st.markdown("#### 🌐 Curated Open-Source Open Learning Platform Pathways")
        for res in data["resources"]:
            st.markdown(f"🔗 *[{res} Global Training Portal Link](https://www.google.com/search?q={res.replace(' ', '+')}+course)*")
        st.markdown('</div>', unsafe_with_html=True)

    # Cache reset button
    if st.button("🔄 Clear Profile Cache Engine & Initialize State Reset"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()

import streamlit as st

st.set_page_config(page_title="PathPilot AI v2.0", page_icon="🎓", layout="wide")

st.title("🎓 PathPilot AI v2.0")
st.subheader("Your Personalized Student Success Mentor")

PATHWAYS = {
    "Technology": {
        "careers": {"AI Engineer": 60, "Software Engineer": 58, "Data Scientist": 55, "Cybersecurity Specialist": 52},
        "dream": ["MIT", "Stanford"],
        "strong": ["NUST", "FAST"],
        "affordable": ["COMSATS", "Air University"],
        "skills": ["Python", "Git", "Data Structures", "Machine Learning", "Project Building"],
        "resources": ["CS50", "freeCodeCamp", "Kaggle", "Andrew Ng Courses"],
        "projects": ["AI Career Mentor", "Expense Tracker", "Study Planner"],
        "opportunities": ["Hackathons", "Coding Competitions", "Science Fairs"]
    },
    "Business": {
        "careers": {"Entrepreneur": 60, "Product Manager": 58, "Business Analyst": 56, "Marketing Manager": 54},
        "dream": ["Stanford", "Wharton"],
        "strong": ["LUMS", "IBA"],
        "affordable": ["COMSATS", "Air University"],
        "skills": ["Leadership", "Marketing", "Communication", "Finance"],
        "resources": ["Y Combinator Startup School", "HubSpot Academy", "Coursera Business"],
        "projects": ["Startup Idea Validator", "Business Planner", "Marketing Dashboard"],
        "opportunities": ["Startup Weekends", "Business Challenges"]
    },
    "Healthcare": {
        "careers": {"Doctor": 60, "Medical Researcher": 58, "Pharmacist": 55},
        "dream": ["Harvard", "Johns Hopkins"],
        "strong": ["Aga Khan University", "KEMU"],
        "affordable": ["Public Medical Colleges"],
        "skills": ["Biology", "Research", "Communication"],
        "resources": ["Khan Academy", "PubMed"],
        "projects": ["Nutrition Tracker", "Health Awareness Website"],
        "opportunities": ["Science Olympiads", "Research Competitions"]
    },
    "Education": {
        "careers": {"Teacher": 60, "Professor": 57, "Education Consultant": 54},
        "dream": ["Harvard", "Oxford"],
        "strong": ["LUMS", "NUST"],
        "affordable": ["Public Universities"],
        "skills": ["Teaching", "Communication", "Leadership"],
        "resources": ["Coursera", "edX"],
        "projects": ["Quiz App", "Learning Platform"],
        "opportunities": ["Teaching Workshops", "Community Tutoring"]
    },
    "Engineering": {
        "careers": {"Mechanical Engineer": 60, "Electrical Engineer": 60, "Civil Engineer": 56},
        "dream": ["MIT", "Stanford"],
        "strong": ["NUST", "UET"],
        "affordable": ["COMSATS", "Air University"],
        "skills": ["Physics", "Mathematics", "Design Thinking"],
        "resources": ["MIT OpenCourseWare", "Khan Academy"],
        "projects": ["Smart Traffic System", "Engineering Calculator"],
        "opportunities": ["Robotics Competitions", "Engineering Challenges"]
    },
    "Creative Arts": {
        "careers": {"Graphic Designer": 60, "Animator": 57, "Content Creator": 55},
        "dream": ["RISD", "CalArts"],
        "strong": ["NCA", "AIVA"],
        "affordable": ["Local Design Institutes"],
        "skills": ["Design", "Creativity", "Storytelling"],
        "resources": ["Canva Design School", "Figma Learn"],
        "projects": ["Portfolio Website", "Animation Showcase"],
        "opportunities": ["Design Competitions", "Art Exhibitions"]
    }
}

grade = st.selectbox("Grade", ["O-Level", "A-Level", "FSc", "Matric", "Other"])
subjects = st.multiselect("Favorite Subjects", ["Computer Science","Mathematics","Physics","Chemistry","Biology","Business","Economics","English","Art"])
interest = st.selectbox("Main Interest Area", list(PATHWAYS.keys()))
strengths = st.multiselect("Your Strengths", ["Problem Solving","Creativity","Leadership","Communication","Analytical Thinking","Teamwork"])
activities = st.multiselect("Activities You Enjoy", ["Coding","Building Projects","Research","Reading","Business","Teaching","Sports","Designing"])
leadership = st.selectbox("Do You Enjoy Leading Teams?", ["Yes","Sometimes","No"])
goal = st.text_input("Dream Career or Goal")

if st.button("Generate My Career Report"):
    data = PATHWAYS[interest]
    scores = data["careers"].copy()

    for trait in ["Problem Solving", "Analytical Thinking", "Leadership"]:
        if trait in strengths:
            for c in scores:
                scores[c] += 5

    if leadership == "Yes":
        for c in scores:
            scores[c] += 5

    ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    top3 = ranked[:3]

    readiness = min(100, 40 + len(strengths)*8 + len(activities)*6)

    st.success("Career Report Generated")
    c1, c2, c3 = st.columns(3)
    c1.metric("Career Readiness", f"{readiness}%")
    c2.metric("Top Career", top3[0][0])
    c3.metric("Skills To Learn", len(data["skills"]))

    st.header("🏆 Top Career Matches")
    for career, score in top3:
        st.write(f"**{career}**")
        st.progress(min(score,100)/100)
        st.write(f"{score}% match")

    st.header("🎓 Universities")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader("Dream")
        st.write(data["dream"])
    with col2:
        st.subheader("Strong")
        st.write(data["strong"])
    with col3:
        st.subheader("Affordable")
        st.write(data["affordable"])

    st.header("🛠 Skills")
    for s in data["skills"]:
        st.write("•", s)

    st.header("🚀 Projects")
    for p in data["projects"]:
        st.write("•", p)

    if goal:
        st.info(f"Goal: {goal}")

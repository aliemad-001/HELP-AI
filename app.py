import streamlit as st

st.set_page_config(page_title="PathPilot AI", page_icon="🎓", layout="wide")

st.title("🎓 PathPilot AI")
st.subheader("Personalized Career Mentor for Students")

st.markdown("Answer the questions below to receive a personalized career report.")

grade = st.selectbox("Grade", ["O-Level", "A-Level", "FSc", "Matric", "Other"])

subjects = st.multiselect(
    "Favorite Subjects",
    ["Computer Science", "Mathematics", "Physics", "Chemistry", "Biology",
     "Business", "Economics", "English", "Art"]
)

interest = st.selectbox(
    "Main Interest Area",
    ["Technology", "Business", "Healthcare", "Education", "Engineering", "Creative Arts"]
)

strengths = st.multiselect(
    "Your Strengths",
    ["Problem Solving", "Creativity", "Leadership", "Communication",
     "Analytical Thinking", "Teamwork"]
)

weaknesses = st.multiselect(
    "Skills to Improve",
    ["Programming", "Public Speaking", "Mathematics",
     "Time Management", "Confidence", "Writing"]
)

activities = st.multiselect(
    "Activities You Enjoy",
    ["Coding", "Building Projects", "Research", "Reading",
     "Business", "Teaching", "Sports", "Designing"]
)

leadership = st.selectbox(
    "Do you enjoy leading teams?",
    ["Yes", "Sometimes", "No"]
)

goal = st.text_input("Dream Career or Goal")

if st.button("Generate My Career Report"):

    pathways = {
        "Technology": {
            "careers": {
                "AI Engineer": 60,
                "Software Engineer": 60,
                "Data Scientist": 55,
                "Cybersecurity Specialist": 50
            },
            "dream": ["MIT", "Stanford"],
            "strong": ["NUST", "FAST"],
            "affordable": ["COMSATS", "Air University"],
            "skills": ["Python", "Data Structures", "Projects", "Machine Learning"],
            "resources": [
                "freeCodeCamp",
                "W3Schools",
                "Kaggle",
                "Andrew Ng AI Courses"
            ]
        },
        "Business": {
            "careers": {
                "Entrepreneur": 60,
                "Product Manager": 55,
                "Business Analyst": 55,
                "Marketing Manager": 50
            },
            "dream": ["Stanford", "Wharton"],
            "strong": ["LUMS", "IBA"],
            "affordable": ["COMSATS", "Air University"],
            "skills": ["Leadership", "Communication", "Marketing", "Finance Basics"],
            "resources": [
                "Y Combinator Startup School",
                "HubSpot Academy",
                "Coursera Business Courses"
            ]
        },
        "Healthcare": {
            "careers": {
                "Doctor": 60,
                "Medical Researcher": 55,
                "Pharmacist": 50
            },
            "dream": ["Harvard", "Johns Hopkins"],
            "strong": ["Aga Khan University", "King Edward Medical University"],
            "affordable": ["Public Medical Colleges"],
            "skills": ["Biology", "Research", "Communication"],
            "resources": ["Khan Academy Biology", "PubMed", "Coursera Health Courses"]
        },
        "Education": {
            "careers": {
                "Teacher": 60,
                "Professor": 55,
                "Education Consultant": 50
            },
            "dream": ["Harvard", "Oxford"],
            "strong": ["LUMS", "NUST"],
            "affordable": ["Public Universities"],
            "skills": ["Teaching", "Communication", "Leadership"],
            "resources": ["edX", "Coursera", "Teaching Channel"]
        },
        "Engineering": {
            "careers": {
                "Mechanical Engineer": 60,
                "Electrical Engineer": 60,
                "Civil Engineer": 55
            },
            "dream": ["MIT", "Stanford"],
            "strong": ["NUST", "UET"],
            "affordable": ["COMSATS", "Air University"],
            "skills": ["Physics", "Mathematics", "Design Thinking"],
            "resources": ["MIT OpenCourseWare", "Khan Academy", "Engineering Explained"]
        },
        "Creative Arts": {
            "careers": {
                "Graphic Designer": 60,
                "Animator": 55,
                "Content Creator": 55
            },
            "dream": ["RISD", "CalArts"],
            "strong": ["NCA", "AIVA"],
            "affordable": ["Local Design Institutes"],
            "skills": ["Design", "Creativity", "Storytelling"],
            "resources": ["Canva Design School", "Figma Learn", "Adobe Tutorials"]
        }
    }

    data = pathways[interest]
    career_scores = data["careers"].copy()

    if "Problem Solving" in strengths:
        for c in career_scores:
            career_scores[c] += 5

    if "Leadership" in strengths or leadership == "Yes":
        for c in career_scores:
            career_scores[c] += 5

    if "Analytical Thinking" in strengths:
        for c in career_scores:
            career_scores[c] += 5

    if "Coding" in activities and interest == "Technology":
        career_scores["AI Engineer"] += 10
        career_scores["Software Engineer"] += 10

    if "Mathematics" in subjects and interest in ["Technology", "Engineering"]:
        for c in career_scores:
            career_scores[c] += 5

    ranked = sorted(career_scores.items(), key=lambda x: x[1], reverse=True)

    st.success("Your PathPilot Career Report")

    st.header("👤 Student Profile")

    profile = []
    if "Problem Solving" in strengths:
        profile.append("Strong problem solver")
    if "Creativity" in strengths:
        profile.append("Creative thinker")
    if "Leadership" in strengths:
        profile.append("Leadership potential")
    if "Analytical Thinking" in strengths:
        profile.append("Analytical mindset")

    if profile:
        for p in profile:
            st.write("✅", p)

    st.header("🚀 Career Match Scores")

    for career, score in ranked:
        st.write(f"### {career}")
        st.progress(min(score, 100) / 100)
        st.write(f"Match Score: {min(score,100)}%")

    st.header("🎓 University Recommendations")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("Dream")
        for u in data["dream"]:
            st.write("⭐", u)

    with col2:
        st.subheader("Strong Options")
        for u in data["strong"]:
            st.write("🎯", u)

    with col3:
        st.subheader("Affordable")
        for u in data["affordable"]:
            st.write("💡", u)

    st.header("📚 Skills Roadmap")

    roadmap = [
        "Next 3 Months: Learn fundamentals",
        "Next 6 Months: Build projects",
        "Next 12 Months: Develop advanced skills",
        "University Phase: Specialize and gain experience"
    ]

    for item in roadmap:
        st.write("✅", item)

    st.header("🛠 Skills to Focus On")

    for skill in data["skills"]:
        st.write("📌", skill)

    st.header("🌐 Learning Resources")

    for resource in data["resources"]:
        st.write("🔗", resource)

    st.header("💪 Improve Your Strengths")

    tips = {
        "Problem Solving": "Practice challenges and real projects.",
        "Creativity": "Design, write, build, and experiment regularly.",
        "Leadership": "Lead clubs, events, and group projects.",
        "Communication": "Practice speaking and writing frequently.",
        "Analytical Thinking": "Solve puzzles and analyze case studies.",
        "Teamwork": "Work on collaborative projects."
    }

    for s in strengths:
        if s in tips:
            st.write(f"**{s}:** {tips[s]}")

    st.header("📖 Show Interest in Your Subjects")

    subject_tips = {
        "Computer Science": "Build projects and create a GitHub portfolio.",
        "Mathematics": "Join competitions and solve advanced problems.",
        "Physics": "Participate in science fairs and experiments.",
        "Biology": "Read research and join science clubs.",
        "Business": "Start small projects and learn entrepreneurship.",
        "Art": "Build a portfolio and publish your work."
    }

    for subject in subjects:
        if subject in subject_tips:
            st.write(f"**{subject}:** {subject_tips[subject]}")

    st.header("💡 Personalized Advice")

    st.info(
        f"You are interested in {interest}. Focus on building practical skills, creating projects, and exploring opportunities related to your goals. Stay consistent and keep learning."
    )

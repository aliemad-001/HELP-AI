import streamlit as st

st.set_page_config(
    page_title="PathPilot AI",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 PathPilot AI")
st.subheader("Your Personalized Student Success Mentor")

st.markdown("""
Discover career paths, universities, skills, projects,
and opportunities tailored specifically for you.
""")

# =========================
# USER INPUTS
# =========================

grade = st.selectbox(
    "Grade",
    ["O-Level", "A-Level", "FSc", "Matric", "Other"]
)

subjects = st.multiselect(
    "Favorite Subjects",
    [
        "Computer Science",
        "Mathematics",
        "Physics",
        "Chemistry",
        "Biology",
        "Business",
        "Economics",
        "English",
        "Art"
    ]
)

interest = st.selectbox(
    "Main Interest Area",
    [
        "Technology",
        "Business",
        "Healthcare",
        "Education",
        "Engineering",
        "Creative Arts"
    ]
)

strengths = st.multiselect(
    "Your Strengths",
    [
        "Problem Solving",
        "Creativity",
        "Leadership",
        "Communication",
        "Analytical Thinking",
        "Teamwork"
    ]
)

weaknesses = st.multiselect(
    "Skills To Improve",
    [
        "Programming",
        "Public Speaking",
        "Mathematics",
        "Time Management",
        "Confidence",
        "Writing"
    ]
)

activities = st.multiselect(
    "Activities You Enjoy",
    [
        "Coding",
        "Building Projects",
        "Research",
        "Reading",
        "Business",
        "Teaching",
        "Sports",
        "Designing"
    ]
)

leadership = st.selectbox(
    "Do You Enjoy Leading Teams?",
    [
        "Yes",
        "Sometimes",
        "No"
    ]
)

goal = st.text_input(
    "Dream Career or Goal"
)

# =========================
# MAIN BUTTON
# =========================

if st.button("Generate My Career Report"):

    pathways = {

        "Technology": {

            "careers": {
                "AI Engineer": 60,
                "Software Engineer": 58,
                "Data Scientist": 55,
                "Cybersecurity Specialist": 52
            },

            "dream": [
                "MIT",
                "Stanford"
            ],

            "strong": [
                "NUST",
                "FAST"
            ],

            "affordable": [
                "COMSATS",
                "Air University"
            ],

            "skills": [
                "Python",
                "Git",
                "Data Structures",
                "Machine Learning",
                "Project Building"
            ],

            "resources": [
                "CS50",
                "freeCodeCamp",
                "Kaggle",
                "Andrew Ng Courses"
            ],

            "projects": [
                "AI Career Mentor",
                "Expense Tracker",
                "Study Planner"
            ],

            "opportunities": [
                "Hackathons",
                "Coding Competitions",
                "Science Fairs"
            ]
        },

        "Business": {

            "careers": {
                "Entrepreneur": 60,
                "Product Manager": 58,
                "Business Analyst": 56,
                "Marketing Manager": 54
            },

            "dream": [
                "Stanford",
                "Wharton"
            ],

            "strong": [
                "LUMS",
                "IBA"
            ],

            "affordable": [
                "COMSATS",
                "Air University"
            ],

            "skills": [
                "Leadership",
                "Marketing",
                "Communication",
                "Finance"
            ],

            "resources": [
                "Y Combinator Startup School",
                "HubSpot Academy",
                "Coursera Business"
            ],

            "projects": [
                "Startup Idea Validator",
                "Business Planner",
                "Marketing Dashboard"
            ],

            "opportunities": [
                "Startup Weekends",
                "Business Challenges",
                "Entrepreneurship Competitions"
            ]
        },

        "Healthcare": {

            "careers": {
                "Doctor": 60,
                "Medical Researcher": 58,
                "Pharmacist": 55
            },

            "dream": [
                "Harvard",
                "Johns Hopkins"
            ],

            "strong": [
                "Aga Khan University",
                "King Edward Medical University"
            ],

            "affordable": [
                "Public Medical Colleges"
            ],

            "skills": [
                "Biology",
                "Research",
                "Communication"
            ],

            "resources": [
                "Khan Academy",
                "PubMed",
                "Coursera Health"
            ],

            "projects": [
                "Nutrition Tracker",
                "Medical Information Portal",
                "Health Awareness Website"
            ],

            "opportunities": [
                "Science Olympiads",
                "Research Competitions",
                "Medical Campaigns"
            ]
        },
   "Education": {

        "careers": {
            "Teacher": 60,
            "Professor": 57,
            "Education Consultant": 54
        },

        "dream": [
            "Harvard",
            "Oxford"
        ],

        "strong": [
            "LUMS",
            "NUST"
        ],

        "affordable": [
            "Public Universities"
        ],

        "skills": [
            "Teaching",
            "Communication",
            "Leadership"
        ],

        "resources": [
            "Coursera",
            "edX",
            "Teaching Channel"
        ],

        "projects": [
            "Quiz App",
            "Learning Platform",
            "Student Progress Tracker"
        ],

        "opportunities": [
            "Teaching Workshops",
            "Debates",
            "Community Tutoring"
        ]
    },

    "Engineering": {

        "careers": {
            "Mechanical Engineer": 60,
            "Electrical Engineer": 60,
            "Civil Engineer": 56
        },

        "dream": [
            "MIT",
            "Stanford"
        ],

        "strong": [
            "NUST",
            "UET"
        ],

        "affordable": [
            "COMSATS",
            "Air University"
        ],

        "skills": [
            "Physics",
            "Mathematics",
            "Design Thinking"
        ],

        "resources": [
            "MIT OpenCourseWare",
            "Khan Academy",
            "Engineering Explained"
        ],

        "projects": [
            "Smart Traffic System",
            "Energy Tracker",
            "Engineering Calculator"
        ],

        "opportunities": [
            "Robotics Competitions",
            "Engineering Challenges",
            "Science Exhibitions"
        ]
    },

    "Creative Arts": {

        "careers": {
            "Graphic Designer": 60,
            "Animator": 57,
            "Content Creator": 55
        },

        "dream": [
            "RISD",
            "CalArts"
        ],

        "strong": [
            "NCA",
            "AIVA"
        ],

        "affordable": [
            "Local Design Institutes"
        ],

        "skills": [
            "Design",
            "Creativity",
            "Storytelling"
        ],

        "resources": [
            "Canva Design School",
            "Figma Learn",
            "Adobe Tutorials"
        ],

        "projects": [
            "Portfolio Website",
            "Animation Showcase",
            "Creator Dashboard"
        ],

        "opportunities": [
            "Design Competitions",
            "Art Exhibitions",
            "Content Creation Challenges"
        ]
    }
}

data = pathways[interest]

career_scores = data["careers"].copy()

# =========================
# SMART SCORING ENGINE
# =========================

if "Problem Solving" in strengths:
    for c in career_scores:
        career_scores[c] += 5

if "Analytical Thinking" in strengths:
    for c in career_scores:
        career_scores[c] += 5

if "Leadership" in strengths:
    for c in career_scores:
        career_scores[c] += 5

if leadership == "Yes":
    for c in career_scores:
        career_scores[c] += 5

if "Coding" in activities and interest == "Technology":
    career_scores["AI Engineer"] += 10
    career_scores["Software Engineer"] += 10

if "Business" in activities and interest == "Business":
    career_scores["Entrepreneur"] += 10

if "Research" in activities and interest == "Healthcare":
    career_scores["Medical Researcher"] += 10

if "Teaching" in activities and interest == "Education":
    career_scores["Teacher"] += 10

if "Designing" in activities and interest == "Creative Arts":
    career_scores["Graphic Designer"] += 10

if "Mathematics" in subjects:
    for c in career_scores:
        career_scores[c] += 3

ranked = sorted(
    career_scores.items(),
    key=lambda x: x[1],
    reverse=True
)

top_three = ranked[:3]

top_career = ranked[0][0]
top_score = ranked[0][1]

# =========================
# CAREER READINESS SCORE
# =========================

readiness_score = 40

readiness_score += len(strengths) * 8
readiness_score += len(activities) * 6

if leadership == "Yes":
    readiness_score += 10

elif leadership == "Sometimes":
    readiness_score += 5

if len(subjects) >= 2:
    readiness_score += 10

readiness_score = min(
    readiness_score,
    100
)

st.success("Your PathPilot Career Report")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Career Readiness",
        f"{readiness_score}/100"
    )

with col2:
    st.metric(
        "Top Career",
        top_career
    )

with col3:
    st.metric(
        "Skills To Learn",
        len(data["skills"])
    )

# =========================
# STUDENT PROFILE
# =========================

st.header("👤 Student Profile")

profile = []

if "Problem Solving" in strengths:
    profile.append("Strong Problem Solver")

if "Creativity" in strengths:
    profile.append("Creative Thinker")

if "Leadership" in strengths:
    profile.append("Leadership Potential")

if "Analytical Thinking" in strengths:
    profile.append("Analytical Mindset")

if len(profile) == 0:
    profile.append("Developing Student")

for item in profile:
    st.write("✅", item)

# =========================
# BEST CAREER MATCH
# =========================

st.header("🏆 Best Career Match")

st.success(
    f"{top_career} ({top_score}%)"
)

# =========================
# TOP 3 CAREERS
# =========================

st.header("🚀 Top Career Matches")

for career, score in top_three:

    st.subheader(career)

    st.progress(
        min(score, 100) / 100
    )

    st.write(
        f"Match Score: {min(score,100)}%"
    )

# =========================
# WHY IT MATCHES
# =========================

st.header("🧠 Why These Careers Match You")

reasons = []

if "Problem Solving" in strengths:
    reasons.append(
        "You enjoy solving problems."
    )

if "Analytical Thinking" in strengths:
    reasons.append(
        "You think logically."
    )

if "Leadership" in strengths:
    reasons.append(
        "You show leadership potential."
    )

if "Coding" in activities:
    reasons.append(
        "You enjoy building solutions."
    )

if "Research" in activities:
    reasons.append(
        "You enjoy learning deeply."
    )

if "Creativity" in strengths:
    reasons.append(
        "You enjoy creating new ideas."
    )

for reason in reasons:
    st.write("✅", reason)

# =========================
# UNIVERSITYS
# =========================

st.header("🎓 University Recommendations")

col1, col2, col3 = st.columns(3)

with col1:

    st.subheader("Dream")

    for uni in data["dream"]:
        st.write("⭐", uni)

with col2:

    st.subheader("Strong Options")

    for uni in data["strong"]:
        st.write("🎯", uni)

with col3:

    st.subheader("Affordable")

    for uni in data["affordable"]:
        st.write("💡", uni)

# =========================
# ROADMAP
# =========================

st.header("📚 Success Roadmap")

roadmap = [

    "Next 3 Months: Learn fundamentals",

    "Next 6 Months: Build 2-3 projects",

    "Next 12 Months: Join competitions and strengthen portfolio",

    "University Phase: Specialize and gain practical experience"

]

for step in roadmap:
    st.write("✅", step)

# =========================
# SKILLS
# =========================

st.header("🛠 Skills To Focus On")

for skill in data["skills"]:
    st.write("📌", skill)

# =========================
# RESOURCES
# =========================

st.header("🌐 Learning Resources")

for resource in data["resources"]:
    st.write("🔗", resource)

# =========================
# PROJECTS
# =========================

st.header("🚀 Suggested Portfolio Projects")

for project in data["projects"]:
    st.write("🚀", project)

# =========================
# OPPORTUNITIES
# =========================

st.header("🏆 Competitions & Opportunities")

for opportunity in data["opportunities"]:
    st.write("⭐", opportunity)

# =========================
# STRENGTH IMPROVEMENT
# =========================

st.header("💪 Improve Your Strengths")

tips = {

    "Problem Solving":
    "Solve real-world problems and projects.",

    "Creativity":
    "Design, write, build, and experiment.",

    "Leadership":
    "Lead clubs, teams, and events.",

    "Communication":
    "Practice public speaking and writing.",

    "Analytical Thinking":
    "Analyze case studies and solve puzzles.",

    "Teamwork":
    "Work on collaborative projects."
}

for strength in strengths:

    if strength in tips:

        st.write(
            f"**{strength}:** {tips[strength]}"
        )

# =========================
# SUBJECT INTEREST
# =========================

st.header("📖 Show Interest In Your Subjects")

subject_tips = {

    "Computer Science":
    "Build projects and create a GitHub portfolio.",

    "Mathematics":
    "Join competitions and solve advanced problems.",

    "Physics":
    "Participate in science fairs and experiments.",

    "Biology":
    "Read research and join science clubs.",

    "Business":
    "Start mini-business projects and study startups.",

    "Art":
    "Build a portfolio and publish your work."
}

for subject in subjects:

    if subject in subject_tips:

        st.write(
            f"**{subject}:** {subject_tips[subject]}"
        )

# =========================
# PERSONALIZED ADVICE
# =========================

st.header("💡 Personalized Advice")

advice = []

if "Programming" in weaknesses:
    advice.append(
        "Practice coding consistently every week."
    )

if "Time Management" in weaknesses:
    advice.append(
        "Use a planner and set weekly goals."
    )

if "Public Speaking" in weaknesses:
    advice.append(
        "Join debates and presentations."
    )

if "Confidence" in weaknesses:
    advice.append(
        "Take on small leadership opportunities."
    )

if len(advice) == 0:
    advice.append(
        "Keep building projects and exploring opportunities."
    )

for item in advice:
    st.write("✅", item)

# =========================
# GOAL SECTION
# =========================

if goal:

    st.header("🎯 Your Goal")

    st.info(
        f"Your goal is '{goal}'. Focus your skills, projects, and learning activities around this objective."
    )

    st.success(
        "PathPilot recommends building a portfolio aligned with this goal."
    )


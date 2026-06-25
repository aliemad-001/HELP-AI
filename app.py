import streamlit as st

st.set_page_config(
    page_title="PathPilot AI",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 PathPilot AI")
st.subheader("Your Personalized Career Mentor")

st.markdown("---")

# Basic Information

grade = st.selectbox(
    "What grade are you in?",
    ["O-Level", "A-Level", "FSc", "Matric", "Other"]
)

subjects = st.multiselect(
    "Select your favorite subjects",
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
    "Which area interests you the most?",
    [
        "Technology",
        "Business",
        "Healthcare",
        "Education",
        "Engineering",
        "Creative Arts"
    ]
)

work_style = st.selectbox(
    "What do you enjoy most?",
    [
        "Building Things",
        "Helping People",
        "Research",
        "Leading Teams",
        "Designing"
    ]
)

goal = st.text_input(
    "What is your dream career or goal?"
)

# New Personalized Questions

st.markdown("---")
st.markdown("## Tell us more about yourself")

strengths = st.multiselect(
    "What are your strengths?",
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
    "What skills would you like to improve?",
    [
        "Public Speaking",
        "Programming",
        "Mathematics",
        "Time Management",
        "Confidence",
        "Writing"
    ]
)

activities = st.multiselect(
    "What activities do you enjoy?",
    [
        "Coding",
        "Building Projects",
        "Reading",
        "Research",
        "Sports",
        "Business",
        "Teaching",
        "Designing"
    ]
)

leadership = st.selectbox(
    "Do you enjoy leading teams?",
    [
        "Yes",
        "Sometimes",
        "No"
    ]
)

if st.button("Generate Career Report"):

    careers = []
    universities = []
    skills = []

    # Technology Path

    if interest == "Technology":

        careers = [
            "AI Engineer",
            "Software Engineer",
            "Data Scientist",
            "Cybersecurity Specialist"
        ]

        universities = [
            "MIT",
            "Stanford",
            "NUST",
            "FAST"
        ]

        skills = [
            "Python",
            "Problem Solving",
            "Data Structures",
            "Machine Learning",
            "Building Projects"
        ]

    # Business Path

    elif interest == "Business":

        careers = [
            "Entrepreneur",
            "Product Manager",
            "Business Analyst",
            "Marketing Manager"
        ]

        universities = [
            "LUMS",
            "Stanford",
            "Wharton",
            "IBA"
        ]

        skills = [
            "Communication",
            "Leadership",
            "Finance Basics",
            "Marketing",
            "Startup Skills"
        ]

    # Healthcare Path

    elif interest == "Healthcare":

        careers = [
            "Doctor",
            "Researcher",
            "Pharmacist"
        ]

        universities = [
            "Aga Khan University",
            "King Edward Medical University"
        ]

        skills = [
            "Biology",
            "Research",
            "Communication"
        ]

    # Education Path

    elif interest == "Education":

        careers = [
            "Teacher",
            "Professor",
            "Education Consultant"
        ]

        universities = [
            "Harvard",
            "Oxford",
            "LUMS"
        ]

        skills = [
            "Communication",
            "Teaching",
            "Leadership"
        ]

    # Engineering Path

    elif interest == "Engineering":

        careers = [
            "Mechanical Engineer",
            "Electrical Engineer",
            "Civil Engineer"
        ]

        universities = [
            "MIT",
            "NUST",
            "UET"
        ]

        skills = [
            "Physics",
            "Mathematics",
            "Design Thinking"
        ]

    # Creative Arts Path

    else:

        careers = [
            "Graphic Designer",
            "Animator",
            "Content Creator"
        ]

        universities = [
            "RISD",
            "NCA",
            "AIVA"
        ]

        skills = [
            "Creativity",
            "Design",
            "Communication"
        ]

    st.success("Your Personalized Career Report")

    # Student Profile

    st.markdown("## 👤 Student Profile")

    profile = []

    if "Problem Solving" in strengths:
        profile.append("Strong problem solver")

    if "Creativity" in strengths:
        profile.append("Creative thinker")

    if "Leadership" in strengths:
        profile.append("Natural leader")

    if "Analytical Thinking" in strengths:
        profile.append("Analytical mindset")

    if leadership == "Yes":
        profile.append("Shows leadership potential")

    if "Coding" in activities:
        profile.append("Enjoys technology and building solutions")

    if profile:
        for item in profile:
            st.write("✅", item)

    # Career Matches

    st.markdown("## 🚀 Career Matches")

    for career in careers:
        st.write("🎯", career)

    # Universities

    st.markdown("## 🎓 Recommended Universities")

    for uni in universities:
        st.write("🏛️", uni)

    # Skills Roadmap

    st.markdown("## 📚 Skills Roadmap")

    for skill in skills:
        st.write("📌", skill)

    # Areas for Improvement

    if weaknesses:

        st.markdown("## 📈 Areas for Growth")

        for weakness in weaknesses:
            st.write("🔹 Improve:", weakness)

    # Advice

    st.markdown("## 💡 Personalized Advice")

    st.info(
        f"""
Based on your interest in {interest}, strengths, and activities,
you should focus on building practical skills, creating projects,
and exploring opportunities related to your chosen field.

Keep learning consistently and stay curious.
"""
    )

    st.balloons()

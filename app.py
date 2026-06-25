import streamlit as st

st.set_page_config(
    page_title="PathPilot AI",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 PathPilot AI")
st.subheader("Personalized Career Guidance for Students")

st.markdown("---")

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
    "Which area interests you most?",
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

if st.button("Generate Career Plan"):

    careers = []
    universities = []
    skills = []

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

    st.success("Your Personalized Career Report")

    st.markdown("## Career Matches")

    for career in careers:
        st.write("✅", career)

    st.markdown("## Recommended Universities")

    for uni in universities:
        st.write("🎓", uni)

    st.markdown("## Skills Roadmap")

    for skill in skills:
        st.write("📚", skill)

    st.markdown("## Advice")

    st.info(
        f"Based on your interest in {interest}, you should focus on building relevant skills and projects. Start early and explore opportunities related to your goals."
    )

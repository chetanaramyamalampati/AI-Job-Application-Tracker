import streamlit as st
import pandas as pd
from src.skill_extractor import extract_skills
from src.email_generator import generate_follow_up_email

st.set_page_config(page_title="AI Job Application Tracker", layout="wide")

st.title("AI Job Application Tracker")

uploaded_file = st.file_uploader("Upload job applications CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
else:
    df = pd.DataFrame(columns=["company", "title", "status", "date_applied", "job_description"])

st.subheader("Applications")
st.dataframe(df, use_container_width=True)

if not df.empty:
    st.subheader("Application Status Count")
    st.bar_chart(df["status"].value_counts())

    all_skills = []
    for jd in df["job_description"].fillna(""):
        all_skills.extend(extract_skills(jd))

    st.subheader("Skills Found in Job Descriptions")
    st.write(", ".join(sorted(set(all_skills))))

    selected_company = st.selectbox("Generate follow-up email for company", df["company"].unique())
    selected_row = df[df["company"] == selected_company].iloc[0]

    if st.button("Generate Follow-Up Email"):
        email = generate_follow_up_email(selected_row["company"], selected_row["title"])
        st.text_area("Follow-Up Email", email, height=220)

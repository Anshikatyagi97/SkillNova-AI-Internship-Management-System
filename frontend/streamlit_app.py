"""
SkillNova AI Internship Management System — Streamlit Frontend (for testing)

This is a minimal, multi-page Streamlit app used to manually exercise
the backend APIs during development. It is NOT the production frontend
for SkillNova — that will be built separately by the Web Development team.

Run with:
    streamlit run frontend/streamlit_app.py

Pages (see frontend/pages/):
    1_Intern_Profile.py
    2_Mentor_Dashboard.py
    3_Analytics.py
    4_Certificate_Checker.py
    5_GitHub_Analyzer.py

TODO (Interns):
- Once the backend endpoints return real data, remove the placeholder
  fallback values used throughout these pages.
"""

import streamlit as st
from utils.api_client import get

st.set_page_config(page_title="SkillNova AI Internship System", page_icon="🎓", layout="wide")

st.title("🎓 SkillNova — AI Internship Management System")
st.caption("Starter template dashboard. Use the sidebar to navigate to a specific view.")

st.markdown(
    """
    Welcome! This is the **home / overview page** of the testing frontend.

    Use the pages in the left sidebar to explore:
    - **Intern Profile** — progress tracker for a single intern
    - **Mentor Dashboard** — AI insights for mentors
    - **Analytics** — platform-wide analytics
    - **Certificate Checker** — certificate eligibility lookup
    - **GitHub Analyzer** — analyze a GitHub repository

    > ⚠️ This project ships with **dummy/placeholder data**. Backend
    > endpoints will return real AI-generated insights once the
    > TODOs in `ai_modules/` and `backend/services/` are implemented.
    """
)

st.divider()
st.subheader("Backend Connectivity Check")

health = get("/health")
if health:
    st.success(f"✅ Connected to backend: {health}")
else:
    st.error(
        "❌ Could not reach the backend. Make sure it's running:\n\n"
        "`uvicorn backend.main:app --reload`"
    )

# TODO (Interns): Add a quick summary widget here once /api/analytics
# returns real data (e.g. total interns, active interns, health score).

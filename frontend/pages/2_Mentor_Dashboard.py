"""Streamlit page: Mentor Dashboard — stats and AI insights for mentors."""

import streamlit as st
from utils.api_client import get

st.set_page_config(page_title="Mentor Dashboard", page_icon="🧑‍🏫", layout="wide")
st.title("🧑‍🏫 AI Mentor Dashboard")

mentor_name = st.text_input("Filter by mentor name (optional)")

data = get("/api/mentor-dashboard", params={"mentor_name": mentor_name} if mentor_name else None)

if data and data.get("data"):
    stats = data["data"]

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Interns", stats.get("total_interns", 0))
    col2.metric("Active", stats.get("active_interns", 0))
    col3.metric("Inactive", stats.get("inactive_interns", 0))
    col4.metric("Pending Submissions", stats.get("pending_submissions", 0))

    st.subheader("🏆 Top Performers")
    st.table(stats.get("top_performers", []))

    st.subheader("⚠️ Weak Performers")
    st.table(stats.get("weak_performers", []))

    st.subheader("🤖 AI Alerts")
    for alert in stats.get("ai_alerts", []):
        st.info(alert)

    st.subheader("💡 Mentor Recommendations")
    for rec in stats.get("mentor_recommendations", []):
        st.success(rec)
else:
    st.error("Could not load mentor dashboard data from the backend.")

# TODO (Interns): Once ai_modules/mentor_dashboard is implemented, the
# "AI Alerts" section should show real, dynamically-generated insights
# instead of the placeholder TODO strings.

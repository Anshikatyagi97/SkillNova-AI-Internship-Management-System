"""Streamlit page: Platform-wide Analytics Dashboard."""

import streamlit as st
import pandas as pd
from utils.api_client import get

st.set_page_config(page_title="Analytics Dashboard", page_icon="📊", layout="wide")
st.title("📊 Internship Analytics Dashboard")

data = get("/api/analytics")

if data and data.get("data"):
    stats = data["data"]

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Interns", stats.get("total_interns", 0))
    col2.metric("Active Interns", stats.get("active_interns", 0))
    col3.metric("Completion %", stats.get("internship_completion_percentage", 0))
    col4.metric("Health Score", stats.get("overall_health_score", 0))

    st.subheader("🌐 Domain-wise Distribution")
    domain_data = stats.get("domain_wise_distribution", [])
    if domain_data:
        df = pd.DataFrame(domain_data)
        st.bar_chart(df.set_index("domain"))
    else:
        st.info("No domain distribution data available yet.")

    st.subheader("👩‍🏫 Mentor Workload")
    st.table(stats.get("mentor_workload", []))

    st.subheader("🤖 AI Insights")
    insights = stats.get("ai_insights", {})
    st.write("**Weekly Summary:**", insights.get("weekly_summary", ""))
    st.write("**Batch Performance Report:**", insights.get("batch_performance_report", ""))
    st.write("**Department Statistics:**", insights.get("department_statistics", ""))
else:
    st.error("Could not load analytics data from the backend.")

# TODO (Interns): Add filters for batch / domain / date range once the
# backend supports query parameters for scoped analytics.

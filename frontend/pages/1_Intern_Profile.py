"""Streamlit page: Intern Profile — progress, attendance, task recommendations."""

import streamlit as st
from utils.api_client import get

st.set_page_config(page_title="Intern Profile", page_icon="👤")
st.title("👤 Intern Profile")

intern_id = st.text_input("Enter Intern ID (e.g. INT-0001)", value="INT-0001")

if st.button("Load Profile"):
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📈 Progress")
        progress = get(f"/api/progress/{intern_id}")
        if progress and progress.get("data"):
            st.json(progress["data"])
        else:
            st.warning("No data returned. Showing placeholder.")
            st.json({"completion_percentage": 0, "note": "TODO: backend not returning real data yet."})

    with col2:
        st.subheader("🗓️ Attendance")
        attendance = get(f"/api/attendance/{intern_id}")
        if attendance and attendance.get("data"):
            st.json(attendance["data"])
        else:
            st.warning("No data returned. Showing placeholder.")
            st.json({"attendance_percentage_overall": 0, "note": "TODO: backend not returning real data yet."})

    st.subheader("🎯 Task Recommendations")
    recs = get(f"/api/task-recommendations/{intern_id}")
    if recs and recs.get("data"):
        st.json(recs["data"])
    else:
        st.warning("No data returned. Showing placeholder.")

# TODO (Interns): Replace text_input with a dropdown populated from
# GET /api/mentor-dashboard or a dedicated /api/interns list endpoint.

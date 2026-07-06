"""Streamlit page: Certificate Eligibility Checker."""

import streamlit as st
from utils.api_client import get

st.set_page_config(page_title="Certificate Checker", page_icon="🎓")
st.title("🎓 Certificate Eligibility Checker")

intern_id = st.text_input("Enter Intern ID", value="INT-0001")

if st.button("Check Eligibility"):
    data = get(f"/api/certificate/{intern_id}")
    if data and data.get("data"):
        result = data["data"]
        status = result.get("status", "Unknown")

        if status == "Eligible":
            st.success(f"✅ Status: {status}")
        elif status == "Not Eligible":
            st.error(f"❌ Status: {status}")
        else:
            st.warning(f"⚠️ Status: {status}")

        st.write("**Explanation:**")
        st.write(result.get("explanation", ""))
    else:
        st.error("Could not load certificate data from the backend.")

# TODO (Interns): Once ai_modules/certificate_analyzer is implemented,
# also display the underlying metrics (attendance %, completion %,
# GitHub score, etc.) that fed into the decision, for transparency.

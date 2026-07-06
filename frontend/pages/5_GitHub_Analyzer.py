"""Streamlit page: GitHub Repository Analyzer."""

import streamlit as st
from utils.api_client import post

st.set_page_config(page_title="GitHub Analyzer", page_icon="🐙")
st.title("🐙 AI GitHub & Code Review Assistant")

repo_url = st.text_input("Enter a GitHub repository URL", value="https://github.com/example/repo")

if st.button("Analyze Repository"):
    data = post("/api/github-analysis", json_body={"repo_url": repo_url})
    if data and data.get("data"):
        result = data["data"]

        col1, col2, col3 = st.columns(3)
        col1.metric("Commits", result.get("commits", 0))
        col2.metric("README Score", result.get("readme_score", 0))
        col3.metric("Code Quality", result.get("code_quality_score", 0))

        st.subheader("🤖 AI Suggestions")
        for suggestion in result.get("suggestions", []):
            st.info(suggestion)
    else:
        st.error("Could not load GitHub analysis from the backend.")

# TODO (Interns): Once ai_modules/github_analyzer is implemented, replace
# the dummy commit/readme/code-quality scores with real GitHub API data.

"""
AI GitHub & Code Review Assistant - Service Layer

TODO (Interns):
1. Implement `analyze_repository()` - fetch repo metadata via the
   GitHub API (commits, branches, README presence, file structure).
2. Implement `score_readme_quality()`.
3. Implement `score_code_quality()` - could use static analysis tools
   (e.g. pylint/flake8 output) as a starting signal.
4. Implement `generate_git_suggestions()` - natural-language suggestions.
"""

from typing import Dict, List


def analyze_repository(repo_url: str) -> Dict:
    """
    Analyze a GitHub repository submitted by an intern.

    TODO: Use the GitHub REST API (requests + a GitHub token) to fetch:
          - commit history / commit frequency
          - branch list
          - presence and length of README.md
          - folder/file structure
    """
    return {
        "repo_url": repo_url,
        "commits": 0,
        "branches": 0,
        "readme_score": 0.0,
        "doc_score": 0.0,
        "code_quality_score": 0.0,
        "completeness_score": 0.0,
    }


def score_readme_quality(readme_text: str) -> float:
    """
    Score README quality on a 0-10 scale.

    TODO: Consider length, presence of sections (Installation, Usage,
          Screenshots), and clarity. Could use an LLM to grade this.
    """
    return 0.0


def score_code_quality(repo_url: str) -> float:
    """
    Score overall code quality on a 0-10 scale.

    TODO: Consider running static analysis (pylint/flake8) or asking
          an LLM to review a sample of files.
    """
    return 0.0


def generate_git_suggestions(repo_analysis: Dict) -> List[str]:
    """
    Turn a repo analysis dict into actionable suggestions, e.g.:
      "Improve documentation", "Increase commit frequency",
      "Follow better Git practices", "Improve project structure".

    TODO: Implement rule-based suggestions first (thresholds on each
          score), then optionally polish the phrasing with an LLM.
    """
    return ["TODO: AI-generated Git/GitHub suggestion goes here."]

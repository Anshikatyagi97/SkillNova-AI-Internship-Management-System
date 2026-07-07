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
from backend.ai.llm_service import llm

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

def generate_ai_repository_summary(
    repo_url: str,
    commits: int,
    branches: int,
    readme_score: float,
    code_quality_score: float,
) -> str:
    """
    Generate AI-powered GitHub repository review.
    """

    prompt = f"""
You are an expert Software Engineering Mentor.

Repository:
{repo_url}

Statistics:

Commits: {commits}

Branches: {branches}

README Score: {readme_score}/10

Code Quality Score: {code_quality_score}/10

Write a professional repository review.

Include:
- Repository health
- Documentation quality
- Code quality
- Suggestions for improvement

Keep the response within 4-5 sentences.
"""

    return llm.generate_response(prompt)


def calculate_repository_health(
    readme_score: float,
    code_quality_score: float,
) -> str:
    """
    Calculate repository health.
    """

    average = (
        readme_score +
        code_quality_score
    ) / 2

    if average >= 8:
        return "Excellent"

    elif average >= 6:
        return "Good"

    elif average >= 4:
        return "Average"

    return "Needs Improvement"


def generate_repository_recommendations(
    readme_score: float,
    code_quality_score: float,
) -> List[str]:
    """
    Generate repository improvement suggestions.
    """

    recommendations = []

    if readme_score < 7:
        recommendations.append(
            "Improve README with installation and usage instructions."
        )

    if code_quality_score < 7:
        recommendations.append(
            "Improve code structure and follow coding standards."
        )

    if not recommendations:
        recommendations.append(
            "Repository is well maintained. Keep following best practices."
        )

    return recommendations
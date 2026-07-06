"""Helper utilities for the GitHub Analyzer AI module."""


def extract_repo_owner_and_name(repo_url: str) -> tuple:
    """
    Parse a GitHub URL like https://github.com/owner/repo into (owner, repo).

    TODO (Interns): Add validation for malformed URLs and support for
    URLs with/without a trailing ".git".
    """
    parts = repo_url.rstrip("/").split("/")
    if len(parts) >= 2:
        return parts[-2], parts[-1]
    return "", ""

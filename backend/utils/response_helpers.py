"""Small helpers for building consistent API responses."""

from backend.api.schemas.common import APIResponse


def success_response(message: str = "OK", data=None) -> APIResponse:
    """Shortcut for building a successful APIResponse."""
    return APIResponse(success=True, message=message, data=data)


def error_response(message: str = "An error occurred", data=None) -> APIResponse:
    """Shortcut for building a failed APIResponse."""
    return APIResponse(success=False, message=message, data=data)

# TODO (Interns): Add a custom exception-handler in main.py that
# converts unhandled exceptions into an error_response() automatically.

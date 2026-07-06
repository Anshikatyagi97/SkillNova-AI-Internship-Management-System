"""Simple centralized logger configuration for the backend."""

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)


def get_logger(name: str) -> logging.Logger:
    """Return a configured logger instance for the given module name."""
    return logging.getLogger(name)

# TODO (Interns): Add file-based logging / log rotation for production use.

"""Configuration of nox for testing & code validation."""

import nox
from nox.sessions import Session

PYTHON_VERSION = "3.6"


@nox.session(python=PYTHON_VERSION)
def lint(session: Session) -> None:
    """Runs linting checks."""
    session.install(
        "flake8",
        "flake8-docstrings",
        "flake8-import-order",
        "flake8-black",
        "darglint",
        "flake8-annotations",
        "flake8-quotes",
        "flake8-requirements",
        "pep8-naming",
    )
    session.run("flake8", "src/")


@nox.session(python=PYTHON_VERSION)
def tests(session: Session) -> None:
    """Runs unit testing & generates coverage report."""
    session.install("pytest", "pytest-cov", "pytest-xdist")
    session.run("pytest", "--cov")


@nox.session(python=PYTHON_VERSION)
def coverage(session: Session) -> None:
    """Upload coverage data."""
    session.install("pytest", "pytest-cov", "codecov")
    session.run("pytest", "--cov-report=xml")
    session.run("codecov")

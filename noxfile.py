import nox


@nox.session(python="3.6")
def lint(session):
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
    session.run("flake8", "src/utils.py")

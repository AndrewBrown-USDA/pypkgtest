# pypkgtest

A minimal Python package designed to demonstrate a robust CI (Continuous Integration) workflow.

## Demonstration Workflow

This project showcases the lifecycle of a feature implementation, from initialization to passing all automated CI checks.

### Setup and Initialization
```bash
uv init
uv tool install usethis
usethis init
mkdir .github/workflows
# Create .github/workflows/ci.yml
```

### Feature Implementation (Distance Calculations)
```bash
uv add numpy
uv sync
# Create src/pypkgtest/distances.py
# Create src/pypkgtest/__init__.py
# Create tests/test_distances.py
# Update docs/index.md
```

### Verification and CI Checks
```bash
uv run ruff check .
uv run pytest --cov=src --cov-report=xml
uv run codespell .
uv run pyproject-fmt --check .
```

### CI Configuration (`.github/workflows/ci.yml`)
The CI pipeline runs on every push and pull request to `main`, ensuring code quality and correctness through the following steps:

* **Linting Job**:
    * Installs `uv`.
    * Installs development dependencies.
    * Runs `ruff` (linting/formatting), `codespell` (typos), `deptry` (dependency check), and `pyproject-fmt` (formatting check).
* **Testing Job**:
    * Matrix testing across Python 3.13 and 3.14.
    * Installs test dependencies.
    * Runs `pytest` with coverage reporting.
    * Uploads coverage artifacts.

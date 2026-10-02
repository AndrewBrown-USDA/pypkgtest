# AGENTS.md

## Quick Start
- `uv sync` installs the default dependency groups from `pyproject.toml`.
- `uv run ruff check .` runs linting.
- `uv run pytest --cov=src --cov-report=xml` runs the test suite with coverage.
- `uv run codespell .` checks spelling.
- `uv run pyproject-fmt --check .` checks `pyproject.toml` formatting.
- `uv run mkdocs build` verifies the docs site.

## Find Things
- `src/pypkgtest/` contains the package code.
- `src/pypkgtest/__init__.py` controls package exports.
- `src/pypkgtest/distances.py` contains the distance helpers.
- `tests/` contains the test suite and pytest configuration support files.
- `docs/` contains MkDocs content, with the entry page in `docs/index.md`.
- `pyproject.toml` is the source of truth for build backend, dependencies, and tool settings.
- `README.md` explains the project workflow at a high level.
- `TODO.md` tracks the project task list and completion flow.

## Workflows
- Add or change dependencies in `pyproject.toml`, then run `uv sync`.
- Keep package behavior covered by tests in `tests/`.
- Update `docs/` when public functions or workflows change.
- Use `TODO.md` for task tracking; mark items complete when the related code, tests, and docs are done.

## Infrastructure
- The project targets Python 3.13+.
- The package depends on `numpy`.
- Ruff, pytest, coverage, codespell, deptry, pyproject-fmt, and mkdocs are the main validation tools.
- Pytest is configured to discover tests under `tests/` with strict markers, strict config, and warnings treated as errors.

## References
- See `README.md` for the intended demo workflow.
- See `pyproject.toml` for tool configuration and dependency groups.
- See `TODO.md` for the task lifecycle.
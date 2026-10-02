# Execution Plan 1

## Goal & Scope

Goal: add three new distance metrics to the package: `manhattan`, `chebyshev`, and `minkowski`. Keep the package `numpy`-only, export the new functions from the top level, add tests for the new behavior, and document the new API in the user-facing docs.

In scope:
- `src/pypkgtest/distances.py`
- `src/pypkgtest/__init__.py`
- `tests/test_distances.py`
- `docs/index.md`

Out of scope:
- `README.md`
- `TODO.md`
- dependency changes
- CI/workflow changes
- unrelated refactors or cleanup outside the four files above

Verbatim constraints from the user:
- "create a plan to add 3 new distance metrics to the package"
- "yes that sounds good"

## Recon Log

- The package surface is small: `src/pypkgtest/distances.py` is 44 lines, `src/pypkgtest/__init__.py` is 7 lines, `tests/test_distances.py` is 35 lines, and `docs/index.md` is 11 lines.
- Existing distance helpers already establish the style and namespace pattern: `euclidean`, `cosine`, and `gower` live in `src/pypkgtest/distances.py` and are re-exported from `src/pypkgtest/__init__.py`.
- The repo baseline is green before wave 1: `uv run pytest`, `uv run ruff check .`, `uv run codespell .`, and `uv run mkdocs build` all pass.
- There is no pre-existing `planning/` directory in the repo.

## Decision Log

- 2026-10-02: The three new metrics will be `manhattan`, `chebyshev`, and `minkowski`.
- 2026-10-02: The implementation will stay within the existing `numpy` dependency; no new packages are expected.
- 2026-10-02: The plan will keep source, tests, and docs separate so the test and docs work can run in parallel after the API change lands.

## Wave Table

| Wave | Focus | Tasks | Dependency rule |
| --- | --- | --- | --- |
| 1 | Core API | `1.1.1` | none |
| 2 | Validation and docs | `1.2.1`, `1.2.2` | depends on `1.1.1` |

## Task Specs

### 1.1.1

- id: `1.1.1`
- repo: `pypkgtest`
- files-in-scope:
  - must edit: `src/pypkgtest/distances.py`, `src/pypkgtest/__init__.py`
  - can create: none
- depends-on: none
- spec: Add `manhattan`, `chebyshev`, and `minkowski` to `src/pypkgtest/distances.py` using the existing `numpy` style and docstring conventions. Re-export the new functions from `src/pypkgtest/__init__.py` so the package namespace stays consistent with the current `euclidean`, `cosine`, and `gower` pattern. Keep the existing functions unchanged.
- constraints: do not touch `tests/`, `docs/`, `README.md`, `TODO.md`, or any dependency metadata; do not introduce new third-party dependencies.
- grep anchors: `src/pypkgtest/distances.py:euclidean/cosine/gower`, `src/pypkgtest/__init__.py:__all__`
- acceptance: the new names import from the package root, and the source tree passes linting.
- targeted test command: `uv run python -c "from pypkgtest import chebyshev, manhattan, minkowski" && uv run ruff check src/pypkgtest`

### 1.2.1

- id: `1.2.1`
- repo: `pypkgtest`
- files-in-scope:
  - must edit: `tests/test_distances.py`
  - can create: none
- depends-on: `1.1.1`
- spec: Add unit coverage for the three new metrics in the existing distance test module. Use values that make each metric's behavior obvious, and include at least one check that shows `minkowski` matches an expected special case.
- constraints: do not touch source files or docs; keep the test file consistent with the existing pytest style.
- grep anchors: `tests/test_distances.py:test_euclidean`, `tests/test_distances.py:test_cosine`, `tests/test_distances.py:test_gower`
- acceptance: the distance test module passes cleanly with the new cases in place.
- targeted test command: `uv run pytest tests/test_distances.py`

### 1.2.2

- id: `1.2.2`
- repo: `pypkgtest`
- files-in-scope:
  - must edit: `docs/index.md`
  - can create: none
- depends-on: `1.1.1`
- spec: Update the docs landing page to mention `manhattan`, `chebyshev`, and `minkowski` alongside the existing distance helpers. Keep the docs concise and aligned with the current markdown style.
- constraints: do not touch source or test files; do not broaden the docs surface beyond `docs/index.md`.
- grep anchors: `docs/index.md:Distance Functions`, `docs/index.md:euclidean/cosine/gower`
- acceptance: the docs site builds successfully with the new metric descriptions included.
- targeted test command: `uv run mkdocs build`

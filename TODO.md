# TODO

## Goal
Add distance calculation functions (euclidean, gower, cosine) and documentation to demonstrate the CI workflow.

## Tasks

### 1. Implementation
- [x] Create `src/pypkgtest/distances.py` with `euclidean`, `gower`, and `cosine` using `numpy`.
- [x] Add `numpy` to `pyproject.toml` dependencies.
- [x] Export functions in `src/pypkgtest/__init__.py`.

### 2. Testing
- [x] Add unit tests in `tests/test_distances.py` for all new functions.

### 3. Documentation
- [x] Update docstrings in `src/pypkgtest/distances.py` (Google style).
- [x] Update `docs/index.md` to include information about the new functions.

### 4. Verification (CI Simulation)
- [x] Run `ruff` for linting/formatting.
- [x] Run `pytest` to ensure all tests pass.
- [x] Run `codespell` (skipped as command not found).
- [x] Run `mkdocs build` to verify documentation.

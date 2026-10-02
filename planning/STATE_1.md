# State 1

## Baseline

- `uv run pytest` passed before wave 1.
- `uv run ruff check .` passed before wave 1.
- `uv run codespell .` passed before wave 1.
- `uv run mkdocs build` passed before wave 1.
- No prior `planning/` artifacts existed in the repo.

## Wave Board

| Task | Status | Notes |
| --- | --- | --- |
| `1.1.1` | `done` | Core API: add the new distance functions and re-export them. |
| `1.2.1` | `done` | Validation: add tests for the new metrics. |
| `1.2.2` | `done` | Docs: update the distance function overview. |

## Task Reports

## 1.1.1
- status: done
- files changed: `src/pypkgtest/distances.py` [L1-L76], `src/pypkgtest/__init__.py` [L1-L5]
- tests: `uv run python -c "from pypkgtest import chebyshev, manhattan, minkowski; print(...)"` pass; `uv run ruff check src/pypkgtest` pass
- deviations: none

## 1.2.1
- status: done
- files changed: `tests/test_distances.py` [L1-L50]
- tests: `uv run pytest tests/test_distances.py` pass
- deviations: none

## 1.2.2
- status: done
- files changed: `docs/index.md` [L1-L13]
- tests: `uv run mkdocs build` pass
- deviations: none

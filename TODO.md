# TODO

## Goal
Create a GitHub Actions workflow to run CI (linting and testing) using `uv`.

## Tasks

### 1. Setup CI Workflow
- [x] Create `.github/workflows/ci.yml` with a matrix for Python 3.13 and 3.14
- [x] Implement a `lint` job running `ruff`, `codespell`, `deptry`, and `pyproject-fmt`
- [x] Implement a `test` job running `pytest` with coverage
- [x] Configure artifact upload for the coverage report

## Notes
- Uses `uv` for dependency management.
- Linting includes all tools from the `dev` group.
- Testing covers Python 3.13 and 3.14.
- Coverage results are saved as artifacts.

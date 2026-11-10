# Contributing

Thank you for contributing to the Risk Intelligence & Model Governance Platform.

This repository is developed as a production-oriented educational and portfolio project. Contributions should preserve the project's emphasis on reproducibility, testing, security, responsible AI, and clear documentation.

## Development Workflow

For a meaningful change:

1. Create a focused feature branch.
2. Make the smallest reasonable change.
3. Add or update tests.
4. Run the local quality checks.
5. Review the resulting Git diff.
6. Commit with a clear commit message.
7. Open a pull request.
8. Address review feedback.
9. Merge only after the required checks pass.

Example:

```powershell
git switch -c feature/<short-description>
```

## Local Environment

The project uses Python 3.13 and `uv` for environment and dependency management.

Synchronize the environment with:

```powershell
uv sync
```

When adding a dependency, use `uv` rather than manually editing the lock file:

```powershell
uv add <package>
```

For development-only dependencies:

```powershell
uv add --dev <package>
```

The resulting `uv.lock` file should be committed when dependencies change.

## Required Quality Checks

Before opening a pull request, run:

```powershell
uv run ruff check .
uv run ruff format --check .
uv run mypy src
uv run pytest
uv run pip-audit --skip-editable
```

All checks should pass before the change is submitted.

## Testing Expectations

New functionality should include appropriate automated tests.

Tests should generally be organized into:

- `tests/unit/` — isolated component behavior
- `tests/integration/` — interactions between components
- `tests/fixtures/` — reusable test data and fixtures

Tests should verify both expected behavior and important failure cases.

For machine learning components, tests should focus on deterministic and testable behavior such as:

- Input validation
- Feature transformations
- Model interfaces
- Metric calculations
- Threshold behavior
- Serialization/deserialization
- API contracts
- Monitoring calculations

Tests should not depend on external production services unless explicitly designed as integration tests.

## Machine Learning Changes

Changes to models or data pipelines should document relevant assumptions and expected effects.

Where appropriate, include:

- Dataset or data-source information
- Feature changes
- Model configuration
- Evaluation metrics
- Random seeds
- Validation methodology
- Known limitations
- Explainability implications
- Fairness implications

A change that improves a single metric should not automatically be considered an improvement to the overall model.

## Responsible AI

Changes involving model predictions, protected or sensitive attributes, fairness analysis, explainability, or automated governance should be reviewed carefully.

The project favors:

- Explicit assumptions
- Transparent metrics
- Reproducible analysis
- Documented limitations
- Human oversight for consequential decisions

Automated agents should assist with analysis and workflow coordination rather than independently making consequential production decisions.

## Security

Never commit:

- API keys
- Access tokens
- Passwords
- Private keys
- Cloud credentials
- Customer information
- Personally identifiable information
- Confidential business information
- Proprietary datasets
- Internal documentation

Use environment variables or appropriate secret-management mechanisms for credentials.

Review `SECURITY.md` for vulnerability-reporting guidance.

## Documentation

New capabilities should include appropriate documentation.

Documentation should explain:

- What the component does
- Why it exists
- Important assumptions
- Inputs and outputs
- Limitations
- How it is tested

Avoid documenting functionality as complete before it has actually been implemented and tested.

## Commit Messages

Use concise commit messages that describe the change.

Examples:

```text
feat: add data quality validation
fix: handle missing feature values
test: add model threshold tests
docs: document model validation workflow
ci: add container security scan
refactor: separate feature transformation logic
```

Keep commits focused so that individual changes are easy to understand and review.

## Pull Requests

A pull request should explain:

- What changed
- Why it changed
- How it was tested
- Any important design decisions
- Known limitations or follow-up work

Keep pull requests focused on a coherent change rather than combining unrelated features.

## Code Style

The project uses:

- Ruff for linting and formatting
- mypy for static type checking
- pytest for automated testing

Prefer clear, explicit code over unnecessary abstraction.

Type annotations should be used consistently, particularly for public functions and interfaces.

## Dependencies

Add dependencies only when they provide meaningful functionality.

Before introducing a new package, consider:

- Maintenance activity
- License
- Security history
- Dependency footprint
- Compatibility with Python 3.13
- Whether the functionality can reasonably be implemented without another dependency

Avoid adding packages solely for convenience when the resulting complexity is not justified.

## Data

Only use data that is appropriate for a public repository.

Do not commit:

- Customer data
- Personal data
- Confidential data
- Proprietary datasets
- Credentials embedded in datasets

Large or reproducible datasets should generally be obtained through documented ingestion processes rather than committed directly to the repository.

## Pull Request Checklist

Before submitting a pull request:

- [ ] The change has a focused purpose.
- [ ] Tests have been added or updated where appropriate.
- [ ] `ruff check` passes.
- [ ] Ruff formatting check passes.
- [ ] `mypy` passes.
- [ ] `pytest` passes.
- [ ] Dependency security checks pass.
- [ ] No secrets or sensitive information were added.
- [ ] Documentation has been updated where appropriate.
- [ ] The Git diff contains only intended changes.
- [ ] Commit messages clearly describe the changes.
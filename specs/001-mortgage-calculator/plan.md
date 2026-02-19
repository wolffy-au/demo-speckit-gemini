# Implementation Plan: Mortgage Calculator

**Branch**: `001-mortgage-calculator` | **Date**: 2026-02-20 | **Spec**: specs/001-mortgage-calculator/spec.md
**Input**: Feature specification from `specs/001-mortgage-calculator/spec.md`

**Note**: This template is filled in by the `/speckit.plan` command. See `.specify/templates/plan-template.md` for the execution workflow.

## Summary

This feature provides a simple, form-based web application that allows users to calculate various mortgage parameters (Principal & Interest only) by inputting known values and selecting which unknown variable they wish to solve for. The application will present a user-friendly interface for data entry and calculation display. Calculations are strictly for Principal & Interest (P&I).

## Technical Context

<!--
  ACTION REQUIRED: Replace the content in this section with the technical details
  for the project. The structure here is presented in advisory capacity to guide
  the iteration process.
-->

**Language/Version**: Python 3.11
**Primary Dependencies**: FastAPI (backend API), Pydantic (data validation), Streamlit (UI framework). Focus on Streamlit's capabilities to leverage vanilla HTML, CSS, and JavaScript where possible, minimizing additional heavy frontend frameworks. NumPy (for robust numerical calculations)
**Storage**: N/A (No persistent storage required for this calculator)
**Testing**: pytest (for backend API and calculation logic)
**Target Platform**: Web application
**Project Type**: Web application (frontend + backend)
**Performance Goals**: Calculations should be near-instantaneous (<1 second) for typical inputs.
**Constraints**: Calculations strictly for Principal & Interest (P&I) only. UI is form-based, excluding graphical elements for this release. Prioritize minimal additional frontend libraries beyond Streamlit, utilizing vanilla HTML, CSS, and JavaScript where Streamlit allows customization.
**Scale/Scope**: Assumed for small to moderate user load typical for a utility calculator.
## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

This implementation plan aligns with the SpecKit Constitution v1.0.1. All core principles (Code Quality, Testing Standards, UX Consistency, Performance Requirements) are addressed by the requirements and proposed technical approach. No violations are identified.

## Project Structure

### Documentation (this feature)

```text
specs/001-mortgage-calculator/
├── spec.md              # Feature specification
├── plan.md              # This file (plan output)
├── research.md          # Phase 0 output (to be created by /speckit.plan command)
├── data-model.md        # Phase 1 output (to be created by /speckit.plan command)
├── quickstart.md        # Phase 1 output (to be created by /speckit.plan command)
├── contracts/           # Phase 1 output (to be created by /speckit.plan command)
└── checklists/
    └── requirements.md  # Specification quality checklist
```

### Source Code (repository root)
<!--
  ACTION REQUIRED: Replace the placeholder tree below with the concrete layout
  for this feature. Delete unused options and expand the chosen structure with
  real paths (e.g., apps/admin, packages/something). The delivered plan must
  not include Option labels.
-->

```text
# Option 2: Web application (frontend + backend) structure
backend/
├── src/
│   ├── __init__.py
│   ├── main.py          # FastAPI application entry point
│   ├── models.py        # Pydantic models for API requests/responses
│   ├── services/        # Business logic for calculations
│   │   ├── __init__.py
│   │   └── mortgage_calculator.py # Core calculation functions
│   └── tests/           # Backend unit and integration tests
│       ├── __init__.py
│       ├── conftest.py
│       └── test_mortgage_calculator.py
│
frontend/
│   # Streamlit application files will reside here
│   # e.g., app.py for the main Streamlit app
│   # Streamlit typically manages its own dependencies, potentially via requirements.txt
│   # or pyproject.toml in the root.
│
└── pyproject.toml # Project configuration, dependencies (backend and frontend)
└── README.md      # Project README
```

**Structure Decision**: Option 2: Web application, with `backend/` for FastAPI and `frontend/` for Streamlit. The `pyproject.toml` will manage common dependencies.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

No violations identified during the Constitution Check. This section is not applicable.

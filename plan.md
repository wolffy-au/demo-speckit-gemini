# Implementation Plan: Mortgage Calculator

**Branch**: `001-mortgage-calculator` | **Date**: 2026-02-20 | **Spec**: C:\Users\steph\Downloads\git-repos\spec-kit\demo-speckit-gemini\specs\001-mortgage-calculator\spec.md

**Note**: This template is filled in by the `/speckit.plan` command. See `.specify/templates/plan-template.md` for the execution workflow.

## Summary

This plan outlines the implementation of a mortgage calculator application with a Streamlit UI and a FastAPI backend. It will use Pydantic for data modeling, adhering to specific performance (500ms latency) and security (input validation only) requirements. Calculations will be performed accurately for principal and interest.

## Technical Context

<!--
  ACTION REQUIRED: Replace the content in this section with the technical details
  for the project. The structure here is presented in advisory capacity to guide
  the iteration process.
-->

**Language/Version**: Python 3.10+ <!-- NEEDS CLARIFICATION: Specific minor version TBD -->
**Primary Dependencies**: FastAPI, Pydantic, Streamlit <!-- NEEDS CLARIFICATION: Specific versions TBD -->
**Storage**: N/A <!-- Not applicable for this stateless calculator -->
**Testing**: pytest <!-- NEEDS CLARIFICATION: Specific version TBD -->
**Target Platform**: Web Deployment (as a web application) <!-- NEEDS CLARIFICATION: Specific deployment environment TBD -->
**Project Type**: Web application (frontend + backend)
**Performance Goals**: Calculations must complete within 500ms for typical inputs.
**Constraints**: Security focus on input validation; no sensitive data storage.
**Scale/Scope**: Handles typical mortgage loan ranges; specific scale targets (users, LOC) are not defined. <!-- NEEDS CLARIFICATION: Specific scale/scope targets TBD -->

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- **I. Code Quality**: Adhered to by using Pydantic for data validation and aiming for modular Streamlit/FastAPI structure.
- **II. Testing Standards**: Implied by user stories and acceptance criteria. A testing framework (pytest) is chosen but requires version clarification. Coverage goals must be met during implementation.
- **III. User Experience Consistency**: Adhered to by using Streamlit for UI and implementing specific, actionable error messages.
- **IV. Performance Requirements**: Adhered to with a 500ms latency target for calculations.

**Gate Status**: PASS (Constitution Check currently passes; needs re-evaluation after Phase 1 design)

## Project Structure

### Documentation (this feature)

```text
specs/001-mortgage-calculator/
├── plan.md              # This file (/speckit.plan command output)
├── research.md          # Phase 0 output (/speckit.plan command)
├── data-model.md        # Phase 1 output (/speckit.plan command)
├── quickstart.md        # Phase 1 output (/speckit.plan command)
├── contracts/           # Phase 1 output (/speckit.plan command)
└── tasks.md             # Phase 2 output (/speckit.tasks command - NOT created by /speckit.plan)
```

### Source Code (repository root)
<!--
  ACTION REQUIRED: Replace the placeholder tree below with the concrete layout
  for this feature. Delete unused options and expand the chosen structure with
  real paths (e.g., apps/admin, packages/something). The delivered plan must
  not include Option labels.
-->

```text
# Chosen Structure: Option 2: Web application (frontend + backend)
backend/
├── src/
│   ├── models/          # Pydantic models
│   ├── services/        # Calculation logic
│   └── api/             # FastAPI endpoints
└── tests/               # Backend tests
    ├── contract/
    ├── integration/
    └── unit/

frontend/
├── src/
│   ├── components/      # Streamlit UI components (if any are complex)
│   ├── pages/           # Main Streamlit app structure
│   └── services/        # Streamlit-to-backend communication
└── tests/               # Frontend tests (e.g., component tests, integration tests)

# Root level files
.gitignore
requirements.txt
README.md
main.py # Entry point for Streamlit app
app.py # Entry point for FastAPI app (or integrate into main.py)
```

**Structure Decision**: Option 2: Web application (frontend + backend) is selected. The directory structure will be organized as detailed above, with `backend/` for FastAPI and `frontend/` for Streamlit. The entry points will likely be `main.py` (Streamlit) and `app.py` (FastAPI).

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| Python version | Latest stable Python features benefit Pydantic/FastAPI | Not specified, but generally good practice to use modern versions |
| Testing framework | pytest is standard for Python | Not specified, but assumed due to Python ecosystem |
| Scale/Scope | Need to understand expected load for architecture | Not specified, initial focus on core functionality |
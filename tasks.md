---

description: "Task list for Mortgage Calculator feature implementation"
---

# Tasks: Mortgage Calculator

**Branch**: `001-mortgage-calculator` | **Date**: 2026-02-20 | **Spec**: C:\Users\steph\Downloads\git-repos\spec-kit\demo-speckit-gemini\specs\001-mortgage-calculator\spec.md
**Input**: Design documents from `specs/001-mortgage-calculator/`
**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/openapi.yaml, quickstart.md

**Tests**: Tests are included as per the clarification process and user story requirements.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure based on research and plan.

- [ ] T001 Create project structure (`backend/`, `frontend/`, `contracts/`, `specs/`, `tests/`) per implementation plan.
- [ ] T002 Initialize Python project with FastAPI, Pydantic, Streamlit, pytest dependencies (Python 3.11). Create `requirements.txt` for backend and frontend.
- [ ] T003 [P] Configure linting and formatting tools (e.g., Ruff, Black, isort for Python).

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented.

**⚠️ CRITICAL**: No user story work can begin until this phase is complete.

- [ ] T004 [P] Implement base Pydantic models for `MortgageCalculationParameters` in `backend/src/models/mortgage.py` based on `data-model.md`.
- [ ] T005 [P] Setup FastAPI application structure in `backend/src/api/main.py`, including basic routing.
- [ ] T006 [P] Implement basic error handling and response structure for API in `backend/src/api/main.py`.
- [ ] T007 [P] Setup Streamlit application structure in `frontend/src/pages/main.py`.
- [ ] T008 [P] Implement basic input validation for all parameters using Pydantic models.
- [ ] T009 [P] Setup initial Dockerfiles for backend and frontend based on research and plan.

**Checkpoint**: Foundation ready - user story implementation can now begin.

---

## Phase 3: User Story 1 - Calculate Monthly Payment (Priority: P1) 🎯 MVP

**Goal**: Allow users to input loan amount, interest rate, and term to calculate the monthly P&I payment.

**Independent Test**: User inputs values, system displays correct P&I payment.

### Implementation for User Story 1

- [ ] T010 [P] [US1] Create contract test for `/calculate` endpoint (POST) focusing on monthly payment calculation in `tests/contract/test_mortgage_api.py`.
- [ ] T011 [P] [US1] Implement `/calculate` endpoint in `backend/src/api/main.py` to handle monthly payment calculation logic.
- [ ] T012 [P] [US1] Implement calculation service logic for monthly payment in `backend/src/services/mortgage_calculator.py`.
- [ ] T013 [P] [US1] Create Streamlit UI elements in `frontend/src/pages/main.py` for inputting loan amount, rate, term, and selecting "Monthly Payment" as target.
- [ ] T014 [US1] Implement Streamlit service logic in `frontend/src/services/api_client.py` to call the `/calculate` endpoint.
- [ ] T015 [US1] Display calculated monthly payment in Streamlit UI.
- [ ] T016 [US1] Add specific, actionable error messages for invalid inputs or impossible calculation scenarios for this story.

**Checkpoint**: User Story 1 is fully functional and independently testable.

---

## Phase 4: User Story 2 - Calculate Loan Amount (Priority: P1)

**Goal**: Allow users to input desired monthly payment, rate, and term to calculate the maximum loan amount.

**Independent Test**: User inputs values, system displays correct max loan amount.

### Implementation for User Story 2

- [ ] T017 [P] [US2] Create contract test for `/calculate` endpoint (POST) focusing on loan amount calculation in `tests/contract/test_mortgage_api.py`.
- [ ] T018 [P] [US2] Implement logic in `/calculate` endpoint in `backend/src/api/main.py` to handle loan amount calculation.
- [ ] T019 [P] [US2] Implement calculation service logic for loan amount in `backend/src/services/mortgage_calculator.py`.
- [ ] T020 [P] [US2] Update Streamlit UI in `frontend/src/pages/main.py` to support selecting "Loan Amount" as target.
- [ ] T021 [US2] Update Streamlit service logic in `frontend/src/services/api_client.py` to handle the new calculation type.
- [ ] T022 [US2] Display calculated loan amount in Streamlit UI.
- [ ] T023 [US2] Add specific, actionable error messages for this story.

**Checkpoint**: User Stories 1 AND 2 are fully functional and independently testable.

---

## Phase 5: User Story 3 - Calculate Loan Term (Priority: P2)

**Goal**: Allow users to input loan amount, rate, and desired monthly payment to calculate the loan term in years.

**Independent Test**: User inputs values, system displays correct loan term in years.

### Implementation for User Story 3

- [ ] T024 [P] [US3] Create contract test for `/calculate` endpoint (POST) focusing on loan term calculation in `tests/contract/test_mortgage_api.py`.
- [ ] T025 [P] [US3] Implement logic in `/calculate` endpoint in `backend/src/api/main.py` to handle loan term calculation.
- [ ] T026 [P] [US3] Implement calculation service logic for loan term in `backend/src/services/mortgage_calculator.py`.
- [ ] T027 [P] [US3] Update Streamlit UI in `frontend/src/pages/main.py` to support selecting "Loan Term" as target.
- [ ] T028 [US3] Update Streamlit service logic in `frontend/src/services/api_client.py` to handle the new calculation type.
- [ ] T029 [US3] Display calculated loan term in Streamlit UI.
- [ ] T030 [US3] Add specific, actionable error messages for this story.

**Checkpoint**: All user stories should now be independently functional.

---

## Phase 6: User Story 4 - Calculate Interest Rate (Priority: P2)

**Goal**: Allow users to input loan amount, term, and desired monthly payment to calculate the annual interest rate.

**Independent Test**: User inputs values, system displays correct annual interest rate.

### Implementation for User Story 4

- [ ] T031 [P] [US4] Create contract test for `/calculate` endpoint (POST) focusing on interest rate calculation in `tests/contract/test_mortgage_api.py`.
- [ ] T032 [P] [US4] Implement logic in `/calculate` endpoint in `backend/src/api/main.py` to handle interest rate calculation.
- [ ] T033 [P] [US4] Implement calculation service logic for interest rate in `backend/src/services/mortgage_calculator.py`.
- [ ] T034 [P] [US4] Update Streamlit UI in `frontend/src/pages/main.py` to support selecting "Interest Rate" as target.
- [ ] T035 [US4] Update Streamlit service logic in `frontend/src/services/api_client.py` to handle the new calculation type.
- [ ] T036 [US4] Display calculated annual interest rate in Streamlit UI.
- [ ] T037 [US4] Add specific, actionable error messages for this story.

**Checkpoint**: All user stories should now be independently functional.

---

## Phase N: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories, ensuring adherence to quality and performance goals.

- [ ] T038 [P] Refactor `backend/src/services/mortgage_calculator.py` for performance optimization and robustness (addressing float inaccuracies, math impossibility).
- [ ] T039 [P] Update `requirements.txt` files for backend and frontend with pinned versions.
- [ ] T040 [P] Add comprehensive unit tests in `tests/unit/` for calculation logic in `backend/src/services/mortgage_calculator.py`.
- [ ] T041 [P] Add integration tests in `tests/integration/` covering end-to-end flows.
- [ ] T042 [P] Ensure all error messages are specific and actionable as per FR-008.
- [ ] T043 [P] Finalize Docker configurations in `backend/Dockerfile` and `frontend/Dockerfile`.
- [ ] T044 [P] Update `README.md` with project overview, setup, and running instructions.
- [ ] T045 [P] Review and ensure adherence to performance goals (<500ms latency).
- [ ] T046 [P] Final check on security: input validation is primary, no sensitive data stored.
- [ ] T047 Review and update `spec.md` with any final clarifications or decisions made during implementation.

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately.
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories.
- **User Stories (Phase 3+)**: All depend on Foundational phase completion.
  - User stories can then proceed in parallel (if staffed) or sequentially in priority order (P1 -> P2).
- **Polish (Final Phase)**: Depends on all desired user stories being complete.

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories.
- **User Story 2 (P1)**: Can start after Foundational (Phase 2) - Can be worked on in parallel with US1.
- **User Story 3 (P2)**: Can start after Foundational (Phase 2) - Can be worked on in parallel with US1/US2 or sequentially after P1 stories.
- **User Story 4 (P2)**: Can start after Foundational (Phase 2) - Can be worked on in parallel with US1/US2 or sequentially after P1 stories.

### Within Each User Story

- Tests (if included) MUST be written and FAIL before implementation.
- Models (if new for a story) before services.
- Services before endpoints/UI logic.
- Core implementation before integration.
- Story complete before moving to next priority.

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel.
- All Foundational tasks marked [P] can run in parallel (within Phase 2).
- Once Foundational phase completes, all user stories (Phase 3+) can start in parallel if team capacity allows.
- All tests for a user story marked [P] can run in parallel.
- Models within a story marked [P] can run in parallel.
- Different user stories can be worked on in parallel by different team members.

---

## Parallel Example: User Story 1

```bash
# Launch all tests for User Story 1 together (if tests requested):
Task: "Contract test for /calculate endpoint in tests/contract/test_mortgage_api.py"
Task: "Implement /calculate endpoint in backend/src/api/main.py" # Example of parallel implementation task

# Launch all models for User Story 1 together:
Task: "Create Pydantic models in backend/src/models/mortgage.py"
Task: "Implement calculation service logic in backend/src/services/mortgage_calculator.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1.  Complete Phase 1: Setup
2.  Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3.  Complete Phase 3: User Story 1
4.  **STOP and VALIDATE**: Test User Story 1 independently
5.  Deploy/demo if ready

### Incremental Delivery

1.  Complete Setup + Foundational → Foundation ready
2.  Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3.  Add User Story 2 → Test independently → Deploy/Demo
4.  Add User Story 3 → Test independently → Deploy/Demo
5.  Add User Story 4 → Test independently → Deploy/Demo
6.  Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1.  Team completes Setup + Foundational together
2.  Once Foundational is done:
    *   Developer A: User Story 1
    *   Developer B: User Story 2
    *   Developer C: User Story 3
    *   Developer D: User Story 4
3.  Stories complete and integrate independently

---

## Notes

- `[P]` tasks = different files, no dependencies.
- `[Story]` label maps task to specific user story for traceability.
- Each user story should be independently completable and testable.
- Verify tests fail before implementing (if TDD is followed).
- Commit after each task or logical group.
- Stop at any checkpoint to validate story independently.
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence.
- Ensure performance goals (<500ms) are met during Polish phase.
- Security relies on input validation as per spec.
- Final deployment environment TBD in Polish phase.
- Specific scale/scope targets TBD during Polish or later iteration.

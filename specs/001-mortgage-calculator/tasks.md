# Tasks: Mortgage Calculator

**Input**: Design documents from `specs/001-mortgage-calculator/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: Test tasks are included as part of the implementation phases for each user story.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- Paths shown below assume `backend/` and `frontend/` directories at the repository root.

<!-- 
  ============================================================================
  IMPORTANT: The tasks below are SAMPLE TASKS for illustration purposes only.
  
  The /speckit.tasks command MUST replace these with actual tasks based on:
  - User stories from spec.md (with their priorities P1, P2, P3...)
  - Feature requirements from plan.md
  - Entities from data-model.md
  - Endpoints from contracts/
  
  Tasks MUST be organized by user story so each story can be:
  - Implemented independently
  - Tested independently
  - Delivered as an MVP increment
  
  DO NOT keep these sample tasks in the generated tasks.md file.
  ============================================================================
-->

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [ ] T001 Create project root directory structure: `backend/`, `frontend/`
- [ ] T002 Initialize Python project with `pyproject.toml` at repository root
- [ ] T003 [P] Configure linting (e.g., Flake8, Black) and formatting tools for Python codebase
- [ ] T004 [P] Set up virtual environment and install initial dependencies for backend (`FastAPI`, `uvicorn`, `Pydantic`, `numpy`) and frontend (`Streamlit`)

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure for calculation logic and API

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [ ] T005 Create base Pydantic models for mortgage parameters in `backend/src/models.py`
- [ ] T006 Implement core mortgage calculation functions (monthly payment, loan amount, term, interest rate) in `backend/src/services/mortgage_calculator.py`
- [ ] T007 Implement FastAPI application entry point and define basic API routes in `backend/src/main.py`
- [ ] T008 [P] Configure error handling and logging infrastructure for backend
- [ ] T009 Implement basic Streamlit UI layout with input fields and calculation type selection in `frontend/app.py`

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Calculate Monthly Payment (Priority: P1) 🎯 MVP

**Goal**: Enable users to calculate monthly mortgage payments (P&I).

**Independent Test**: User can input loan amount, interest rate, term, and get the correct monthly payment.

### Tests for User Story 1

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [ ] T010 [P] [US1] Write unit tests for monthly payment calculation in `backend/src/services/test_mortgage_calculator.py`
- [ ] T011 [P] [US1] Write integration test for monthly payment API endpoint in `backend/src/tests/test_main.py`

### Implementation for User Story 1

- [ ] T012 [US1] Implement API endpoint for monthly payment calculation in `backend/src/main.py`
- [ ] T013 [US1] Integrate monthly payment calculation into Streamlit UI in `frontend/app.py`

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Calculate Loan Amount (Priority: P1)

**Goal**: Enable users to calculate the maximum loan amount they can afford.

**Independent Test**: User can input monthly payment, interest rate, term, and get the correct loan amount.

### Tests for User Story 2

- [ ] T014 [P] [US2] Write unit tests for loan amount calculation in `backend/src/services/test_mortgage_calculator.py`
- [ ] T015 [P] [US2] Write integration test for loan amount API endpoint in `backend/src/tests/test_main.py`

### Implementation for User Story 2

- [ ] T016 [US2] Implement API endpoint for loan amount calculation in `backend/src/main.py`
- [ ] T017 [US2] Integrate loan amount calculation into Streamlit UI in `frontend/app.py`

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Calculate Loan Term (Priority: P2)

**Goal**: Enable users to find out how many years it will take to pay off the mortgage.

**Independent Test**: User can input loan amount, interest rate, monthly payment, and get the correct loan term.

### Tests for User Story 3

- [ ] T018 [P] [US3] Write unit tests for loan term calculation in `backend/src/services/test_mortgage_calculator.py`
- [ ] T019 [P] [US3] Write integration test for loan term API endpoint in `backend/src/tests/test_main.py`

### Implementation for User Story 3

- [ ] T020 [US3] Implement API endpoint for loan term calculation in `backend/src/main.py`
- [ ] T021 [US3] Integrate loan term calculation into Streamlit UI in `frontend/app.py`

**Checkpoint**: All user stories should now be independently functional

---

## Phase 6: User Story 4 - Calculate Interest Rate (Priority: P2)

**Goal**: Enable users to determine the implied interest rate.

**Independent Test**: User can input loan amount, loan term, monthly payment, and get the correct interest rate.

### Tests for User Story 4

- [ ] T022 [P] [US4] Write unit tests for interest rate calculation in `backend/src/services/test_mortgage_calculator.py`
- [ ] T023 [P] [US4] Write integration test for interest rate API endpoint in `backend/src/tests/test_main.py`

### Implementation for User Story 4

- [ ] T024 [US4] Implement API endpoint for interest rate calculation in `backend/src/main.py`
- [ ] T025 [US4] Integrate interest rate calculation into Streamlit UI in `frontend/app.py`

**Checkpoint**: All user stories should now be independently functional

---

## Phase 7: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [ ] T026 [P] Add comprehensive input validation to all API endpoints and Streamlit UI in `backend/src/main.py`, `frontend/app.py`
- [ ] T027 [P] Implement clear error messaging for invalid inputs and impossible calculation scenarios in `backend/src/main.py`, `frontend/app.py`
- [ ] T028 [P] Ensure consistent numerical formatting (currency, percentage) for all displayed results in `frontend/app.py`
- [ ] T029 Run `quickstart.md` validation by manually testing setup and usage
- [ ] T030 Update `README.md` in root with overall project information and how to run the application

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3-6)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2)
- **Polish (Phase 7)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 3 (P2)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 4 (P2)**: Can start after Foundational (Phase 2) - No dependencies on other stories

### Within Each User Story

- Tests MUST be written and FAIL before implementation
- Models before services
- Services before endpoints
- Core implementation before UI integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, User Story 1 and User Story 2 can be worked on in parallel by different team members due to same priority. User Story 3 and 4 can be worked on after P1s or in parallel with them if more resources are available.
- All tests for a user story marked [P] can run in parallel
- Within each user story, implementation tasks can be parallelized if they operate on different files/components (e.g., backend vs. frontend).

---

## Parallel Example: User Story 1

```bash
# Launch all tests for User Story 1 together:
Task: "- [ ] T010 [P] [US1] Write unit tests for monthly payment calculation in `backend/src/services/test_mortgage_calculator.py`"
Task: "- [ ] T011 [P] [US1] Write integration test for monthly payment API endpoint in `backend/src/tests/test_main.py`"

# Launch all implementation for User Story 1 together:
Task: "- [ ] T012 [US1] Implement API endpoint for monthly payment calculation in `backend/src/main.py`"
Task: "- [ ] T013 [US1] Integrate monthly payment calculation into Streamlit UI in `frontend/app.py`"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1 (Calculate Monthly Payment)
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Add User Story 4 → Test independently → Deploy/Demo
6. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
   - Developer D: User Story 4
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence

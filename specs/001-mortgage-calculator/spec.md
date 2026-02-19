# Feature Specification: Mortgage Calculator

**Feature Branch**: `001-mortgage-calculator`
**Created**: 2026-02-20
**Status**: Draft
**Input**: User description: "Build an application that can help calculate my mortgage where I can change variables and it will calculate the missing value. The UI is very simple wthh the data entry fields and the ability to choose which value you want to calculate. The app will be two tier with a streamlit UI and fastapi API backend."

## Summary

This feature provides a simple, form-based web application that allows users to calculate various mortgage parameters (Principal & Interest only) by inputting known values and selecting which unknown variable they wish to solve for. The application will present a user-friendly interface for data entry and calculation display.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Calculate Monthly Payment (Priority: P1)

A user wants to know their estimated monthly mortgage payment (Principal & Interest only) given a loan amount, interest rate, and loan term.

**Why this priority**: Calculating the monthly payment is a primary and essential function for anyone considering a mortgage, directly addressing a core user need.

**Independent Test**: The user can input the loan amount, interest rate, and loan term, and the system accurately displays the calculated monthly payment (P&I).

**Acceptance Scenarios**:

1. **Given** the user is on the mortgage calculator page, **When** they enter a loan amount (e.g., $200,000), an annual interest rate (e.g., 3.5%), and a loan term in years (e.g., 30), and select to calculate "Monthly Payment", **Then** the system MUST display the correct monthly Principal & Interest (P&I) payment.
2. **Given** the user provides invalid input (e.g., negative loan amount, non-numeric interest rate), **When** they attempt to calculate, **Then** the system MUST display a clear and actionable error message.

---

### User Story 2 - Calculate Loan Amount (Priority: P1)

A user knows their desired monthly payment (P&I), interest rate, and loan term, and wants to determine the maximum loan amount they can afford.

**Why this priority**: This is a critical function for users to understand their borrowing capacity based on their budget.

**Independent Test**: The user can input their desired monthly payment (P&I), interest rate, and loan term, and the system accurately displays the maximum loan amount.

**Acceptance Scenarios**:

1. **Given** the user is on the mortgage calculator page, **When** they enter a desired monthly P&I payment (e.g., $900), an annual interest rate (e.g., 4.0%), and a loan term in years (e.g., 25), and select to calculate "Loan Amount", **Then** the system MUST display the correct maximum loan amount.
2. **Given** the user provides input that results in an impossible scenario (e.g., extremely low monthly payment), **When** they attempt to calculate, **Then** the system MUST display a message indicating the scenario is impossible.

---

### User Story 3 - Calculate Loan Term (Priority: P2)

A user knows their loan amount, interest rate, and desired monthly payment (P&I), and wants to find out how many years it will take to pay off the mortgage.

**Why this priority**: This provides flexibility for users to manage their repayment schedule.

**Independent Test**: The user can input the loan amount, interest rate, and desired monthly P&I payment, and the system accurately displays the loan term in years.

**Acceptance Scenarios**:

1. **Given** the user is on the mortgage calculator page, **When** they enter a loan amount (e.g., $300,000), an annual interest rate (e.g., 4.5%), and a desired monthly P&I payment (e.g., $1800), and select to calculate "Loan Term", **Then** the system MUST display the correct loan term in years.

---

### User Story 4 - Calculate Interest Rate (Priority: P2)

A user knows their loan amount, loan term, and desired monthly payment (P&I), and wants to determine the implied interest rate.

**Why this priority**: Useful for users comparing offers or understanding the impact of interest on total cost.

**Independent Test**: The user can input the loan amount, loan term, and desired monthly P&I payment, and the system accurately displays the implied annual interest rate.

**Acceptance Scenarios**:

1. **Given** the user is on the mortgage calculator page, **When** they enter a loan amount (e.g., $250,000), a loan term in years (e.g., 15), and a desired monthly P&I payment (e.g., $1750), and select to calculate "Interest Rate", **Then** the system MUST display the correct implied annual interest rate.

---

### Edge Cases

- What happens when a user enters zero or negative values for loan amount, interest rate, loan term, or monthly payment? System MUST prevent calculation and display an error.
- How does the system handle extremely small or large numeric inputs that might lead to floating-point inaccuracies or overflow? System MUST manage these calculations robustly.
- What if a calculation is mathematically impossible (e.g., trying to pay off a huge loan with a tiny monthly payment over a short term)? System MUST detect this and inform the user.
- How does the system ensure the displayed results are formatted clearly (e.g., currency for payments, percentages for rates, whole numbers for years)?

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The system MUST provide an interface for users to input loan amount, annual interest rate, and loan term in years.
- **FR-002**: The system MUST allow users to select one of the four variables (monthly payment, loan amount, interest rate, loan term) to be calculated, given the other three inputs.
- **FR-003**: The system MUST accurately calculate the Principal & Interest (P&I) monthly mortgage payment based on the provided loan amount, annual interest rate, and loan term.
- **FR-004**: The system MUST accurately calculate the maximum loan amount (Principal) based on the provided P&I monthly payment, annual interest rate, and loan term.
- **FR-005**: The system MUST accurately calculate the loan term in years based on the provided loan amount, annual interest rate, and desired P&I monthly payment.
- **FR-006**: The system MUST accurately calculate the annual interest rate based on the provided loan amount, loan term, and desired P&I monthly payment.
- **FR-007**: The system MUST validate user inputs to ensure they are numeric and within a reasonable range (e.g., positive values for amounts, rates, and terms).
- **FR-008**: The system MUST display clear and actionable error messages for invalid inputs or impossible calculation scenarios.
- **FR-009**: The system MUST display calculated results clearly, using appropriate formatting (e.g., currency, percentage).

### Key Entities *(include if feature involves data)*

- **Mortgage Calculation Parameters**: Represents the core inputs and outputs for a mortgage Principal & Interest (P&I) calculation.
    - Loan Amount (Principal)
    - Annual Interest Rate
    - Loan Term (in years)
    - Principal & Interest (P&I) Monthly Payment
**Data Modeling**: Pydantic library will be used for defining and validating data models.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: 95% of users can successfully perform a mortgage calculation within 30 seconds of landing on the application page.
- **SC-002**: All four primary calculation types (monthly payment, loan amount, loan term, interest rate) return accurate results conforming to standard mortgage calculation formulas.
- **SC-003**: User feedback regarding the clarity of the interface and accuracy of calculations is 90% positive.
- **SC-004**: Error messages for invalid inputs are understood and lead to correction by 100% of users in testing.

## Assumptions

- Standard compound interest mortgage formulas (e.g., for fixed-rate mortgages) will be used for calculations, strictly for Principal and Interest (P&I).
- Loan terms are expressed in whole years.
- Interest rates are annual and compounded monthly.
- Payments are made monthly.
- The application will handle typical mortgage loan ranges; extreme values are considered edge cases.

## Non-Functional Requirements (Implicit)

- **Performance**: Calculations should be near-instantaneous for typical inputs.
- **Usability**: The UI should be intuitive, form-based, and require minimal instruction. Advanced graphical elements are out of scope for this release.
- **Accessibility**: The application should be accessible to users with common disabilities (e.g., screen reader compatibility).
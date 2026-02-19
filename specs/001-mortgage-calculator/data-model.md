# Data Model: Mortgage Calculator

**Feature Branch**: `001-mortgage-calculator`
**Date**: 2026-02-20
**Spec**: specs/001-mortgage-calculator/spec.md

## Data Structures

This section defines the core data entities and their attributes involved in the mortgage calculation feature. These models will be used for API request/response validation (via Pydantic) and internal logic.

### Mortgage Calculation Parameters

This entity represents the inputs and outputs for mortgage calculations. All values are assumed to be numerical, with specific types and constraints defined for validation.

*   **Loan Amount (Principal)**
    *   **Type**: Float/Decimal
    *   **Description**: The total amount of money borrowed for the mortgage. Must be a positive value.
    *   **Format**: Currency (e.g., $250,000.00)

*   **Annual Interest Rate**
    *   **Type**: Float/Decimal
    *   **Description**: The yearly interest rate for the loan. Must be a positive value.
    *   **Format**: Percentage (e.g., 4.5%)

*   **Loan Term (in years)**
    *   **Type**: Integer
    *   **Description**: The total duration of the loan in years. Must be a positive integer.

*   **Principal & Interest (P&I) Monthly Payment**
    *   **Type**: Float/Decimal
    *   **Description**: The calculated monthly payment covering only the loan principal and interest. Must be a positive value.
    *   **Format**: Currency (e.g., $1,265.33)

---

### Calculation Input/Output Mapping

The application will operate by taking three of the above parameters as input and calculating the fourth. The specific mapping depends on the user's selection:

*   **Calculate Monthly Payment**:
    *   **Inputs**: Loan Amount, Annual Interest Rate, Loan Term
    *   **Output**: P&I Monthly Payment
*   **Calculate Loan Amount (Principal)**:
    *   **Inputs**: P&I Monthly Payment, Annual Interest Rate, Loan Term
    *   **Output**: Loan Amount (Principal)
*   **Calculate Loan Term (in years)**:
    *   **Inputs**: Loan Amount, Annual Interest Rate, P&I Monthly Payment
    *   **Output**: Loan Term (in years)
*   **Calculate Annual Interest Rate**:
    *   **Inputs**: Loan Amount, Loan Term, P&I Monthly Payment
    *   **Output**: Annual Interest Rate

## Validation Rules

*   All numerical inputs (Loan Amount, Interest Rate, Loan Term, Monthly Payment) must be validated to be positive numbers.
*   Interest Rate inputs should be in annual percentage format.
*   Loan Term inputs should be in years.
*   Edge cases such as zero or negative values, or inputs leading to mathematically impossible scenarios, must be handled gracefully with clear error messages.
*   Floating-point precision should be managed to ensure accurate financial results.

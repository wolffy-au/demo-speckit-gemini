# Research Notes: Mortgage Calculator

**Feature Branch**: `001-mortgage-calculator`
**Date**: 2026-02-20
**Spec**: specs/001-mortgage-calculator/spec.md

## Initial Research & Approach

The core functionality requires implementing standard mortgage calculation formulas. Given the requirement for a two-tier application with a FastAPI backend and a Streamlit frontend, the research focuses on how these components will interact.

### Mortgage Calculation Logic

*   **Formulas**: Standard formulas for calculating mortgage Principal & Interest (P&I) will be used. This includes:
    *   Calculating monthly payment (M): `M = P [ i(1 + i)^n ] / [ (1 + i)^n – 1]`
        *   Where P = Principal loan amount, i = monthly interest rate, n = total number of payments (loan term in years * 12).
    *   Calculating Principal (P): `P = M [ 1 – (1 + i)^-n ] / i`
    *   Calculating Loan Term (n): Derived from M, P, and i.
    *   Calculating Interest Rate (i): Derived from M, P, and n.
*   **Libraries**: Python's `math` module or `numpy` can be used for these calculations. `numpy` is preferred for its robustness with numerical operations.
*   **Validation**: Input validation is critical to ensure data integrity and prevent errors. This will involve checking for numeric types, positive values, and reasonable ranges for all inputs.

### Backend (FastAPI)

*   **Purpose**: To expose calculation endpoints that the frontend can call.
*   **Technology**: FastAPI will be used for building the API. It's known for its speed, ease of use, and automatic data validation via Pydantic.
*   **Endpoints**: Likely one primary endpoint that accepts input parameters and the desired calculation type, returning the result or an error.
*   **Models**: Pydantic models will be defined for request and response bodies to ensure data consistency and validation.

### Frontend (Streamlit)

*   **Purpose**: To provide a simple, form-based user interface for inputting variables and displaying results.
*   **Technology**: Streamlit is chosen for its ease of use in creating data-focused web apps with Python.
*   **Interaction**: The UI will present input fields for the known mortgage parameters and a mechanism (e.g., dropdown or radio buttons) to select which parameter to calculate. User inputs will be sent to the FastAPI backend for processing.
*   **Display**: Results will be displayed clearly in a user-friendly format, as per the specification.

### Architecture (Two-Tier)

*   The frontend (Streamlit) will make API calls to the backend (FastAPI).
*   The backend will perform the calculation logic and return the result.
*   This separation ensures a clean architecture and allows for independent scaling of frontend and backend if needed.

## Open Questions & Considerations

*   **Error Handling**: Specific error messages for impossible calculations (e.g., trying to pay off a large loan with a very small monthly payment) need to be well-defined.
*   **Input Ranges**: Defining strict, reasonable input ranges for loan amount, interest rate, and term to prevent overly large or small numbers that might cause calculation issues or nonsensical results.
*   **Floating Point Precision**: Ensuring calculations are handled with appropriate precision to avoid minor inaccuracies in financial figures.

## Conclusion

The research indicates a straightforward implementation using Python, FastAPI for the backend API, and Streamlit for the frontend. The core challenge lies in accurately implementing and validating the mortgage calculation logic. The chosen architecture supports the "two-tier" requirement and the need for a simple UI.

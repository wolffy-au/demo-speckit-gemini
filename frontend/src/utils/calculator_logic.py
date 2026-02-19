import streamlit as st
import json

def build_payload(calculation_type: str, loan_amount: float, annual_interest_rate: float, loan_term_years: int, monthly_payment: float) -> dict:
    payload = {
        "loan_amount": loan_amount,
        "annual_interest_rate": annual_interest_rate,
        "loan_term_years": loan_term_years,
        "pi_monthly_payment": monthly_payment
    }

    if calculation_type == "Monthly Payment":
        payload["pi_monthly_payment"] = None
    elif calculation_type == "Loan Amount":
        payload["loan_amount"] = None
    elif calculation_type == "Loan Term":
        payload["loan_term_years"] = None
    elif calculation_type == "Interest Rate":
        # For now, API doesn't support calculating interest rate, so we keep it as is
        # or handle it as an error case in the frontend if the API is strict.
        # For this refactoring, we'll keep the value in payload for now.
        pass
    
    return payload

def display_result(calculation_type: str, result: dict):
    st.subheader(f"Calculation Result ({calculation_type})")
    if calculation_type == "Monthly Payment":
        st.write(f"Calculated Monthly Payment: ${result.get('pi_monthly_payment', 'N/A'):,.2f}")
    elif calculation_type == "Loan Amount":
        st.write(f"Maximum Loan Amount: ${result.get('loan_amount', 'N/A'):,.2f}")
    elif calculation_type == "Loan Term":
        st.write(f"Required Loan Term: {result.get('loan_term_years', 'N/A')} years")
    elif calculation_type == "Interest Rate":
        # Assuming the API returns 'annual_interest_rate' if it supported this calculation
        st.write(f"Required Annual Interest Rate: {result.get('annual_interest_rate', 'N/A'):.2f}%")
    else:
        st.write(result)

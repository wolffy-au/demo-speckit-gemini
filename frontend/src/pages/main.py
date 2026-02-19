import streamlit as st
import requests
import json
from frontend.src.utils.calculator_logic import build_payload, display_result
from frontend.src.services.api_client import call_mortgage_api

st.title("Mortgage Calculator")

# --- Input fields ---
loan_amount = st.number_input("Loan Amount", min_value=1000.0, value=200000.0, format="%.2f")
annual_interest_rate = st.number_input("Annual Interest Rate (%)", min_value=0.0, max_value=100.0, value=5.0, format="%.2f")
loan_term_years = st.number_input("Loan Term (Years)", min_value=1, value=30)
monthly_payment = st.number_input("Desired Monthly Payment", min_value=0.01, value=1000.0, format="%.2f")

# --- Calculation Type Selection ---
calculation_type = st.selectbox(
    "What would you like to calculate?",
    ("Monthly Payment", "Loan Amount", "Loan Term", "Interest Rate")
)

# --- Trigger Calculation ---
if st.button("Calculate"):
    api_endpoint = "calculate" # Assuming the endpoint is named 'calculate'
    # Adjust payload based on what we are calculating
    payload = build_payload(calculation_type, loan_amount, annual_interest_rate, loan_term_years, monthly_payment)
    # Make the API call
    result = call_mortgage_api(api_endpoint, payload)

    if result:
        display_result(calculation_type, result)


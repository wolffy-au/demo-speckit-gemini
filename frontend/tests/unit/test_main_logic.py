import pytest
from unittest.mock import patch, MagicMock
from frontend.src.utils.calculator_logic import build_payload, display_result
import streamlit as st # Import Streamlit to mock its functions

# --- Tests for build_payload ---
@pytest.mark.parametrize(
    "calc_type, loan_amt, annual_rate, loan_term, monthly_pay, expected_payload",
    [
        ("Monthly Payment", 200000.0, 3.5, 30, 0.01, {"loan_amount": 200000.0, "annual_interest_rate": 3.5, "loan_term_years": 30, "pi_monthly_payment": None}),
        ("Loan Amount", 200000.0, 3.5, 30, 1000.0, {"loan_amount": None, "annual_interest_rate": 3.5, "loan_term_years": 30, "pi_monthly_payment": 1000.0}),
        ("Loan Term", 200000.0, 3.5, 30, 1000.0, {"loan_amount": 200000.0, "annual_interest_rate": 3.5, "loan_term_years": None, "pi_monthly_payment": 1000.0}),
        ("Interest Rate", 200000.0, 3.5, 30, 1000.0, {"loan_amount": 200000.0, "annual_interest_rate": 3.5, "loan_term_years": 30, "pi_monthly_payment": 1000.0}),
    ]
)
def test_build_payload(calc_type, loan_amt, annual_rate, loan_term, monthly_pay, expected_payload):
    payload = build_payload(calc_type, loan_amt, annual_rate, loan_term, monthly_pay)
    assert payload == expected_payload

# --- Tests for display_result ---
@pytest.mark.parametrize(
    "calc_type, api_result, expected_st_writes",
    [
        ("Monthly Payment", {"pi_monthly_payment": 1234.56}, ["Calculated Monthly Payment: $1,234.56"]),
        ("Loan Amount", {"loan_amount": 300000.00}, ["Maximum Loan Amount: $300,000.00"]),
        ("Loan Term", {"loan_term_years": 25}, ["Required Loan Term: 25 years"]),
        ("Interest Rate", {"annual_interest_rate": 4.25}, ["Required Annual Interest Rate: 4.25%"]),
        ("Unknown Type", {"foo": "bar"}, ["{'foo': 'bar'}"]), # Mock a generic API result for unknown type
    ]
)
@patch('streamlit.subheader')
@patch('streamlit.write')
def test_display_result(mock_st_write, mock_st_subheader, calc_type, api_result, expected_st_writes):
    display_result(calc_type, api_result)

    mock_st_subheader.assert_called_once_with(f"Calculation Result ({calc_type})")
    # Verify st.write calls
    actual_writes = [call.args[0] for call in mock_st_write.call_args_list]

    if calc_type == "Unknown Type":
        assert actual_writes[0] == api_result # Directly compare the dictionary
    else:
        assert len(actual_writes) == len(expected_st_writes)
        for i, expected_write_prefix in enumerate(expected_st_writes):
            # Check if the expected prefix is in the actual output, allowing for formatting variations
            assert expected_write_prefix.split(":")[0] in actual_writes[i]

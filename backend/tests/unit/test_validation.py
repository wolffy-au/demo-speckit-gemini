import pytest
from pydantic import ValidationError
from backend.src.models.mortgage import MortgageCalculationParameters

def test_mortgage_params_valid_input():
    params = MortgageCalculationParameters(
        loan_amount=100000.0,
        annual_interest_rate=3.5,
        loan_term_years=30,
        pi_monthly_payment=449.04
    )
    assert params.loan_amount == 100000.0
    assert params.annual_interest_rate == 3.5
    assert params.loan_term_years == 30
    assert params.pi_monthly_payment == 449.04

def test_mortgage_params_invalid_loan_amount():
    with pytest.raises(ValidationError):
        MortgageCalculationParameters(loan_amount=500.0) # Below minimum

def test_mortgage_params_invalid_interest_rate_high():
    with pytest.raises(ValidationError):
        MortgageCalculationParameters(annual_interest_rate=101.0) # Above maximum

def test_mortgage_params_invalid_interest_rate_low():
    with pytest.raises(ValidationError):
        MortgageCalculationParameters(annual_interest_rate=-1.0) # Below minimum

def test_mortgage_params_invalid_loan_term():
    with pytest.raises(ValidationError):
        MortgageCalculationParameters(loan_term_years=0) # Below minimum

def test_mortgage_params_invalid_pi_monthly_payment():
    with pytest.raises(ValidationError):
        MortgageCalculationParameters(pi_monthly_payment=0.0) # Below minimum

def test_mortgage_params_nullable_fields():
    # Should allow one field to be None if others are present
    params = MortgageCalculationParameters(
        loan_amount=100000.0,
        annual_interest_rate=3.5,
        loan_term_years=30,
        pi_monthly_payment=None # Valid case for calculation
    )
    assert params.pi_monthly_payment is None

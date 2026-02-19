import pytest
import httpx
import json

# Base URL for the API. In a real scenario, this might be configurable
# or set via environment variables. For contract tests, we assume a running instance.
# For now, we'll use localhost:8000 as per quickstart.md
API_BASE_URL = "http://localhost:8000"

@pytest.mark.asyncio
async def test_calculate_monthly_payment_contract():
    """
    Contract test for calculating monthly payment.
    Verifies the API can calculate the monthly payment given other parameters.
    """
    test_data = {
        "loan_amount": 200000.00,
        "annual_interest_rate": 3.5,
        "loan_term_years": 30,
        # pi_monthly_payment is null because it's the target to calculate
        "pi_monthly_payment": None
    }

    async with httpx.AsyncClient(base_url=API_BASE_URL) as client:
        response = await client.post("/calculate", json=test_data)

    # Assert status code
    assert response.status_code == 200

    # Assert response content type and structure
    assert "application/json" in response.headers["content-type"]
    response_json = response.json()

    # Assert that the calculated monthly payment is a positive float
    assert "pi_monthly_payment" in response_json
    calculated_payment = response_json["pi_monthly_payment"]
    assert isinstance(calculated_payment, float)
    assert calculated_payment > 0.01 # Based on schema minimum

    # Optionally, assert other fields returned (they might be echoed back)
    assert "loan_amount" in response_json
    assert response_json["loan_amount"] == test_data["loan_amount"]
    assert "annual_interest_rate" in response_json
    assert response_json["annual_interest_rate"] == test_data["annual_interest_rate"]
    assert "loan_term_years" in response_json
    assert response_json["loan_term_years"] == test_data["loan_term_years"]

# Add more contract tests for other calculation types (loan_amount, loan_term, interest_rate)
# and for error cases (e.g., invalid inputs) as needed.

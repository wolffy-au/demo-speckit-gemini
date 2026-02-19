import pytest
from httpx import AsyncClient, ASGITransport
from backend.src.api.main import app # Assuming app is directly imported from main
from backend.src.models.mortgage import MortgageCalculationParameters

@pytest.mark.asyncio
async def test_calculate_monthly_payment_success():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        response = await ac.post(
            "/calculate",
            json={
                "loan_amount": 200000.0,
                "annual_interest_rate": 3.5,
                "loan_term_years": 30,
                "pi_monthly_payment": None  # Target to calculate
            }
        )
    assert response.status_code == 200
    data = response.json()
    assert data["pi_monthly_payment"] == pytest.approx(898.09, rel=1e-2) # Example expected value

@pytest.mark.asyncio
async def test_calculate_monthly_payment_invalid_input():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        response = await ac.post(
            "/calculate",
            json={
                "loan_amount": 500.0, # Invalid loan amount
                "annual_interest_rate": 3.5,
                "loan_term_years": 30,
                "pi_monthly_payment": None
            }
        )
    assert response.status_code == 422 # Pydantic validation error
    assert "detail" in response.json()

@pytest.mark.asyncio
async def test_calculate_loan_amount_success():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        response = await ac.post(
            "/calculate",
            json={
                "loan_amount": None, # Target to calculate
                "annual_interest_rate": 4.0,
                "loan_term_years": 25,
                "pi_monthly_payment": 900.00
            }
        )
    assert response.status_code == 200
    data = response.json()
    assert data["loan_amount"] == pytest.approx(171052.79, rel=1e-2) # Example expected value

@pytest.mark.asyncio
async def test_calculate_loan_term_success():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        response = await ac.post(
            "/calculate",
            json={
                "loan_amount": 300000.0,
                "annual_interest_rate": 4.5,
                "loan_term_years": None, # Target to calculate
                "pi_monthly_payment": 1800.00
            }
        )
    assert response.status_code == 200
    data = response.json()
    assert data["loan_term_years"] == pytest.approx(22.0, rel=1e-2) # Example expected value (approx 22 years)


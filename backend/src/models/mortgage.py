from pydantic import BaseModel, Field

class MortgageCalculationParameters(BaseModel):
    loan_amount: float | None = Field(None, gt=1000.00, description="The total principal loan amount.")
    annual_interest_rate: float = Field(..., ge=0.0, le=100.0, description="The annual interest rate for the mortgage.")
    loan_term_years: int | None = Field(None, ge=1, description="The duration of the loan in years.")
    pi_monthly_payment: float | None = Field(None, ge=0.01, description="The monthly Principal & Interest payment.")

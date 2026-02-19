from fastapi import FastAPI, HTTPException, status
from backend.src.models.mortgage import MortgageCalculationParameters
from backend.src.services.mortgage_calculator import calculate_monthly_payment, calculate_loan_amount, calculate_loan_term_years

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Mortgage Calculator API"}

@app.post("/calculate", status_code=status.HTTP_200_OK)
async def calculate_mortgage(params: MortgageCalculationParameters):
    calculable_fields = [
        params.loan_amount,
        params.annual_interest_rate,
        params.loan_term_years,
        params.pi_monthly_payment
    ]
    none_count = calculable_fields.count(None)

    if none_count == 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No field to calculate. All parameters are provided."
        )
    elif none_count > 1:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Only one of 'loan_amount', 'loan_term_years', or 'pi_monthly_payment' can be None for calculation."
        )

    response_data = params.model_dump()

    try:
        if params.pi_monthly_payment is None:
            monthly_payment = calculate_monthly_payment(
                loan_amount=params.loan_amount,
                annual_interest_rate=params.annual_interest_rate,
                loan_term_years=params.loan_term_years
            )
            response_data["pi_monthly_payment"] = monthly_payment
        elif params.loan_amount is None:
            loan_amount = calculate_loan_amount(
                pi_monthly_payment=params.pi_monthly_payment,
                annual_interest_rate=params.annual_interest_rate,
                loan_term_years=params.loan_term_years
            )
            response_data["loan_amount"] = loan_amount
        elif params.loan_term_years is None:
            loan_term_years = calculate_loan_term_years(
                loan_amount=params.loan_amount,
                pi_monthly_payment=params.pi_monthly_payment,
                annual_interest_rate=params.annual_interest_rate
            )
            response_data["loan_term_years"] = loan_term_years
        # Add other calculation cases here (e.g., annual_interest_rate if it becomes calculable)

        return response_data
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

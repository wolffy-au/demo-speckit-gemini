import math
from pydantic import BaseModel, Field

# Placeholder for the Pydantic model, will be imported from backend.src.models.mortgage
# class MortgageCalculationParameters(BaseModel):
#     loan_amount: float = Field(..., gt=1000.00, description="The total principal loan amount.")
#     annual_interest_rate: float = Field(..., ge=0.0, le=100.0, description="The annual interest rate for the mortgage.")
#     loan_term_years: int = Field(..., ge=1, description="The duration of the loan in years.")
#     pi_monthly_payment: float = Field(..., ge=0.01, description="The monthly Principal & Interest payment.")

def calculate_monthly_payment(loan_amount: float, annual_interest_rate: float, loan_term_years: int) -> float:
    """
    Calculates the monthly Principal & Interest (P&I) payment for a mortgage.

    Formula: M = P [ i(1 + i)^n ] / [ (1 + i)^n – 1]
    Where:
        M = Monthly Payment
        P = Principal Loan Amount
        i = Monthly Interest Rate (annual_interest_rate / 12 / 100)
        n = Total Number of Payments (loan_term_years * 12)

    Args:
        loan_amount (float): The principal loan amount.
        annual_interest_rate (float): The annual interest rate (e.g., 3.5 for 3.5%).
        loan_term_years (int): The loan term in years.

    Returns:
        float: The calculated monthly P&I payment.

    Raises:
        ValueError: If inputs are invalid or calculation is impossible.
    """
    if loan_amount <= 0:
        raise ValueError("Loan amount must be positive.")
    if annual_interest_rate < 0 or annual_interest_rate > 100:
        raise ValueError("Annual interest rate must be between 0 and 100.")
    if loan_term_years <= 0:
        raise ValueError("Loan term must be positive.")

    if annual_interest_rate == 0:
        # Handle zero interest rate case to avoid division by zero
        if loan_term_years * 12 == 0: # Should not happen due to loan_term_years > 0
             return 0.0
        return loan_amount / (loan_term_years * 12)

    # Convert annual interest rate to monthly interest rate
    monthly_interest_rate = (annual_interest_rate / 100) / 12
    number_of_payments = loan_term_years * 12

    # Calculate monthly payment using the formula
    # M = P * [ i(1 + i)^n ] / [ (1 + i)^n – 1]
    try:
        # Using math.pow for (1 + i)^n
        numerator = monthly_interest_rate * math.pow(1 + monthly_interest_rate, number_of_payments)
        denominator = math.pow(1 + monthly_interest_rate, number_of_payments) - 1
        
        if denominator == 0: # Avoid division by zero if somehow calculated as zero
            raise ValueError("Calculation resulted in division by zero.")

        monthly_payment = loan_amount * (numerator / denominator)
        
        # Return rounded to 2 decimal places for currency
        return round(monthly_payment, 2)
        
    except OverflowError:
        raise ValueError("Calculation resulted in overflow. Inputs may be too large.")
    except Exception as e:
        # Catch any other unexpected math errors
        raise ValueError(f"An error occurred during calculation: {e}")

def calculate_loan_amount(pi_monthly_payment: float, annual_interest_rate: float, loan_term_years: int) -> float:
    """
    Calculates the principal loan amount (P) for a mortgage.

    Formula: P = M * [ (1 + i)^n – 1] / [ i(1 + i)^n ]
    Where:
        M = Monthly Payment
        P = Principal Loan Amount
        i = Monthly Interest Rate (annual_interest_rate / 12 / 100)
        n = Total Number of Payments (loan_term_years * 12)
    """
    if pi_monthly_payment <= 0:
        raise ValueError("Monthly payment must be positive.")
    if annual_interest_rate < 0 or annual_interest_rate > 100:
        raise ValueError("Annual interest rate must be between 0 and 100.")
    if loan_term_years <= 0:
        raise ValueError("Loan term must be positive.")

    monthly_interest_rate = (annual_interest_rate / 100) / 12
    number_of_payments = loan_term_years * 12

    if monthly_interest_rate == 0:
        return round(pi_monthly_payment * number_of_payments, 2)

    try:
        pow_n = math.pow(1 + monthly_interest_rate, number_of_payments)
        numerator = pi_monthly_payment * (pow_n - 1)
        denominator = monthly_interest_rate * pow_n
        
        if denominator == 0:
            raise ValueError("Calculation resulted in division by zero.")

        loan_amount = numerator / denominator
        return round(loan_amount, 2)
    except OverflowError:
        raise ValueError("Calculation resulted in overflow. Inputs may be too large.")
    except Exception as e:
        raise ValueError(f"An error occurred during calculation: {e}")

def calculate_loan_term_years(loan_amount: float, pi_monthly_payment: float, annual_interest_rate: float) -> int:
    """
    Calculates the loan term in years (n) for a mortgage.

    Formula derived from: M = P [ i(1 + i)^n ] / [ (1 + i)^n – 1]
    n = - log(1 - (P*i)/M) / log(1 + i)
    Where:
        M = Monthly Payment
        P = Principal Loan Amount
        i = Monthly Interest Rate (annual_interest_rate / 12 / 100)
        n = Total Number of Payments (loan_term_years * 12)
    """
    if loan_amount <= 0:
        raise ValueError("Loan amount must be positive.")
    if pi_monthly_payment <= 0:
        raise ValueError("Monthly payment must be positive.")
    if annual_interest_rate < 0 or annual_interest_rate > 100:
        raise ValueError("Annual interest rate must be between 0 and 100.")

    monthly_interest_rate = (annual_interest_rate / 100) / 12

    if monthly_interest_rate == 0:
        if pi_monthly_payment == 0:
            raise ValueError("Cannot calculate loan term with zero interest and zero monthly payment.")
        return math.ceil(loan_amount / pi_monthly_payment / 12) # Integer years

    try:
        # Check for edge case where monthly payment is too low to ever pay off the loan
        if pi_monthly_payment < (loan_amount * monthly_interest_rate):
            raise ValueError("Monthly payment is too low to pay off the loan.")

        # From M = P [ i(1 + i)^n ] / [ (1 + i)^n – 1]
        # Rearranging for n:
        # (1 + i)^n = (M/P) / (M/P - i)
        # n * log(1 + i) = log((M/P) / (M/P - i))
        # n = log((M/P) / (M/P - i)) / log(1 + i)

        term_numerator = math.log(pi_monthly_payment / (pi_monthly_payment - (loan_amount * monthly_interest_rate)))
        term_denominator = math.log(1 + monthly_interest_rate)

        if term_denominator == 0: # Should not happen with positive interest rate
            raise ValueError("Calculation resulted in division by zero for loan term.")

        total_payments = term_numerator / term_denominator
        loan_term_years = math.ceil(total_payments / 12) # Round up to the next full year
        return int(loan_term_years)

    except ValueError as e:
        raise ValueError(f"An error occurred during calculation: {e}")
    except Exception as e:
        raise ValueError(f"An error occurred during calculation: {e}")


# Data Model

## Entity: MortgageCalculationParameters

This entity represents the inputs and outputs for mortgage Principal & Interest (P&I) calculations.

### Fields

- **loan\_amount**: `float`
    - Description: The total principal loan amount.
    - Constraints: Must be a positive number, with a minimum value of 1000.00.
- **annual\_interest\_rate**: `float`
    - Description: The annual interest rate for the mortgage.
    - Constraints: Must be a percentage between 0.0 and 100.0.
- **loan\_term\_years**: `int`
    - Description: The duration of the loan in years.
    - Constraints: Must be a positive integer, with a minimum value of 1.
- **pi\_monthly\_payment**: `float`
    - Description: The monthly Principal & Interest payment.
    - Constraints: Must be a positive number, with a minimum value of 0.01.

### Relationships

No relationships defined for this entity in the current scope.

### Validation

All fields will be validated using Pydantic models according to the types and constraints defined above.

# Quickstart Guide

This guide provides instructions on how to set up and run the Mortgage Calculator application locally.

## Prerequisites

*   Python 3.10+
*   Pip (Python package installer)
*   Git
*   Docker (for development/deployment environment)

## Project Setup

1.  **Clone the repository**:
    ```bash
    git clone <repository_url>
    cd demo-speckit-gemini
    git checkout 001-mortgage-calculator
    ```

2.  **Set up Python environment**:
    It is recommended to use a virtual environment.
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows use `source .venv\Scripts\activate`
    ```

3.  **Install backend dependencies**:
    Navigate to the backend directory and install requirements.
    ```bash
    cd backend
    pip install -r requirements.txt # Assuming requirements.txt exists or will be created
    ```
    If `requirements.txt` is not yet generated, it should include:
    ```
    fastapi
    uvicorn
    pydantic
    ```

4.  **Install frontend dependencies**:
    Navigate to the frontend directory and install requirements.
    ```bash
    cd ../frontend
    pip install -r requirements.txt # Assuming requirements.txt exists or will be created
    ```
    If `requirements.txt` is not yet generated, it should include:
    ```
    streamlit
    ```

## Running the Application

1.  **Start the FastAPI backend**:
    Ensure you are in the `backend` directory.
    ```bash
    uvicorn src.api.main:app --reload
    ```
    (Note: Adjust `src.api.main:app` if your FastAPI app entry point is different.)

2.  **Start the Streamlit frontend**:
    Ensure you are in the `frontend` directory.
    ```bash
    streamlit run src/pages/main.py # Assuming main.py is your entry point
    ```
    (Note: Adjust `src/pages/main.py` if your Streamlit app entry point is different.)

The application should now be accessible via your web browser, typically at `http://localhost:8501` for Streamlit and `http://localhost:8000` for FastAPI.

## Development Notes

- The API contract is defined in `contracts/openapi.yaml`.
- Data models are defined using Pydantic and documented in `data-model.md`.
- Calculations are designed to meet performance goals (500ms latency).
- Security relies on input validation as sensitive data is not stored.

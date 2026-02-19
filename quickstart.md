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
    ```bash
    pip install -r backend/requirements.txt
    ```
    (This assumes `requirements.txt` will be in the `backend/` directory and will include `fastapi`, `uvicorn`, `pydantic`.)

4.  **Install frontend dependencies**:
    ```bash
    pip install -r frontend/requirements.txt
    ```
    (This assumes `requirements.txt` will be in the `frontend/` directory and will include `streamlit`.)

## Running the Application

1.  **Start the FastAPI backend**:
    ```bash
    uvicorn backend.src.api.main:app --reload
    ```
    (Note: Adjust `backend.src.api.main:app` if your FastAPI app entry point is different.)

2.  **Start the Streamlit frontend**:
    ```bash
    streamlit run frontend/src/pages/main.py
    ```
    (Note: Adjust `frontend/src/pages/main.py` if your Streamlit app entry point is different.)

The application should now be accessible via your web browser, typically at `http://localhost:8501` for Streamlit and `http://localhost:8000` for FastAPI.

## Development Notes

- The API contract is defined in `contracts/openapi.yaml`.
- Data models are defined using Pydantic and documented in `data-model.md`.
- Calculations are designed to meet performance goals (500ms latency).
- Security relies on input validation as sensitive data is not stored.

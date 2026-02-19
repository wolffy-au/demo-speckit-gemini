# Demo SpecKit Gemini Application

This is a demonstration application showcasing a backend API built with FastAPI and a frontend interface built with Streamlit. It includes a mortgage calculator functionality.

## Prerequisites

Before you begin, ensure you have the following installed:

*   **Python 3.8+**: This project requires Python 3.8 or newer.
*   **pip**: Python's package installer, usually comes with Python.

## Installation

Follow these steps to set up the project and install its dependencies:

1.  **Clone the Repository (if not already done):**
    ```bash
    git clone <repository-url> # Replace <repository-url> with the actual URL
    cd demo-speckit-gemini
    ```

2.  **Create and Activate a Virtual Environment:**

    It's recommended to use a virtual environment to manage project dependencies.

    *   **Windows:**
        ```bash
        python -m venv .venv
        .\.venv\Scripts\activate
        ```
    *   **macOS / Linux:**
        ```bash
        python3 -m venv .venv
        source ./.venv/bin/activate
        ```

3.  **Install Backend Dependencies:**
    With your virtual environment activated:
    ```bash
    pip install -r backend/requirements.txt
    ```

4.  **Install Frontend Dependencies:**
    With your virtual environment activated:
    ```bash
    pip install -r frontend/requirements.txt
    ```

## Running the Application

Once the dependencies are installed and the virtual environment is activated, you can start the backend and frontend services.

1.  **Start the Backend Service:**
    Open a terminal, activate your virtual environment, and run:
    The backend API is built with FastAPI and will run on `http://localhost:8000`.
    ```bash
    python -m uvicorn backend.src.api.main:app --host 0.0.0.0 --port 8000 --reload
    ```
    *Keep this terminal open as the backend service runs. For background operation, you might need to use a process manager like `nohup` or `screen` (on Linux/macOS) or run it as a service.*

2.  **Start the Frontend Service:**
    Open a *new terminal*, activate the virtual environment, and start the Streamlit frontend. It will run on `http://localhost:8501`.
    ```bash
    python -m streamlit run frontend/src/pages/main.py --server.port 8501 --server.headless true
    ```
    You can then access the frontend application in your web browser at `http://localhost:8501`.

## Running Tests

To run the project's tests, ensure your virtual environment is activated and execute the following command:

```bash
python -m pytest tests/contract/test_mortgage_api.py
```
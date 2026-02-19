import pytest
from unittest.mock import patch, MagicMock
from frontend.src.services.api_client import call_mortgage_api
import requests # Import requests to mock it

@patch('requests.post')
def test_call_mortgage_api_success(mock_post):
    # Mock a successful API response
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"pi_monthly_payment": 1000.0}
    mock_response.raise_for_status.return_value = None # Simulate no HTTP errors
    mock_post.return_value = mock_response

    endpoint = "calculate"
    data = {"loan_amount": 200000.0, "annual_interest_rate": 3.5, "loan_term_years": 30, "pi_monthly_payment": None}

    result = call_mortgage_api(endpoint, data)

    mock_post.assert_called_once_with(f"http://localhost:8000/{endpoint}", json=data)
    assert result == {"pi_monthly_payment": 1000.0}

@patch('requests.post')
def test_call_mortgage_api_http_error(mock_post):
    # Mock an HTTP error response (e.g., 404, 500)
    mock_response = MagicMock()
    mock_response.status_code = 404
    mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError("404 Client Error")
    mock_post.return_value = mock_response

    endpoint = "calculate"
    data = {"loan_amount": 200000.0, "annual_interest_rate": 3.5, "loan_term_years": 30, "pi_monthly_payment": None}

    # Simulate Streamlit's st.error to capture its call
    with patch('streamlit.error') as mock_st_error:
        result = call_mortgage_api(endpoint, data)

        mock_post.assert_called_once_with(f"http://localhost:8000/{endpoint}", json=data)
        mock_st_error.assert_called_once_with("API Error: 404 Client Error")
        assert result is None

@patch('requests.post')
def test_call_mortgage_api_connection_error(mock_post):
    # Mock a connection error
    mock_post.side_effect = requests.exceptions.ConnectionError("Connection refused")

    endpoint = "calculate"
    data = {"loan_amount": 200000.0, "annual_interest_rate": 3.5, "loan_term_years": 30, "pi_monthly_payment": None}

    with patch('streamlit.error') as mock_st_error:
        result = call_mortgage_api(endpoint, data)

        mock_post.assert_called_once_with(f"http://localhost:8000/{endpoint}", json=data)
        mock_st_error.assert_called_once_with("API Error: Connection refused")
        assert result is None

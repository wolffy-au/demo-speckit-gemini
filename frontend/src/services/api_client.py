import streamlit as st
import requests

def call_mortgage_api(endpoint, data):
    try:
        # Assuming FastAPI is running on localhost:8000
        response = requests.post(f"http://localhost:8000/{endpoint}", json=data)
        response.raise_for_status()  # Raise an exception for bad status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"API Error: {e}")
        return None

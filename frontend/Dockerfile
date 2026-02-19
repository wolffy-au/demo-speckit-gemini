# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy requirements.txt first to leverage Docker layer caching
COPY frontend/requirements.txt ./

# Install frontend dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application's source code
COPY frontend/src ./src
COPY frontend/tests ./tests

# Expose the port Streamlit runs on
EXPOSE 8501

# Command to run the application using Streamlit
CMD ["streamlit", "run", "src/pages/main.py", "--server.port", "8501", "--server.headless", "true"]

# Use an official Python runtime as a parent image
FROM python:3.11-slim as builder

# Set the working directory in the container
WORKDIR /app

# Install Poetry for dependency management
RUN pip install poetry

# Copy pyproject.toml and poetry.lock (if it exists)
COPY pyproject.toml poetry.lock* ./

# Install dependencies using Poetry
RUN poetry install --no-root --no-interaction --no-ansi

# Copy the rest of the application's source code
COPY . ./

# Expose the port Uvicorn will run on
EXPOSE 8000

# Command to run the application using Uvicorn
# Using --reload for development convenience. Remove for production.
CMD ["poetry", "run", "uvicorn", "backend.src.api.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

# Note: For a production build, consider a multi-stage build to create a smaller image.

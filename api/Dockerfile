# Use official Python runtime as base image
FROM python:3.12-slim

# Install curl (required for healthcheck)
# hadolint ignore=DL3008
RUN apt-get update && apt-get install -y --no-install-recommends curl \
    && rm -rf /var/lib/apt/lists/*

# Set working directory inside container
WORKDIR /app

# Copy requirements first (for better caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY main.py .

# Healthcheck (required for docker-compose dependency conditions)
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
  CMD curl -f http://localhost:8000/health || exit 1

# Expose the port the app runs on
EXPOSE 8000

# Command to run the API server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

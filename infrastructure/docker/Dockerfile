# Use a lightweight stable Python base to reduce image size and attack surface
FROM python:3.11-slim

# Define internal working directory inside the container
WORKDIR /app

# Copy requirements first to leverage Docker layer caching (faster builds)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project structure (src, infrastructure, tests, etc.)
COPY . .

# Monitoring: Basic health check to ensure the environment is ready
HEALTHCHECK --interval=30s --timeout=3s \
  CMD python -c "import os; exit(0 if os.path.exists('src/netgen.py') else 1)"

# Entrypoint: Executes the generator. 
# We target the src/ folder specifically.
ENTRYPOINT ["python", "src/netgen.py"]
# 1. Use a lightweight stable Python base
FROM python:3.11-slim

# 2. Set the working directory
WORKDIR /app

# 3. Install system dependencies (needed for curl healthchecks)
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# 4. Copy requirements and install (Layer caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the entire project structure
COPY . .

# 6. CRITICAL: Set PYTHONPATH so the API can find src/logic.py
ENV PYTHONPATH=/app

# 7. Monitoring: Updated to check the actual API status
HEALTHCHECK --interval=30s --timeout=10s --retries=3 \
  CMD curl -f http://localhost:8000/health || exit 1

# 8. Entrypoint: Starts the FastAPI server instead of a one-time script
EXPOSE 8000
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
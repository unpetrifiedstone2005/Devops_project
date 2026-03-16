# Use a lightweight stable Python base
FROM python:3.11-slim

# Define internal working directory
WORKDIR /app

# Install dependencies first to optimize Docker layer caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code and configurations
COPY . .

# Default entrypoint for the generator tool
ENTRYPOINT ["python", "src/netgen.py"]
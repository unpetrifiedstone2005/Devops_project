# Container Network Policy Generator 🚀

## Overview

This DevOps utility automates the generation of Kubernetes `NetworkPolicy` manifests via a **Secure REST API**. By exposing the generator through **FastAPI**, it allows teams to dynamically request security policies by providing application dependencies in a structured JSON format. This tool enforces **Zero Trust** and **Least Privilege** network security across microservices, eliminating the need for manual YAML authoring.

---

## 📂 Project Structure

Following professional DevOps directory standards, the repository is organized as follows:

```text
Devops_project/
│
├── .github/workflows/         # CI/CD pipeline (Linting, Tests, Docker Build)
├── docs/                      # Technical documentation (architecture, guides)
├── infrastructure/
│   ├── kubernetes/            # Configuration management data (app.json)
│   └── docker/                # Dockerfile and docker-compose.yml
├── src/                       # Core Python implementation
│   ├── main.py                # FastAPI Service (API Entry point)
│   ├── logic.py               # Core Generation Engine
│   └── tests/                 # Unit and Integration tests (pytest)
├── requirements.txt           # Python dependency manifest
└── README.md
```

---

## 🛠️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/unpetrifiedstone2005/Devops_project.git
cd Devops_project
```

### 2. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

---

## 🚀 Usage

### Local API Execution

To run the generator as a live local service:

```bash
python -m uvicorn src.main:app --reload
```

```text
The service will be available at http://127.0.0.1:8000. Access the Interactive Swagger UI at http://127.0.0.1:8000/docs.
```

---

### Docker Execution

The tool is fully containerized and orchestrated via Docker Compose to ensure portability and environment consistency.

#### Start the Service

```bash
docker compose -f infrastructure/docker/docker-compose.yml up --build
```

#### Test the API (Input Data via Postman/Curl)

```text
Since the tool is a REST API, you "input" data using a POST request. You must include the X-API-KEY header for authentication.
```

#### Using Curl:

```bash
curl -X POST http://localhost:8000/generate \
     -H "Content-Type: application/json" \
     -H "X-API-KEY: devops-internal-secret" \
     -d '{
       "name": "frontend-service",
       "labels": {"app": "web-ui"},
       "ingress_sources": [{"app_name": "load-balancer", "port": 80}]
     }'
```

---

## 🛡️ DevOps Implementation Details

### ✅ Secure REST API (FastAPI)

The tool uses Pydantic for strict data validation, ensuring that only valid JSON schemas can generate Kubernetes manifests.

---

### ✅ Authentication & Security
Following Zero Trust principles, the API is protected by a custom header-based authentication system (X-API-KEY). This prevents unauthorized access to internal infrastructure tools.

---

### ✅ CI/CD Pipeline
Automated via GitHub Actions. Every push triggers a workflow that:

Sets up a Python 3.11 environment.

Performs Linting (flake8) to ensure code quality.

Runs the pytest suite covering both core logic and API endpoints.

Executes a Docker Build Check to verify infrastructure integrity.

---

### Configuration Management & IaC
Following Infrastructure as Code (IaC) principles, application configuration is separated from logic. Service dependency definitions can be stored in infrastructure/kubernetes/app.json, allowing policies to be updated without modifying source code.

---

## 🧪 Testing

Run the automated test suite to verify generator logic:

```bash
python -m pytest src/tests/
```

---

## 💡 Updating the Repository

If you encounter a rejected push when updating the repository, run:

```bash
git add .
git commit -m "docs: complete enterprise readme and structure update"
git push origin main --force
```

---

## 📌 Summary

The **Container Network Policy Generator** provides a lightweight DevOps tool that:

* Automatically generates Kubernetes `NetworkPolicy` manifests
* Enforces **Zero Trust networking**
* Implements **Infrastructure as Code**
* Integrates **CI/CD testing pipelines**
* Supports **containerized execution via Docker**

This helps DevOps teams maintain secure and scalable microservice communication without manual policy configuration.

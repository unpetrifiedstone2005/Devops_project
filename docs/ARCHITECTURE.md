# Technical Architecture: Network Policy Generator Service 🏗️

## Overview
The Network Policy Generator has evolved from a CLI utility into a **Secure RESTful Microservice**. It automates the creation of Kubernetes `NetworkPolicy` manifests by acting as an abstraction layer between high-level service requirements (JSON) and low-level infrastructure configuration (YAML).



---

## 🛰️ System Components

### 1. API Layer (FastAPI)
The entry point of the application. It manages the lifecycle of the HTTP request and handles:
* **Routing**: Directing traffic to the `/generate` and `/health` endpoints.
* **Authentication**: Intercepting requests to verify the `X-API-KEY` header.
* **Asynchronous Handling**: Utilizing Uvicorn to handle concurrent requests efficiently.

### 2. Validation Layer (Pydantic)
Before any logic is executed, the raw JSON payload is parsed into **Pydantic Models**. 
* **Schema Enforcement**: Ensures that ports are integers, names are strings, and lists are formatted correctly.
* **Auto-Documentation**: Generates the OpenAPI/Swagger schema used for the interactive docs at `/docs`.

### 3. Core Engine (Logic Layer)
The transformation engine located in `src/logic.py`. 
* **Mapping**: Translates the validated `AppSpec` objects into the Kubernetes `networking.k8s.io/v1` specification.
* **Policy Templating**: Dynamically builds the `podSelector`, `ingress`, and `egress` blocks based on the provided intent.

### 4. Infrastructure Layer (Docker & Compose)
The service is encapsulated in a **Debian-based Python slim image** to ensure a minimal attack surface.
* **Docker Compose**: Orchestrates the environment, managing port mapping (`8000:8000`), volume mounts, and environment variables.

---

## 🔄 Logic Flow
1. **Request**: A client (Postman/Curl/CI-CD) sends a `POST` request with a JSON body and an API Key.
2. **AuthN/AuthZ**: The API Layer validates the secret key.
3. **Parse & Validate**: Pydantic converts the JSON into a Python object; if invalid, it returns a `422` error.
4. **Transform**: The Logic Engine iterates through the `ingress_sources` and `egress_destinations` to build the YAML structure.
5. **Response**: The service returns a JSON object containing the ready-to-use Kubernetes YAML manifest.



---

## 🛡️ Security & Impact
* **Zero Trust Enforcement**: The tool defaults to a "Deny All" mindset by requiring explicit definitions for every connection.
* **Credential Management**: Security is handled via environment variables (`API_KEY`), ensuring secrets are never hardcoded in the logic.
* **Attack Surface Reduction**: By providing a containerized API, the tool can be deployed as an internal utility within a cluster, accessible only to authorized CI/CD runners.

---

## 📊 Monitoring & Observability
* **Structured Logging**: Standardized logs track every request, capturing timestamps, source IPs, and generation status.
* **Health Monitoring**: A dedicated `/health` endpoint allows orchestrators (like Kubernetes or Docker) to perform liveness and readiness probes.

---

## ⚙️ Configuration Management
Adhering to **Infrastructure as Code (IaC)** principles, the application logic is strictly decoupled from configuration:
* **Input Decoupling**: Service intents are defined in `infrastructure/kubernetes/app.json`.
* **Environment Parity**: The same Docker image is used across Dev, Test, and Prod, with behavior altered only by environment variables and injected JSON data.
# Container Network Policy Generator 🚀

## Overview

This DevOps utility automates the generation of Kubernetes `NetworkPolicy` manifests. By defining application dependencies in a structured JSON format, the tool enforces **Zero Trust** and **Least Privilege** network security across microservices, eliminating the need for manual YAML authoring.

---

## 📂 Project Structure

Following professional DevOps directory standards, the repository is organized as follows:

```
Devops_project/
│
├── .github/workflows/        # CI/CD pipeline definitions (GitHub Actions)
├── docs/                     # Technical documentation (architecture, guides)
├── infrastructure/
│   ├── kubernetes/           # Configuration management data (app.json)
│   └── docker/               # Containerization logic and Dockerfile
├── src/                      # Core Python implementation and logic
├── tests/
│   └── unit/                 # Automated unit tests using pytest
├── requirements.txt          # Python dependency manifest
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

### Local Execution

To generate a network policy using the default configuration:

```bash
python src/netgen.py infrastructure/kubernetes/app.json
```

---

### Docker Execution

The tool is fully containerized to ensure portability and environment consistency.

#### Build the Image

```bash
docker build -t netgen .
```

#### Run the Generator

**Windows (PowerShell / CMD)**

```bash
docker run -v %cd%:/app netgen infrastructure/kubernetes/app.json
```

**Linux / Mac**

```bash
docker run -v $(pwd):/app netgen infrastructure/kubernetes/app.json
```

The generated Kubernetes `NetworkPolicy` YAML will be output to the mounted directory.

---

## 🛡️ DevOps Implementation Details

### ✅ CI/CD Pipeline

Automated via **GitHub Actions**. Every push triggers a workflow that:

* Sets up a **Python 3.11 environment**
* Installs required dependencies
* Runs the **pytest test suite** located in `tests/unit/`
* Performs a **smoke test** by executing the generator to ensure valid artifact creation

---

### ✅ Monitoring & Observability

The project uses Python’s built-in **logging** library to provide structured operational logs.

This ensures:

* Validation errors are clearly visible
* Execution results are traceable
* Logs can be easily integrated with external log aggregation tools

---

### ✅ Configuration Management

Following **Infrastructure as Code (IaC)** principles, application configuration is separated from logic.

All service dependency definitions are stored in:

```
infrastructure/kubernetes/app.json
```

This allows network policies to be updated without modifying source code.

---

### ✅ Containerization

The project includes a **multi-layered Dockerfile** using the lightweight base image:

```
python:3.11-slim
```

Benefits:

* Reduced attack surface
* Faster build times
* Consistent runtime environment across systems

---

## 🧪 Testing

Run the automated test suite to verify generator logic:

```bash
python -m pytest tests/unit/
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

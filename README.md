Markdown

# Container Network Policy Generator 🚀

## Overview
This DevOps utility automates the generation of Kubernetes `NetworkPolicy` manifests. By defining application dependencies in a structured JSON format, the tool ensures **Zero Trust** and **Least Privilege** network security across microservices, eliminating the need for manual YAML authoring.

---

## 📂 Project Structure
Following professional DevOps directory standards, the repository is organized as follows:

* **`.github/workflows/`**: CI/CD pipeline definitions (GitHub Actions).
* **`docs/`**: Technical documentation including Architecture and User Guides.
* **`infrastructure/`**: 
    * `kubernetes/`: Configuration management data (`app.json`).
    * `docker/`: Containerization logic and Dockerfile.
* **`src/`**: Core Python implementation and logic.
* **`tests/unit/`**: Automated unit tests using `pytest`.
* **`requirements.txt`**: Project dependency manifest.

---

## 🛠️ Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone [https://github.com/unpetrifiedstone2005/Devops_project.git](https://github.com/unpetrifiedstone2005/Devops_project.git)
   cd Devops_project
Install dependencies:

Bash

python -m pip install -r requirements.txt
🚀 Usage
1. Local Execution
To generate a policy using the default configuration:

Bash

python src/netgen.py infrastructure/kubernetes/app.json
2. Docker Execution
The tool is fully containerized to ensure portability and environment consistency.

Bash

# Build the image from the root directory
docker build -t netgen .

# Run the generator and output the YAML to your current directory
# Windows (PowerShell/CMD):
docker run -v %cd%:/app netgen infrastructure/kubernetes/app.json

# Linux/Mac:
docker run -v $(pwd):/app netgen infrastructure/kubernetes/app.json
🛡️ DevOps Implementation Details
✅ CI/CD Pipeline
Automated via GitHub Actions. Every push triggers a workflow that:

Sets up a Python 3.11 environment.

Installs required dependencies.

Executes the pytest suite in tests/unit/.

Performs a validation "Smoke Test" by running the generator logic to ensure artifact creation.

✅ Monitoring & Observability
The tool utilizes the Python logging library to provide structured operational logs. This ensures that success states and validation errors are easily trackable by log aggregation tools, satisfying infrastructure monitoring requirements.

✅ Configuration Management
Adhering to "Infrastructure as Code" (IaC) principles, application intent is decoupled from logic. The network rules are managed via infrastructure/kubernetes/app.json, allowing for policy updates without source code modification.

✅ Containerization
The project includes a multi-layered Dockerfile utilizing a python:3.11-slim base image to ensure a minimal security attack surface and rapid deployment across different environments.

🧪 Testing
Run the automated test suite to verify logic integrity:

Bash

python -m pytest tests/unit/



### 💡 Final Steps to Sync GitHub
Now that your file is ready, run these exact commands in your terminal to fix that "rejected" error and update your repo:

1. `git add .`
2. `git commit -m "docs: complete enterprise readme and structure update"`
3. `git push origin main --force` 


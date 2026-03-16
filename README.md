# Container Network Policy Generator 🚀

## Overview
This DevOps utility automates the creation of Kubernetes `NetworkPolicy` manifests. By defining application dependencies in a simple JSON format, developers can ensure "Least Privilege" network security without manually writing complex YAML.

## 📂 Project Structure
- `src/`: Core logic and input specifications.
- `tests/`: Automated unit tests using `pytest`.
- `docs/`: Technical architecture and security context.
- `Dockerfile`: Containerization configuration.
- `.github/workflows/`: CI/CD pipeline automation.

## 🛠️ Installation & Setup
1. **Clone the repository** and navigate to the project root.
2. **Install dependencies**:
   ```cmd
   python -m pip install -r requirements.txt
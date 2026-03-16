# Configuration & User Guide

## 🛠️ Input Specification (`app.json`)
The generator uses a JSON schema to define network intent. This file acts as your **Configuration Management** source.

### File Location
`infrastructure/kubernetes/app.json`

### Field Definitions
| Field | Type | Description |
| :--- | :--- | :--- |
| `name` | String | The unique name of the application. |
| `namespace` | String | The K8s namespace (e.g., `production`, `staging`). |
| `labels` | Object | The labels used to identify the target Pods. |
| `ingress_sources` | Array | Services allowed to send traffic TO this app. |
| `egress_destinations` | Array | Services this app is allowed to communicate WITH. |

---

## ➕ How to Add a New Rule

To allow a new service (e.g., `metrics-server`) to access your app on port `9090`:

1.  Open **`infrastructure/kubernetes/app.json`**.
2.  Add the following object to the `ingress_sources` array:
    ```json
    {
      "app_name": "metrics-server", 
      "port": 9090
    }
    ```
3.  Save the file and re-run the generator.

---

## 🚀 Running the Tool

### Local Execution
Ensure you are in the project root and run:
```bash
python src/netgen.py infrastructure/kubernetes/app.json
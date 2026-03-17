# Configuration & User Guide 📖

## 🛠️ Input Specification (`app.json`)
The generator uses a structured JSON schema to define network intent. This file serves as your **Infrastructure as Code (IaC)** source of truth.

### File Location
`infrastructure/kubernetes/app.json`

### Field Definitions
| Field | Type | Description |
| :--- | :--- | :--- |
| `name` | String | **Required.** The unique name of the application. |
| `namespace` | String | The K8s namespace (Defaults to `default`). |
| `labels` | Object | **Required.** Labels used to identify the target Pods. |
| `ingress_sources` | Array | Services allowed to send traffic **TO** this app. |
| `egress_destinations` | Array | Services this app is allowed to communicate **WITH**. |

---

## ➕ How to Update Network Rules

To allow a new service (e.g., `monitoring-agent`) to access your app on port `9090`:

1.  **Modify the JSON**: Open your request body or `app.json` and update the `ingress_sources`:
    ```json
    {
      "app_name": "monitoring-agent", 
      "port": 9090
    }
    ```
2.  **Submit to API**: Send the updated JSON via a `POST` request to the `/generate` endpoint.
3.  **Apply to Cluster**: Take the returned YAML and run `kubectl apply -f manifest.yaml`.

---

## 🚀 Running the Service

### 1. Local Development Mode
Use this for rapid testing without the overhead of containers.

**Start the Server:**
```bash
python -m uvicorn src.main:app --reload
```
### Test with curl

```bash
curl -X POST [http://127.0.0.1:8000/generate](http://127.0.0.1:8000/generate) \
     -H "Content-Type: application/json" \
     -H "X-API-KEY: devops-internal-secret" \
     -d @infrastructure/kubernetes/app.json
```

### 2. Docker Compose (Production-Ready)

Use this to ensure your environment exactly matches the CI/CD pipeline.

### Start the Orchestrated Service:

```bash
docker compose -f infrastructure/docker/docker-compose.yml up --build
```


## 🧪 Interactive Documentation (Swagger)

FastAPI automatically generates an interactive testing environment.

1. Run the service.
Open your browser to: ```text http://127.0.0.1:8000/docs ```
Click Authorize and enter ```text devops-internal-secret ```.
Expand the POST ```text /generate``` section to test the API directly from the UI.






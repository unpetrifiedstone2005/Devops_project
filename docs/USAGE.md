# Configuration Guide

## Input Specification (`app.json`)
The generator uses a JSON schema to define network intent.

### Fields
| Field | Type | Description |
| :--- | :--- | :--- |
| `name` | String | The unique name of the application. |
| `namespace` | String | The K8s namespace (e.g., `production`, `staging`). |
| `labels` | Object | The labels used to identify the Pods. |
| `ingress_sources` | Array | List of apps allowed to send traffic TO this app. |
| `egress_destinations` | Array | List of apps this app is allowed to talk TO. |

### How to add a new rule
To allow a new service (e.g., `metrics-server`) to access your app on port `9090`:
1. Open `src/app.json`.
2. Add the following to the `ingress_sources` list:
   ```json
   {"app_name": "metrics-server", "port": 9090}
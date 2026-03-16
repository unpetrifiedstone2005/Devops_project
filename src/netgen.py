import json
import yaml
import sys
import logging
from pydantic import BaseModel, Field, ValidationError
from typing import List, Dict

# Configure logging for operational visibility
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

# Schema Definition: Ensures input data integrity using Pydantic
class AppSpec(BaseModel):
    name: str
    namespace: str = "default"
    labels: Dict[str, str]
    ingress_sources: List[Dict] = []
    egress_destinations: List[Dict] = []

def generate_policy(spec: AppSpec) -> dict:
    """Translates AppSpec into a Kubernetes NetworkPolicy manifest."""
    return {
        "apiVersion": "networking.k8s.io/v1",
        "kind": "NetworkPolicy",
        "metadata": {
            "name": f"{spec.name}-policy",
            "namespace": spec.namespace
        },
        "spec": {
            "podSelector": {"matchLabels": spec.labels},
            "policyTypes": ["Ingress", "Egress"], # Implements 'Default Deny' security
            "ingress": [
                {
                    "from": [{"podSelector": {"matchLabels": {"app": src["app_name"]}}}],
                    "ports": [{"protocol": "TCP", "port": src["port"]}]
                } for src in spec.ingress_sources
            ],
            "egress": [
                {
                    "to": [{"podSelector": {"matchLabels": {"app": dst["app_name"]}}}],
                    "ports": [{"protocol": "TCP", "port": dst["port"]}]
                } for dst in spec.egress_destinations
            ]
        }
    }

if __name__ == "__main__":
    # Handle CLI arguments: Default to src/app.json for local/docker runs
    input_file = sys.argv[1] if len(sys.argv) > 1 else "src/app.json"
    
    try:
        with open(input_file, "r") as f:
            data = json.load(f)
        
        # Validate input against schema
        spec = AppSpec(**data)
        policy = generate_policy(spec)
        
        # Export artifact to root directory for easy access
        output_file = f"{spec.name}-policy.yaml"
        with open(output_file, "w") as f:
            yaml.dump(policy, f, sort_keys=False)
            
        logging.info(f"✅ Success! Generated {output_file}")
        
    except ValidationError as e:
        logging.error(f"❌ Input Validation Failed: {e}")
    except FileNotFoundError:
        logging.error(f"❌ Error: {input_file} not found.")
    except Exception as e:
        logging.error(f"❌ Unexpected Runtime Error: {e}")
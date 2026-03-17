import yaml
from pydantic import BaseModel
from typing import List, Dict

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
            "policyTypes": ["Ingress", "Egress"],
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
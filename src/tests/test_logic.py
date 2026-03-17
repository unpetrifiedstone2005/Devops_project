import pytest
from src.logic import AppSpec, generate_policy

def test_policy_structure():
    """Verify that the generated YAML contains essential Kubernetes fields."""
    data = {
        "name": "test-app",
        "labels": {"app": "test-app"},
        "ingress_sources": [{"app_name": "web", "port": 80}]
    }
    spec = AppSpec(**data)
    policy = generate_policy(spec)
    
    assert policy["kind"] == "NetworkPolicy"
    assert "Ingress" in policy["spec"]["policyTypes"]
    # Ensure port mapping is correct
    assert policy["spec"]["ingress"][0]["ports"][0]["port"] == 80

def test_invalid_data():
    """Ensure Pydantic catches missing required fields (like 'labels')."""
    invalid_data = {"name": "fail-app"}
    with pytest.raises(Exception):
        AppSpec(**invalid_data)
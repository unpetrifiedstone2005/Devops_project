# Technical Architecture

## Overview
This tool automates the creation of Kubernetes NetworkPolicies. In a microservices environment, security is managed via "Least Privilege" access.

## Logic Flow
1. **Parser**: Reads `app.json` and validates data types using Pydantic.
2. **Generator**: Maps JSON objects to Kubernetes `networking.k8s.io/v1` API specs.
3. **Output**: Generates a YAML manifest ready for `kubectl apply`.

## Security Impact
By explicitly defining Ingress (incoming) and Egress (outgoing) rules, this tool prevents "lateral movement" if one container is compromised.

## Monitoring & Observability
The tool implements structured logging to provide operational visibility. By using the Python logging library, the generator produces standardized logs that track execution flow, validation successes, and detailed error reports, allowing for integration with log aggregation systems.

## Configuration Management
Adhering to DevOps best practices, the application logic is decoupled from its configuration. All network intents are defined in src/app.json, allowing for rapid updates to security policies without modifying the source code. This enables version-controlled configuration management and easier audits.
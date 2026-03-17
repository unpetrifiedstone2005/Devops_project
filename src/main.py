import os
from fastapi import FastAPI, Header, HTTPException, Depends
from src.logic import AppSpec, generate_policy

app = FastAPI()
API_KEY = os.getenv("API_KEY", "devops-internal-secret")

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/generate")
def api_generate(spec: AppSpec, x_api_key: str = Header(None)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Unauthorized")
    return {"yaml": generate_policy(spec)}
from fastapi import APIRouter
import pandas as pd
import joblib
import requests


healthcheck_router = APIRouter(tags=['Healthcheck'])


@healthcheck_router.get("/healthcheck")
def healthcheck()->dict:
    url = 'http://127.0.0.1:8000/'
    with open('model.pkl', 'rb') as file:
        model = joblib.load(file)
    
    if model is None:
        return  {"status": "error", "reason": "model"}
    
    response = requests.get(url, timeout=5)

    if response.status_code==200 and model:
        return {"status": "ok"}
    print(response.status_code)
    return {"status": "error", "reason": "unknown"}
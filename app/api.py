import uvicorn
from fastapi import FastAPI
from routes.prediction import prediction_router
from routes.healthcheck import healthcheck_router 
import subprocess
import os


app=FastAPI()
app.include_router(prediction_router)
app.include_router(healthcheck_router)

@app.get("/")
def home():
    return {"message": "Welcome to the Wine detection service home page!"}


if __name__ == "__main__":
    uvicorn.run("api:app", host="127.0.0.1", port=8000)

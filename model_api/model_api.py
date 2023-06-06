from fastapi import FastAPI
from .classifier import predict

app = FastAPI()

@app.post("/model_request")
async def model_request(text: str):
    prediction = predict(text)
    return {"prediction": prediction}
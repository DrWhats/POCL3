from fastapi import FastAPI
from classifier import predict
import database

app = FastAPI()


@app.post("/model_request")
async def model_request(text: dict):
    prediction = predict(text['question'])
    database.update_request_label(prediction, text['question'])
    return {"prediction": prediction}

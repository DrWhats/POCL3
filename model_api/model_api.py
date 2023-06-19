from fastapi import FastAPI
<<<<<<< Updated upstream
=======
import bot
>>>>>>> Stashed changes
from classifier import predict
import database

app = FastAPI()


@app.post("/model_request")
async def model_request(text: dict):
    prediction = predict(text['question'])
    database.update_request_label(prediction, text['question'])
<<<<<<< Updated upstream
    return {"prediction": prediction}
=======
    label_id = database.get_type_by_label(prediction)
    moders = database.get_type_moders(label_id)
    bot.send_notification_to_users(moders, "Aloha!")

>>>>>>> Stashed changes

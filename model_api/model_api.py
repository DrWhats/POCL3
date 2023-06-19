from fastapi import FastAPI
import bot
from classifier import predict
import database

app = FastAPI()


@app.post("/model_request")
async def model_request(text: dict):
    prediction = predict(text['question'])
    database.update_request_label(prediction, text['question'])
    label_id = database.get_type_by_label(prediction)
    moders = database.get_type_moders(label_id)
    bot.send_notification_to_users(moders, f"Новая заявка! \n"
                                           f"Пользователь: {text['fio']} \n"
                                           f"Телефон: {text['phone_number']} \n"
                                           f"Почта: {text['email']} \n"
                                           f"Тип проблемы: {prediction} \n"
                                           f"Описание: {text['question']}")

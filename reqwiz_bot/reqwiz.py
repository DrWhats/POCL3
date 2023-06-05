from telebot import TeleBot
import database

bot = TeleBot('6044613463:AAFQLGVBq_UJxIKJiYBYqVWeum1_VMSpIKk')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "/start":
        bot.send_message(message.from_user.id,
                         "Привет! напиши /reg, чтобы привязать учетную запись своего личного кабинета.")
    elif message.text == '/reg':
        bot.send_message(message.from_user.id, "Какой у тебя логин от личного кабинета?")
        bot.register_next_step_handler(message, get_login)  # следующий шаг – функция get_login
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши /reg, чтобы привязать учетную запись своего личного кабинета.")
    elif message.text == "Привет":
        print(database.get_all_types())
        bot.send_message(message.from_user.id, database.get_all_types())
        bot.send_message(message.from_user.id,
                         "Привет! напиши /reg, чтобы привязать учетную запись своего личного кабинета.")
    elif message.text == "привет":
        bot.send_message(message.from_user.id,
                         "Привет! напиши /reg, чтобы привязать учетную запись своего личного кабинета.")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю( Напиши /help или /reg.")


def get_login(message):  # получаем логин пользователя
    global login
    login = message.text
    bot.send_message(message.from_user.id, 'Какой у тебя пароль?')
    bot.register_next_step_handler(message, get_password)  # следующий шаг – функция get_password
    print(login)


def get_password(message):  # получаем пароль пользователя
    global password
    password = message.text
    print(password)


bot.polling(none_stop=True, interval=0)

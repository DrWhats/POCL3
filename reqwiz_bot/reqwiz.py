from telebot import TeleBot
import database
import textphrases as tf

bot = TeleBot('6044613463:AAFQLGVBq_UJxIKJiYBYqVWeum1_VMSpIKk')


@bot.message_handler(func=lambda message: message.text == 'Привет')
def get_hello(message):
    bot.send_message(message.from_user.id, tf.hello)


@bot.message_handler(commands=['start'])
def get_start(message):
    bot.send_message(message.from_user.id, tf.hello)


@bot.message_handler(commands=['reg'])
def reg(message):
    bot.send_message(message.from_user.id, tf.reg_login)
    bot.register_next_step_handler(message, get_login)  # следующий шаг – функция get_login


def get_login(message):  # получаем логин пользователя
    user = {'email': message.text}
    bot.send_message(message.from_user.id, tf.reg_password)
    bot.register_next_step_handler(message, get_password, user)  # следующий шаг – функция get_password


def get_password(message, user):  # получаем пароль пользователя
    user['password'] = message.text
    bot.send_message(message.from_user.id, "Ай маладес: " + str(user))
    check_user(user, message)


def check_user(user, message):
    if database.check_user(user['email'], user['password']):
        database.save_user(user['email'], message.from_user.id)
        bot.send_message(message.from_user.id, tf.wait_category)
    else:
        bot.send_message(message.from_user.id, tf.not_moder)


bot.polling(none_stop=True, interval=0)

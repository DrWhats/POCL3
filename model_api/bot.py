from telebot import TeleBot

bot = TeleBot('6044613463:AAFQLGVBq_UJxIKJiYBYqVWeum1_VMSpIKk')


def send_notification_to_users(user_ids, message_text):
    for user_id in user_ids:
        try:
            bot.send_message(chat_id=user_id, text=message_text)
        except Exception as e:
            print(f"Error sending message to user {user_id}: {e}")

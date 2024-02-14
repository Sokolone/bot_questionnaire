import telebot

from info import (
    start_message)

token = '6442534302:AAEN8cebwVk_IMk-RgLmpUL6nCjCxh8GGOo'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def bot_start_message(message):
    bot.send_message(message.chat.id, start_message)


bot.polling()


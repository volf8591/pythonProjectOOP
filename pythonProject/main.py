# pip install pyTelegramBotAPI
# https://t.me/BotFather
# https://t.me/assasigunssdottiebot.
import telebot

bot = telebot.TeleBot("6365662949:AAEpRrdVrDiM6BCD-VvLsnoluhRLKcnMNDY")


@bot.message_handler(content_types=['text'])
def answer(message):
    bot.send_message(message.chat.id, f'Ты написал мне: {message.text}')


bot.infinity_polling()

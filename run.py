'''
модуль для работы телеграм бота с дверью
'''

from moduls.door_lock import door_lock

import telebot
from telebot import types

test_key_bot = '1350151278:AAFiJZMSdAT5DTNNfUA3C-jVdx8RQDwI3Vg'
IP_DOOR = '192.168.0.196'
POST_DOOR = 9091
DEBUG = False

bot = telebot.TeleBot(test_key_bot, parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN
lock = door_lock(IP_DOOR, POST_DOOR, DEBUG)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start', 'menu'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(row_width=1)
    itembtn1 = types.KeyboardButton('Открыть дверь')
    itembtn2 = types.KeyboardButton('Отключить дверь')
    itembtn3 = types.KeyboardButton('Включить дверь')

    markup.add(itembtn1, itembtn2, itembtn3)
    chat_id = message.chat.id
    bot.send_message(chat_id, "Выберете пункт:", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def comanda(message):
    if message.text == 'Открыть дверь':
        bot.send_message(message.chat.id, 'Дверь будет открыта в течении 3 сек')
        lock.open_door()

    if message.text == 'Отключить дверь':
        bot.send_message(message.chat.id, 'Дверь отключена')
        lock.disable_door()

    if message.text == 'Включить дверь':
        bot.send_message(message.chat.id, 'Дверь включена')
        lock.enable_door()


bot.polling()
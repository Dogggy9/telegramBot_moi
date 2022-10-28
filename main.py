import importlib

import telebot
from telebot.types import CallbackQuery, Message
from config import TOKEN
from parserService import ParserService
from bot_callbacks import Callbacks
from keyboards import AnekdotKeyboards
import url
import sys

bot = telebot.TeleBot(TOKEN)
parser_service = ParserService()
anekdots = []

WEBHOOK_PORT = 8444
WEBHOOK_HOST = '127.0.0.1'
WEBHOOK_URL = 'https://cc60-92-101-61-40.eu.ngrok.io'


# anekdot = parser_service.get_about_anekdot()
# # anekdot = anekdots.pop(0)
# print(len(parser_service.anekdots))
# sys.exit()


@bot.message_handler(commands=['start'])
def start(message: Message):
    keyboard = AnekdotKeyboards.get_base_keyboard()
    bot.send_message(message.chat.id, 'Выбери', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def handle(call: CallbackQuery):
    if call.data == Callbacks.GET_ANEKDOT:
        anekdot, amount = parser_service.get_about_anekdot(*url.anekdot.values())
        bot.send_message(call.message.chat.id, f'{anekdot}\nосталось {amount} анекдотов',
                         reply_markup=AnekdotKeyboards.get_base_keyboard())
    elif call.data == Callbacks.GET_HISTORY:
        history, amount = parser_service.get_about_hisrory(*url.history.values())
        bot.send_message(call.message.chat.id, f'{history}\nосталось {amount} историй',
                         reply_markup=AnekdotKeyboards.get_base_keyboard())

    elif call.data == Callbacks.BACK:
        pass

    bot.answer_callback_query(call.id)


bot.remove_webhook()
bot.polling()

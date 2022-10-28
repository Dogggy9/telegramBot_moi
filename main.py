import importlib

import telebot
from telebot.types import CallbackQuery, Message
from config import *
# from parserService import ParserService
from getAbout import GetAbout
from bot_callbacks import Callbacks
from keyboards import AnekdotKeyboards
from sessinons import Session
import flask
import logging
import url
import sys

bot = telebot.TeleBot(TOKEN)
get_about = GetAbout()
anekdots = []



# logger = telebot.logger
# telebot.logger.setLevel(logging.DEBUG)
app = flask.Flask(__name__)
session = Session(bot)
session.load()


# anekdot = get_about.get_about_anekdot()
# # anekdot = anekdots.pop(0)
# print(len(get_about.anekdots))
# sys.exit()


@bot.message_handler(commands=['start'])
def start(message: Message):
    keyboard = AnekdotKeyboards.get_base_keyboard()
    bot.send_message(message.chat.id, 'Выбери', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def handle(call: CallbackQuery):
    if call.data == Callbacks.GET_ANEKDOT:
        anekdot, amount = get_about.get_about_anekdot(*url.anekdot.values())
        bot.send_message(call.message.chat.id, f'{anekdot}\nосталось {amount} анекдотов',
                         reply_markup=AnekdotKeyboards.get_base_keyboard())
    elif call.data == Callbacks.GET_HISTORY:
        history, amount = get_about.get_about_hisrory(*url.history.values())
        bot.send_message(call.message.chat.id, f'{history}\nосталось {amount} историй',
                         reply_markup=AnekdotKeyboards.get_base_keyboard())
    elif call.data == Callbacks.GET_APHORISM:
        aphorism, amount = get_about.get_about_aphorism(*url.aphorism.values())
        bot.send_message(call.message.chat.id, f'{aphorism}\nосталось {amount} афоризмов',
                         reply_markup=AnekdotKeyboards.get_base_keyboard())

    elif call.data == Callbacks.BACK:
        pass

    bot.answer_callback_query(call.id)

# Process webhook calls
@app.route('/' + TOKEN, methods=['POST'])
def webhook():
    # logger.debug(flask.request.get_data())
    if flask.request.headers.get('content-type') == 'application/json':
        json_string = flask.request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        session.save()
        return '200'
    else:
        flask.abort(403)


if __name__ == '__main__':
    bot.remove_webhook()
    bot.set_webhook(WEBHOOK_URL + "/" + TOKEN)
    app.run(host=WEBHOOK_HOST, port=WEBHOOK_PORT)

import importlib

import requests
import telebot
from telebot.types import CallbackQuery, Message
from config import *
# from parserService import ParserService
from getAbout import GetAbout
from bot_callbacks import Callbacks
from keyboards import AnekdotKeyboards
from sessinons import Session
from users import User
from states import *
import flask
import json
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

URL = 'https://api.telegram.org/bot5721389141:AAE3hEZfKPk5NsfbG-oDnIQF4XDYLH41IM8/'

def write_json(data, filename='answer.json'):
    with open(filename, 'a') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def read_json():
    with open('answer.json', 'r') as json_file:
        users = json.load(json_file)
        return users

def main():
    r = requests.get(URL + 'getMe')
    write_json(r.json())

# main()

def create_state_for_user(context: Session, id: int):
    args = ()
    kw = {"contex": session}
    module = importlib.import_module('states.state')
    klass = getattr(module, context.users[id].state)
    state = klass(*args, **kw)
    return state


@bot.message_handler(commands=['start'])
def start(message: Message):
    user_id = message.from_user.id
    if user_id not in read_json():
        write_json(message.json)
        # session.users[user_id] = User(user_id, BaseState(session))

    state = create_state_for_user(session, user_id)
    state.handle(message)
    # keyboard = AnekdotKeyboards.get_base_keyboard()
    # bot.send_message(message.chat.id, 'Выбери', reply_markup=keyboard)
    # write_json(message.json)

@bot.message_handler(func=lambda message: True)
def handle_message(message: Message):
    state = create_state_for_user(session, message.from_user.id)
    state.handle(message)
    bot.delete_message(chat_id=message.chat.id, message_id=message.id)


@bot.callback_query_handler(func=lambda call: True)
def handle(call: CallbackQuery):
    state = BaseState(session)
    if call.data == Callbacks.GET_ANEKDOT:
        anekdot, amount = get_about.get_about_anekdot(*url.anekdot.values())
        bot.send_message(call.message.chat.id, f'{anekdot}\nосталось {amount} анекдотов',
                         reply_markup=AnekdotKeyboards.get_base_keyboard())
        write_json(call.from_user)
        print(call.from_user)
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
    # bot.infinity_polling()
    bot.set_webhook(WEBHOOK_URL + "/" + TOKEN)
    app.run(host=WEBHOOK_HOST, port=WEBHOOK_PORT)

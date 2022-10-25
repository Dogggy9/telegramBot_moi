import importlib

import telebot
from telebot.types import CallbackQuery, Message
from config import TOKEN, URL
from parserService import ParserService
from bot_callbacks import Callbacks
from keyboards import AnekdotKeyboards
import sys

bot = telebot.TeleBot(TOKEN)
parser_service = ParserService(URL)
anekdots = []
anekdot = parser_service.get_about_anekdot()
# anekdot = anekdots.pop(0)
print(len(parser_service.anekdots))
sys.exit()



@bot.message_handler(commands=['start'])
def start(message: Message):
    keyboard = AnekdotKeyboards.get_base_keyboard()
    bot.send_message(message.chat.id, 'Выбери', reply_markup=keyboard)

@bot.message_handler(commands=['exit'])
def start(message: Message):
    bot.close()

# @bot.message_handler(func=lambda message: True)
# def handle_message(message: Message):
#     bot.send_message(message.chat.id, message.text)
# @bot.message_handler(content_types=['text'])
# def anekdots(message: Message):
#     if message.text.isdigit():
#         bot.send_message(message.chat.id, list_anekdots[0])
#         del list_anekdots[0]
#     else:
#         bot.send_message(message.chat.id, 'Введите любую цифру')

@bot.callback_query_handler(func=lambda call: True)
def handle(call: CallbackQuery):

    if call.data == Callbacks.GET_ANEKDOT:
        anekdot = parser_service.get_about_anekdot()
        bot.send_message(call.message.chat.id, anekdot, reply_markup=AnekdotKeyboards.get_base_keyboard())


    # elif call.data == Callbacks.CHANGE_CITY:
    #     state = ChangeCityState(session)
    #     session.users[call.from_user.id].state = state

    # elif call.data == Callbacks.ABOUT_AUTHOR:
    #     state = AboutAuthorState(session)

    elif call.data == Callbacks.BACK:
        pass

    bot.answer_callback_query(call.id)


bot.remove_webhook()
bot.polling()

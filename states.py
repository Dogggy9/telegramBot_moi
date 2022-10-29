from telebot.types import Message, CallbackQuery
from keyboards import AnekdotKeyboards
from sessinons import Session


class State:
    def __init__(self, contex: Session):
        self.name = self.__class__.__name__
        self.contex = contex

    def handle(self, event):
        pass


class BaseState(State):
    def handle(self, event):
        if isinstance(event, Message):
            chat_id = event.chat.id
            message_id = event.message_id
        elif isinstance(event, CallbackQuery):
            chat_id = event.message.chat.id
            message_id = event.message.message_id

        self.contex.users[event.from_user.id].state = self.name
        self.contex.bot.send_message(chat_id,
                                     "Привет! Я анекдотный бот и я умею выполнять следующие действия:",
                                     reply_markup=AnekdotKeyboards.get_base_keyboard())
        self.contex.bot.delete_message(chat_id=chat_id, message_id=message_id)

from telebot.types import Message, CallbackQuery
from keyboards import AnekdotKeyboards
from sessinons import Session


class State:
    def __init__(self, contex: Session):
        self.name = self.__class__.__name__
        self.contex = contex

    def handle(self, event):
        pass
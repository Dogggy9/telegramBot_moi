from telebot import types
from bot_callbacks import Callbacks


class AnekdotKeyboards:
    @classmethod
    def get_base_keyboard(cls):
        keyboard = types.InlineKeyboardMarkup()
        item_btn_1 = types.InlineKeyboardButton('Анекдот', callback_data=Callbacks.GET_ANEKDOT)
        item_btn_2 = types.InlineKeyboardButton('История', callback_data=Callbacks.GET_HISTORY)
        item_btn_3 = types.InlineKeyboardButton('Афоризм', callback_data=Callbacks.GET_APHORISM)
        # item_btn_n = types.InlineKeyboardButton('Назад', callback_data=Callbacks.BACK)
        keyboard.add(item_btn_1, item_btn_2, item_btn_3)  # , item_btn_n)
        return keyboard

    @classmethod
    def get_back_keyboard(cls):
        inline_keyboard = types.InlineKeyboardMarkup()
        item_btn_0 = types.InlineKeyboardButton('еще', callback_data=Callbacks.MORE)
        item_btn_1 = types.InlineKeyboardButton('Назад', callback_data=Callbacks.BACK)
        inline_keyboard.row(item_btn_0, item_btn_1)
        return inline_keyboard

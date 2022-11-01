import os
import pickle
import telebot
from parserService import ParserService


class Session:
    def __init__(self, bot: telebot, parser: ParserService):
        self.users = {}
        self.bot = bot
        self.parser_service = parser

    def save(self):
        with open('data.pkl', 'wb') as outfile:
            pickle.dump(self.users, outfile)

    def load(self):
        if not os.path.exists('data.pkl'):
            return None

        with open('data.pkl', 'rb') as json_file:
            self.users = pickle.load(json_file)
            print(self.users)

        if self.users is None:
            self.users = {}

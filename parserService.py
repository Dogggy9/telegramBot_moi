import requests
import random
from bs4 import BeautifulSoup as bs



class ParserService:
    def __init__(self):
        self.anekdots = []
        self.old_anekdots = []
        self.history = []
        self.old_history = []
        self.r = ''

    def parser(self, url: str):
        # if not self.r:
        self.r = requests.get(url)
        print('r = ', self.r)
        soup = bs(self.r.text, 'html.parser')
        texts = soup.find_all('div', class_='text')
        return [c.text for c in texts]

    def get_about_anekdot(self, url: str):
        if not self.anekdots:
            self.anekdots = self.parser(url)
            random.shuffle(self.anekdots)
        amount = len(self.anekdots) - 1
        anekdot = self.anekdots.pop(0)
        self.old_anekdots.append(anekdot)
        if not amount:
            self.anekdots = self.old_anekdots
        return anekdot, amount

    def get_about_hisrory(self, url: str):
        if not self.history:
            self.history = self.parser(url)
            random.shuffle(self.history)
        amount = len(self.history) - 1
        history = self.history.pop(0)
        self.old_history.append(history)
        if not amount:
            self.history = self.old_history
        return history, amount

import requests
import random
from bs4 import BeautifulSoup as bs



class ParserService:
    def __init__(self):
        self.anekdots = []
        self.old_anekdots = []
        self.r = ''

    def parser(self, url: str):
        if not self.r:
            self.r = requests.get(url)
        print('r = ', self.r)
        soup = bs(self.r.text, 'html.parser')
        anekdots = soup.find_all('div', class_='text')
        return [c.text for c in anekdots]

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

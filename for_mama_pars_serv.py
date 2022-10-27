import requests
import random
from bs4 import BeautifulSoup as bs


class ParserService:
    def __init__(self, url: str):
        self.url = url
        self.anekdots = []

    def parser(self, url):
        r = requests.get(url)
        soup = bs(r.text, 'html.parser')
        anekdots = soup.find_all('p', class_='sfst')
        return [c.text for c in anekdots]

    def get_about_anekdot(self):
        if len(self.anekdots) == 0:
            self.anekdots = self.parser(self.url)
            random.shuffle(self.anekdots)
        anekdot = self.anekdots.pop(0)
        return anekdot

if __name__ == '__main__':
    p = ParserService('https://pozdravok.com/pozdravleniya/den-rozhdeniya/prikolnye/')
    print(pozd := p.get_about_anekdot())
    print(type(pozd))

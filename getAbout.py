import url
from parserService import ParserService


class GetAbout:
    def __init__(self):
        self.anekdots = []
        self.old_anekdots = []
        self.history = []
        self.old_history = []
        self.aphorism = []
        self.old_aphorism = []

    def get_about_anekdot(self, url: str):
        if not self.anekdots:
            self.anekdots = ParserService.parser(url)
        amountA = len(self.anekdots) - 1
        anekdot = self.anekdots.pop(0)
        self.old_anekdots.append(anekdot)
        if not amountA:
            self.anekdots = self.old_anekdots
            self.old_anekdots = []
        return anekdot, amountA

    def get_about_hisrory(self, url: str):
        if not self.history:
            self.history = ParserService.parser(url)
        amountH = len(self.history) - 1
        history = self.history.pop(0)
        self.old_history.append(history)
        if not amountH:
            self.history = self.old_history
            self.old_history = []
        return history, amountH

    def get_about_aphorism(self, url: str):
        if not self.aphorism:
            self.aphorism = ParserService.parser(url)
        amountAp = len(self.aphorism) - 1
        aphorism = self.aphorism.pop(0)
        self.old_aphorism.append(aphorism)
        if not amountAp:
            self.aphorism = self.old_aphorism
            self.old_aphorism = []
        return aphorism, amountAp


if __name__ == '__main__':
    g = GetAbout()
    print(g.get_about_anekdot(*url.anekdot.values()))

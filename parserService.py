import requests
import random
from bs4 import BeautifulSoup as bs
import url


class ParserService:

    @staticmethod
    def parser(url: str):
        r = requests.get(url)
        soup = bs(r.text, 'html.parser')
        texts = soup.find_all('div', class_='text')
        date = soup.find_all('div', class_='subdate')
        print(date)
        texts = [c.text for c in texts]
        random.shuffle(texts)
        return texts

    @staticmethod
    def vchera_zavtra(url: str):
        href = {}
        r = requests.get(url)
        soup = bs(r.text, 'html.parser')
        texts = soup.find_all('div', class_='text')
        date = soup.find_all('div', class_='subdate')
        date = date[0].text
        print(date)
        texts = [c.text for c in texts]
        urlka = soup.find_all('div', class_='voteresult')
        for num, a_tag in enumerate(urlka[0].find_all('a')):
            href[num] = a_tag
        yesterday = href.pop(0)
        print(yesterday)
        tomorrow = href.pop(1, None)
        print(tomorrow)
        random.shuffle(texts)
        return texts, date, yesterday, tomorrow


if __name__ == '__main__':
    p = ParserService()
    print(p.vchera_zavtra('https://www.anekdot.ru'+'/an/an2210/j221031;100.html'))  # анекдоты
    print(p.vchera_zavtra('https://www.anekdot.ru'+'/an/an2211/o221101;100.html'))  # истории
    a, *b = p.vchera_zavtra('https://www.anekdot.ru'+'/an/an2211/a221101;100.html')  # афоризмы
    # print(p.parser(*url.anekdot.values()))
    print(a)
    print(b)

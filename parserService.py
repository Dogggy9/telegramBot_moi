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
        texts = [c.text for c in texts]
        random.shuffle(texts)
        return texts


if __name__ == '__main__':
    p = ParserService()
    print(p.parser(*url.anekdot.values()))

import lxml.html
import requests
from bs4 import BeautifulSoup

from Modules.BuildTag import BuildTag


class BoardGameBliss:
    def __init__(self, search):
        self.search_name = search

    def get_img(self, html):
        link_img = 'https:'
        link_img += html.find('img', attrs={'class': 'product-item__primary-image'})['src']
        link_img = link_img.replace('60x', '270x')
        return link_img

    def get_price(self, html):
        price = html.find('span', attrs={'class': 'price'})
        return price.contents[0]

    def get_text(self, html):
        text = html.find('a', attrs={'class': 'product-item__title text--strong link'})
        link = "https://boardgamebliss.com"
        link += text['href']

        return link, text.contents[0]

    def search(self):
        session = requests.session()

        boardgamebliss = session.get(f'https://boardgamebliss.com')
        boardgamebliss_html = lxml.html.fromstring(boardgamebliss.text)
        hidden_inputs = boardgamebliss_html.xpath(r'//form//input[@type="hidden"]')
        form = {x.attrib["name"]: x.attrib["value"] for x in hidden_inputs}

        form['q'] = self.search_name
        search_response = session.post(f'https://boardgamebliss.com/search', data=form)
        return search_response.text

    def return_results(self, count):
        boardgamebliss = BeautifulSoup('<div class="boardgamebliss"></div>', 'html.parser')

        search_response = self.search()

        if self.search_name in search_response:
            soup = BeautifulSoup(search_response, 'html.parser')
            products = soup.find('div', attrs={'class': 'product-list product-list--collection'})
            boxes = products.find_all('div', attrs={'class': 'product-item product-item--vertical 1/3--tablet 1/4--lap-and-up'})

            for idx, box in enumerate(boxes):
                img = self.get_img(box)
                price = self.get_price(box)
                text = self.get_text(box)

                if text[1].lower() != self.search_name.lower():
                    continue

                tg = BuildTag(img, price, text[1], text[0], "Board Game Bliss", "boardgamebliss")

                tag = tg.build_div()
                boardgamebliss.div.append(tag)
                if (idx + 1) == count:
                    break

        return boardgamebliss


if __name__ == "__main__":
    bliss = BoardGameBliss("Small World")
    print(bliss.return_results(1))
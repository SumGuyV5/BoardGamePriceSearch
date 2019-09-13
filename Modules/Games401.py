import lxml.html
import requests
from bs4 import BeautifulSoup

from Modules.BuildTag import BuildTag


class Games401:
    def __init__(self, search):
        self.search_name = search

    def get_img(self, html):
        link_img = 'https:'
        link_img += html.find('img', attrs={'class': 'card__image'})['data-src']
        link_img = link_img.replace('{width}', '270')
        return link_img

    def get_price(self, html):
        price = html.find('span', attrs={'class': 'money'})
        return price.contents[0]

    def get_text(self, html):
        text = html.find('a', attrs={'class': 'title'})
        link = "https://store.401games.ca"
        link += text['href']

        return link, text.contents[0]

    def search(self):
        session = requests.session()

        games401 = session.get(f'https://store.401games.ca')
        games401_html = lxml.html.fromstring(games401.text)
        hidden_inputs = games401_html.xpath(r'//form//input[@type="hidden"]')
        form = {x.attrib["name"]: x.attrib["value"] for x in hidden_inputs}

        form['q'] = self.search_name
        search_response = session.post(f'https://store.401games.ca/search', data=form)

        return search_response.text

    def return_results(self, count):
        games401 = BeautifulSoup('<div class="games401"></div>', 'html.parser')

        search_response = self.search()
        if self.search_name in search_response:
            soup = BeautifulSoup(search_response, 'html.parser')
            products = soup.find('div', attrs={'class': 'products products-grid search-grid'})
            boxes = products.find_all('div', attrs={'class': 'box product'})

            for idx, box in enumerate(boxes):
                img = self.get_img(box)
                price = self.get_price(box)
                text = self.get_text(box)

                if text[1].lower() != self.search_name.lower():
                    continue

                tg = BuildTag(img, price, text[1], text[0], "401 Games", "games401")

                tag = tg.build_div()
                games401.div.append(tag)
                if (idx + 1) == count:
                    break

        return games401

if __name__ == "__main__":
    games401 = Games401("Small World")
    print(games401.return_results(1))
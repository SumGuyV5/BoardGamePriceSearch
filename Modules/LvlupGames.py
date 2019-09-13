import lxml.html
import requests
from bs4 import BeautifulSoup

from Modules.BuildTag import BuildTag


class LvlupGames:
    def __init__(self, search):
        self.search_name = search

    def get_img(self, html):
        link_img = 'https:'
        link_img += html.find('img')['src']
        link_img = link_img.replace('500x', '270x')
        return link_img

    def get_price(self, html):
        price = html.find('span', attrs={'class': 'money'})
        if price is None:
            return ""
        return price.contents[0]

    def get_text(self, html):
        text = html.find('a', attrs={'class': 'hidden-product-link'})
        link = "https://lvlupgames.ca"
        link += text['href']

        return link, text.contents[0]

    def search(self):
        session = requests.session()

        lvlupgames = session.get(f'https://lvlupgames.ca')
        lvlupgames_html = lxml.html.fromstring(lvlupgames.text)
        hidden_inputs = lvlupgames_html.xpath(r'//form//input[@type="hidden"]')
        form = {x.attrib["name"]: x.attrib["value"] for x in hidden_inputs}

        form['q'] = self.search_name
        search_response = session.post(f'https://lvlupgames.ca/search', data=form)

        return search_response.text

    def return_results(self, count):
        lvlupgames = BeautifulSoup('<div class="lvlupgames"></div>', 'html.parser')

        search_response = self.search()
        if self.search_name in search_response:
            soup = BeautifulSoup(search_response, 'html.parser')
            products = soup.find('div', attrs={'class': 'container'})
            boxes = products.find_all('div', attrs={'class': 'product-wrap'})

            for idx, box in enumerate(boxes):
                img = self.get_img(box)
                price = self.get_price(box)
                text = self.get_text(box)

                if text[1].lower() != self.search_name.lower():
                    continue

                tg = BuildTag(img, price, text[1], text[0], "LVLUP Games", "lvlupgames")

                tag = tg.build_div()
                lvlupgames.div.append(tag)
                if (idx + 1) == count:
                    break

        return lvlupgames

if __name__ == "__main__":
    lvlupgames = LvlupGames("Small World")
    print(lvlupgames.return_results(1))
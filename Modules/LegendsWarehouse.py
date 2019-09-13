import lxml.html
import requests
from bs4 import BeautifulSoup

from Modules.BuildTag import BuildTag


class LegendsWarehouse:
    def __init__(self, search):
        self.search_name = search

    def get_img(self, html):
        link_img = 'https:'
        link_img += html.find('img', attrs={'class': 'featured-image'})['src']
        #link_img = link_img.replace('60x', '270x')
        return link_img

    def get_price(self, html):
        price = html.find('span', attrs={'class': 'price'})
        if price is None:
            price = html.find('span', attrs={'class': 'price-sale'})
            if price is None:
                price = html.find('span', attrs={'class': 'sold-out'})
        return price.contents[0]

    def get_text(self, html):
        h5 = html.find('h5', attrs={'class': 'product-name'})
        text = h5.find('a')
        link = "https://legendswarehouse.ca"
        link += text['href']

        return link, text.contents[0]

    def search(self):
        session = requests.session()

        legendswarehouse = session.get(f'https://legendswarehouse.ca')
        legendswarehouse_html = lxml.html.fromstring(legendswarehouse.text)
        hidden_inputs = legendswarehouse_html.xpath(r'//form//input[@type="hidden"]')
        form = {x.attrib["name"]: x.attrib["value"] for x in hidden_inputs}

        form['q'] = self.search_name
        search_response = session.post(f'https://legendswarehouse.ca/search', data=form)

        return search_response.text

    def return_results(self, count):
        legendswarehouse = BeautifulSoup('<div class="legendswarehouse"></div>', 'html.parser')

        search_response = self.search()

        if self.search_name in search_response:
            soup = BeautifulSoup(search_response, 'html.parser')
            products = soup.find('div', attrs={'class': 'cata-product'})
            boxes = products.find_all('div', attrs={'class': 'product-grid-item'})

            for idx, box in enumerate(boxes):
                img = self.get_img(box)
                price = self.get_price(box)
                text = self.get_text(box)

                if text[1].lower() != self.search_name.lower():
                    if text[1].lower().replace(" ", "") != self.search_name.lower().replace(" ", ""):
                        continue

                tg = BuildTag(img, price, text[1], text[0], "Legends Warehouse", "legendswarehouse")

                tag = tg.build_div()
                legendswarehouse.div.append(tag)
                if (idx + 1) == count:
                    break

        return legendswarehouse


if __name__ == "__main__":
    bliss = LegendsWarehouse("Small World")
    print(bliss.return_results(1))
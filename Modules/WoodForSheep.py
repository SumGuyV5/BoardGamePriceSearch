import lxml.html
import requests
from bs4 import BeautifulSoup

from Modules.BuildTag import BuildTag


class WoodForSheep:
    def __init__(self, search):
        self.search_name = search

    def get_img(self, html):
        div = html.find('div', attrs={'class': 'product-image'})
        link_img = 'https:'
        link_img += div.find('img')['src']
        #link_img = link_img.replace('60x.jpg', '270x.jpg')
        return link_img

    def get_price(self, html):
        price = html.find('span', attrs={'class': 'CategoryProductPrice'})
        if price is None:
            return ""
        return price.contents[0]

    def get_text(self, html):
        div = html.find('div', attrs={'class': 'product-info'})
        text = div.find('a')
        link = "https://www.woodforsheep.ca"
        link += text['href']

        return link, text.contents[0]

    def search(self):
        session = requests.session()

        woodforsheep = session.get(f'https://www.woodforsheep.ca')
        woodforsheep_html = lxml.html.fromstring(woodforsheep.text)
        hidden_inputs = woodforsheep_html.xpath(r'//form//input[@type="hidden"]')
        form = {}
        for x in hidden_inputs:
            value = ""
            try:
                value = x.attrib["value"]
            except KeyError:
                pass
            form[x.attrib["name"]] = value


        form['q'] = self.search_name
        search_response = session.post(f'https://www.woodforsheep.ca/search', data=form)

        return search_response.text

    def return_results(self, count):
        woodforsheep = BeautifulSoup('<div class="woodforsheep"></div>', 'html.parser')

        search_response = self.search()

        if self.search_name in search_response:
            soup = BeautifulSoup(search_response, 'html.parser')
            products = soup.find('table', attrs={'id': 'collection'})
            boxes = products.find_all('tr')

            for idx, box in enumerate(boxes):
                img = self.get_img(box)
                price = self.get_price(box)
                text = self.get_text(box)

                if text[1].lower() != self.search_name.lower():
                    continue

                tg = BuildTag(img, price, text[1], text[0], "Wood for Sheep", "woodforsheep")

                tag = tg.build_div()
                woodforsheep.div.append(tag)
                if (idx + 1) == count:
                    break

        return woodforsheep


if __name__ == "__main__":
    bliss = WoodForSheep("Small World")
    print(bliss.return_results(1))
import lxml.html
import requests
from bs4 import BeautifulSoup

from Modules.BuildTag import BuildTag


class MeepleMart:
    def __init__(self, search):
        self.search_name = search

    def get_img(self, html):
        link_img = 'https://meeplemart.com'
        link_img += html.find('img', attrs={'class': 'CategoryProductThumbnail'})['src']
        #link_img = link_img.replace('60x.jpg', '270x.jpg')
        return link_img

    def get_price(self, html):
        price = html.find('span', attrs={'class': 'CategoryProductPrice'})
        return price.contents[0]

    def get_text(self, html):
        div = html.find('div', attrs={'class': 'CategoryItemName'})
        text = div.find('a')
        link = "https://meeplemart.com"
        link += text['href']

        return link, text.contents[0]

    def search(self):
        session = requests.session()

        meeplemart = session.get(f'https://meeplemart.com')
        meeplemart_html = lxml.html.fromstring(meeplemart.text)
        hidden_inputs = meeplemart_html.xpath(r'//form//input[@type="hidden"]')
        form = {}
        for x in hidden_inputs:
            value = ""
            try:
                value = x.attrib["value"]
            except KeyError:
                pass
            form[x.attrib["name"]] = value


        form['SearchTerms'] = self.search_name
        search_response = session.post(f'https://meeplemart.com/store/Search.aspx', data=form)

        return search_response.text

    def return_results(self, count):
        meeplemart = BeautifulSoup('<div class="meeplemart"></div>', 'html.parser')

        search_response = self.search()

        if self.search_name in search_response:
            soup = BeautifulSoup(search_response, 'html.parser')
            products = soup.find('table', attrs={'id': 'dlProducts'})
            boxes = products.find_all('div', attrs={'class': 'CategoryItem'})

            for idx, box in enumerate(boxes):
                img = self.get_img(box)
                price = self.get_price(box)
                text = self.get_text(box)

                if text[1].lower() != self.search_name.lower():
                    continue

                tg = BuildTag(img, price, text[1], text[0], "Meeplemart", "meeplemart")

                tag = tg.build_div()
                meeplemart.div.append(tag)
                if (idx + 1) == count:
                    break

        return meeplemart


if __name__ == "__main__":
    mart = MeepleMart("Small World")
    print(mart.return_results(1))
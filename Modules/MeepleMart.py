import lxml.html
import requests
from bs4 import BeautifulSoup

from Modules.BuildTag import BuildTag
from Modules.WebsiteSearch import WebsiteSearch


class MeepleMart(WebsiteSearch):
    def __init__(self, search_text, fuzzy=False):
        super(MeepleMart, self).__init__(search_text, 'Meeple Mart', 'https://meeplemart.com', 'meeplemart', fuzzy)

    def get_img(self, html):
        link_img = super(MeepleMart, self).get_img(html, 'CategoryProductThumbnail')
        link_img = link_img.replace('https:', 'https://meeplemart.com')
        return link_img

    def get_price(self, html):
        price = super(MeepleMart, self).get_price(html, 'CategoryProductPrice')
        if price is None:
            price = ""
        return price

    def get_text(self, html):
        div = html.find('div', attrs={'class': 'CategoryItemName'})
        return super(MeepleMart, self).get_text(div, '')

    def search(self):
        return super(MeepleMart, self).search('SearchTerms', '/store/Search.aspx')

    def results(self, count): # dlProducts is for a table tag
        return super(MeepleMart, self).results('dlProducts', 'CategoryItem', count)


if __name__ == "__main__":
    mart = MeepleMart("Adventure Island")
    print(mart.results(3))
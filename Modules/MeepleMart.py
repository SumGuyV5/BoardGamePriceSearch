from Modules.WebsiteSearch import WebsiteSearch
from bs4 import BeautifulSoup


class MeepleMart(WebsiteSearch):
    def __init__(self, search_text):
        super(MeepleMart, self).__init__(search_text, 'Meeple Mart', 'https://meeplemart.com', 'meeplemart')

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
        try:
            div = html.find('div', attrs={'class': 'CategoryItemName'})
        except AttributeError:
            div = None
        return super(MeepleMart, self).get_text(div, '')

    def search(self):
        return super(MeepleMart, self).search('SearchTerms', '/store/Search.aspx')

    def results(self, count, results_html):  # dlProducts is for a table tag
        return super(MeepleMart, self).results('dlProducts', 'CategoryItem', count, results_html)


if __name__ == "__main__":
    soup = BeautifulSoup('<div class="grid-container"></div>', "html.parser")
    mart = MeepleMart("Adventure Island")
    mart.search()
    print(mart.results(3, soup))

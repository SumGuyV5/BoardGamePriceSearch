from Modules.WebsiteSearch import WebsiteSearch
from bs4 import BeautifulSoup


class BoardGameBliss(WebsiteSearch):
    def __init__(self, search_text):
        super(BoardGameBliss, self).__init__(search_text, 'Board Game Bliss', 'https://boardgamebliss.com',
                                             'boardgamebliss')

    def get_img(self, html):
        link_img = super(BoardGameBliss, self).get_img(html, 'product-item__primary-image')
        return link_img.replace('60x', '270x')

    def get_price(self, html):
        price = super(BoardGameBliss, self).get_price(html, 'price')
        if price is None:
            return ""
        return price

    def get_text(self, html):
        return super(BoardGameBliss, self).get_text(html, 'product-item__title text--strong link')

    def search(self):
        return super(BoardGameBliss, self).search('q', '/search')

    def results(self, count, results_html):
        return super(BoardGameBliss, self).results('product-list product-list--collection',
                                                   'product-item product-item--vertical 1/3--tablet 1/4--lap-and-up',
                                                   count, results_html)


if __name__ == "__main__":
    soup = BeautifulSoup('<div class="grid-container"></div>', "html.parser")
    bliss = BoardGameBliss("Adventure Island")
    bliss.search()
    print(bliss.results(1, soup))

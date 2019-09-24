from Modules.WebsiteSearch import WebsiteSearch
from bs4 import BeautifulSoup


class Games401(WebsiteSearch):
    def __init__(self, search_text):
        super(Games401, self).__init__(search_text, '401 Games', 'https://store.401games.ca', 'games401')

    def get_img(self, html):
        link_img = super(Games401, self).get_img(html, 'card__image', 'data-src')
        return link_img.replace('{width}', '270')

    def get_price(self, html):
        prices = super(Games401, self).get_price(html, 'money')
        return prices

    def get_text(self, html):
        return super(Games401, self).get_text(html, 'title')

    def search(self):
        return super(Games401, self).search('q', '/search')

    def results(self, count, results_html):
        return super(Games401, self).results('products products-grid search-grid', 'box product', count, results_html)


if __name__ == "__main__":
    soup = BeautifulSoup('<div class="grid-container"></div>', "html.parser")
    games401 = Games401("Viticulture Moor")
    games401.search()
    print(games401.results(1, soup))

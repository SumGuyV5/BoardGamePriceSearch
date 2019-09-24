from Modules.WebsiteSearch import WebsiteSearch
from bs4 import BeautifulSoup


class LegendsWarehouse(WebsiteSearch):
    def __init__(self, search_text):
        super(LegendsWarehouse, self).__init__(search_text, 'Legends Warehouse', 'https://legendswarehouse.ca',
                                               'legendswarehouse')

    def get_img(self, html):
        link_img = super(LegendsWarehouse, self).get_img(html, 'featured-image')
        return link_img

    def get_price(self, html):
        price = super(LegendsWarehouse, self).get_price(html, 'price')
        price_sale = super(LegendsWarehouse, self).get_price(html, 'price-sale')
        sold_out = super(LegendsWarehouse, self).get_price(html, 'sold-out')
        if not price:
            if not price_sale:
                return sold_out
            else:
                return price_sale
        return price

    def get_text(self, html):
        h5 = html.find('h5', attrs={'class': 'product-name'})
        return super(LegendsWarehouse, self).get_text(h5, '')

    def search(self):
        return super(LegendsWarehouse, self).search('q', '/search')

    def results(self, count, results_html):
        return super(LegendsWarehouse, self).results('cata-product', 'product-grid-item', count, results_html)


if __name__ == "__main__":
    soup = BeautifulSoup('<div class="grid-container"></div>', "html.parser")
    legends = LegendsWarehouse("Starfinder: Combat Pad")
    legends.search()
    print(legends.results(4, soup))

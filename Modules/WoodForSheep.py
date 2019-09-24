from Modules.WebsiteSearch import WebsiteSearch
from bs4 import BeautifulSoup


class WoodForSheep(WebsiteSearch):
    def __init__(self, search_test):
        super(WoodForSheep, self).__init__(search_test, 'Wood for Sheep', 'https://www.woodforsheep.ca', 'woodforsheep')

    def get_img(self, html, html_class='product-image'):
        div = html.find('div', attrs={'class': html_class})
        if div is None:
            div = html.find('div', attrs={'id': html_class})
            if div is None:
                return ""
            else:
                return super(WoodForSheep, self).get_img(div, 'reflect')
        link_img = super(WoodForSheep, self).get_img(div)
        return link_img

    def get_price(self, html):
        div = html.find('div', attrs={'class': 'price'})
        price = div.find('span', attrs={'id': 'price-field'})
        if not price:
            return ["Null"]
        return [str(price.contents[0]).strip()]

    def get_text(self, html):
        div = html.find('div', attrs={'class': 'product-info'})
        if div is None:
            return "", "No Item"
        return super(WoodForSheep, self).get_text(div)

    def search(self):
        return super(WoodForSheep, self).search('q', '/search')

    def results(self, count, results_html):
        """ Note we pass "woodforsheepfix" not because it is a class but so that the code can't find a div tag and will
        fail to find a div tag and search for a tr tag"""
        return super(WoodForSheep, self).results('span-17 last', 'woodforsheepfix', count, results_html)


if __name__ == "__main__":
    soup = BeautifulSoup('<div class="grid-container"></div>', "html.parser")
    sheep = WoodForSheep("Small World")
    sheep.search()
    print(sheep.results(4, soup))

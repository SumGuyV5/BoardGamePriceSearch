from Modules.WebsiteSearch import WebsiteSearch


class WoodForSheep(WebsiteSearch):
    def __init__(self, search_test, fuzzy=False):
        super(WoodForSheep, self).__init__(search_test, 'Wood for Sheep', 'https://www.woodforsheep.ca',
                                           'woodforsheep', fuzzy)

    def get_img(self, html):
        div = html.find('div', attrs={'class': 'product-image'})
        if div is None:
            return ""
        link_img = super(WoodForSheep, self).get_img(div)
        return link_img

    def get_price(self, html):
        price = super(WoodForSheep, self).get_price(html, 'CategoryProductPrice')
        if not price:
            return ["Null"]
        return price

    def get_text(self, html):
        div = html.find('div', attrs={'class': 'product-info'})
        if div is None:
            return "", "No Item"
        return super(WoodForSheep, self).get_text(div)

    def search(self):
        return super(WoodForSheep, self).search('q', '/search')

    def results(self, count):
        """ Note we pass "woodforsheepfix" not because it is a class but so that the code can't find a div tag and will
        fail to find a div tag and search for a tr tag"""
        return super(WoodForSheep, self).results('span-17 last', 'woodforsheepfix', count)


if __name__ == "__main__":
    sheep = WoodForSheep("Small World")
    sheep.search()
    print(sheep.results(4))

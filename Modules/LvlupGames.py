from Modules.WebsiteSearch import WebsiteSearch


class LvlupGames(WebsiteSearch):
    def __init__(self, search_text, fuzzy=False):
        super(LvlupGames, self).__init__(search_text, 'LVLUP Games', 'https://lvlupgames.ca', 'lvlupgames', fuzzy)

    def get_img(self, html):
        link_img = super(LvlupGames, self).get_img(html, 'lazyload lazyload--fade-in primary', 'data-src')
        return link_img.replace('900x', '270x')

    def get_price(self, html):
        price = super(LvlupGames, self).get_price(html, 'money')
        if price is None:
            return ""
        return price

    def get_text(self, html):
        return super(LvlupGames, self).get_text(html, 'hidden-product-link')

    def search(self):
        return super(LvlupGames, self).search('q', '/search')

    def results(self, count):
        return super(LvlupGames, self).results('container', 'product-wrap', count)


if __name__ == "__main__":
    lvlupgames = LvlupGames("Polyhero Dice")
    print(lvlupgames.results(1))
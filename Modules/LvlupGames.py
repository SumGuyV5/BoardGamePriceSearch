from Modules.WebsiteSearch import WebsiteSearch
from bs4 import BeautifulSoup


class LvlupGames(WebsiteSearch):
    def __init__(self, search_text):
        super(LvlupGames, self).__init__(search_text, 'LVLUP Games', 'https://lvlupgames.ca', 'lvlupgames')

    def get_img(self, html):
        link_img = super(LvlupGames, self).get_img(html, 'productitem--image-primary', 'src')
        return link_img.replace('900x', '270x')

    def get_price(self, html):
        price = super(LvlupGames, self).get_price(html, 'money')
        if price is None:
            return ""
        return price

    def get_text(self, html):
        try:
            text = html.find('div', attrs={'class': 'productitem--info'}).find('a')
            link = self.website_address
            link += text['href']
        except AttributeError:
            return '', 'No Item'

        return link, text.contents[0]

    def search(self):
        return super(LvlupGames, self).search('q', '/search')

    def results(self, count, results_html):
        return super(LvlupGames, self).results('container', 'productitem', count, results_html)


if __name__ == "__main__":
    soup = BeautifulSoup('<div class="grid-container"></div>', "html.parser")
    lvlupgames = LvlupGames("Polyhero Dice")
    lvlupgames.search()
    print(lvlupgames.results(1, soup))

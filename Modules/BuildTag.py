from bs4 import BeautifulSoup


class BuildTag:
    def __init__(self, img, price, text, text_link, store, store_class):
        self.tag = BeautifulSoup('<div class="grid-item"></div>', "html.parser")
        self.img = img
        self.price = price
        self.text = text
        self.text_link = text_link
        self.store = store
        self.store_class = store_class
        self.a = self.tag.new_tag('a', href=self.text_link)

    def build_span(self, text):
        span = self.tag.new_tag('span')
        span.string = str(text)
        return span

    def build_store(self):
        store = self.build_span(self.store)

        div_span = self.tag.new_tag('div', attrs={'class': f'store_name {self.store_class}'})
        div_span.append(store)
        self.tag.div.append(div_span)

    def build_img(self):
        image = self.tag.new_tag('img', attrs={'src': self.img})
        div_img = self.tag.new_tag('div', attrs={'class': 'image'})
        div_img.append(image)
        self.a.append(div_img)

    def build_name(self):
        div_name = self.tag.new_tag('div', attrs={'class': 'boardgamename'})
        div_name.append(self.build_span(self.text))
        self.a.append(div_name)

    def build_price(self):
        span = self.build_span(self.price)
        self.tag.div.append(span)

    def build_div(self):
        self.build_store()
        self.build_img()
        self.build_name()
        self.tag.div.append(self.a)
        self.build_price()
        return self.tag

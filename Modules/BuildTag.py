from bs4 import BeautifulSoup


class BuildTag:
    def __init__(self, img, price, text, text_link, store, store_class):
        self.tag = BeautifulSoup('<div class="box"></div>', "html.parser")
        self.img = img
        self.price = price
        self.text = text
        self.text_link = text_link
        self.store = store
        self.store_class = store_class

    def build_span(self, text):
        span = self.tag.new_tag('span')
        span.string = text
        return span

    def build_store(self):
        store = self.build_span(self.store)
        div_span = self.tag.new_tag('div', attrs={'class': f'store_name {self.store_class}'})
        div_span.append(store)
        self.tag.div.append(div_span)

    def build_img(self):
        image = self.tag.new_tag('img', attrs={'src': self.img})
        div_img = self.tag.new_tag('div', attrs={'class': 'img'})
        div_img.append(image)
        self.tag.div.append(div_img)

    def build_a(self):
        a = self.tag.new_tag('a', href=self.text_link)
        a.string = self.text
        div_a = self.tag.new_tag('div', attrs={'class': 'link'})
        div_a.append(a)
        self.tag.div.append(div_a)

    def build_price(self):
        span = self.build_span(self.price)
        self.tag.div.append(span)

    def build_div(self):
        self.tag = BeautifulSoup('<div class="box"></div>', "html.parser")

        self.build_store()
        self.build_img()
        self.build_a()
        self.build_price()

        return self.tag
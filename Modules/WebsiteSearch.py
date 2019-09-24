import lxml.html
from requests_futures.sessions import FuturesSession
from bs4 import BeautifulSoup

from Modules.BuildTag import BuildTag


class WebsiteSearch:
    def __init__(self, search_text, store_name, website_address, div_class):
        self.search_text = search_text
        self.store_name = store_name
        self.website_address = website_address

        self.div_class = div_class

        self.session = FuturesSession()
        self.website_session = self.session.get(self.website_address)

    def get_img(self, html, html_class='', src='src'):
        link_img = 'https:'
        try:
            link_img += html.find('img', attrs={'class': html_class})[src]
        except AttributeError:
            link_img = ''

        return link_img

    def get_price(self, html, html_class=''):
        span_tags = ""
        try:
            span_tags = html.find_all('span', attrs={'span', html_class})
        except AttributeError:
            pass
        normal_price = []
        for span_tag in span_tags:
            normal_price.append(str(span_tag.contents[0]).strip())

        return normal_price

    def get_text(self, html, html_class=''):
        try:
            text = html.find('a', attrs={'class': html_class})
            link = self.website_address
            link += text['href']
        except AttributeError:
            return '', 'No Item'

        return link, text.contents[0]

    def initial_visit(self):
        response = self.website_session.result()
        website_html = lxml.html.fromstring(response.content)
        hidden_inputs = website_html.xpath(r'//form//input[@type="hidden"]')
        form = {}
        for x in hidden_inputs:
            value = ""
            try:
                value = x.attrib["value"]
            except KeyError:
                pass
            form[x.attrib["name"]] = value

        return form

    def search(self, key='q', search_page='/search'):
        form = self.initial_visit()
        form[key] = self.search_text
        self.website_session = self.session.post(f'{self.website_address}{search_page}', data=form)

    def results(self, products_class, boxes_class, count, results_html):
        search_response = self.website_session.result().text

        if self.search_text in search_response:
            soup = BeautifulSoup(search_response, 'html.parser')
            products = soup.find('div', attrs={'class': products_class})
            if products is None:
                products = soup
            boxes = products.find_all('div', attrs={'class': boxes_class})
            if not boxes and boxes_class == 'woodforsheepfix':
                boxes = products.find_all('tr')

            for box in boxes:
                img = self.get_img(box)
                prices = sorted(self.get_price(box))
                text = self.get_text(box)

                tg = BuildTag(img, prices[0], text[1], text[0], self.store_name, self.div_class)

                tag = tg.build_div()
                results_html.div.append(tag)
                count -= 1
                if count == 0:
                    break

            for x in range(count):
                empty_div = BuildTag('', 'Null', 'No Item', '', self.store_name, self.div_class)
                results_html.div.append(empty_div.build_div())

        return results_html


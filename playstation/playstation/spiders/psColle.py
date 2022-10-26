import scrapy
from ..items import PlaystationItem

class PscolleSpider(scrapy.Spider):
    name = 'psColle'
    page_number = 2
    allowed_domains = ['store.playstation.com', 'www.store.playstation.com/en-id']
    start_urls = ['https://store.playstation.com/en-id/category/c0907339-a199-4f07-9bd2-6996c6cdd117/1']

    def parse(self, response):

        items = PlaystationItem()

        for text in response.xpath("//*[@class='psw-l-w-1/2@mobile-s psw-l-w-1/2@mobile-l psw-l-w-1/6@tablet-l psw-l-w-1/4@tablet-s psw-l-w-1/6@laptop psw-l-w-1/8@desktop psw-l-w-1/8@max']"):

            product_name = text.xpath(".//*[@class='psw-t-body psw-c-t-1 psw-t-truncate-2 psw-m-b-2']/text()").extract()
            product_price = text.xpath(".//*[@class='psw-m-r-3']/text()").extract()

            items['product_name'] = product_name
            items['product_price'] = product_price

            yield items

        next_page = 'https://store.playstation.com/en-id/category/c0907339-a199-4f07-9bd2-6996c6cdd117/' + str(PscolleSpider.page_number)
        if PscolleSpider.page_number <= 3:
            PscolleSpider.page_number += 1
            yield response.follow(next_page, callback = self.parse)
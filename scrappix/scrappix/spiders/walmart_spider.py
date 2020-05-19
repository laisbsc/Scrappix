# -*- coding: utf-8 -*-
import scrapy
from ..items import ScrappixItem


class WalmartSpiderSpider(scrapy.Spider):
    name = 'walmart_spider'
    # allowed_domains = ['walmart.com']
    page_number = 2
    search_term = 'laptops'
    start_urls = ['https://www.walmart.com/browse/electronics/all-laptop-computers/3944_3951_1089430_132960?page=' + str(page_number)]

    def parse(self, response):
        # instance of items class
        items = ScrappixItem()

        item_name = response.css('.truncate-title span::text').extract()
        price = response.css('.price-main span::text').extract()
        image = response.css('#searchProductResult img::attr(src)').extract()
        # stock = response.css('.a-color-price::text').extract()

        items['item_name'] = item_name
        items['price'] = price
        # items['stock'] = stock
        items['image'] = image

        yield items

        next_page = 'https://www.walmart.com/browse/electronics/all-laptop-computers/' \
                    '3944_3951_1089430_132960?page='+str(WalmartSpiderSpider.page_number)
        """
        if the search haven't reached the 100th page, go to next and scrape it all again.
        """
        if WalmartSpiderSpider.page_number <= 100:
            WalmartSpiderSpider.page_number += 1
            yield response.follow(next_page, callback=self.parse)

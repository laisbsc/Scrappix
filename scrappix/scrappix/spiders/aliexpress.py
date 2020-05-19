# -*- coding: utf-8 -*-
import scrapy
from ..items import ScrappixItem #not sure this will be like this further on

""" not currently working due to website's policy on data scraping """

class AliexpressSpider(scrapy.Spider):
    name = 'aliexpress'
    search_term = 'laptop'
    start_urls = ['https://www.aliexpress.com/wholesale?catId=0&initiative_id=SB_20200515075819&SearchText='+search_term]

    def parse(self, response):
        # instance of items class
        items = ScrappixItem()

        item_name = response.css('.item-title::text').extract()
        price = response.css('.price-current::text').extract()
        image = response.css('.list .product-img .item-img::attr(src)').extract()
        stock = response.css('.sale-value-link::text').extract()

        items['item_name'] = item_name
        items['price'] = price
        items['stock'] = stock
        items['image'] = image

        yield items

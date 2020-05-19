# -*- coding: utf-8 -*-

# Define here the models for your scraped items
# items.py
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrappixItem(scrapy.Item):
    item_name = scrapy.Field()
    price = scrapy.Field()
    image = scrapy.Field()
    stock = scrapy.Field()

    # sold_units for aliexpress
    # sold_units = scrapy.Field()


# -*- coding: utf-8 -*-
import scrapy
from ..items import ScrappixItem #db schema


class ArgosScraperSpider(scrapy.Spider):
    name = 'argos_scraper'
    search_term = 'laptop'
    page_number = 2
    start_urls = ['https://www.argos.ie/webapp/wcs/stores/servlet/Search?storeId=10152&catalogId=15051&langId=111&searchTerms='+str.upper(search_term)+'&authToken=368915570%252CT21vQMRnFgykHAv2T8FBa%252BDPrxI%253D']

    def parse(self, response):
        # instance of items class
        items = ScrappixItem()

        item_name = response.css('.description a:nth-child(1)::text').extract()
        price = response.css('.price::text').extract()
        image = response.css('.searchProductImgList::attr(src)').extract()
        # stock = response.css('.a-color-price::text').extract()

        items['item_name'] = item_name
        items['price'] = price
        # items['stock'] = stock
        items['image'] = image

        yield items

        next_page = 'https://www.argos.ie/webapp/wcs/stores/servlet/Search?storeId=10152&langId=111&q=LAPTOP&pp=20&s=Relevance&canned_results_trigger=%28free_text%3D%3D%28+LAPTOP%29%29&p='+str(ArgosScraperSpider.page_number*2)+'1'
        """
        if the search haven't reached the 100th page, go to next and scrape it all again.
        """
        if ArgosScraperSpider.page_number <= 100:
            ArgosScraperSpider.page_number += 1
            yield response.follow(next_page, callback=self.parse)

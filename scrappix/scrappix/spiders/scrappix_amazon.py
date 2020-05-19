import scrapy
from scrapy import signals
from ..items import ScrappixItem

# key term for online search
search_term = 'headphones'

class ScrappixAmazonSpider(scrapy.Spider):
    name = 'amazon_crawler'
    page_number = 2
    start_urls = ['https://www.amazon.co.uk/s?k='+ search_term +'&ref=nb_sb_noss_2']

    def parse(self, response):
        #instance of items class
        items = ScrappixItem()

        item_name = response.css('.a-color-base.a-text-normal::text').extract()
        price = response.css('.a-price:nth-child(1) span::text').extract()
        image = response.css('.s-image::attr(src)').extract()
        stock = response.css('.a-color-price::text').extract()

        items['item_name'] = item_name
        items['price'] = price
        items['stock'] = stock
        items['image'] = image
        yield items

        next_page = 'https://www.amazon.co.uk/s?k='+search_term+'&page='+ str(ScrappixAmazonSpider.page_number) +'&qid=1588749933&ref=sr_pg_2'
        """
        if the search haven't reached the 100th page, go to next and scrape it all again.
        """
        if ScrappixAmazonSpider.page_number <= 100:
            ScrappixAmazonSpider.page_number += 1
            yield response.follow(next_page, callback = self.parse)


# class ScrappixSpider2(scrapy.Spider):
#     name = 'did_electrical'
#     page_number = 2
#     start_urls = ['https://www.did.ie/catalogsearch/result/where/q/'+search_term]
#
#     @classmethod
#     def from_crawler(cls, crawler, *args, **kwargs):
#         spider = super(ScrappixSpider2, cls).from_crawler(crawler, *args, **kwargs)
#         # crawler.signals.connect(spider.spider_closed, signals.spider_closed)
#         return spider
#
#     def parse(self, response):
#         # instance of items class
#         items = ScrappixItem()
#
#         item_name = response.css('.product-name a::text').extract()
#         price = response.css('.price-now .price::text').extract()
#         image = response.css('..product-image img::attr(src)').extract()
#         stock = response.css('.stock-info span::text').extract()
#
#         items['item_name'] = item_name
#         items['price'] = price
#         items['stock'] = stock
#         items['image'] = image
#         yield items
#
"""
 code snippet taken from Scrapy Documentation
 https://docs.scrapy.org/en/latest/topics/practices.html#running-multiple-spiders-in-the-same-process
"""
# while True:
#     process = CrawlerProcess(get_project_settings())
#     # crawler.signals.connect(spider.spider_closed, signals.spider_closed)
#     # process.crawl(ScrappixAmazonSpider)
# process.crawl(ScrappixSpider2)
# process.start()






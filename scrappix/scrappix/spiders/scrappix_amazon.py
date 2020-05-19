import scrapy
from ..items import ScrappixItem


class ScrappixAmazonSpider(scrapy.Spider):
    name = 'scrappix_amazon'
    page_number = 2
    search_term = 'laptop'
    start_urls = ['https://www.amazon.co.uk/s?k='+ search_term +'&ref=nb_sb_noss_2']

    # def start_requests(self):
        #item = ScrappixItem()

    def parse(self, response):
        #instance of items class
        items = ScrappixItem()

        item_name = response.css('.a-color-base.a-text-normal::text').extract()
        price = response.css('.a-size-base.a-link-normal::text').extract()
        image = response.css('.s-image::attr(src)').extract()
        stock = response.css('.a-color-price::text').extract()

        items['item_name'] = item_name
        items['price'] = price
        items['stock'] = stock
        items['image'] = image

        yield items

        next_page = 'https://www.amazon.co.uk/s?k=laptops&page='+ str(ScrappixAmazonSpider.page_number) +'&qid=1588749933&ref=sr_pg_2'
        """
        if the search haven't reached the 100th page, go to next and scrape it all again.
        """
        if ScrappixAmazonSpider.page_number <= 100:
            ScrappixAmazonSpider.page_number += 1
            yield response.follow(next_page, callback = self.parse)


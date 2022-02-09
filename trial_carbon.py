import scrapy
from ..items import TrialItem


class TrialCarbonSpider(scrapy.Spider):
    name = 'trial_carbon'
    allowed_domains = ['https://carbon38.com/collections/tops']
    start_urls = ['http://https://carbon38.com/collections/tops/']

    def parse(self, response):
        items=TrialItem()
        brand=response.css('span.product-detail-label::text').extract()
        product_name=response.css('h1.title::text').extract()
        price=response.css('span.current-price theme-money::text').extract()
        items['brand']=brand
        items['product_name']=product_name
        items['price']=price
        yield items




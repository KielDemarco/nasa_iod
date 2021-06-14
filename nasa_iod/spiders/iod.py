import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from nasa_iod.items import NasaIodItem


class IodSpider(CrawlSpider):
    name = 'iod'
    allowed_domains = ['apod.nasa.gov']
    start_urls = ['https://apod.nasa.gov/apod/archivepix.html']

    rules = (
        Rule(LinkExtractor(restrict_xpaths='.//a'), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths='.//a'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = NasaIodItem()
        item['image_url'] = response.xpath('img').xpath('@src').getall()
        yield item

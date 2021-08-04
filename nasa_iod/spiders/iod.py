import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.pipelines.images import ImagesPipeline
from nasa_iod.items import NasaIodItem


class IodSpider(CrawlSpider):
    name = 'iod'
    allowed_domains = ['apod.nasa.gov']
    start_urls = ['https://apod.nasa.gov/apod/archivepix.html']
    #moves through the urls that contains the images
    rules = (
        Rule(LinkExtractor(restrict_xpaths='.//a'), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths='.//a'), callback='parse_item', follow=True),
    )
    #this is suppose to extract the image links
    def parse_item(self, response):
        item = NasaIodItem()
        srcs = response.css('img').xpath('@src').getall()
        item['image_urls'] = [response.urljoin(src) for src in srcs]
        print(item)
        return item

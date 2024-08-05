# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class IndexbotItem(scrapy.Item):
    url = scrapy.Field()
    canonical_url = scrapy.Field()
    language = scrapy.Field()
    title = scrapy.Field()
    meta = scrapy.Field()
    opengraph = scrapy.Field()
    publishing = scrapy.Field()
    headers = scrapy.Field()
    gen = scrapy.Field()
    metrics = scrapy.Field()
    schema = scrapy.Field()
    status_code = scrapy.Field()
    timestamp = scrapy.Field()

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class IndexbotPipeline:
    def process_item(self, item, spider):
        return item

import json

class JsonWriterPipeline:
    def open_spider(self, spider):
        self.file = open('crawled_data.jl', 'w')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(item) + "\n"
        self.file.write(line)
        return item
    

class TxtWriterPipeline:
    def open_spider(self, spider):
        self.file = open('crawled_sites.txt', 'w')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = item["url"] + "\n"
        self.file.write(line)
        return item

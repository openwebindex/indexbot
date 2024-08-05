import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

import os
import time
import requests

from indexbot.items import IndexbotItem
from indexbot.utils.schema_parser import parse_schema
#from indexbot.utils.text_processing import extract_keywords, generate_summary

class IndexbotSpider(CrawlSpider):
    name = "indexbot"
    
    # Load start URLs from sources.txt
    start_urls = []
    try:
        seed_url = os.getenv("SEED_URL")
        res = requests.get(seed_url)
    except:
        res = requests.get("https://cdn.data.openwebindex.org/seeds/default/seed.txt")
    for line in res.text.split("\n"):
        if line.strip() and not line.startswith("#"):
            start_urls.append(line.strip())
    
    # Restrict crawling to the start URLs if RESTRICT_CRAWL is set
    if os.getenv("RESTRICT_CRAWL"):
        allowed_domains = start_urls
        
    #allowed_domains = ["producthunt.com"]  # Replace with the target domain(s)
    #start_urls = ["http://producthunt.com"]  # Replace with the initial URL(s)

    rules = (
        Rule(LinkExtractor(), callback="parse_item", follow=True),
    )

    def parse_item(self, response):
        # Extract all paragraph content
        paragraphs = response.xpath("//p//text()").getall()
        content = ' '.join(paragraphs).strip()
        content = content[:2000] + "..." # limit content to 2000 characters

        # Generate RAKE keywords and SUMY summary
        #keywords = extract_keywords(content)
        #summary = generate_summary(content, sentences=3)

        # Parse schema data
        schema_data = parse_schema(response)
        
        item = IndexbotItem(
            url = response.url,  # The URL of the page
            canonical_url = response.xpath("//link[@rel='canonical']/@href").get(),  # Canonical URL
            language = response.xpath("//html/@lang").get(),  # Language of the page
            title = response.xpath("//title/text()").get(),  # Page title
            content = content,  # Page content
            meta = {
                "description": response.xpath("//meta[@name='description']/@content").get(),  # Meta description
                "keywords": response.xpath("//meta[@name='keywords']/@content").get(),  # Meta keywords
            },
            opengraph = {
                "url": response.xpath("//meta[@property='og:url']/@content").get(),  # Open Graph URL
                "title": response.xpath("//meta[@property='og:title']/@content").get(),  # Open Graph title
                "description": response.xpath("//meta[@property='og:description']/@content").get(),  # Open Graph description
                "locale": response.xpath("//meta[@property='og:locale']/@content").get(),  # Open Graph locale
            },
            publishing = {
                "author": response.xpath("//meta[@name='author']/@content").get(),  # Author of the content
                "date": response.xpath("//meta[@property='article:published_time']/@content").get(),  # Publishing date
            },
            headers = {
                "content_type": response.headers.get("Content-Type", b"").decode("utf-8"),  # Content-Type header
                "content_length": response.headers.get("Content-Length", b"").decode("utf-8"),  # Content-Length header
                "server": response.headers.get("Server", b"").decode("utf-8"),  # Server header
            },
            #gen = {
            #    "keywords": keywords,  # RAKE keywords
            #    "summary": summary,  # SUMY summary
            #},
            metrics={
                "content_length": len(response.text),  # Length of the page content
                "internal_links": len(response.xpath("//a[starts-with(@href, '/')]/@href").getall()), # Number of internal links
                "external_links": len(response.xpath("//a[starts-with(@href, 'http')]/@href").getall()), # Number of external links
                "images": len(response.xpath("//img").getall()),  # Total number of images
            },
            schema = schema_data,  # Schema.org JSON-LD data
            status_code = response.status,  # HTTP status code of the response
            timestamp = time.time()  # Timestamp of the scraping
        )
        yield item


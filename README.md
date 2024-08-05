# indexbot

[![CodeQL](https://github.com/openwebindex/indexbot/actions/workflows/github-code-scanning/codeql/badge.svg)](https://github.com/openwebindex/indexbot/actions/workflows/github-code-scanning/codeql)
[![Docker](https://github.com/openwebindex/indexbot/actions/workflows/docker-publish.yml/badge.svg)](https://github.com/openwebindex/indexbot/actions/workflows/docker-publish.yml)


Indexbot is the primary web crawler of the Open Web Index. It's a crawler designed to crawl a big portion of the internet to create an independent web index, which could be useful for research projects or independent search engines. 

This web crawler was made with [Scrapy](https://scrapy.org), an open source framework, which is useful for making web crawlers.


## FAQ – Indexbot

### How can I block/allow your bot?
Our Indexbot respects robots.txt files. If you wish to block our bot, simply disallow our specific bot in the robots.txt file of your website:

```
User-agent: indexbot
Disallow: /
```

If you want to unblock/allow our bot, simply allow our specific bot in the robots.txt file of your website:

```
User-agent: indexbot
Disallow:
```

### Is this a commercial project?
No, the Open Web Index is designed to be a publicly available, free to use, and open source index of the internet. We may ask for support or funding to cover the costs of indexing the web and saving our large datasets.

### Can I get my data removed?
If our bot captured personal information or illegal/copyrighted/licensed material please contact us immediately. Please list all effected files. Our bot only captures content, which is publicly available on the internet.


## Run the container

1. Pull the image and create a container
```
docker run -d -v $(pwd)/data:/data --name indexbot ghcr.io/openwebindex/indexbot:latest
```
2. Check if the container is running
```
docker ps
```
3. Manage the container
```
docker logs/start/stop indexbot
```
4. Retrieve the output
```
docker cp indexbot:app/output/crawled_data.jl crawled_data.jl
docker cp indexbot:app/output/crawled_sites.txt crawled_data.txt
```

## Development

1. Clone the repository and `cd` into it
2. Create a Python (3.11.x or above) virtual environment and activate it (optional but recommended)
3. Install requirements
```
pip install -r requirements.txt
```
4. Start the crawler
```
cd indexbot
scrapy crawl indexbot 
```


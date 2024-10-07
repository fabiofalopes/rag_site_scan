import scrapy
from urllib.parse import urljoin

class UlusofanaURLSpider(scrapy.Spider):
    name = 'ulusofona_url_spider'
    start_urls = ['https://www.ulusofona.pt/']
    allowed_domains = ['ulusofona.pt']
    urls = set()

    def parse(self, response):
        # Follow links within the same domain
        for href in response.css('a::attr(href)').extract():
            url = urljoin(response.url, href)
            if url.startswith(('http://www.ulusofona.pt', 'https://www.ulusofona.pt')):
                if url not in self.urls:
                    self.urls.add(url)
                    yield scrapy.Request(url, callback=self.parse)

    def closed(self, reason):
        # Save the list of URLs to a file
        with open('urls.txt', 'w', encoding='utf-8') as f:
            for url in self.urls:
                f.write(url + '\n') 
import scrapy
import markdown
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import os

class UlusofanaSpider(scrapy.Spider):
    name = 'ulusofona_spider'
    start_urls = ['https://www.ulusofona.pt/']
    allowed_domains = ['ulusofona.pt']

    def parse(self, response):
        # Extract and clean the content
        soup = BeautifulSoup(response.body, 'lxml')
        for script in soup(["script", "style"]):
            script.decompose()
        content = soup.get_text(separator='\n', strip=True)

        # Create a markdown structure
        md_content = f"# {soup.title.string if soup.title else 'Untitled'}\n\n"
        md_content += content

        # Save the Markdown content
        filename = self.url_to_filename(response.url)
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(md_content)

        # Follow links within the same domain
        for href in response.css('a::attr(href)').extract():
            url = urljoin(response.url, href)
            if url.startswith(('http://www.ulusofona.pt', 'https://www.ulusofona.pt')):
                yield scrapy.Request(url, callback=self.parse)

    def url_to_filename(self, url):
        # Convert URL to a valid filename
        filename = url.split('://')[1].replace('/', '_') + '.md'
        return os.path.join('ulusofona_content', filename)
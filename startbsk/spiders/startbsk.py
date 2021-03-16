import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst
from datetime import datetime
from startbsk.items import Article


class StartbskSpider(scrapy.Spider):
    name = 'startbsk'
    start_urls = ['https://www.start-bsk.de/start/ueberuns/News']

    def parse(self, response):
        articles = response.xpath('//div[@class="panel panel-bawag"]')
        for article in articles:
            item = ItemLoader(Article())
            item.default_output_processor = TakeFirst()

            title = article.xpath('.//h4/a/text()').get().strip()

            content = article.xpath('.//div[@class="panel-body"]//text()').getall()
            content = [text for text in content if text.strip()]
            content = "\n".join(content).strip()

            item.add_value('title', title)
            item.add_value('content', content)

            yield item.load_item()




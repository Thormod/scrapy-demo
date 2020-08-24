import scrapy
import uuid
from scrapyTutorial.items import NewsPostItem
from scrapy.exceptions import CloseSpider


class NewsSpider(scrapy.Spider):
    name = 'news'
    allowed_domains = ['las2orillas.co']
    start_urls = ['https://www.las2orillas.co/c/poder/']

    page_counter = 2
    scrap_until = 'agosto 11, 2020'

    def parse(self, response):
        for news_post in response.css("div[id*='post-']"):
            news_href_url = news_post.css(
                "h4.entry-title > a::attr(href)").get()
            yield scrapy.Request(news_href_url, callback=self.get_news_details)

        next_page_url = '/c/poder/page/' + str(self.page_counter)
        yield scrapy.Request(response.urljoin(next_page_url), callback=self.parse)
        self.page_counter += 1

    def get_news_details(self, response):
        news_post_title = response.css("h1.entry-title::text").extract_first()
        news_post_summary = response.css(
            "div.entry-excerpt > p::text").extract_first()
        # news_post_summary = response.css(
        #     "div[itemscope]::text").extract_first()
        news_post_date = response.css("span.meta-time::text").extract_first()
        date = news_post_date.lstrip()
        if(date != self.scrap_until):
            newsPostItem = NewsPostItem(
                NewsID=str(uuid.uuid1()),
                title=news_post_title,
                summary=news_post_summary,
                Date=news_post_date)
            yield newsPostItem
        else:
            raise CloseSpider('date_too_old')

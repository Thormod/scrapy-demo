import scrapy

class NewsPostItem(scrapy.Item):
    NewsID = scrapy.Field()
    title = scrapy.Field()
    summary = scrapy.Field()
    Date = scrapy.Field()
    pass

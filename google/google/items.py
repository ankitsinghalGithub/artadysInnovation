import scrapy


class GoogleItem(scrapy.Item):
	title = scrapy.Field()
	link = scrapy.Field()
	desc = scrapy.Field()

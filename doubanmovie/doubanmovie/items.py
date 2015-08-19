# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanmovieItem(scrapy.Item):
    subject_id = scrapy.Field()
    title = scrapy.Field()
    director = scrapy.Field()
    scriptwriter = scrapy.Field()
    actor = scrapy.Field()
    category = scrapy.Field()
    area = scrapy.Field()
    language = scrapy.Field()
    released_date= scrapy.Field()
    length = scrapy.Field()
    imdb = scrapy.Field()
    score = scrapy.Field()
    alias = scrapy.Field()
    introduce = scrapy.Field()
    top_order = scrapy.Field()
# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QijiProjectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class DhinahrItem(scrapy.Item):
    url = scrapy.Field()
    pname = scrapy.Field()
    smoney = scrapy.Field()
    emoney = scrapy.Field()
    location = scrapy.Field()
    syear = scrapy.Field()
    eyear = scrapy.Field()
    degree = scrapy.Field()
    ptype = scrapy.Field()
    tags = scrapy.Field()
    date_pub = scrapy.Field()
    advantage = scrapy.Field()
    jobdesc = scrapy.Field()
    jobaddr = scrapy.Field()
    company = scrapy.Field()
    crawl_time = scrapy.Field()

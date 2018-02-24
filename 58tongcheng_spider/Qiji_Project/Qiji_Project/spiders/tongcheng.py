# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import re
import datetime
from datetime import timedelta
from Qiji_Project.items import TongchengItem
from scrapy_redis.spiders import RedisCrawlSpider

class TongchengSpider(RedisCrawlSpider):
    name = 'tongcheng'
    allowed_domains = ['58.com']
    # start_urls = ['http://bj.58.com']
    redis_key = 'tongchengspider:urls'

    rules = (
        Rule(LinkExtractor(allow=r'http://bj.58.com/job.shtml'), follow=True),
        Rule(LinkExtractor(allow=r'.*.58.com/tech/$'), follow=True),
        Rule(LinkExtractor(allow=r'.*.58.com/tech/pn\d+/$'), follow=True),
        Rule(LinkExtractor(allow=r'\d+?x.shtml'), callback='parse_item', follow=False),
    )
    num_pattern = re.compile(r'\d+')
    #解析职位详情
    def parse_item(self, response):
        # print(response.url)
        item = TongchengItem()
        url = response.url
        # print(url)//*[@class="pos_base_info"]/span[1]/text()
        pname = response.xpath('//*[@class="pos_base_info"]/span[1]/text()').extract()[0]
        smoney = response.xpath('//*[@class="pos_base_info"]/span[2]/text()').extract()[0]
        emoney = response.xpath('//*[@class="pos_base_info"]/span[2]/text()').extract()[0]
        location = response.xpath('//*[@class="pos-area"]/span/span[1]/text()').extract()[0]
        tags = response.xpath('//*[@class="item_con pos_info"]/span/text()').extract()[0]
        advantage = response.xpath('//*[@class="pos_welfare"]/span/text()').extract()
        advantage = ','.join(advantage)
        num = response.xpath('//*[@class="pos_base_condition"]/span[1]/text()').extract()[0]
        degree = response.xpath('//*[@class="pos_base_condition"]/span[2]/text()').extract()[0]
        syear = response.xpath('//*[@class="pos_base_condition"]/span[3]/text()').extract()
        eyear = response.xpath('//*[@class="pos_base_condition"]/span[3]/text()').extract()
        # syear , eyear = self.process_year(year)
        jobaddr = response.xpath('//*[@class="pos-area"]/span[2]/text()').extract()[0]
        jobdesc = response.xpath('//*[@class="des"]/text()').extract()
        jobdesc = ','.join(jobdesc)
        company = response.xpath('//*[@class="baseInfo_link"]/a/text()').extract()[0]
        crawl_time = datetime.datetime.now().strftime('%Y-%m-%d')

        item['url'] = url
        item['pname'] = pname
        item['smoney'] = smoney
        item['emoney'] = emoney
        item['location'] = location
        item['tags'] = tags
        item['advantage'] = advantage
        item['num'] = num
        item['degree'] = degree
        item['syear'] = syear
        item['eyear'] = eyear
        item['jobaddr'] = jobaddr
        item['jobdesc'] = jobdesc
        item['company'] = company
        item['crawl_time'] = crawl_time
        yield item

    # def process_year(self, year):
    #     if '-' in year:
    #         res = self.num_pattern.findall(year)
    #         syear = res[0]
    #         eyear = res[1]
    #     elif '以上' in year:
    #         res = self.num_pattern.search(year)
    #         syear = res.group()
    #         eyear = res.group()
    #     else:
    #         syear = 0
    #         eyear = 0
    #     return syear,eyear

    # def remove_splash(self, value):
    #     return value.replace('/', '').strip()
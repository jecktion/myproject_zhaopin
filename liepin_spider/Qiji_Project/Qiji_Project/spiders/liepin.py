# -*- coding: utf-8 -*-
import scrapy

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule
import re
import datetime
from datetime import timedelta
from Qiji_Project.items import LiepinItem
from scrapy_redis.spiders import RedisCrawlSpider



class LiepinSpider(RedisCrawlSpider):
    name = 'liepin'
    allowed_domains = ['liepin.com']
    # start_urls = ['https://www.liepin.com/zhaopin/?']
    redis_key = 'liepinspider:urls'

    rules = (
        # Rule(LinkExtractor(allow=r'.*/zhaopin/.*'), follow=True),
        # Rule(LinkExtractor(allow=r'https://www.liepin.com/job/\d+?.shtml'), callback='parse_item', follow=False),
        Rule(LinkExtractor(allow=r'https://www.liepin.com/job/.*'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'.*/zhaopin/.*'), follow=False),
    )


    num_pattern = re.compile(r'\d+')

    def parse_item(self, response):
        item = LiepinItem()
        # item = {}
        url = response.url
        print(url)
        pname = response.xpath('//*[@class="title-info"]//h1/text()').extract()[0]
        print(pname)
        money = response.xpath('//*[@class="job-title-left"]//p[1]/text()').extract()[0]
        smoney,emoney = self.process_money(money)


        print(smoney,emoney)
        location = response.xpath('//*[@class="job-title-left"]//p[2]/span/a/text()').extract()[0]
        print(location)

        year = response.xpath('//*[@class="job-qualifications"]//span[2]/text()').extract()[0]
        syear, eyear = self.process_year(year)
        print(year)
        degree = response.xpath('//*[@class="job-qualifications"]//span[1]/text()').extract()[0]
        print(degree)

        date_pub = response.xpath('//*[@class="job-title-left"]/p[2]//time/text()').extract()[0]
        date_pub = self.process_date(date_pub)
        print(date_pub)
        advantage = response.xpath('//*[@class="tag-list"]//span/text()').extract()
        advantage = ','.join(advantage)
        print(advantage)
        jobdesc = response.xpath('//*[@class="content content-word"]//text()').extract()
        jobdesc = ''.join(jobdesc[:-1])
        print(jobdesc)
        jobaddr = response.xpath('//*[@class="new-compwrap"]//ul/li[3]/text()').extract()[0]
        print(jobaddr)

        company = response.xpath('//*[@class="company-logo"]//p/a/text()').extract()[0]
        print(company)
        crawl_time = datetime.datetime.now().strftime('%Y-%m-%d')
        print(crawl_time)

        item['url'] = url
        item['pname'] = pname
        item['smoney'] = smoney
        item['emoney'] = emoney
        item['location'] = location
        item['syear'] = syear
        item['eyear'] = eyear
        item['degree'] = degree
        item['date_pub'] = date_pub
        item['advantage'] = advantage
        item['jobdesc'] = jobdesc
        item['jobaddr'] = jobaddr
        item['company'] = company
        item['crawl_time'] = crawl_time

        yield item


    def process_date(self,value):
        if '小时以前' in value:
            res = self.num_pattern.search(value).group()
            date_pub = (datetime.datetime.now() - timedelta(days=int(res))).strftime('%Y-%m-%d')
        else:
            date_pub = datetime.datetime.now().strftime('%Y-%m-%d')
        return date_pub

    def process_year(self,year):
        if '-' in year:
            res = self.num_pattern.findall(year)
            syear = res[0]
            eyear = res[1]
        elif '及以上' in year:
            res = self.num_pattern.search(year)
            syear = res.group()
            eyear = res.group()
        else:
            syear = 0
            eyear = 0
        return syear,eyear

    def remove_splash(self,value):
        return value.replace('/','').strip()


    def process_money(self, money):
        if '-' in money:
            res = self.num_pattern.findall(money)
            smoney = res[0]
            emoney = res[1]
        elif '万' in money:
            res = self.num_pattern.search(money)
            smoney = res.group()[0]
            emoney = res.group()[1]

        else:
            smoney = 0
            emoney = 0
        return smoney, emoney
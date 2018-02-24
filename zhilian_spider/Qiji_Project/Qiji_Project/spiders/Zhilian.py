# -*- coding: utf-8 -*-
import re
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from Qiji_Project.items import QijiProjectItem
import datetime
from scrapy_redis.spiders import RedisCrawlSpider
class ZhilianSpider(RedisCrawlSpider):
    name = 'Zhilian'
    allowed_domains = ['zhaopin.com']

    # start_urls = ['http://sou.zhaopin.com/']
    redis_key = 'zhilian:start_urls'
    num_pattern = re.compile(r'\d+')

    rules = (
        Rule(LinkExtractor(allow=r'\d+.htm',deny=r'company'), callback='parse_item', follow=False),
        Rule(LinkExtractor(allow='/jobs/searchresult\.ashx\?jl=\d+&bj=\d+&sj=\d+', deny=r're=\d+'), follow=True),

    )


    def bai(self, i):
        if i:
            is1 = i[0]
        else:
            is1 = ''
        return is1



    def remove_splash(self, value):
        jobdesc = ''.join(value).replace('\r\n', '').strip()
        return jobdesc



    def parse_item(self,response):
        item = {}
        url = response.url
        pname = response.xpath('//div[@class="top-fixed-box"]/div[1]//h1/text()').extract()
        money = response.xpath('//div[@class="terminalpage-left"]/ul/li[1]/strong/text()').extract()

        try:
            if '面议' not in money:
                money = money[0]
                res = self.num_pattern.findall(money)
                smoney = res[0]
                emoney = res[1]
            else:
                smoney='面议'
                emoney='面议'
        except:
            smoney = None
            emoney = None
        location = response.xpath('//div[@class="terminalpage clearfix"]//li[2]//strong[1]//a/text()').extract()
        year = response.xpath('//div[@class="terminalpage-left"]/ul/li[5]/strong/text()').extract()
        try:
            if '不限' not in year:
                year = year[0]
                res = self.num_pattern.findall(year)
                syear = res[0]
                eyear = res[1]
            else:
                syear='不限'
                eyear='不限'
        except:
            syear = None
            eyear = None
        degree = response.xpath('//div[@class="terminalpage clearfix"]//li[6]//strong[1]/text()').extract()
        ptype = response.xpath('//div[@class="terminalpage clearfix"]//li[8]//strong//text()').extract()
        tags = response.xpath('//div[@class="welfare-tab-box"][1]//span/text()').extract()
        date_pub = response.xpath('//span[@id="span4freshdate"]/text()').extract()
        advantage = response.xpath('//div[@class="top-fixed-box"]/div[1]/div[@class="fl"]/div/span/text()').extract()
        jobdesc = response.xpath('//div[@class="tab-inner-cont"][1]/p/text()').extract()
        jobaddr = response.xpath('//div[@class="tab-inner-cont"]/h2/text()').extract()
        company = response.xpath('//div[@class="top-fixed-box"]/div[1]//h2/a/text()').extract()
        crawl_time = datetime.datetime.now().strftime('%Y-%m-%d')


        pname = self.bai(pname)
        location = self.bai(location)
        degree = self.bai(degree)
        ptype = self.bai(ptype)

        # date_pub = self.bai(date_pub)
        jobdesc = self.remove_splash(jobdesc)
        jobaddr = self.remove_splash(jobaddr)
        company = self.bai(company)
        advantage = self.bai(advantage)

        item['url'] = url
        item['pname'] = pname
        item['smoney'] = smoney
        item['emoney'] = emoney
        item['location'] = location
        item['syear'] = syear
        item['eyear'] = eyear
        item['degree'] = degree
        item['ptype'] = ptype
        item['tags'] = ','.join(tags)
        item['date_pub'] = ''.join(date_pub).split(' ')[0]
        item['advantage'] = advantage
        item['jobdesc'] = jobdesc
        item['jobaddr'] = jobaddr
        item['company'] = company
        item['crawl_time'] = crawl_time

        yield item
        # print(url,pname,smoney,emoney,location,syear,eyear,degree,ptype,tags,date_pub,jobdesc,jobaddr,company,crawl_time)





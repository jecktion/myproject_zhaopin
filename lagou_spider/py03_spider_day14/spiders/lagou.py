# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import re
import datetime
from datetime import timedelta
from py03_spider_day14.items import LagouItem

class LagouSpider(CrawlSpider):
    name = 'lagou'
    allowed_domains = ['lagou.com']
    start_urls = ['https://www.lagou.com']

    rules = (
        Rule(LinkExtractor(allow=r'zhaopin/.*'), follow=True),
        # Rule(LinkExtractor(allow=r'gongsi/j\d+.html'),follow=True),
        # Rule(LinkExtractor(allow=r'jobs/list_.*'), follow=True),
        Rule(LinkExtractor(allow=r'jobs/\d+.html'), callback='parse_item', follow=False),
    )

    num_pattern = re.compile(r'\d+')

    # 解析职位详情
    def parse_item(self, response):
        item = LagouItem()

        url = response.url
        pname = response.css('.job-name::attr(title)').extract()[0]

        money = response.css('.job_request .salary::text').extract()[0]
        smoney = money.lower().replace('k','').split('-')[0]
        emoney = money.lower().replace('k','').split('-')[1]

        location = response.xpath('//*[@class="job_request"]/p/span[2]/text()').extract()[0]
        location = self.remove_splash(location)

        year = response.xpath('//*[@class="job_request"]/p/span[3]/text()').extract()[0]
        syear ,eyear = self.process_year(year)

        degree = response.xpath('//*[@class="job_request"]/p/span[4]/text()').extract()[0]
        degree = self.remove_splash(degree)

        ptype = response.xpath('//*[@class="job_request"]/p/span[5]/text()').extract()[0]
        ptype = self.remove_splash(ptype)

        tags = response.css('.position-label li::text').extract()
        tags = ','.join(tags)

        date_pub = response.css('.publish_time::text').extract()[0]
        date_pub = self.process_date(date_pub)

        advantage = response.css('.job-advantage p::text').extract()[0]

        jobdesc = response.css('.job_bt div p::text').extract()
        jobdesc = ''.join(jobdesc)

        jobaddr1 = response.css('.work_addr a::text').extract()[:-1]
        jobaddr2 = response.css('.work_addr::text').extract()[-2].strip()
        jobaddr = ''.join(jobaddr1) + jobaddr2

        company = response.css('#job_company dt a img::attr(alt)').extract()[0]
        crawl_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        item['url'] = url
        item['pname'] = pname
        item['smoney'] = smoney
        item['emoney'] = emoney
        item['location'] = location
        item['syear'] = syear
        item['eyear'] = eyear
        item['degree'] = degree
        item['ptype'] = ptype
        item['tags'] = tags
        item['date_pub'] = date_pub
        item['advantage'] = advantage
        item['jobdesc'] = jobdesc
        item['jobaddr'] = jobaddr
        item['company'] = company
        item['crawl_time'] = crawl_time

        yield item

    def process_date(self,value):
        if '天前' in value:
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
        elif '以上' in year:
            res = self.num_pattern.search(year)
            syear = res.group()
            eyear = res.group()
        else:
            syear = 0
            eyear = 0
        return syear,eyear

    def remove_splash(self,value):
        return value.replace('/','').strip()

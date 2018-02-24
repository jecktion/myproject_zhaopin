# -*- coding: utf-8 -*-
# import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import datetime
import re
from Qiji_Project.items import WuyoujobItem
from scrapy_redis.spiders import RedisCrawlSpider


# class A51jobSpider(scrapy.Spider):
# class A51jobSpider(CrawlSpider):
class A51jobSpider(RedisCrawlSpider):
    name = 'A51job'
    allowed_domains = ['51job.com']
    # start_urls = ['http://www.51job.com']
    redis_key = '51jobspider:urls'
    # print('ok11111111111111111111111111111')

    rules = (
        # 定位
        Rule(LinkExtractor(allow=r'http://www.51job.com/[a-z]+$'), follow=True),

        # 列表页 http://search.51job.com
        # Rule(LinkExtractor(allow=r'http://search.51job.com/list/.+.html'), follow=True),

        # 详情页 http://jobs.51job.com/
        Rule(LinkExtractor(allow=r'http://jobs.51job.com/[a-z]+/\d+.html'), callback='parse_detail', follow=True),
        # Rule(LinkExtractor(allow=r'http://search.51job.com/list/[a-z]+-[a-z]+/\d+.html'), callback='parse_detail', follow=False),
        # Rule(LinkExtractor(allow=r'http://search.51job.com/list/[a-z]+-[a-z]+/\d+.html'), callback='parse_detail', follow=False),
    )
    num_pattern = re.compile(r'\d+')
    def parse_detail(self, response):
        print(response.url)
        item = WuyoujobItem()
        # print(response.body)
        # print(response.text)
        url = response.url
        pname = response.xpath('//h1/text()').extract()[0]
        money = response.xpath('//div[@class="cn"]/strong/text()').extract()
        if money:
            money = money[0]
            if '天' in money:
                smoney = money[:-3]
                emoney = money[:-3]
            elif '月' in money:
                if '-' in money:
                    smoney = money.split('-')[0]
                    emoney = money.split('-')[1][:-3]
                else:
                    smoney = money[:-5]
                    emoney = money[:-5]
            elif '年' in money:
                if '-' in money:
                    smoney = money.split('-')[0] + '年'
                    emoney = money.split('-')[1][:-3] + '年'
                else:
                    smoney = money[:-5]
                    emoney = money[:-5]
                # smoney = money.split('-')[0] + '年'
                # emoney = money.split('-')[1][:-3] + '年'
        else:
            money = '面议'
            smoney = money
            emoney = money
        location = response.xpath('//div[@class="cn"]/span/text()').extract()[0]
        # // div / span[em[@class ="i1"]] / text()
        # year = response.xpath('//div[@class="t1"]//em[@class="i1"]/text()').extract()[0]
        year = response.xpath('//div/span[em[@class ="i1"]]/text()').extract()[0]
        if '无' in year:
            syear = 0
            eyear = 0
        elif '-' in year:
            syear = year.split('-')[0]
            eyear = year.split('-')[1][0]
        else:
            syear = year[0]
            eyear = year[0]
        degree = response.xpath('//div/span[em[@class ="i2"]]/text()').extract()
        if degree:
            degree = degree[0]
        else:
            degree = '无'
        num = response.xpath('//div/span[em[@class ="i3"]]/text()').extract()
        if num:
            num = self.num_pattern.search(str(num))
            if num:
                num = num.group()
            else:
                num = '若干'
        else:
            num = '若干'
        tags = response.xpath('//div[@class="cn"]/p/text()').extract()[2].replace('\t', '').replace(' ', '').replace('\xa0', '').replace('\r', '').replace('\n', '')
        crawl_time = datetime.datetime.now().strftime('%Y-%m-%d')
        date_pub = response.xpath('//div/span[em[@class ="i4"]]/text()').extract()[0]
        if date_pub:
            date_pub = datetime.datetime.now().strftime('%Y') + '-' + date_pub[:-2]
        else:
            date_pub = '无'
        advantage = response.xpath('//p[@class="t2"]/span/text()').extract()
        advantage = '|'.join(advantage)
        # jobdesc = response.xpath('//div[@class="bmsg job_msg inbox"]/text()').extract()
        jobdesc = response.xpath('//div[@class="bmsg job_msg inbox"][br]/text()').extract()
        jobdesc = ''.join(jobdesc).replace('\t', '').replace('\r', '').replace('\n', '')
        if not jobdesc:
            jobdesc = '无'
        jobaddr = response.xpath('//p[@class="fp"]/text()').extract()
        jobaddr = ''.join(jobaddr).replace('\t', '').replace('\r', '').replace('\n', '')
        if not jobaddr:
            jobaddr = '无'
        company = response.xpath('//div[@class="cn"]/p[@class="cname"]/a/text()').extract()[0]
        ptype = ''
        # print(date_pub)

        item['url'] = url
        item['pname'] = pname
        item['smoney'] = smoney
        item['emoney'] = emoney
        item['location'] = location
        item['syear'] = syear
        item['eyear'] = eyear
        item['num'] = num
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

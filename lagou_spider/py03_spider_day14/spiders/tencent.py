# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor # 提取页面中所有超链接
from scrapy.spiders import CrawlSpider, Rule
from py03_spider_day14.items import TencentItem


class TencentSpider(CrawlSpider):
    name = 'tencent'
    allowed_domains = ['tencent.com']
    start_urls = ['http://hr.tencent.com']

    # 定义提取url链接的规则
    rules = (
        # 如果LinkExtractor不指定参数，则获取所有超链接
        #
        # Rule 构建请求
        # follow 是否跟进页面 继续按照规则进行匹配，生成请求
        # 详情页链接规则
        Rule(LinkExtractor(allow=(r'position_detail')), callback='parse_item', follow=True),
        # 列表页或者其它页
        Rule(LinkExtractor(allow=(r'position.php')),follow=True),
    )

    def parse_item(self, response):
        item = TencentItem()

        pname = response.css('#sharetitle::text').extract()[0]
        tr_info = response.css('.bottomline td::text').extract()

        location = tr_info[0]
        ptype = tr_info[1]
        number = tr_info[2].strip('人')

        duty = response.xpath('//tr[@class="c"][1]//ul[@class="squareli"]/li/text()').extract()
        requirement = response.xpath('//tr[@class="c"][2]//ul[@class="squareli"]/li/text()').extract()
        duty = ''.join(duty)
        requirement = ''.join(requirement)

        item['pname'] = pname
        item['location'] = location
        item['ptype'] = ptype
        item['number'] = number
        item['duty'] = duty
        item['requirement'] = requirement

        # 交给管道文件
        yield item



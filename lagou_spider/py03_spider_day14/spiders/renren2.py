# -*- coding: utf-8 -*-
import scrapy

class Renren1Spider(scrapy.Spider):
    name = 'renren2'
    allowed_domains = ['renren.com']


    # 解析start_urls 的方法
    def start_requests(self):
        start_urls = 'http://www.renren.com/PLogin.do'
        data = {
            'email' : '1752570559@qq.com',
            'password' : '1234qwer',
        }
        # FormRequest 发起post请求
        yield scrapy.FormRequest(start_urls,formdata=data,callback=self.parse)

    def parse(self, response):
        print(response.text)

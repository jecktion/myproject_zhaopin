# -*- coding: utf-8 -*-
import scrapy

class Renren1Spider(scrapy.Spider):
    name = 'renren1'
    allowed_domains = ['renren.com']
    start_urls = ['http://renren.com/']
    headers = {
        "Host": "www.renren.com",
        "Connection": "keep-alive",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
        "Upgrade-Insecure-Requests": "1",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        # "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
    }
    Cookie = {
        "anonymid": "j9rsbcfe36yr3u",
        "_r01_": "1",
        "depovince": "BJ",
        "jebecookies": "e3104532-71f3-4406-88fe-2f1c294955b0|||||",
        "ick_login": "f4a72140-23a1-4688-b002-a5e40d697480",
        "_de": "31795CAA550243A1FFFC179CCE3D61136DEBB8C2103DE356",
        "p": "865b6b889d27b88361ae11c80d7ec60b0",
        "first_login_flag": "1",
        "ln_uact": "1752570559@qq.com",
        "ln_hurl": "http://head.xiaonei.com/photos/0/0/men_main.gif",
        "t": "4ff7a9016a6833c2fc9628f8507676bd0",
        "societyguester": "4ff7a9016a6833c2fc9628f8507676bd0",
        "id": "440906810",
        "xnsid": "3d6ece21",
        "JSESSIONID": "abcPhnVtP80nsgUgtKc-v",
        "jebe_key": "e297c8fd-cb3c-4d44-9f8c-f5d0a3aaa281%7C13cfe4e0f2468cd238a9520eb2c92717%7C1510797818791%7C1%7C1510797818689",
        "ver": "7.0",
        "loginfrom": "null",
        "wp_fold": "0",
    }

    def parse(self, response):
        # 构建个人首页请求
        base_url = 'http://www.renren.com/440906810'
        yield scrapy.Request(base_url,callback=self.parsehome,headers=self.headers,cookies=self.Cookie)

    # 处理个人首页的函数
    def parsehome(self,response):
        print(response.text)

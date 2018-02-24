# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from fake_useragent import UserAgent
import random
from py03_spider_day14 import settings
import base64
from py03_spider_day14.utils import get_proxy

class Py03SpiderDay14SpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)



class RandomUserAgent(object):
    # 处理请求的函数
    def __init__(self,crawler):
        '''
        :param crawler: 爬虫对象
        '''
        # 获取配置文件中的配置信息
        self.ua_type = crawler.settings.get('RANDOM_UA_TYPE','random')
        self.ua = UserAgent()

    @classmethod
    def from_crawler(cls,crawler):
        return cls(crawler)

    def process_request(self,request,spider):
        '''
        :param request: 请求对象
        :param spider: 蜘蛛对象
        :return:
        '''

        request.headers.setdefault('User-Agent', getattr(self.ua ,self.ua_type))

class FreeRandomProxy(object):
    def process_request(self,request,spider):
        # 随机选出代理信息
        # proxy = random.choice()
        proxy = get_proxy.getproxy()
        request.meta['proxy'] = '%s://%s:%s' % (proxy[2],proxy[0],proxy[1])

class AuthRandomProxy(object):
    def process_request(self,request,spider):
        # 随机选出代理信息
        proxy = random.choice(settings.AUTH_PROXIES)
        # 设置代理的认证信息
        auth = base64.b64encode(bytes(proxy['auth'],'utf-8'))
        request.headers['Proxy-Authorization'] = b'Basic ' + auth
        # 设置代理ip
        request.meta['proxy'] = 'http://' + proxy['host']
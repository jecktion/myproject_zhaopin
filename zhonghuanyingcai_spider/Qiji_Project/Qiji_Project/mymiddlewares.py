#一个中间件就是一个类
from fake_useragent import UserAgent
from Qiji_Project import settings
import random
import base64
#使用UserAgent
class RandomUserAgent(object):
    #处理请求的函数
    def __init__(self,crawler):
        '''

        :param crawler: 爬虫对象
        '''
        #获取配置文件中的配置信息
        #RANDOM_UA_TYPEp 在setting中设置随机浏览器方式
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
        request.headers.setdefault('User-Agent',getattr(self.ua,self.ua_type))

# #随机选择免费代理
# class FreeRandomProxy(object):
#     def process_request(self,request,spider):
#         # 随机选出代理信息
#         # 这个是在setting中设置ip , 随机选择一个
#         proxy = random.choice(settings.PROXIES)
#         request.meta['proxy'] = 'http://' + proxy['host']



# 随机选择付费代理
class AuthRandomProxy(object):
    def process_request(self,request,spider):
        #随机选出代理信息
        proxy = random.choice(settings.AUTH_PROXIES)
        #设置代理的认证信息
        auth = base64.b64encode(bytes(proxy['auth'],'utf-8'))
        request.headers['Proxy-Authorization'] = b'Basic ' + auth
        #设置代理ip
        request.meta['proxy'] = 'http://' + proxy['host']
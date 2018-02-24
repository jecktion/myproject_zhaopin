# -*- coding: utf-8 -*-

# Scrapy settings for Qiji_Project project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'Qiji_Project'

SPIDER_MODULES = ['Qiji_Project.spiders']
NEWSPIDER_MODULE = 'Qiji_Project.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'Qiji_Project (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 10

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# 下载器在下载同一个网站下一个页面前需要等待的时间。该选项可以用来限制爬取速度， 减轻服务器压力。同时也支持小数:
DOWNLOAD_DELAY = 0.5
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False
cookie = {
    "chrId":"0b3540266dee430eac4749de7875f6d7",
    "wmda_uuid":"85849fa765cad07d9bbd9978699fcdee",
    "wmda_new_uuid":"1",
    "wmda_visited_projects":"%3B1732047435009",
    "gr_user_id":"448e31a5-a5a1-4e3c-b0e1-e309acad9e1b",
    "closeCompletCv":"1",
    "als":"0",
    "_ga":"GA1.2.847972919.1511161464",
    "_gid":"GA1.2.2009349692.1511161464",
    "gtid":"3e1edb6ae40b446d9273a1ec78e9a3cb",
    "58tj_uuid":"e570b88c-6ced-4aa7-8eed-1e191e5d7004",
    "channel":"social",
    "new_session":"0",
    "new_uv":"3",
    "utm_source":"",
    "spm":"",
    "init_refer":"http%253A%252F%252Fwww.chinahr.com%252Fjob%252F6143299991473155.html",
    "gr_session_id_be17cdb1115be298":"1204bbcc-68e3-4b87-8fe2-82947b355df7",
    "RecentVisitCity":"398_beijing",
    "RecentVisitCityFullpathPc":'"34,398"',
    "wmda_session_id":"1511184817906-76bc2ee2-3ec8-2a03",
}

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    "Host":"www.chinahr.com",
    "Connection":"keep-alive",
    "Cache-Control":"max-age=0",
    "Upgrade-Insecure-Requests":"1",
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36",
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Referer":"http://www.chinahr.com/zhengzhou/",
    "Accept-Language":"zh-CN,zh;q=0.9",
}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'Qiji_Project.middlewares.QijiProjectSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   # 'Qiji_Project.middlewares.MyCustomDownloaderMiddleware': 543,
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware':None,
    #User-Agent
    'Qiji_Project.mymiddlewares.RandomUserAgent':1,
    #免费代理的使用
    'Qiji_Project.mymiddlewares.AuthRandomProxy': 2,
}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   # 'Qiji_Project.pipelines.QijiProjectPipeline': 300,
   #  'scrapy_redis.pipelines.RedisPipeline':999,
    # 配置redis管道文件，权重数字相对最大
    'scrapy_redis.pipelines.RedisPipeline': 999, # redis管道文件，自动把数据加载到redis
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


#分布式爬取
#下载超时 , 用于检测过滤重复请求的类
DOWNLOAD_TIMEOUT = 15

#记录所有重复请求
# DUPEFILTER_DEBUG = True

#url 指纹过滤器
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"

# 调度器
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# 设置爬虫是否可以中断
SCHEDULER_PERSIST = True

# 设置请求队列类型
SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderPriorityQueue" # 按优先级入队列
# SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderQueue"  # 按照队列模式
# SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderStack" # 按照栈进行请求的调度

# redis 连接配置
REDIS_HOST = '101.132.179.75'
REDIS_PORT = 8001



# #免费代理的使用(没有从数据库中获取)
# PROXIES = [
#     {'host' : '114.227.97.50:9000'},
#     {'host' : '115.148.27.10:9000'},
#     {'host': '117.139.45.248:8123'},
#     {'host': '117.90.0.155:9000'},
#     {'host': '120.27.10.38:8090'},
#     {'host': '121.232.147.38:9000'},
#     {'host': '121.232.148.150:9000'},
#     {'host': '223.151.209.189:9000'},

# ]

#付费代理的使用
AUTH_PROXIES = [
    {'host' : '120.78.166.84:6666', 'auth' : 'alice:123456'}
]

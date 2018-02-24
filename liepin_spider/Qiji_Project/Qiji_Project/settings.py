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
# USER_AGENT = {
#     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
#     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
# }
# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 32  #并发量

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0.1    #下载间隔时间
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False       #不遵守爬取规则

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
# "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
# "Accept-Encoding" : "gzip, deflate, br",
# "Accept-Language" : "zh-CN,zh;q=0.9",
# "Cache-Control" : "max-age=0",
# "Connection" : "keep-alive",
# "Cookie" : "_fecdn_=1; gr_user_id=07f38336-0ef5-42b6-9576-45c7229b70b0; __uuid=1511613920679.65; slide_guide_home_new=1; slide_guide_home=1; verifycode=5e1e424a894e40278d9958ee805a2d48; abtest=0; JSESSIONID=67B6DF9D12013A99420AB10045CC086C; __tlog=1511613920679.95%7C00000000%7CR000000075%7Cs_o_001%7Cs_o_001; __session_seq=9; __uv_seq=9; Hm_lvt_a2647413544f5a04f00da7eee0d5e200=1511613921,1511614248,1511614452; Hm_lpvt_a2647413544f5a04f00da7eee0d5e200=1511614479; gr_session_id_bf8a73282d811a1b=081ac934-e477-484b-a3fd-864b54198af3",
# "Host" : "www.liepin.com",
# "Referer" : "https://www.liepin.com/zhaopin/?d_sfrom=search_fp_nvbar&init=1",
# "Upgrade-Insecure-Requests" : "1",
# "User-Agent" : "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
# }

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'Qiji_Project.middlewares.QijiProjectSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#     # 'Qiji_Project.middlewares.MyCustomDownloaderMiddleware': 543,
#     'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
#     'Qiji_Project.middlewares.RandomUserAgent': 1,
#     'Qiji_Project.middlewares.AuthRandomProxy': 2,
#     # 'Qiji_Project.middlewares.FreeRandomProxy': 2,
# }
#超时时间
DOWNLOAD_TIMEOUT = 100

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html


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


# PROXIES = [
#     {'host' : '110.72.47.220:8123'},
#     {'host' : '119.36.92.46:81'},
#     {'host' : '185.82.203.221:1080'},
#     {'host' : '39.104.28.72:8080'},
#     {'host' : '103.251.165.9:1080'},
#     {'host' : '103.226.152.93:9797'},
#     {'host' : '103.21.77.117:8080'},

 # ]

# AUTH_PROXIES = [
#
#     {'host': '120.78.166.84:6666', 'auth': 'alice:123456'}
#     # {'host': '121.42.63.89:16816', 'auth': '492741071:tl8g3zs5'}
# ]




# url指纹过滤器
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"

# 调度器
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# 设置爬虫是否可以中断
SCHEDULER_PERSIST = True

# 设置请求队列类型
# SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderPriorityQueue" # 按优先级入队列
# SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderQueue"  # 按照队列模式  先进先出
SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderStack" # 按照栈进行请求的调度  先进后出

# 配置redis管道文件，权重数字相对最大
ITEM_PIPELINES = {
    'scrapy_redis.pipelines.RedisPipeline': 999,  # redis管道文件，自动把数据加载到redis
}

# ITEM_PIPELINES = {
#     'Qiji_Project.pipelines.LiepinMysqlPipeline': 999,
#
# }
# redis连接配置
REDIS_HOST = '101.132.179.75'
REDIS_PORT = 8001
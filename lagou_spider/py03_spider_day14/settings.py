# -*- coding: utf-8 -*-

# Scrapy settings for py03_spider_day14 project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'py03_spider_day14'

SPIDER_MODULES = ['py03_spider_day14.spiders']
NEWSPIDER_MODULE = 'py03_spider_day14.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'py03_spider_day14 (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# 并发量
CONCURRENT_REQUESTS = 16

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0.2
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# 是否启用cookie
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
"Host" : "www.lagou.com",
"Connection" : "keep-alive",
"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
"Content-type" : "application/json;charset=utf-8",
"Accept" : "*/*",
"Referer" : "https://www.lagou.com/jobs/3737258.html",
"Accept-Encoding" : "gzip, deflate, br",
"Accept-Language" : "zh-CN,zh;q=0.9",
"Cookie" : "user_trace_token=20171116192426-b45997e2-cac0-11e7-98fd-5254005c3644; LGUID=20171116192426-b4599a6d-cac0-11e7-98fd-5254005c3644; index_location_city=%E5%85%A8%E5%9B%BD; JSESSIONID=ABAAABAAAGFABEFC0E3267F681504E5726030548F107348; _gat=1; X_HTTP_TOKEN=d8b7e352a862bb108b4fd1b63f7d11a7; _gid=GA1.2.1718159851.1510831466; _ga=GA1.2.106845767.1510831466; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1510836765,1510836769,1510837049,1510838482; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1510839167; LGSID=20171116204415-da8c7971-cacb-11e7-930c-525400f775ce; LGRID=20171116213247-a2658795-cad2-11e7-9360-525400f775ce",
}
# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'py03_spider_day14.middlewares.Py03SpiderDay14SpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'py03_spider_day14.middlewares.RandomUserAgent': 1,
    # 'py03_spider_day14.middlewares.FreeRandomProxy': 2,
}

DOWNLOAD_TIMEOUT = 10

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    # 'py03_spider_day14.pipelines.TencentPipeline': 1,
    'py03_spider_day14.pipelines.LagouMysqlPipeline': 1,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

AUTH_PROXIES = [
    {'host': '120.78.166.84:6666', 'auth': 'alice:123456'}
]

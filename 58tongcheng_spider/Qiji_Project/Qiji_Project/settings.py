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
CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0.8
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"
    # "Cookie" : 'userid360_xml=859BA0571AF1C7103202DED2190EF4C6; time_create=1512616723390; f=n; id58=c5/ns1oBJXpmSiigAzTWAg==; als=0; commontopbar_myfeet_tooltip=end; gr_usMozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36Query String Parametersview sourceview URL encodeder_id=9a08d77b-36c0-4dc6-a79a-aade1c88bbed; wmda_uuid=683993f87a9ebe0d0d293b2b15b97c55; wmda_new_uuid=1; param8616=0; param8716=1; Hm_lvt_a3013634de7e7a5d307653e15a0584cf=1510024761; isSmartSortTipShowed=true; bj58_id58s="KzEwaVVHMEtJS1BlNjM2OA=="; UM_distinctid=15f96c828052c4-0c14a6d731fb65-7b1030-e1000-15f96c828062db; Hm_lvt_3bb04d7a4ca3846dcc66a99c3e861511=1510024591,1511144035; Hm_lvt_e15962162366a86a6229038443847be7=1510024597,1511144036; wmda_visited_projects=%3B1409632296065%3B1731916484865%3B1731918550401; myfeet_tooltip=end; hots=%5B%7B%22d%22%3A0%2C%22s1%22%3A%22it%22%2C%22s2%22%3A%22%22%2C%22n%22%3A%22sou%22%7D%5D; __utma=253535702.1844258092.1510024598.1511178383.1511178383.1; __utmz=253535702.1511178383.1.1.utmcsr=bj.58.com|utmccn=(referral)|utmcmd=referral|utmcct=/; Hm_lvt_b4a22b2e0b326c2da73c447b956d6746=1511194461; Hm_lvt_67fc2f6a158bd2fe1dfbbc465557cfa0=1511230694; job_detail_resume_guide_close=1; bj58_new_uv=7; mcity=bj; mcityName=%E5%8C%97%E4%BA%AC; nearCity=%5B%7B%22cityName%22%3A%22%E9%83%91%E5%B7%9E%22%2C%22city%22%3A%22zz%22%7D%2C%7B%22cityName%22%3A%22%E5%8C%97%E4%BA%AC%22%2C%22city%22%3A%22bj%22%7D%5D; job_detail_show_time=8; 58app_hide=1; Hm_lvt_5a7a7bfd6e7dfd9438b9023d5a6a4a96=1511244143; sessionid=e698fcbf-fb53-440e-b90e-603af719be1d; commontopbar_ipcity=bj%7C%E5%8C%97%E4%BA%AC%7C0; 58home=bj; city=bj; Hm_lvt_e2d6b2d0ec536275bb1e37b421085803=1511322940; Hm_lpvt_e2d6b2d0ec536275bb1e37b421085803=1511322940; GA_GTID=0d4037f6-016b-caaa-7062-280fc5e4c352; _ga=GA1.2.1844258092.1510024598; _gid=GA1.2.326129460.1511322941; final_history=29296791988560; bdshare_firstime=1511322941479; f=n; JSESSIONID=AED48FF06A0DD5BEA018695CEBCAB7C0; Hm_lvt_5bcc464efd3454091cf2095d3515ea05=1511144151,1511267014,1511274560,1511311400; Hm_lpvt_5bcc464efd3454091cf2095d3515ea05=1511330364; 58tj_uuid=7d3b1370-076c-4383-a615-6f939f4d3ca8; new_session=0; new_uv=24; utm_source=; spm=; init_refer=; Hm_lvt_b2c7b5733f1b8ddcfc238f97b417f4dd=1510062633,1511166312,1511255585,1511275941; Hm_lpvt_b2c7b5733f1b8ddcfc238f97b417f4dd=1511331240; gr_session_id_b4113ecf7096b7d6=b798fa6f-e71c-4d6e-bc6c-d479921ff9ca; wmda_session_id=1511329391427-5177a31b-84eb-a721; ppStore_fingerprint=98A86A5F8F9F515D4386FD9F5333D90C0E2EBB710069F8C2%EF%BC%BF1511331241353; commontopbar_new_city_info=1%7C%E5%8C%97%E4%BA%AC%7Cbj; xxzl_deviceid=T5EJZMP7r2joG%2BIxmcnQCCJLvVj9IilZSMSPXyvRCFnt9ODQXABGDrgJaAxAqOFj'

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
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'Qiji_Project.middlewares.RandomUserAgent': 1,
}

DOWNLOAD_TIMEOUT = 3

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#     # 'Qiji_Project.pipelines.QijiProjectPipeline': 300,
#     'Qiji_Project.pipelines.TongchengMysqlPipeline': 999,
# }

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


AUTH_PROXIES = [
    {'host': '120.78.166.84:6666', 'auth': 'alice:123456'}
]

# url指纹过滤器
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"

# 调度器
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# 设置爬虫是否可以中断
SCHEDULER_PERSIST = True

# 设置请求队列类型
SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderPriorityQueue" # 按优先级入队列
SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderQueue"  # 按照队列模式
# SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderStack" # 按照栈进行请求的调度

# 配置redis管道文件，权重数字相对最大
ITEM_PIPELINES = {
    'scrapy_redis.pipelines.RedisPipeline': 999,  # redis管道文件，自动把数据加载到redis
}

# redis连接配置
REDIS_HOST = '39.106.67.138'
REDIS_PORT = 6379
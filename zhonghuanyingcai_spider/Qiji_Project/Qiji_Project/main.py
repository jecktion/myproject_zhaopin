from scrapy import cmdline
import os
os.chdir('spiders')
# cmdline.execute('scrapy crawl chinahr'.split())
cmdline.execute('scrapy runspider chinahr.py'.split())
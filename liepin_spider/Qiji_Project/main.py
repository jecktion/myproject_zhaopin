from scrapy import cmdline
import os

os.chdir('Qiji_Project/spiders')

cmdline.execute('scrapy runspider liepin.py'.split())

# cmdline.execute('scrapy crawl liepin'.split())
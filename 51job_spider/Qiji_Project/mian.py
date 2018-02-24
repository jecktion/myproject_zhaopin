from scrapy import cmdline
import os
os.chdir('Qiji_Project/spiders')
# cmdline.execute('scrapy crawl wuyoujob'.split())
cmdline.execute('scrapy runspider wuyoujob.py'.split())

from scrapy import cmdline
import os
os.chdir('Qiji_Project/spiders')
cmdline.execute('scrapy runspider tongcheng.py'.split())
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


import json
import pymysql

class QijiProjectPipeline(object):
    def process_item(self, item, spider):
        return item

class MysqlPipeline(object):
    def __init__(self):
        self.conn = pymysql.connect('127.0.0.1','root','root','mydb_qiji',charset='utf8')
        self.cursor = self.conn.cursor()
    def close_spider(self,spider):
        self.cursor.close()
        self.conn.close()

class TongchengMysqlPipeline(MysqlPipeline):
    def process_item(self,item, spider):
        if spider.name == 'tongcheng':
            sql = 'insert into qiji_job(url,pname,smoney,emoney,location,tags,advantage,num,degree,syear,eyear,jobaddr,jobdesc,company,crawl_time) ' \
                  'VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) on duplicate key update advantage=values(advantage),smoney=VALUES(smoney),emoney=values(emoney)'

            try:
                self.cursor.execute(sql,(item["url"],item["pname"],item["smoney"],item["emoney"],item["location"],item["tags"],item["advantage"],item["num"],item["degree"],item["syear"],item["eyear"],item["jobaddr"],item["jobdesc"],item["company"],item["crawl_time"]))

                self.conn.commit()
            except Exception as e:
                self.conn.rollback()
                print(e)
                print('执行语句失败')
            # 返回交给下一个管道文件处理
        return item

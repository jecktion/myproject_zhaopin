import threading
import requests
from lxml import etree
import time
import random
import json
import queue

#定义一个解析线程类
class Data(threading.Thread):
    def __init__(self,number,req_thread,data_list,f):
        #调用父类的初始化 ,放置被覆盖
        super(Data,self).__init__()
        self.number = number
        self.data_list = data_list
        self.req_thread = req_thread
        self.f = f
        self.is_parse = True  #判断是否从数据队列中提取到数据

    def run(self):
        print('{0}线程解析'.format(self.number))
        #无限循环
        while True:
            #如何判断解析线程的条件结束
            for t in self.req_thread: #循环所有采集线程
                if t.is_alive(): #判断线程是是否存活
                    break
            else: #循环完毕 , 如果采集线程都不存活
                if self.data_list.qsize() == 0: #判断数据队列是否为空
                    self.is_parse == False
            #判断是否继续解析
            if self.is_parse: #解析
                try:
                    data = self.data_list.get(timeout=3) #从数据队列中提取数据
                except Exception as e: #超时以后进入异常
                    data = None
                if data is not None:
                    self.parse(data) #调用解析方法
            else:
                break #如果不用解析 结束循环
        print('退出{0}号解析线程'.format(self.number))
    def parse(self,data):
        html = etree.HTML(data)
        # 获取所有段子div
        duanzi_div = html.xpath('//div[@id="content-left"]/div')

        for duanzi in duanzi_div:
            # 获取昵称
            nick = duanzi.xpath('./div//h2/text()')[0]
            nick = nick.replace('\n', '')
            # 获取年龄
            age = duanzi.xpath('.//div[@class="author clearfix"]/div/text()')
            if len(age) > 0:
                age = age[0]
            else:
                age = 0
            # 获取性别
            gender = duanzi.xpath('.//div[@class="author clearfix"]/div/@class')
            if len(gender) > 0:
                if 'women' in gender[0]:
                    gender = '女'
                else:
                    gender = '男'
            else:
                gender = '中'

            # 获取段子内容
            content = duanzi.xpath('.//div[@class="content"]/span[1]/text()')[0].strip()

            # 获取好笑数
            good_num = duanzi.xpath('./div//span[@class="stats-vote"]/i/text()')[0]

            # 获取评论
            common_num = duanzi.xpath('./div//span[@class="stats-comments"]//i/text()')[0]

            item = {
                'nick': nick,
                'age': age,
                'gender': gender,
                'content': content,
                'good_num': good_num,
                'common_num': common_num,
            }

            self.f.write(json.dumps(item, ensure_ascii=False) + '\n')


#定义一个请求线程类
class Crawl(threading.Thread):
    def __init__(self,number,req_list,data_list):
        #调用super父类初始化方法,放置被覆盖
        super(Crawl,self).__init__()
        self.number = number
        self.req_list = req_list
        self.data_list = data_list
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36'
        }
    #线程启动的时候调用
    def run(self):
        #输出线程启动的时候得信息
        print('启动采用线程{0}号'.format(self.number))
        while self.req_list.qsize() > 0:
            #从队列中提取路由信息发起请求
            base_url = self.req_list.get()
            print('{0}号线程采集{1}'.format(self.number,base_url))
            #放置请求频率过快 , 随机设置阻塞时间
            time.sleep(random.randint(1,3))
            #发起http请求,获取响应内容 , 追加到数据队列中 , 等待解析
            requests.packages.urllib3.disable_warnings() #解决ssl警告问题
            response = requests.get(base_url,headers = self.headers,verify = False)
            data = response.text
            #将请求数据放入解析队列中
            self.data_list.put(data)




def main():
    #创建一个请求队列
    req_list = queue.Queue()
    #创建一个数据解析队列
    data_list = queue.Queue()
    #创建文件对象
    f = open('duanzi.json','w',encoding='utf-8')

    #将请求地址放入请求队列中
    for i in range(1,13+1):
        base_url = 'https://www.qiushibaike.com/8hr/page/{0}'.format(i)
        req_list.put(base_url)
    #定义一个存放请求线程的列表
    req_thread = []
    #创建三个请求线程
    for i in range(3):
        t = Crawl(i,req_list,data_list)
        t.start()
        req_thread.append(t)

    #定义一个存放请求线程的列表
    data_thread = []
    #创建三个解析数据线程
    for i in range(3):
        t = Data(i,req_thread,data_list,f)
        t.start()
        data_thread.append(t)
    #当请求线程结束后执行父线程
    for t in req_thread:
        t.join()
    #当所有解析线程结束后执行父线程
    for t in data_thread:
        t.join()
    #关闭文件对象
    f.close()
if __name__ == '__main__':
    main()
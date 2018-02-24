import requests
import json
import threading
from bs4 import BeautifulSoup
import time
import queue

class Req(threading.Thread):
    def __init__(self,number,data_list,req_list):
        super(Req, self).__init__()
        self.number = number
        self.data_list = data_list
        self.req_list = req_list

    def run(self):
        headers = {
            "Host": "talent.baidu.com",
            "Connection": "keep-alive",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "X-Requested-With": "XMLHttpRequest",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded",
            "Referer": "http://talent.baidu.com/external/baidu/index.html",
            "Accept-Language": "zh-CN,zh;q=0.8",
        }
        print('{0}号请求线程启动'.format(self.number))
        while self.req_list.qsize() > 0:
            # 获取请求队列中的数据
            base_url = self.req_list.get()
            print('{0}号线程请求{1}'.format(self.number, base_url))
            # 发送请求,获取数据进行解析
            response = requests.get(base_url, headers=headers)
            data = response.text
            self.data_list.put(data)

class Data(threading.Thread):
    def __init__(self,number,data_list,req_thread,fp):
        #调用父类的初始化 , 放置被覆盖
        super(Data,self).__init__()
        self.number = number
        self.data_list = data_list
        self.req_thread =req_thread
        self.fp = fp
        self.is_parse = True  #判断是否从数据队列里提取到数据
    #当线程调用时执行函数
    def run(self):
        while True:
            for t in self.req_thread: #循环请求线程
                if t.is_alive(): #如果线程存活
                    break
            else: #如果请求线程都结束 判断解析队列是否还有数据
                if self.data_list.qsize() == 0:
                    self.is_parse = False

            #判断是否解析
            if self.is_parse: #如果解析队列中有数据就解析 , 没有就跳出循环
                try:
                    data = self.data_list.get(timeout=3)
                except Exception as e: #请求超时后进入异常
                    data = None
                if data is not None:
                    self.detail(data)
            else:
                break
        print('退出%d号解析线程' % self.number)
    def detail(self,data):
        html = json.loads(data)
        item = {}
        for info in html['postList']:
            print(info)
            item['发布时间'] = info['publishDate']
            item['公司岗位'] = info['name']
            item['职位要求'] = info['serviceCondition']
            item['工作地点'] = info['workPlace']
            item['职业类别'] = info['postType']
            if 'education' not in info:
                item['学历要求'] = '无'
            else:
                item['学历要求'] = info['education']
            self.fp.write(json.dumps(item, ensure_ascii=False) + '\n')
def main():
    req_list = queue.Queue()
    data_list = queue.Queue()
    # 创建一个文件
    fp = open('baidu.json', 'w+', encoding='utf-8')
    # 获取最大页数
    headers = {
        "Host": "talent.baidu.com",
        "Connection": "keep-alive",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded",
        "Referer": "http://talent.baidu.com/external/baidu/index.html",
        "Accept-Language": "zh-CN,zh;q=0.8",
    }
    page_url = 'http://talent.baidu.com/baidu/web/httpservice/getPostList?workPlace=0%2F4%2F7%2F9&recruitType=2&pageSize=10&curPage=1&keyWord=python&_=1510064326404'
    response = requests.get(page_url, headers=headers)
    html = response.text
    html = json.loads(html)
    totalPage = html['totalPage']
    print(totalPage)
    totalPage = int(totalPage) + 1

    for page in range(1,totalPage):
        base_url = 'http://talent.baidu.com/baidu/web/httpservice/getPostList?workPlace=0%2F4%2F7%2F9&recruitType=2&pageSize=10&curPage={0}&keyWord=python&_=1510060576359'.format(page)
        req_list.put(base_url)

    req_thread = []
    for i in range(3):
        t = Req(i,data_list,req_list)
        t.start()
        req_thread.append(t)

    data_thread = []
    for i in range(3):
        t = Data(i,data_list,req_thread,fp)
        t.start()
        data_thread.append(t)

    for t in req_thread:
        t.join()

    for t in data_thread:
        t.join()

    fp.close()

if __name__ == '__main__':
    main()
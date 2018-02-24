import requests
import json
import threading
from bs4 import BeautifulSoup
import time
import queue

#创建一个请求类
class Req(threading.Thread):
    def __init__(self,number,data_list,req_list,headers):
        #调用父类的初始化 ,放置被覆盖
        super(Req,self).__init__()
        self.number = number
        self.data_list = data_list
        self.req_list = req_list
        self.headers = headers
    #调用线程的时候启动
    def run(self):
        print('{0}号请求线程启动'.format(self.number))
        while self.req_list.qsize() > 0:
            #获取请求队列中的数据
            base_url = self.req_list.get()
            print('{0}号线程请求{1}'.format(self.number,base_url))
            #发送请求,获取数据进行解析
            response = requests.get(base_url,headers = self.headers)
            data = response.text
            data = BeautifulSoup(data, 'lxml')
            # print(type(html)) #这个html属于bs4.BeautifulSoup类
            # 进行数据筛选
            li_list = data.select('li.job_item')
            item = {}
            for lis in li_list:
                # print(type(lis))  #这个lis属于bs4.element.Tag类
                address = lis.select('span.address')[0].text
                name = lis.select('span.name')[0].text
                job_salary = lis.select('p.job_salary')[0].text
                company_name = lis.select('a.fl')[0].text
                # 选出a标签
                # 筛选工资不低于8000的招聘信息
                job_list = job_salary.split('-')
                # print(job_list)
                if job_list[0].isdigit():
                    if int(job_list[0]) >= 8000:
                        # print(job_salary)
                        href = lis.select('a')[0]['href']
                        # 将提取出来的数据放入字典中
                        item['adress'] = address
                        item['name'] = name
                        item['job_salary'] = job_salary
                        item['company_nam'] = company_name
                        item['href'] = href
                        #将数据放入解析队列中
                        self.data_list.put(item)
#定义一个解析类
class Data(threading.Thread):
    def __init__(self,number,data_list,req_thread,headers,fp):
        #调用父类的初始化 , 放置被覆盖
        super(Data,self).__init__()
        self.number = number
        self.data_list = data_list
        self.req_thread =req_thread
        self.headers = headers
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

    def detail(self,data):
        detail_url = data['href']
        # 提交请求获取HTML文件
        response = requests.get(detail_url, headers=self.headers)
        html = response.text
        # print(html)
        # 将文件转换成beautifulsoup类型
        html = BeautifulSoup(html, 'lxml')
        # 获取想要的数据
        detail_list = html.select('div.des')
        for details in detail_list:
            info = details.text
            data['info'] = info
            # print(data)
            self.fp.write(json.dumps(data, ensure_ascii=False) + '\n')






#定义一个主函数
def main():
    #请求头部
    headers = {
        "Host": "bj.58.com",
        "Connection": "keep-alive",
        "Cache-Control": "max-age=0",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
        "Upgrade-Insecure-Requests": "1",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Referer": "http://bj.58.com/job/pn2/?key=python&final=1&jump=1&PGTID=0d302408-0000-1a33-30be-1ff961d478f6&ClickID=3",
        "Accept-Language": "zh-CN,zh;q=0.8",
    }
    #创建一个请求数据队列
    req_list = queue.Queue()
    #创建一个解析数据队列
    data_list = queue.Queue()
    #创建一个文件
    fp = open('58.json','w+',encoding='utf-8')

    for i in range(1,3):
        base_url = 'http://bj.58.com/job/pn{0}/?key=python&final=1&jump=1&PGTID=0d302408-0000-14b7-edb7-f194792e9023&ClickID=3'.format(i)
        #将路由放入请求队列中
        req_list.put(base_url)

    req_thread = []
    #创建2个请求线程
    for i in range(2):
        t = Req(i,data_list,req_list,headers)
        t.start()
        req_thread.append(t)
    data_thread = []
    #创建4个解析线程
    for i in range(4):
        t = Data(i,data_list,req_thread,headers,fp)
        t.start()
        data_thread.append(t)

    #线程结束
    for t in req_thread:
        t.join()

    for t in data_thread:
        t.join()
    #关闭文件
    fp.close()

if __name__ == '__main__':
    main()

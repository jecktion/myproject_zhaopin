import requests
from bs4 import BeautifulSoup
import json,time
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
def base_main():
    #有页面可知共2页
    for i in range(1,3):
        base_url = 'http://bj.58.com/job/pn{0}/?key=python&final=1&jump=1&PGTID=0d302408-0000-14b7-edb7-f194792e9023&ClickID=3 '
        #构造请求对象 , 返回response对象
        print('获取第%d页内容'%i)
        response = requests.get(base_url.format(i),headers)
        print(base_url.format(i))
        html = response.text  #html属于字符串
        #将HTML文本转换成 bs4.BeautifulSoup
        html = BeautifulSoup(html,'lxml')
        # print(type(html)) #这个html属于bs4.BeautifulSoup类
        #进行数据筛选
        li_list = html.select('li.job_item')
        item = {}
        for lis in li_list:
            # print(type(lis))  #这个lis属于bs4.element.Tag类
            address = lis.select('span.address')[0].text
            name = lis.select('span.name')[0].text
            job_salary = lis.select('p.job_salary')[0].text
            company_name = lis.select('a.fl')[0].text
            # 选出a标签
            #筛选工资不低于8000的招聘信息
            job_list = job_salary.split('-')
            # print(job_list)
            if job_list[0].isdigit():
                if int(job_list[0]) >= 8000:
                    # print(job_salary)
                    href = lis.select('a')[0]['href']
                    #将提取出来的数据放入字典中
                    item['adress'] = address
                    item['name'] = name
                    item['job_salary'] = job_salary
                    item['company_nam'] = company_name
                    item['href'] = href
                    #到详情页面提取信息
                    detail(item)
#详情页面提取信息
def detail(item):
    time.sleep(0.5)
    detail_url = item['href']
    #提交请求获取HTML文件
    response = requests.get(detail_url,headers=headers)
    html = response.text
    # print(html)
    #将文件转换成beautifulsoup类型
    html = BeautifulSoup(html,'lxml')
    #获取想要的数据
    detail_list = html.select('div.des')
    with open('58.json','a+',encoding='utf-8') as fp:
        #遍历数据将内容存放在文档中
        for details in detail_list:
            info = details.text
            item['info'] = info
            print(item)
            fp.write(json.dumps(item,ensure_ascii=False)+'\n')



if __name__ == '__main__':
    base_main()
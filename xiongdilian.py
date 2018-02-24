import requests
from lxml import etree
import json
def stu():
    base_url = "http://www.itxdl.cn/activity/jiuyejianbao/"
    headers = {
        "Host": "www.itxdl.cn",
        "Connection": "keep-alive",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
        "Upgrade-Insecure-Requests": "1",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        # "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.8",
    }
    response = requests.get(base_url,headers=headers,verify=False)
    response.encoding = 'gbk'
    html = response.text
    # print(html)
    html = etree.HTML(html)
    data = html.xpath('//div[@class="w715 gaoxin_60 php_kecheng_neirong php_gaoxinjiuye mingxing_1600"]/li//text()')
    # print(data)
    l = 0
    lists = ['时间','姓名','学校','学历','公司','工资','城市']
    y=0
    item ={}
    with open('stu_info.json', 'w+',encoding= 'utf-8') as fp:
        for i in data:
            if l%7 == 0:
                print('\n')
                y = 0
            item[lists[y]] = i.replace('\t',' ')
            y +=1
            l+=1
            if l%7 == 0:
                print(item)
                fp.write(json.dumps(item,ensure_ascii= False) + '\n')
if __name__ == '__main__':
    stu()
import requests
from lxml import etree
import json

def getList():
    base_url = 'https://www.qiushibaike.com/8hr/page/%d/'
    with open('duanzi.json','w',encoding='utf-8') as f:
        for i in range(1,14):
            response = requests.get(base_url % i,verify = False)
            html = etree.HTML(response.text)

            #获取所有段子div
            duanzi_div = html.xpath('//div[@id="content-left"]/div')

            for duanzi in duanzi_div:
                # 获取昵称
                nick = duanzi.xpath('./div//h2/text()')[0]
                nick = nick.replace('\n','')
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
                    'nick' : nick,
                    'age' : age,
                    'gender' : gender,
                    'content' : content,
                    'good_num' : good_num,
                    'common_num' : common_num,
                }

                # 写入文件持久化
                f.write(json.dumps(item,ensure_ascii=False) + '\n')
                # 图片下载到相应目录


if __name__ == '__main__':
    getList()
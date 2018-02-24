import requests
from lxml import etree
import json
import time
def base_main(page_num):
    timetype = int(time.time()*1000)
    base_url = "https://xueqiu.com/stock/cata/stocklist.json?page=%d&size=30&order=desc&orderby=percent&type=11,12&_=%d"%(page_num,timetype)
    headers = {
        "Host": "xueqiu.com",
        "Connection": "keep-alive",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "cache-control": "no-cache",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
        "Referer": "https://xueqiu.com/hq",
        # "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.8",
        "Cookie": "aliyungf_tc=AQAAAN7/jQoAAAoAUhVFeQE9dKTwTCs7; xq_a_token=469ea9edce5537d5d8297aaffcd3474cc8d12273; xq_a_token.sig=8D0Nrw6wLkoY9wJS5_6N_eORSOY; xq_r_token=819ae94ba56378cc0665670983c2afafc34c275b; xq_r_token.sig=6N6ZkaHvfEfPz1FgHKEsoQ_rhaA; u=381509965652071; device_id=3f5d21c7ab7e6873f97f5d4a1d720107; s=eb12lxt1gk; __utmt=1; __utma=1.1235976321.1509965767.1509965767.1509965767.1; __utmb=1.9.10.1509965767; __utmc=1; __utmz=1.1509965767.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); Hm_lvt_1db88642e346389874251b5a1eded6e3=1509965653; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1509969154",
    }
    response = requests.get(base_url,headers=headers,verify=False)
    data = response.text
    # print(data)
    data = json.loads(data)
    for i in data['stocks']:
        # name名称,symbol股票代码,pettm市盈率 current当前价  percent涨跌幅 change涨跌额
        # amount成交额 marketcapital市值  volume成交量
        # 处理市值为字符串
        a = i['marketcapital']
        a = float(a)
        a = '{:.2f}'.format(a / 100000000)

        # 处理成交额
        b = i['amount']
        b = float(b)
        b = '{:.2f}'.format(b / 10000)

        # 处理成交额
        c = i['volume']
        c = float(c)
        c = '{:.2f}'.format(c / 10000)

        str = '股票代码(' + i['symbol'] + ')--名称(' + i['name'] + ')--当前价(' + i['current'] + ')--涨跌额(' + i[
            'change'] + ')--市值(' + a + '亿)--成交量(' + c + '万)--成交额(' + b + '万)' + '\n'
        with open('info.txt', 'a+', encoding='utf-8') as f:
            f.write(str)

if __name__ == '__main__':
    for page_num in range(1,182):
        print('正在获取第%d页数据'%page_num)
        base_main(page_num)

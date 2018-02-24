from urllib import request
import os,re,json

def base_main():
    base_url = 'http://www.66ip.cn/'
    headers = {
        # "Host": "www.66ip.cn",
        # "Connection": "keep-alive",
        # "Cache-Control": "max-age=0",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
        # "Upgrade-Insecure-Requests": "1",
        # "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        # "Referer": "http://www.66ip.cn/2.html",
        # # "Accept-Encoding": "gzip, deflate",
        # "Accept-Language": "zh-CN,zh;q=0.8",
    }
    start = input('输入起始页:')
    end = input('输入结束页:')
    for page in range(int(start),int(end)+1):
        if page == 1:
            base_url = base_url + 'index.html'
        else:
            base_url = 'http://www.66ip.cn/' + str(page) + '.html'
            # print(base_url)
        res = request.Request(base_url,headers=headers)
        response = request.urlopen(res)
        html = response.read().decode('gb2312')
        # print(res)
        ip_num(html)
def ip_num(html):
    ip_pattern = re.compile(r'<tr><td>(.*?)</td><td>(.*?)</td>')
    ip_list = ip_pattern.findall(html)[1:]
    ips = dict(ip_list)
    ips = json.dumps(ips,ensure_ascii=False,indent=4)
    with open('ipnum.text','a+') as fp:
        fp.write(ips)

if __name__ == '__main__':
    base_main()
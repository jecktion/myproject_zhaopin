from urllib import request,parse
import re,os
def getPage():
    start = input('请输入起始页:')
    end = input('请输入结束页:')
    for page in range(int(start),int(end)+1):
        base_url = 'http://www.xicidaili.com/nn/%d'
        fullurl = base_url % page
        headers = {
            "User-Agent": " Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36"
        }
        req = request.Request(fullurl,headers=headers)
        response = request.urlopen(req)
        html = response.read().decode('utf-8')
        #正则提取
        page_parttern = re.compile(r'<tr.*?>.*?</tr>',re.S)
        page_lists = page_parttern.findall(html)[1:]
        dir_name = 'ips/'
        if not os.path.exists(dir_name):
            os.makedirs('ips/')
        with open(dir_name + '第%d页' % page ,'w',encoding='utf-8') as f:
            for tr in page_lists:
                td_parttern = re.compile(r'<td>(.*?)</td>')
                td_lists = td_parttern.findall(tr)
                ip = td_lists[0]
                port = td_lists[1]
                f.write(ip + ":" + port +'\n')

if __name__ == '__main__':
    getPage()
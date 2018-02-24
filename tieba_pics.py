from urllib import request,parse
import re,os

# 计算出总页数 ， 输入 起始 和 结束

# 详情解析函数
def parse_pic(html):
    pic_pattern = re.compile(r'class="BDE_Image"\ssrc="(.*?)"')
    pic_urls = pic_pattern.findall(html)
    for url in pic_urls:
        print('dowloding...... %s' % url)
        req = request.Request(url,headers={})
        response = request.urlopen(req)
        content = response.read()
        fname = url.split('/')[-1]
        with open('./baidu/' + tieba_name + '/' + fname ,'wb') as f:
            f.write(content)

def parse_detail(html):
    detail_pattern = re.compile(r'href="(/p/\d+)"')
    detail_pages = detail_pattern.findall(html)
    for page in detail_pages:
        fullurl = 'https://tieba.baidu.com' + page
        response = request.urlopen(fullurl)
        html = response.read().decode('utf-8')
        parse_pic(html)

def getPage(tieba_name):
    base_url = 'https://tieba.baidu.com/f?'
    qs = {
        'kw' : tieba_name,
        'pn' : 0
    }
    qs = parse.urlencode(qs)

    first_url = base_url + qs
    response = request.urlopen(first_url)
    first_page = response.read().decode('utf-8')
    last_pattern = re.compile(r'(\d+)" class="last pagination-item ')
    res = last_pattern.search(first_page)
    if res is not None:
        total_page = res.group(1)
        # print(total_page)
    else:
        print('尾页获取失败')
        total_page = 10000

    page = int(total_page) / 50 + 1
    print('最大页数：%d' % page)
    start = input('输入起始页：')
    end = input('输入结束页：')
    for p in range(int(start), int(end) + 1):
        qs = {
            'kw' : tieba_name,
            'pn' : (p - 1) * 50
        }
        fullurl = base_url + parse.urlencode(qs)
        print(fullurl)
        response = request.urlopen(fullurl)
        html = response.read().decode('utf-8')
        parse_detail(html)

if __name__ == '__main__':
    tieba_name = input('输入贴吧名称：')
    dir_name = 'baidu/' + tieba_name
    if not os.path.exists(dir_name):
        os.makedirs('baidu/' + tieba_name)
    getPage(tieba_name)


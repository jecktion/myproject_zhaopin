import requests
from lxml import etree
from urllib import request
#获取登录页面
def login():
    base_url = 'https://accounts.douban.com/login?alias=&redir=https%3A%2F%2Fwww.douban.com%2F&source=index_nav&error=1001 '
    response = requests.get(url=base_url,verify=False)
    html = response.text
    # print(html)
    return html

#提交登录页面
def dologin(html):
    #获取验证码信息
    #将HTML格式转换成xpath格式
    base_url =' https://www.douban.com/accounts/login'

    html = etree.HTML(html)
    #下载图片
    img_url = html.xpath('//form//img[@id="captcha_image"]/@src')
    print(img_url)

    captcha_id = html.xpath('//form//div[@class="captcha_block"]//input[@type="hidden"]/@value')
    captcha_solution = input('请输入验证码:')
    data = {
        'form_email':'1752570559@qq.com',
        'form_password': '1234qwer',
        'source':'index_nav',
        'captcha-solution':captcha_solution,
        'captcha-id':captcha_id,
    }
    headers = {
        "Host": "www.douban.com",
        "Connection": "keep-alive",
        "Content-Length": "121",
        "Cache-Control": "max-age=0",
        "Origin": "https://www.douban.com",
        "Upgrade-Insecure-Requests": "1",
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Referer": "https://www.douban.com/",
        # "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.8",
    }
    response = requests.post(base_url,data=data,headers=headers,verify=False)
    html = response.text
    print(html)

if __name__ == '__main__':
    html = login()
    dologin(html)


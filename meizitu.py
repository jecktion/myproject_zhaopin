from urllib import request,parse
import os,re,myproxy,random,time

#搜索函数
user_agnets = [
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; TencentTraveler 4.0; .NET CLR 2.0.50727)',
]
#抓取列表页的数据
def base_main():

    headers = {
        "Host": "www.mzitu.com",
        "Proxy-Connection": "keep-alive",
        "Cache-Control": "max-age=0",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent":random.choice(user_agnets),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Referer": "http://www.mzitu.com/best/",
        # "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.8",

    }
    print('最热妹子图列表页共5页')
    start = input('开始页:')
    opener = myproxy.getOpener()
    if start == 1 :
        base_url = 'http://www.mzitu.com/hot/'
    else:
        base_url = 'http://www.mzitu.com/hot/' + 'page/' + str(start) + '/'
    #构造请求对象
    print('base_url')
    res = request.Request(base_url,headers=headers)
    data = myproxy.downloader(opener,res)
    # print(1)
    #列表页中每张图下面的链接
    if data != None:
        data = data.decode('utf-8')
        serial(data,start)

#列表页中每个图片下的数据
def serial(data,start):
    a_parttern = re.compile(r'<li>.*?<a href="http://www.mzitu.com/(\d+)".*?alt=\'(.*?)\'',re.S)
    a_list = a_parttern.findall(data)
    print('第%d页选择美女'%int(start))
    print(a_list)
    pages = {}
    for tuples in a_list:
        pages[tuples[0]] = tuples[1]
    serial_num = input('输入你看中的美女编号:')
    # url_serial = 'http://www.mzitu.com/'
    headers = {

        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        # "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.8",
        "Cache-Control": "max-age=0",
        "Host": "www.mzitu.com",
        "User-Agent":random.choice(user_agnets),

    }
    for i in range(1,52):
        time.sleep(0.5)
        opener = myproxy.getOpener()
        if i ==1:
            url_serial = 'http://www.mzitu.com/' + str(serial_num)
        else:
            url_serial = 'http://www.mzitu.com/' + str(serial_num)  +'/'+ str(i)
        print(url_serial)
        #构造请求对象
        res = request.Request(url_serial,headers=headers)
        html = myproxy.downloader(opener,res)
        # html = myproxy.downloader(opener,res)
        print(2)
        if html != None:
            html = html.decode('utf-8')
            img_pattern = re.compile(r'class="main-image"(.*?)src="(.*?)"')
            img = img_pattern.search(html)
            img = img.group(2)
            # print(img)
            print('正在下载......%s'%img)
            headers = {
                "Host": "i.meizitu.net",
                "Connection": "keep-alive",
                "User-Agent": random.choice(url_serial),
                "Accept": "image/webp,image/apng,image/*,*/*;q=0.8",
                "Referer": "http://www.mzitu.com/103328/2",
                # "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "zh-CN,zh;q=0.8",

            }
            #构造请求对象
            print(4)
            res = request.Request(img,headers=headers)

            data = myproxy.downloader(opener,res)
            print(3)
            if data != None:
                #创建目录
                fname = pages[serial_num][:4]
                # print(fname)
                tname = img.split('/')[-1]
                if not os.path.exists('img/'+fname):
                    os.makedirs('img/'+fname)
                with open('img/'+fname+'/'+tname,'wb') as fp:
                    fp.write(data)





if __name__ == '__main__':
    base_main()
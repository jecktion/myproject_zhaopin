from Mydb import Mydb
import requests

class ProxyManager(object):
    def __init__(self, mydb):
        self.mydb = mydb
        self.base_url = 'http://www.baidu.com'

    def drop_ip(self,host):
        print('删除代理：%s' % host)
        sql = 'delete from proxy where host="%s"' % host
        self.mydb.exe(sql)

    def filter_proxy(self):
        sql = 'select * from proxy'
        res = self.mydb.query(sql)
        for item in res:
            proxy = {
                'http' : '%s://%s:%s' % (item[2],item[0],item[1]),
                'https' : '%s://%s:%s' % (item[2],item[0],item[1])
            }
            try:
                response = requests.get(self.base_url,timeout=3,proxies=proxy)
                print(response.status_code)
            except Exception as e:
                # 从数据库中删除不可用代理
                self.drop_ip(item[0])
            else:
                if not (200 <= response.status_code <= 300):
                    self.drop_ip(item[0])


if __name__ == '__main__':
    mydb = Mydb('127.0.0.1', 'root', '123456', 'temp', charset='utf8')
    pm = ProxyManager(mydb)
    pm.filter_proxy()

from Mydb import Mydb
import requests
import threading
import queue

class ProxyManager(threading.Thread):
    def __init__(self, mydb,proxy_q,lock):
        super(ProxyManager, self).__init__()
        self.mydb = mydb
        self.base_url = 'http://www.baidu.com'
        self.proxy_q = proxy_q
        self.lock = lock

    def drop_ip(self,host):
        print('删除代理：%s' % host)
        sql = 'delete from proxy_gaoni where host="%s"' % host
        self.mydb.exe(sql)

    # 代理过滤
    def run(self):
        while self.proxy_q.qsize() > 0:
            # 从代理队列里取出一个代理信息
            item = self.proxy_q.get()
            proxy = {
                'http' : '%s://%s:%s' % (item[2],item[0],item[1]),
                'https' : '%s://%s:%s' % (item[2],item[0],item[1])
            }
            try:
                # 尝试发起请求
                response = requests.get(self.base_url,timeout=6,proxies=proxy)
                print(response.status_code)
            except Exception as e:
                # 从数据库中删除不可用代理
                self.lock.acquire() # 上锁
                self.drop_ip(item[0])
                self.lock.release() # 开锁
            else:
                # 如果状态码不是200到300 也从数据库中删除
                if not (200 <= response.status_code <= 300):
                    self.lock.acquire() # 上锁
                    self.drop_ip(item[0])
                    self.lock.release() # 开锁

# 获取代理队列
def get_proxy():
    proxy_q = queue.Queue()
    sql = 'select * from proxy_gaoni'
    res = mydb.query(sql)
    for item in res:
        proxy_q.put(item)
    return proxy_q

if __name__ == '__main__':
    mydb = Mydb('127.0.0.1','root','123456','temp',charset='utf8')
    lock = threading.Lock()

    proxy_q = get_proxy()
    # 初始化线程
    pm_list = []
    for i in range(2):
        pm = ProxyManager(mydb, proxy_q,lock)
        pm.start()
        pm_list.append(pm)

    for pm in pm_list:
        pm.join()

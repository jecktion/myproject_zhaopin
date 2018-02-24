import pymysql

# 数据库操作类
class Mydb:
    def __init__(self,host,user,password,db,charset='utf8'):
        try:
            self.conn = pymysql.connect(host,user,password,db,charset='utf8')
            self.cursor = self.conn.cursor()
        except Exception as e:
            print('连接失败：%s' % str(e))

    # 增删改
    def exe(self,sql):
        try:
            rows = self.cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            # self.conn.rollback()
            print('语句增删改执行失败:%s'% str(e))
            print(sql)
            rows = None

        return rows

    # 查询方法
    def query(self,sql):
        try:
            self.cursor.execute(sql)
            res = self.cursor.fetchall()
        except Exception as e:
            print('执行查询语句失败：%s' % str(e))
            print(sql)
            res = None
        return res

    # 关闭数据库方法
    def close(self):
        self.cursor.close()
        self.conn.close()




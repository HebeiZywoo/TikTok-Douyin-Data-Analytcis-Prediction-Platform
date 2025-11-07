import pymysql
from config import Config


# 建立数据库连接
def conn():
    con = pymysql.connect(host=Config.DB_HOST, port=Config.DB_PORT,
                          user=Config.DB_USER, password=Config.DB_PASSWORD, db=Config.DB_NAME)
    cur = con.cursor()
    return con, cur


# 关闭
def close():
    con, cur = conn()
    cur.close()
    con.close()


# 查询
def query(sql):
    con, cur = conn()
    cur.execute(sql)
    res = cur.fetchall()
    close()
    return res


# 插入、更新、删除
def insert(sql):
    con, cur = conn()
    cur.execute(sql)
    con.commit()
    close()

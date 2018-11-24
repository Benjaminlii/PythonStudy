"""
    pymysql数据库处理模块
    建了50个8*8的表格 有点醉
    2018.11.24
    author：Benjamin
"""
import pymysql

# 连接到数据库
db = pymysql.connect(host="localhost",
                     user="root",
                     password="litao.",
                     db="text",
                     port=3306)
# 游标 相当与输入
cur = db.cursor()
for i in range(50):
    # 先编辑MySQL语句
    sql = """create table table%d(
                n varchar(10),
                a1 varchar(10),
                a2 varchar(10),
                a3 varchar(10),
                a4 varchar(10),
                a5 varchar(10),
                a6 varchar(10),
                a7 varchar(10),
                a8 varchar(10)
            );""" % i
    # 执行语句，下同
    cur.execute(sql)
    sql = """insert into table%d(n, a1, a2, a3, a4, a5, a6, a7, a8) values (null, "A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8");""" % i
    cur.execute(sql)
    for j in range(1, 9):
        sql = """insert into table%d(n, a1, a2, a3, a4, a5, a6, a7, a8) values (\"%s\", "s", "s", "s", "s", "s", "s", "s", "s");""" % (i, "A"+str(j))
        cur.execute(sql)
    # 删除50张表
    # sql = "drop table if exists table%d;" % i
    # cur.execute(sql)
db.close()


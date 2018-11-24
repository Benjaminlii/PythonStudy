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
                n varchar(2),
                A1 varchar(2),
                A2 varchar(2),
                A3 varchar(2),
                A4 varchar(2),
                A5 varchar(2),
                A6 varchar(2),
                A7 varchar(2),
                A8 varchar(2)
            );""" % i
    # 执行语句，下同
    cur.execute(sql)
    # print(sql)
    for j in range(1, 9):
        sql = """insert into table%d(n, a1, a2, a3, a4, a5, a6, a7, a8) values (\"%s\", "s", "s", "s", "s", "s", "s", "s", "s");""" % (i, "A"+str(j))
        # print(sql)
        cur.execute(sql)
db.close()


"""
    读取MySQL中的表的信息
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
sql = "select * from table0;"
cur.execute(sql)
result = cur.fetchall()
print(result)

db.close()

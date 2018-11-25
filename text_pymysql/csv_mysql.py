"""
    csv文件与MySQL数据库的存储和读取
    这个模块的函数需要特定的数据库表的结构
    在database_init.py中，我写了初始化数据库的函数，调用即可

    csv_to_mysql(csv_name, username, password, database_name, port)
    参数：csv_name:要进行存储的csv文件名，要带.csv后缀
          username:数据库用户名
          password:数据库密码
          database_name:要存储的库名，这里需要与database_init.py所创建的库一致
          port:端口号
    功能：将csv_name这个csv文件中的内容保存在MySQL数据库中
    返回值：void

    mysql_to_csv(csv_name, username, password, database_name, port)
    参数：csv_name:生成的.csv文件名，要带后缀
          username:数据库用户名
          password:数据库密码
          database_name:要读取的库名，同上
          port:端口号
    功能：将MySQL数据库中database_name库的与csv_name相应的表中的内容读取出来，存入.csv文件
    返回值：void
    
"""
import pymysql
import pandas as pd
import numpy as np


def csv_to_mysql(csv_name, username, password, database_name, port):
    table_name = csv_name.split('.')[0] + "_"
    db = pymysql.connect(host="localhost",
                         user=username,
                         password=password,
                         db=database_name,
                         port=port,
                         autocommit=True)
    # 游标 相当与输入
    cur = db.cursor()
    data = np.array(pd.read_csv(csv_name))
    for row in data:
        sql = "insert into %s values (%s" % (table_name, str(row[0]))
        for col in row[1:]:
            sql += ", " + str(col)
        sql += ");"
        print(sql)
        cur.execute(sql)
    db.close()


def mysql_to_csv(csv_name, username, password, database_name, port):
    table_name = csv_name.split('.')[0] + "_"
    db = pymysql.connect(host="localhost",
                         user=username,
                         password=password,
                         db=database_name,
                         port=port,
                         autocommit=True)
    # 游标 相当与输入
    cur = db.cursor()
    cur.execute("select * from %s;" % table_name)
    data = pd.DataFrame(np.array(cur.fetchall()))
    data.to_csv(csv_name, index=False)
    db.close()


if __name__ == '__main__':
    # csv_to_mysql("report.csv", "root", "litao.", "database_0", 3306)
    # mysql_to_csv("report.csv", "root", "litao.", "database_0", 3306)
    # csv = np.array(pd.read_csv("report.csv"))
    print(1)

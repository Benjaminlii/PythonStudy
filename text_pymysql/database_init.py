"""
    数据库的初始化创建
    database_init(username, password, database_name, port)
    参数：username：MySQL用户名
          password：MySQL用户密码
          database_name：要创建的库名
          port：端口号
    功能：创建一个库，三张表
    返回值：void

    author:Benjamin
"""
import pymysql


def database_init(username, password, database_name, port):
    db = pymysql.connect(host="localhost",
                         user=username,
                         password=password,
                         port=port,
                         autocommit=True)
    cur = db.cursor()
    cur.execute("drop database if exists %s;" % database_name)
    # 调用函数
    create_database(database_name, cur)
    # 更改默认库
    cur.execute("use " + database_name + ";")
    creat_tables(cur)
    db.close()


def create_database(database_name, cur):
    cur.execute("create database " + database_name + ";")


def creat_tables(cur):
    cur.execute("""create table weight_(
                W0 float,
                W1 float,
                W2 float,
                W3 float,
                W5 float,
                W6 float,
                W7 float,
                W8 float,
                W9 float,
                W10 float,
                W11 float,
                W12 float,
                W13 float,
                W14 float
            );""")
    cur.execute("""create table index_(
                A1 float,
                A2 float,
                A3 float,
                A4 float,
                A5 float,
                A6 float,
                A7 float,
                A8 float,
                A9 float,
                A10 float,
                A11 float,
                A12 float,
                A13 float,
                A14 float
            );""")
    cur.execute("""create table report_(
                R0 float,
                R1 float,
                R2 float,
                R3 float,
                R4 float,
                R5 float,
                R6 float,
                R7 float,
                R8 float,
                R9 float,
                R10 float,
                R11 float,
                R12 float,
                R13 float,
                R14 float
            );""")


if __name__ == "__main__":
    database_init("root", "litao.", "database_0", 3306)

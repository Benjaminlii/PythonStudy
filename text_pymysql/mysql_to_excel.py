"""
    mysql_to_excel(username, password, database_name, port, num)
    参数：username：数据库用户名
          password：数据库用户密码
          database_name：要存入的库的名称
          port：数据库端口
          num：要存的表的数目
    功能：将数据库相应库的num张表存入excel中，保存到当前文件夹
    返回值：void

    这里数据库中的表的名称我默认设置为table+n
"""
import pymysql
import xlwt


def mysql_to_excel(username, password, database_name, port, num):
    # 创建工作簿,设置编码
    one_excel = xlwt.Workbook(encoding='utf-8')
    # 连接到数据库
    db = pymysql.connect(host="localhost",
                         user=username,
                         password=password,
                         db=database_name,
                         port=port)
    # 游标 相当与输入
    cur = db.cursor()
    for i in range(num):
        write_one_table(one_excel, "table%d" % i, cur)
    one_excel.save("50table.xls")
    db.close()


def write_one_table(excel_name, table_name, cur):
    one_sheet = excel_name.add_sheet(table_name)
    sql = "select * from %s;" % table_name
    cur.execute(sql)
    result = cur.fetchall()
    row = 0
    for i in result:
        for col in range(len(i)):
            one_sheet.write(row, col, i[col])
        row += 1


# mysql_to_excel("root", "xxxxxxx", "text", 3306, 50)


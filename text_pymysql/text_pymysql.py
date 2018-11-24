import pymysql

db = pymysql.connect(host="localhost",
                     user="root",
                     password="litao.",
                     db="text",
                     port=3306)
cur = db.cursor()
sql = """creat table """
cur.execute(sql)
results = cur.fetchall()
for i in results:
    print(i)
db.close()


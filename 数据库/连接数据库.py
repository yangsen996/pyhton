import pymysql
#创建连接
conn = pymysql.connect(host='localhost',
                       port=3306,
                       user='root',
                       password='root',
                       database='tpshop2.0',
                       autocommit = True)
#获取游标
cursor = conn.cursor()
#执行sql
cursor.execute("select version()")
result = cursor.fetchall()
print(result)
#查寻结果记录行数
cursor.rowcount
#获取结果第一条数据
cursor.fetchone()
#获取全部结果
cursor.fetchall()
#关闭游标
cursor.close()
#关闭连接
conn.close()

sql = ""
#插入操作
cursor.execute(sql)

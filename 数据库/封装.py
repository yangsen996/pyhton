import pymysql
#创建工具类
class DBUtil():
    __conn = None
    __cursor = None
    #创建连接
    @classmethod
    def __get_conn(cls):
        if cls.__conn is None:
            cls.__conn = pymysql.connect(host = "localhost",
                                         port = "3306",
                                         user = "root",
                                         password = "root",
                                         database = "数据库")
        return cls.__conn
    #创建游标
    @classmethod
    def __get_cursor(cls):
        if cls.__cursor is None:
            cls.__cursor = cls.__get_conn().cursor()
        return cls.__cursor
    #执行sql
    @classmethod
    def exe_sql(cls,sql):
        try:
            #获取游标对象调用execute执行sql
            cursor = cls.__get_cursor()
            cursor.execute(sql)
            #如果是查询，返回所有数据时
            if sql.split()[0].lower() == 'select':
                return cursor.fetchall()
            #不是，提交事务返回受影响的行数
            else:
                cls.__conn.commit()
                return cursor.rowcount
        except Exception as e:
            cls.__conn.rollback()
            print(e)
        finally:
            #关闭游标
            cls.__close_cursor()
            cls.__close_conn()
    #关闭游标
    @classmethod
    def __close_cursor(cls):
        if cls.__cursor:
            cls.__cursor.close()
            cls.__cursor = None
    #关闭连接
    @classmethod
    def __close_conn(cls):
        if cls.__conn:
            cls.__conn.close()
            cls.__conn = None

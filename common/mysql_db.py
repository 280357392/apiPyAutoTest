import pymysql

"""
# 获取一个查询结果，返回元组：
one_row = cur.fetchone()
print(one_row)  # (11, '107班')

# 获取多个查询结果，返回二维元组。
# 注意：one_row获取了第一个，这里是接着获取。也就是获取第2和第3个。
many_row = cur.fetchmany(2)  # 指定获取2个
print(many_row)  # ((12, '108班'), (13, '109班'))

# 获取所有查询结果，返回二维元组。
# 注意：这里是接着获取。也就是排除了以上获取的记录。
all_row = cur.fetchall()
print(all_row)  # ((14, '110班'),)
"""


class MysqlDB:
    def __init__(self):
        # 创建连接（需测试连接失败的情况）
        self.__db = pymysql.connect(host='114.132.123.-snip-',
                                    port=3306,
                                    user='-snip-',
                                    password='-snip-.',
                                    database='mydb',
                                    charset='utf8mb4'
                                    )
        # 创建游标（操作数据库用）
        self.__cur = self.__db.cursor()

    def cud(self, sql):
        """
            增删改
        :param sql: 增删改语句。
        :return: 操作成功返回True
        """
        try:
            # 执行SQL语句
            # sql = "select * from class;"
            self.__cur.execute(sql)  # 不会直接返回结果，通过cur获取结果。
            # 一般执行完SQL需要提交，但只有写操作（新增、修改、删除）才需要提交。
            # 多次写，只提交一次也可以。
            self.__db.commit()
            return True
        except Exception as e:
            self.__db.rollback()  # 退回执行之前的状态。
            print(e)
            return False

    def retrieve(self, sql, args=None):
        """
        数据库查询。

        :param sql: 查询语句
        :param args: 条件列表[]
        :return: 一维元组
        """
        # sql = "select classid,name from student where classid = %s;"
        self.__cur.execute(sql, args)  # 只能给values或条件等传值，不能给表名传值。
        return self.__cur.fetchone()

    def close_db(self):
        # 关闭数据库
        self.__cur.close()
        self.__db.close()


if __name__ == '__main__':
    db = MysqlDB()
    sql = "select classid,name from student where classid = %s;"
    data = db.retrieve(sql, [13])
    db.close_db()
    if data:
        print(data)
        print(data[0])
        print(data[1])
    else:
        assert False, '数据库未查询到相关数据。'

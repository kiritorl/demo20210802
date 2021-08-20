import pymysql

# 建立数据库连接
connection = None
try:
    connection = pymysql.connect(host="127.0.0.1", user="root", password="ruxiao342126",
                                 database="db_bupt", charset="utf8")
    # 创建cursor
    cursor = connection.cursor()
    # 执行SQL语句
    sql = "select * from t_user"
    count = cursor.execute(sql)   # execute会返回条数
    result = cursor.fetchall()    # 结果集
    print(count)
    print(result)
except Exception as e:
    print(e)
finally:
    if connection is not None:
        connection.close()
    pass

try:
    connection = pymysql.connect(host="127.0.0.1", user="root", password="ruxiao342126", port=3306,
                                 database="db_bupt", charset="utf8")
    # 创建cursor
    cursor = connection.cursor()
    # 执行SQL语句
    sql = "update t_user set age=30 where id=1"
    count = cursor.execute(sql)   # execute会返回条数
    connection.commit()
    print(count)
except Exception as e:
    print(e)
finally:
    if connection is not None:
        connection.close()
    pass

# 封装数据库底层操作



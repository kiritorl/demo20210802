import pymysql
import json


class BaseDao():

    def __init__(self, config="mysql.json"):
        self.__params = json.load(open(config, "r", encoding="utf-8"))
        self.__connection = None
        self.__cursor = None
        pass

    def getConnection(self):
        if self.__connection is not None:
            return self.__connection
            pass
        try:
            self.__connection = pymysql.connect(**self.__params)
        except pymysql.DatabaseError as e:
            print(e)
        return self.__connection
        pass

    def execute(self, sql, params=None, ctype="tuple"):
        result = 0
        try:
            self.__connection = self.getConnection()
            if ctype == "dict":
                self.__cursor = self.__connection.cursor(pymysql.cursors.DictCursor)
            else:
                self.__cursor = self.__connection.cursor()
                pass
            result = self.__cursor.execute(sql, params)
        except:
            pass
        return result
        pass

    def fetchOne(self):
        if self.__cursor is not None:
            return self.__cursor.fetchone()
        pass

    def fetchAll(self):
        if self.__cursor is not None:
            return self.__cursor.fetchall()
        pass

    def commit(self):
        if self.__connection is not None:
            self.__connection.commit()
        pass

    def rollback(self):
        if self.__connection is not None:
            self.__connection.rollback()
        pass

    def close(self):
        if self.__connection is not None:
            self.__connection.close()
        pass
        if self.__cursor is not None:
            self.__cursor.close()
        pass

    pass


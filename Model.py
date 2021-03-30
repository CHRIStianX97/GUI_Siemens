import sys
import pymssql
import os
# import pandas as pd
# import pprint as pp
# import numpy as np


class Model():
    def __init__(self, server, user, pwd, db):
        self.server = server
        self.user = user
        self.pwd = pwd
        self.db = db

    def execute_sql(self, sql):
        """
        执行查询语句
        返回的是一个包含tuple的list，list的元素是记录行，tuple的元素是每行记录的字段

        """
        cur = self.db_connect()
        cur.execute(sql)
        resList = cur.fetchall()
        return resList

    def db_connect(self):
        if not self.db:
            raise Exception(NameError, "没有设置数据库信息")
        self.conn = pymssql.connect(self.server, user=self.user, password=self.pwd, database=self.db, charset="gbk")
        # , charset="utf8"
        cur = self.conn.cursor()
        if not cur:
            raise Exception(NameError, "连接数据库失败")
        else:
            return cur

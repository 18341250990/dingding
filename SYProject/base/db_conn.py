# -*- coding: utf-8 -*-
"""
@Description :
@File        : login.py
@Project     : SYProject
@Time        : 2021/5/21 上午10:37
@Author      : dj
@Software    : PyCharm
"""

import pymysql
from base.config import Config
from base.my_logger import Logger
import pandas as pd


class DataBaseConn:
    def __init__(self):
        self.log = Logger('all')
        config = Config(log=self.log,file_name='database.config').config
        self.conn = pymysql.connect(host=config['ADDRESS'],
                                    port=int(config['PORT']),
                                    user=config['USER'],
                                    passwd=config['PASSWORD'],
                                    db=config['DBNAME'],
                                    charset="utf8")

    def exec(self, sql):
        cursor = self.conn.cursor()
        try:
            cursor.execute(sql)
            data = cursor.fetchall()
            return data
        except Exception as e:
            # 如果发生错误则回滚
            self.conn.rollback()
        finally:
            cursor.close()
            self.conn.close()

if __name__ == '__main__':

    sq = 'SELECT * from warehouse_task limit 100'
    db = DataBaseConn()
    df = pd.read_sql(con=db.conn,sql=sq,)
    pd.set_option('display.expand_frame_repr', False)
    aa = pd.DataFrame(df)
    print(aa.loc[0:3])
# coding = utf-8

# @time    : 2019/4/4 11:52 AM
# @author  : alchemistlee
# @fileName: mysql_utility.py
# @abstract:

import time
import pymysql

from config import gen_config
# SQL_GET_ALL_DATA='select id,ent_keys,ent_val,type from en_zh_ent where is_delete=0;'
# SQL_GET_MAX_UPDATE='select update_time from en_zh_ent order by update_time desc limit 1;'

config = gen_config()

HOST = config.MYSQL_HOST
USER = config.MYSQL_USER
PSWD = config.MYSQL_PASSWORD
DB_NAME = config.MYSQL_DATABASE


class MysqlUtil(object):

    def __init__(self, sql_get_all, sql_get_max):
        self._db = pymysql.connect(HOST, USER, PSWD, DB_NAME, charset='utf8')
        self._cursor = self._db.cursor()
        self._sql_get_all_data = sql_get_all
        self._sql_get_max_update = sql_get_max

    def __del__(self):
        self._db.close()

    def get_data(self, sql):
        try:
            self._cursor.execute(sql)
            results = self._cursor.fetchall()
            return results
        except:
            print("Error: unable to fetch data")
        return None

    def get_max_update(self):
        tmp = self.get_data(self._sql_get_max_update)
        res = int(time.mktime(tmp[0][0].timetuple()))
        return res

    def get_all(self):
        return self.get_data(self._sql_get_all_data)


if __name__ == '__main__':
    m = MysqlUtil()
    a = m.get_max_update()
    print(a)
    # b = time.strptime(a[0], "%Y-%m-%d %H:%M:%S")
    # print(int(time.mktime(a[0][0].timetuple())))

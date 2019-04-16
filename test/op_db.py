# coding = utf-8

# @time    : 2019/4/10 5:24 PM
# @author  : alchemistlee
# @fileName: op_db.py
# @abstract:


from util.mysql_utility import *
import config
from util.str_utility import *


class MysqlExtend(MysqlUtil):
  def __init__(self,sql_get_all,sql_get_max,sql_del_by_id):
    super(MysqlExtend,self).__init__(sql_get_all,sql_get_max)
    self._sql_del_by_id = sql_del_by_id

  def __del__(self):
    super(MysqlExtend,self).__del__()

  def del_by_id(self,ids):
    try:
      i =0
      for item_id in ids:
        tmp_sql= self._sql_del_by_id % item_id
        self._cursor.execute(tmp_sql)
        if i % 100 == 0:
          print('batch commit delete ...')
          self._db.commit()
        i+=1
    except:
      # 发生错误时回滚
      self._db.rollback()


def produce_key(input_item):
  ent_key = input_item[1]
  ent_val = input_item[2]
  res = '%s_%s' % (ent_key,ent_val)
  return res


def rm_dup(sql_all,sql_max,sql_del):
  my_db = MysqlExtend(sql_all,sql_max,sql_del)
  all_data  = my_db.get_all()
  global_data = dict()
  rm_ids = list()
  for item in all_data:
    uni_key = produce_key(item)
    tmp_id = item[0]
    if not uni_key in global_data.keys():
      global_data[uni_key]= tmp_id
    else:
      rm_ids.append(tmp_id)

  my_db.del_by_id(rm_ids)


def rm_all_en_in_zh(sql_all=None,sql_max=None,sql_del=None):
  my_db = MysqlExtend(sql_all,sql_max,sql_del)
  all_data = my_db.get_all()
  rm_ids = list()

  for item in all_data:
    tmp_id = item[0]
    tmp_key = item[1]
    if is_all_en(tmp_key):
      rm_ids.append(tmp_id)

  my_db.del_by_id(rm_ids)



if __name__ == '__main__':
  # print('rm en2zh dup !')
  # rm_dup(config.EN2ZH_GET_ALL,config.EN2ZH_GET_MAX,config.EN2ZH_DEL)
  # exit()

  # print('rm zh2en dup !')
  # rm_dup(config.ZH2EN_GET_ALL,config.ZH2EN_GET_MAX,config.ZH2EN_DEL)

  sql_1 = 'select id,ent_keys,ent_val,type,is_replace from zh_en_ent where is_delete=2 and type = 0;'
  rm_all_en_in_zh(sql_all=sql_1,sql_del=config.ZH2EN_DEL)
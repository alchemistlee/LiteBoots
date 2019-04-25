# coding = utf-8

# @time    : 2019/4/1 5:55 PM
# @author  : alchemistlee
# @fileName: pre_post_mapper.py
# @abstract:

import threading
from util.sliding_utility import *

from util.mysql_utility import *

import util.my_logger as log

import config
from util.str_utility import *

class PrePostMapper(object):

  def __init__(self,mysql_obj,name=None,path=None,tpl=None):
    self.path = path
    self._key2id = dict()
    self._keys = list()
    self._vals = list()
    self._pre_key2id = dict()
    self._pre_replace_str_key2id = dict()
    self.replace_tpl = tpl

    self._name=name

    self.mysql_util=mysql_obj
    self.load_data_db()
    self._my_ts=self._get_timestamp()

    t1= threading.Thread(target=self._thread_update)
    t1.start()

  def _get_timestamp(self):
    res = self.mysql_util.get_max_update()
    return res

  def _is_update(self):
    new_ts = self._get_timestamp()
    if new_ts > self._my_ts:
      return True
    return False

  def _thread_update(self):
    while True:
      time.sleep(60)
      if self._is_update():
        log.logger.info('%s begin to update it ... ' % self._name)
        self.load_data_db()
        self._my_ts = self._get_timestamp()
      else:
        log.logger.info('%s no need update ...' % self._name)

  def load_data_db(self):
    tmp_vals = list()
    tmp_keys = list()
    tmp_key2id = dict()
    #提前做替换后，再走翻译
    tmp_pre_key2id= dict()
    tmp_pre_replace_str_key2id = dict()

    log.logger.info('%s go to get_all ... ' % self._name)
    db_data = self.mysql_util.get_all()
    log.logger.info('%s db_data size = %s ' % (self._name,str(len(db_data))))
    index=0
    for item in db_data:
      ori_en_str = item[1].strip()
      ori_zh_str = item[2].strip()
      type = int(item[3])
      if item[4] is None:
        is_replace = 0
      else:
        is_replace = int(item[4])

      tmp_en_lst = ori_en_str.split(';')
      # sort as str size
      if len(tmp_en_lst) > 1:
        tmp_en_lst.sort(key=lambda x: len(x), reverse=True)

      # self._zh_vals.append(ori_zh_str)
      tmp_vals.append(ori_zh_str)
      # self._en_keys.append(tmp_en_lst)
      tmp_keys.append(tmp_en_lst)


      for en_key in tmp_en_lst:
        if en_key.strip() != '':
          # self._en_key2id[en_key]=index
          en_key= en_key.strip()

          if is_replace == 1:
            tmp_pre_replace_str_key2id[en_key]=index

          if type ==3:
            tmp_pre_key2id[en_key]=index
          else:
            lower_en_key = en_key.lower()
            tmp_key2id[lower_en_key] = index
      index += 1
    self._vals = tmp_vals
    self._keys = tmp_keys
    self._key2id = tmp_key2id
    self._pre_key2id = tmp_pre_key2id
    self._pre_replace_str_key2id = tmp_pre_replace_str_key2id

  def load_data(self):
    tmp_vals=list()
    tmp_keys=list()
    tmp_key2id=dict()

    index =0
    for line in open(self.path):
      tmp_list=line.strip().split('\t')

      if len(tmp_list)!=2:
        print(tmp_list)
        continue

      ori_en_str = tmp_list[0].strip()
      ori_zh_str = tmp_list[1].strip()

      tmp_en_lst = ori_en_str.split(';')
      # sort as str size
      if len(tmp_en_lst)>1:
        tmp_en_lst.sort(key=lambda x : len(x),reverse=True)

      # self._zh_vals.append(ori_zh_str)
      tmp_vals.append(ori_zh_str)
      # self._en_keys.append(tmp_en_lst)
      tmp_keys.append(tmp_en_lst)

      for en_key in tmp_en_lst:
        if en_key.strip()!='':
          # self._en_key2id[en_key]=index
          tmp_key2id[en_key]=index
      index+=1
    self._vals=tmp_vals
    self._keys=tmp_keys
    self._key2id=tmp_key2id

  def get_mapped_val(self,input_key):
    if input_key in self._key2id.keys():
      return self._vals[self._key2id[input_key]]
    return None

  def pre_replace(self,input_str):
    post_replace_dict = dict()
    replaced_index =0
    for tmp_keys in self._keys:
      replaced_str = self.replace_tpl % str(replaced_index)
      is_replaced = False
      for i in range(0,len(tmp_keys)):
        item_key = tmp_keys[i]
        if item_key in input_str:
          if not replaced_str in post_replace_dict.keys():
            item_mapping_val = self.get_mapped_val(item_key)
            post_replace_dict[replaced_str]=item_mapping_val

          is_replaced =True
          input_str=input_str.replace(item_key,replaced_str)
      if is_replaced:
        replaced_index+=1

    return input_str,post_replace_dict

  def _compatible_enkey(self,origin_str):
    res = origin_str.lower()
    if len(res)<=2:
      return res
    if res[-1] == 's' and res[-2] == "'":
      res = res[0:-2]
    return res

  def _pre_rep(self,input_str,is_enzh=True):
    res = input_str
    for item in self._pre_replace_str_key2id.keys():
      if item in res :
        rep_val = self._vals[self._pre_replace_str_key2id[item]]
        if is_enzh:
          rep_val = ' %s ' % rep_val
        res=res.replace(item ,rep_val )
    return res

  def _pre_proc(self,input_str):
    input_token = list(jieba.cut(input_str))
    matched = list()

    for sub_window_size in range(1,9):
      tmp_sliding = sliding_it(input_token,sub_window_size)
      for item in tmp_sliding:
        k1 = item[0]
        if k1 in self._pre_key2id.keys():
          new_item = (item[0],item[1],item[2],k1)
          matched.append(new_item)

    no_dup = filter_overlap(matched)

    for item in no_dup:
      tmp_id = self._pre_key2id[item[3]]
      tmp_val = self._vals[tmp_id]
      replaced_str = tmp_val
      input_token=self._rep_in_lst(input_token,item[1],item[2],replaced_str)

    res_str=''.join(input_token)

    return res_str

  def _batch_sliding(self,input_str,input_token=None):
    if input_token is None:
      input_token=list(jieba.cut(input_str))
    print(input_token)
    matched = list()
    for sub_window_size in range(1,9):
      tmp_sliding = sliding_it(input_token,sub_window_size)
      for item in tmp_sliding:
        k1 = self._compatible_enkey(item[0])
        # k2 =item[0]
        if k1 in self._key2id.keys():
          new_item = (item[0],item[1],item[2],k1)
          matched.append(new_item)
        # elif k2 in self._en_key2id.keys():
        #   new_item = (item[0], item[1], item[2], k2)
        #   matched.append(new_item)

    res = filter_overlap(matched)

    return res,input_token

  def _rep_in_lst(self,input_lst,rep_beg,rep_end,rep_val):
    input_lst[rep_beg]=rep_val
    for i in range(rep_beg+1,rep_end+1):
      input_lst[i] = ''
    return input_lst

  def pre_replace_v2(self,input_str,is_enzh=False):
    post_replace_dict = dict()
    replaced_index =2

    input_str = self._pre_rep(input_str,is_enzh)

    pre_proc_str = self._pre_proc(input_str)

    log.logger.info('pre proc = %s ' % pre_proc_str)

    matched,input_token = self._batch_sliding(pre_proc_str)

    for item in matched:
      tmp_val = self.get_mapped_val(item[3])
      replaced_str = self.replace_tpl % str(replaced_index)

      input_token=self._rep_in_lst(input_token,item[1],item[2],replaced_str)

      post_replace_dict[replaced_str]=tmp_val
      replaced_index+=1

    res_str=''.join(input_token)

    return res_str,post_replace_dict

  def post_replace(self,input_str,post_rep_dict,is_zhen=False):
    is_all_right = True
    ret_str = input_str

    if not is_zhen:
      # 处理返回的中文
      ret_str = rm_redundant_space_in_str(ret_str)

    for item_rep_key in post_rep_dict.keys():
      if not item_rep_key in ret_str:
        is_all_right= False
        break
      item_map_val = post_rep_dict[item_rep_key]

      if is_zhen:
        item_map_val = ' %s ' % item_map_val

      ret_str = ret_str.replace(item_rep_key,item_map_val)

    return is_all_right,ret_str


if __name__=='__main__':
  # a = PrePostMapper(MysqlUtil(config.ZH2EN_GET_ALL,config.ZH2EN_GET_MAX),name='test',tpl='<%s>')
  a = PrePostMapper(MysqlUtil(config.EN2ZH_GET_ALL,config.EN2ZH_GET_MAX),name='test',tpl='<%s>')

  t1='Hans Tungbegan his career as an investment banker at Merrill Lynch. He joined GGV in 2013 from Qiming Venture Partners, where he had focused on investments in China and co-led a Series A investment in Xiaomi. Prior to that, he was with Bessemer Venture Partners, where he helped companies like Skype expand into China.'

  t2='Huazhu Group Limited (HTHT) Q4 2018 Earnings Conference Call Transcript'

  t3='PDD is bad'

  t4='虎博科技准备上市'

  t5 = "eden hazard's incredible goal against West Ham left Chelsea fans delighted yet devastated as he nears a 100 million move to Real Madrid "

  t6="eden hazard's incredible goal against West Ham ,We forecast a revenue CAGR of 39% over FY16–18, driven by CAGRs of 34%, 46% and 34% in the accommodation, transportation and package tour segments, respectively. We project FY16 revenue growth of 65% YoY, higher than in FY17–18, due to the full-year consolidation of Qunar, which was acquired in Q4 FY15."

  b_str,b_dict = a.pre_replace_v2(t6,is_enzh=True)
  print(b_str)
  print(b_dict)

  # while 1:
  #   # print(a.test_data)
  #   time.sleep(3)
  #   pass
  # a='8609.HK	永续农业	Eggriculture Foods Ltd.	Eggriculture Foods	 \n'
  # b=a.strip(' \n')
  # print('hello')
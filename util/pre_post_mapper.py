# coding = utf-8

# @time    : 2019/4/1 5:55 PM
# @author  : alchemistlee
# @fileName: pre_post_mapper.py
# @abstract:


class PrePostMapper(object):

  def __init__(self,path,rep_tpl):
    self.path=path
    self._en_key2id=dict()
    self._en_keys=list()
    self._zh_vals=list()
    self.replace_tpl=rep_tpl
    self.load_data()

  def load_data(self):
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

      self._zh_vals.append(ori_zh_str)
      self._en_keys.append(tmp_en_lst)

      for en_key in tmp_en_lst:
        if en_key.strip()!='':
          self._en_key2id[en_key]=index

      index+=1

  def get_mapped_val(self,input_key):
    if input_key in self._en_key2id.keys():
      return self._zh_vals[self._en_key2id[input_key]]
    return None


  def pre_replace(self,input_str):
    post_replace_dict = dict()
    replaced_index =0
    for tmp_keys in self._en_keys:
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

  def post_replace(self,input_str,post_rep_dict):
    is_all_right = True
    ret_str = input_str
    for item_rep_key in post_rep_dict.keys():
      if not item_rep_key in ret_str:
        is_all_right= False
        break
      item_map_val = post_rep_dict[item_rep_key]
      ret_str = ret_str.replace(item_rep_key,item_map_val)
    return is_all_right,ret_str

if __name__=='__main__':
  a =  PrePostMapper('../data/en2zh_data_v2.txt','<%s>')
  a.pre_replace('Prudential Bancorp, Inc.')











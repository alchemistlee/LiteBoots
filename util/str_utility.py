# coding = utf-8

# @time    : 2019/4/2 4:16 PM
# @author  : alchemistlee
# @fileName: str_utility.py
# @abstract:

import re
import jieba


def rm_redundant_space_in_str(input_str):
  tmp_lst = input_str.split()
  return ''.join(tmp_lst)

def find_all(base_str,tar):
  res = []
  i =0
  while True:
    tar_index = base_str.find(tar,i)
    if tar_index == -1:
      break
    else :
      res.append((tar_index,tar_index+len(tar)))
      i= tar_index+len(tar)
  return res

def re_find_all(base_str,tar):
  pass


def sub_str(base_str ,beg_idx , end_idx, rep_str):
  new = []
  for i in range(0,len(base_str)):
    if i >= beg_idx and i < end_idx:
      continue
    elif i== end_idx:
      new.append(rep_str)
      new.append(base_str[i])
    else:
      new.append(base_str[i])
  return ''.join(new)


def batch_sub_str(base_str,idxs,rep_str):
  last_base_str = base_str
  for item_idx in idxs:
    beg = item_idx[0]
    end = item_idx[1]

    last_base_str = sub_str(last_base_str,beg,end,rep_str)
    print(last_base_str)
  return last_base_str


if __name__ == '__main__':
  # base = 'hello world'
  # rep = 'wow'
  # beg=2
  # end=6
  #
  # idxs = [(0,1),(5,7)]

  # print(sub_str(base,beg,end,rep))
  # print(batch_sub_str(base,idxs,rep))
  # b= ' 6ProPhase Labs, Inc. is a great company '
  # r1 = re.findall('[^a-z]ProPhase Labs, Inc\.|^ProPhase Labs, Inc\.',b,flags=re.IGNORECASE)
  # print(r1)
  # print(len(r1))
  t= '虎博是家 好公司'
  # print(t.split())
  # print(list(jieba.cut(t)))



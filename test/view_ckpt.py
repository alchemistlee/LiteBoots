# coding = utf-8

# @time    : 2019/3/21 10:47 AM
# @author  : alchemistlee
# @fileName: view_ckpt.py
# @abstract:


from tensorflow.contrib.framework.python.framework import checkpoint_utils

if __name__ == '__main__':
  var_list = checkpoint_utils.list_variables("/Users/alchemistlee/tigerye/tmp/t2t-train/model.ckpt-500000")
  for v in var_list:
    print(v)
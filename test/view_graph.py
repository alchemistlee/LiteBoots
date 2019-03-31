# coding = utf-8

# @time    : 2019/3/21 11:20 AM
# @author  : alchemistlee
# @fileName: view_graph.py
# @abstract:

import tensorflow as tf
from tensorflow.python import pywrap_tensorflow

# sess = tf.Session()
# check_point_path = '/Users/alchemistlee/tigerye/tmp/t2t-train/model.ckpt-500000'
# saver = tf.train.import_meta_graph('/Users/alchemistlee/tigerye/tmp/t2t-train/model.ckpt-500000.meta')
#
# saver.restore(sess, check_point_path)
#
# graph = tf.get_default_graph()
#
# # print(graph.get_operations())
#
# # with open('op.txt','a') as f:
# #    f.write(str(graph.get_operations()))
# op1 = graph.get_tensor_by_name('transformer/symbol_modality_32806_512/input_emb/weights_0')
# print(op1)


if __name__ == '__main__':

  # checkpoint_path = os.path.join(model_dir, "model.ckpt")
  check_point_path = '/Users/alchemistlee/tigerye/tmp/t2t-train/model.ckpt-500000'

  # Read data from checkpoint file
  reader = pywrap_tensorflow.NewCheckpointReader(check_point_path)
  var_to_shape_map = reader.get_variable_to_shape_map()
  # Print tensor name and values
  for key in var_to_shape_map:
    # if 'symbol_modality_' in key:
      # print('find it ')
      # print(key)
      # exit()
    print( key)
    # print(reader.get_tensor(key))

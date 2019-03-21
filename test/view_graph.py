# coding = utf-8

# @time    : 2019/3/21 11:20 AM
# @author  : alchemistlee
# @fileName: view_graph.py
# @abstract:

import tensorflow as tf

sess = tf.Session()
check_point_path = '/Users/alchemistlee/tigerye/tmp/t2t-train/model.ckpt-500000'
saver = tf.train.import_meta_graph('/Users/alchemistlee/tigerye/tmp/t2t-train/model.ckpt-500000.meta')

saver.restore(sess, check_point_path)

graph = tf.get_default_graph()

# print(graph.get_operations())

# with open('op.txt','a') as f:
#    f.write(str(graph.get_operations()))
op1 = graph.get_tensor_by_name('transformer/symbol_modality_32806_512/input_emb/weights_0')
print(op1)

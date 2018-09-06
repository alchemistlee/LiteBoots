#!/usr/bin/env bash

# export zh2en model
t2t-exporter \
  --model=transformer \
  --hparams_set=transformer_base_single_gpu \
  --problem=translate_zhen_wmt32k \
  --data_dir=/mnt/disk1/yifan.li/t2t_data \
  --output_dir=/mnt/disk1/yifan.li/t2t_train/translate_zhen_wmt32k/transformer-transformer_base_single_gpu

# start server zh2en
nohup tensorflow_model_server \
  --port=9080 \
  --model_name=transformer \
  --model_base_path=/mnt/disk1/yifan.li/t2t_train/translate_zhen_wmt32k/transformer-transformer_base_single_gpu/export/Servo/ &


# query zh2en
t2t-query-server \
  --server=222.73.24.8:9080 \
  --servable_name=transformer \
  --problem=translate_zhen_wmt32k \
  --data_dir=/mnt/disk1/yifan.li/t2t_data


# export en2zh model
t2t-exporter \
  --model=transformer \
  --hparams_set=transformer_base_single_gpu \
  --problem=translate_enzh_wmt32k \
  --data_dir=/mnt/disk1/yifan.li/t2t_data \
  --output_dir=/mnt/disk1/yifan.li/t2t_train/translate_enzh_wmt32k/transformer-transformer_base_single_gpu


# start server en2zh
nohup tensorflow_model_server \
  --port=9081 \
  --model_name=transformer \
  --model_base_path=/mnt/disk1/yifan.li/t2t_train/translate_enzh_wmt32k/transformer-transformer_base_single_gpu/export/Servo/ &

# query en2zh
t2t-query-server \
  --server=222.73.24.8:9081 \
  --servable_name=transformer \
  --problem=translate_enzh_wmt32k \
  --data_dir=/mnt/disk1/yifan.li/t2t_data

# start flask server
nohup python3 my_tf.py &



#!/usr/bin/env bash

## translate

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
  --server=222.73.24.8:081 \
  --servable_name=transformer \
  --problem =translate_enzh_wmt32k \
  --data_dir=/mnt/disk1/yifan.li/t2t_data

# start flask server
nohup python3 my_tf.py &

## sentiment
HOME=/home/root/
PROBLEM=sentiment_imdb
MODEL=transformer_encoder
HPARAMS=transformer_tiny
DATA_DIR=$HOME/t2t_data
TMP_DIR=/tmp/t2t_datagen
TRAIN_DIR=$HOME/t2t_train/$PROBLEM/$MODEL-$HPARAMS
DECODE_FILE=$DATA_DIR/decode-sentiment-imdb.txt
BEAM_SIZE=4
ALPHA=0.6

# decoder
t2t-decoder \
  --data_dir=$DATA_DIR \
  --problem=$PROBLEM \
  --model=$MODEL \
  --hparams_set=$HPARAMS \
  --output_dir=$TRAIN_DIR \
  --decode_hparams="beam_size=$BEAM_SIZE,alpha=$ALPHA" \
  --decode_from_file=$DECODE_FILE \
  --decode_to_file=decode-result.txt

# export
t2t-exporter \
  --model=transformer_encoder \
  --hparams_set=transformer_tiny \
  --problem=sentiment_imdb \
  --data_dir=/home/root/t2t_data \
  --output_dir=$HOME/t2t_train/sentiment_imdb/transformer_encoder-transformer_tiny

# start server
nohup tensorflow_model_server \
  --port=9085 \
  --model_name=transformer_encoder \
  --model_base_path=/home/root/t2t_train/sentiment_imdb/transformer_encoder-transformer_tiny/export/Servo/ &

# query it
t2t-query-server \
  --server=10.0.3.236:9085 \
  --servable_name=transformer_encoder \
  --problem=sentiment_imdb \
  --data_dir=/home/root/t2t_data



#!/usr/bin/env python
# coding = utf-8

# @time    : 2018/8/26 下午9:01
# @author  : alchemistlee
# @fileName: my_tf.py
# @abstract:
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import my_query 

import tensorflow as tf

from langconv import *

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/translate/zh2en/')
def trans_zh2en():
  inputs = request.args.get('in')
  server='222.73.24.8:9080'
  servable_name='transformer'
  problem='translate_zhen_wmt32k'
  data_dir='/mnt/disk1/yifan.li/t2t_data'
  return my_query.entry(inputs,data_dir,problem,servable_name,server)

@app.route('/translate/en2zh/')
def trans_en2zh():
  inputs = request.args.get('in')
  server='222.73.24.8:9081'
  servable_name='transformer'
  problem='translate_enzh_wmt32k'
  data_dir='/mnt/disk1/yifan.li/t2t_data'
  return my_query.entry(inputs,data_dir,problem,servable_name,server)

@app.route("/translate/tr2zh/")
def trans_tr2zh():
  inputs = request.args.get('in')
  sentence = Converter('zh-hans').convert(inputs)
  return sentence

@app.route("/translate/zh2tr/")
def trans_zh2tr():
  inputs = request.args.get('in')
  sentence = Converter('zh-hant').convert(inputs)
  return sentence


if __name__ == '__main__':
  app.run(host='0.0.0.0')

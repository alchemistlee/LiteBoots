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
from flask import render_template


app = Flask(__name__)

@app.route('/translate/zh2en/',methods=['GET'])
def tran_zh2en_interface():
  inputs = request.args.get('in')
  return trans_zh2en(inputs)

def trans_zh2en(inputs):
  server='222.73.24.8:9080'
  servable_name='transformer'
  problem='translate_zhen_wmt32k'
  data_dir='/mnt/disk1/yifan.li/t2t_data'
  return my_query.entry(inputs,data_dir,problem,servable_name,server)

@app.route('/translate/en2zh/',methods=['GET'])
def trans_en2zh_interface():
  inputs = request.args.get('in')
  return trans_en2zh(inputs)

def trans_en2zh(inputs):
  server='222.73.24.8:9081'
  servable_name='transformer'
  problem='translate_enzh_wmt32k'
  data_dir='/mnt/disk1/yifan.li/t2t_data'
  return my_query.entry(inputs,data_dir,problem,servable_name,server)

@app.route("/translate/tr2zh/",methods=['GET'])
def trans_tr2zh_interface():
  inputs = request.args.get('in')
  return trans_tr2zh(inputs)

def trans_tr2zh(inputs):
  sentence = Converter('zh-hans').convert(inputs)
  return sentence

@app.route("/translate/zh2tr/")
def trans_zh2tr_interface():
  inputs = request.args.get('in')
  return trans_zh2tr(inputs)

def trans_zh2tr(inputs):
  sentence = Converter('zh-hant').convert(inputs)
  return sentence

@app.route("/",methods=['GET','POST'])
def index():
  if request.method == 'POST':
    input = request.form['input']
    in_language = request.form['input-language']
    out_language = request.form['output-language']



    if in_language == 'zh':
      if out_language == 'en':
        res = trans_zh2en(input)
      elif out_language == 'tr':
        res = trans_zh2tr(input)
      else:
        res = input
    elif in_language == 'en':
      if out_language == 'zh':
        res = trans_en2zh(input)
      elif out_language == 'tr':
        res = trans_en2zh(input)
        res = trans_zh2tr(res)
      else:
        res = input
    else:
      if out_language == 'zh':
        res = trans_tr2zh(input)
      elif out_language == 'en':
        res = trans_tr2zh(input)
        res = trans_zh2en(res)
      else:
        res = input

    return res
  return render_template('index.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0')

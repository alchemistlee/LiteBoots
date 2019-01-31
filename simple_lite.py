#!/usr/bin/env python
# coding = utf-8

# @time    : 2018/8/26 下午9:01
# @author  : alchemistlee
# @fileName: simple_lite.py
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
import logging
import json
import sys
import random


app = Flask(__name__)

# t2t_data_dir = '/mnt/disk1/yifan.li/t2t_data'
t2t_data_dir = '/home/root/t2t_data_v2/t2t_data'

ports = [9082,9083,9084,9085,9086,9087]


@app.route('/translate/zh2en/',methods=['GET','POST'])
def tran_zh2en_interface():
  inputs = request.args.get('in')
  return trans_zh2en(inputs)

def trans_zh2en(inputs):
  server='127.0.0.1:'
  real_port= random.sample(ports,1)
  server=server+str(real_port)
  logging.info("real server = %s " % server)
  servable_name='transformer'
  problem='translate_zhen_wmt32k'
  data_dir=t2t_data_dir
  return my_query.entry(inputs,data_dir,problem,servable_name,server)


@app.route("/",methods=['GET','POST'])
def index():

  if request.method == 'POST':
    # stdout_backup = sys.stdout
    # sys.stdout = app.logger.info

    input = request.form['input']
    in_language = request.form['input-language']
    out_language = request.form['output-language']

    if in_language == 'zh':
      if out_language == 'en':
        # tmp_input = trans_tr2zh(input)
        # tr2zh_out = tmp_input['output']
        res = trans_zh2en(input)
      # elif out_language == 'tr':
      #   res = trans_zh2tr(input)
      else:
        res = {
          "output":input,
          "input":input,
          "score":1.0
        }
    # else:
    #   # in_language = en
    #
    #   if out_language == 'zh':
    #     res = trans_en2zh(input)
    #   elif out_language == 'tr':
    #     res = trans_en2zh(input)
    #     en2zh_out = res['output']
    #     res = trans_zh2tr(en2zh_out)
    #   else:
    #     res = {
    #       "output":input,
    #       "input":input,
    #       "score":1.0
    #     }


    app.logger.info(str(res))

    # sys.stdout = stdout_backup
    # return str(res)
    return json.dumps(res)
  return render_template('index.html')

if __name__ == '__main__':
  app.debug = True
  logging.basicConfig(stream=sys.stdout)
  handler = logging.FileHandler("/data/logs/my-tf-flask.log",encoding="UTF-8")
  handler.setLevel(logging.DEBUG)
  logging_format = logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s')
  handler.setFormatter(logging_format)
  app.logger.addHandler(handler)
  app.run(host='0.0.0.0')

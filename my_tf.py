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

from util.langconv import *

from flask import Flask
from flask import request
from flask import render_template
import util.my_logger as log
import json

from util.pre_post_mapper import *

app = Flask(__name__)

# t2t_data_dir = '/mnt/disk1/yifan.li/t2t_data'
t2t_data_dir = '/home/root/t2t_data_v2/t2t_data'

en2zh_data_path='./data/en2zh_data_v2.txt'
en2zh_replace_tpl='<%s>'

app.config['en2zhMapper']= PrePostMapper(path=en2zh_data_path,tpl=en2zh_replace_tpl)

# my_logger = get_logger(log_path='/data/logs/my-tf-flask.log')

@app.route('/translate/zh2en/',methods=['GET'])
def tran_zh2en_interface():
  inputs = request.args.get('in')
  return trans_zh2en(inputs)

def trans_zh2en(inputs):
  server='127.0.0.1:9082'
  servable_name='transformer'
  problem='translate_zhen_wmt32k'
  data_dir=t2t_data_dir
  return my_query.entry(inputs,data_dir,problem,servable_name,server)

@app.route('/translate/en2zh/',methods=['GET'])
def trans_en2zh_interface():
  inputs = request.args.get('in')
  return trans_en2zh(inputs)


def trans_en2zh(inputs):
  server='127.0.0.1:9083'
  servable_name='transformer'
  problem='translate_enzh_wmt32k'
  data_dir=t2t_data_dir

  # dealt_with en2zh mapper
  en2zhMapper = app.config['en2zhMapper']
  dealt_input,mark_dict=en2zhMapper.pre_replace_v2(inputs)

  log.logger.info('pre-res = %s ' % dealt_input)
  log.logger.info('mark-dict = %s ' % str(mark_dict))


  model_res = my_query.entry(dealt_input,data_dir,problem,servable_name,server)

  log.logger.info('model-res = %s ' % model_res)

  is_all_right, post_dealt_res = en2zhMapper.post_replace(model_res['output'],mark_dict)

  log.logger.info(' is_all_right = %s , post-res = %s ' % (str(is_all_right),post_dealt_res))

  if is_all_right:
    model_res['output']=post_dealt_res
    return model_res
  else:
    return my_query.entry(inputs,data_dir,problem,servable_name,server)

  #return my_query.entry(inputs,data_dir,problem,servable_name,server)

@app.route("/translate/tr2zh/",methods=['GET'])
def trans_tr2zh_interface():
  inputs = request.args.get('in')
  return trans_tr2zh(inputs)

def trans_tr2zh(inputs):
  sentence = Converter('zh-hans').convert(inputs)
  res = {
          "output":sentence,
          "input":inputs,
          "score":1.0
        }
  return res

@app.route("/translate/zh2tr/")
def trans_zh2tr_interface():
  inputs = request.args.get('in')
  return trans_zh2tr(inputs)

def trans_zh2tr(inputs):
  sentence = Converter('zh-hant').convert(inputs)
  res = {
    "output":sentence,
    "input":inputs,
    "score":1.0
  }
  return res

@app.route("/",methods=['GET','POST'])
def index():
  if request.method == 'POST':
    input = request.form['input']
    in_language = request.form['input-language']
    out_language = request.form['output-language']

    if in_language == 'zh':
      if out_language == 'en':
        tmp_input = trans_tr2zh(input)
        tr2zh_out = tmp_input['output']
        res = trans_zh2en(tr2zh_out)
      elif out_language == 'tr':
        res = trans_zh2tr(input)
      else:
        res = {
          "output":input,
          "input":input,
          "score":1.0
        }
    else:
      # in_language = en

      if out_language == 'zh':
        res = trans_en2zh(input)
      elif out_language == 'tr':
        res = trans_en2zh(input)
        en2zh_out = res['output']
        res = trans_zh2tr(en2zh_out)
      else:
        res = {
          "output":input,
          "input":input,
          "score":1.0
        }
    # else:
    #   if out_language == 'zh':
    #     res = trans_tr2zh(input)
    #   elif out_language == 'en':
    #     res = trans_tr2zh(input)
    #     tr2zh_out = res['ouptput']
    #     res = trans_zh2en(tr2zh_out)
    #   else:
    #     res = {
    #       "output":input,
    #       "input":input,
    #       "score":1.0
    #     }

    log.logger.info(str(res))
    # return str(res)
    return json.dumps(res)
  return render_template('index.html')

if __name__ == '__main__':
  app.debug = True
  # handler = logging.FileHandler("/data/logs/my-tf-flask.log",encoding="UTF-8")
  # handler.setLevel(logging.DEBUG)
  # logging_format = logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s')
  # handler.setFormatter(logging_format)
  # app.logger.addHandler(handler)
  app.run(host='0.0.0.0')

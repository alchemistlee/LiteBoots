# coding = utf-8

# @time    : 2018/9/28 上午12:46
# @author  : alchemistlee
# @fileName: my_sentiment_server.py.py
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

app = Flask(__name__)

# t2t_data_dir = '/mnt/disk1/yifan.li/t2t_data'
t2t_data_dir = '/home/root/t2t_data'


@app.route('/sentiment/api/', methods=['GET'])
def sentiment_it():
  inputs = request.args.get('in')
  return _query_2_sentiment_tf(inputs)


def _query_2_sentiment_tf(inputs):
  server='127.0.0.1:9085'
  servable_name='transformer_encoder'
  problem='sentiment_imdb'
  data_dir=t2t_data_dir
  return my_query.entry(inputs,data_dir,problem,servable_name,server)


@app.route("/", methods=['GET', 'POST'])
def index():
  if request.method == 'POST':
    input = request.form['input']
    # in_language = request.form['input-language']
    # out_language = request.form['output-language']
    res = _query_2_sentiment_tf(input)

    app.logger.info(str(res))
    return str(res)
  return render_template('sentiment_index.html')


if __name__ == '__main__':
  app.debug = True
  handler = logging.FileHandler("/data/logs/my-sentiment-flask.log",encoding="UTF-8")
  handler.setLevel(logging.DEBUG)
  logging_format = logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s')
  handler.setFormatter(logging_format)
  app.logger.addHandler(handler)
  app.run(host='0.0.0.0')
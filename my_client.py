# coding = utf-8

# @time    : 2019/3/19 11:12 PM
# @author  : alchemistlee
# @fileName: my_client.py
# @abstract:

from flask import Flask
from flask import request
from flask import render_template

from my_conn_manager import MyConnManager

import config

import sys
import json

app = Flask(__name__)


MyConnManager.register(config.REMOTE_PUSH_FUNC)
MyConnManager.register(config.REMOTE_RESULT_FUNC)
MyConnManager.register(config.REMOTE_PREDICT_FUNC)
app.config['myConn'] = MyConnManager(hosts=config.REMOTE_ADDRESS, authkey=config.REMOTE_AUTHKEY)


def decode_predict(string):
  try:
    myConn = app.config['myConn']
    result_dict = myConn.result(string)
    # result_dict = dispatch.predict(string)
    status = result_dict.get('status')
    if status and status == -999:
      raise Exception('识别超时')
    rate = result_dict.get('rate')
  except Exception as e:
    raise e
  else:
    return status, rate

app.config['decode_predict_func']=decode_predict

@app.route("/trans/en2zh/",methods=['GET'])
def trans_en2zh():

  result_dict = dict(error_code=1)
  try:
    input_str = request.args.get('in')
    decode_predict_func = app.config['decode_predict_func']
    status, rate = decode_predict_func(input_str)
  except Exception as e:
    result_dict['message'] = str(e)
    print('views action text error: %s' % e)
  else:
    result_dict = {
      'error_code': 0,
      'message': 'success',
      'data': {
        'rate': rate,
        'status': status,
      }
    }
  return result_dict


if __name__ == "__main__":
  app.debug = True
  # logging.basicConfig(stream=sys.stdout)
  # handler = logging.FileHandler("/home/yifan.li/data/logs/my-tf-flask.log", encoding="UTF-8")
  # handler.setLevel(logging.DEBUG)
  # logging_format = logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s')
  # handler.setFormatter(logging_format)
  # app.logger.addHandler(handler)
  app.run(host='0.0.0.0')
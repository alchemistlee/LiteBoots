# coding = utf-8

# @time    : 2019/4/4 3:57 PM
# @author  : alchemistlee
# @fileName: my_logger.py
# @abstract:


import logging
# import os.path
# import sys
# import time


def get_logger(is_test=False, log_path=None):

  logger = logging.getLogger()
  logger.propagate=False
  logger.setLevel(logging.INFO)
  # rq = time.strftime('%Y-%m-%d', time.localtime(time.time()))
  # log_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/Logs/'
  formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
  # logfile = log_path + rq + '{}.log'.format(log_name)

  if is_test:
    sh = logging.StreamHandler()
    sh.setFormatter(formatter)
    logger.addHandler(sh)
    return logger

  else:
    fh = logging.FileHandler(log_path, mode='a',encoding="UTF-8")
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    return logger
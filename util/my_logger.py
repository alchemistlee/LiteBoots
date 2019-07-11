# coding = utf-8

# @time    : 2019/4/4 3:57 PM
# @author  : alchemistlee
# @fileName: my_logger.py
# @abstract:

import sys
import logging

from config import gen_config
# import os.path
# import sys
# import time
# def get_logger(is_test=False, log_path=None):

config = gen_config()

logger = logging.getLogger()
logger.propagate
logger.setLevel(logging.INFO)
# rq = time.strftime('%Y-%m-%d', time.localtime(time.time()))
# log_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/Logs/'
formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
# logfile = log_path + rq + '{}.log'.format(log_name)

# if is_test:
#   sh = logging.StreamHandler()
#   sh.setFormatter(formatter)
#   logger.addHandler(sh)
#   return logger
#
# else:
if config.LOG_STDOUT:
    fh = logging.StreamHandler(sys.stdout)
else:
    fh = logging.FileHandler(config.LOG_FILE_PATH, mode='a', encoding="UTF-8")

fh.setLevel(config.LOG_LEVEL)
fh.setFormatter(formatter)
logger.addHandler(fh)

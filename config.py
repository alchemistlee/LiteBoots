# coding = utf-8

# @time    : 2019/4/9 10:04 AM
# @author  : alchemistlee
# @fileName: config.py
# @abstract:
import os
import logging

class Config():
    EN2ZH_GET_ALL = 'select id,ent_keys,ent_val,type,is_replace from en_zh_ent where is_delete=0;'
    EN2ZH_GET_MAX = 'select update_time from en_zh_ent order by update_time desc limit 1;'
    ZH2EN_GET_ALL = 'select id,ent_keys,ent_val,type,is_replace from zh_en_ent where is_delete=0;'
    ZH2EN_GET_MAX = 'select update_time from zh_en_ent order by update_time desc limit 1;'
    EN2ZH_DEL = 'delete from en_zh_ent where id=%s;'
    ZH2EN_DEL = 'delete from zh_en_ent where id=%s;'

    EN2ZH_DATA_PATH = './data/en2zh_data_v2.txt'

    EN2ZH_REPLACE_TPL = '<%s>'
    ZH2EN_REPLACE_TPL = '<%s>'

    ZH2EN_SERVABLE_NAME = 'transformer_zhen'
    ZH2EN_PROBLEM = 'translate_zhen_wmt32k'

    EN2ZH_SERVABLE_NAME = 'transformer_enzh'
    EN2ZH_PROBLEM = 'translate_enzh_wmt32k'

    EN2CS_SERVABLE_NAME = 'transformer_encs'
    EN2CS_PROBLEM = 'translate_encs_wmt32k'

    CS2EN_SERVABLE_NAME = 'transformer_csen'
    CS2EN_PROBLEM = 'translate_csen_wmt32k'

    EN2DE_SERVABLE_NAME = 'transformer_ende'
    EN2DE_PROBLEM = 'translate_ende_wmt32k'

    DE2EN_SERVABLE_NAME = 'transformer_deen'
    DE2EN_PROBLEM = 'translate_deen_wmt32k'

    EN2ES_SERVABLE_NAME = 'transformer_enes'
    EN2ES_PROBLEM = 'translate_enes_wmt32k'

    ES2EN_SERVABLE_NAME = 'transformer_esen'
    ES2EN_PROBLEM = 'translate_esen_wmt32k'


class DevelopmentConfig(Config):
    DEBUG = True
    LOG_STDOUT = False
    T2T_DATA_DIR = '/data/translate/models/v6/t2t_data'
    ZH2EN_SERVER = '127.0.0.1:9082'
    EN2ZH_SERVER = '127.0.0.1:9083'
    LOG_FILE = 'my-tf-flask.log'
    LOG_LEVEL = logging.DEBUG
    BASE_DIR = os.path.dirname(os.path.realpath(__file__))
    LOG_FILE_PATH = os.path.join(BASE_DIR, LOG_FILE)
    MYSQL_HOST = 'rm-uf67jlfy9n338fqa5.mysql.rds.aliyuncs.com'
    MYSQL_PASSWORD = 'jUOcnRR6ZoZ5'
    MYSQL_DATABASE = 'rt'
    MYSQL_USER = 'rt'


class ProductionConfig(Config):
    DEBUG = os.getenv('DEBUG', False)
    if DEBUG == 'True':
        DEBUG = True
    LOG_STDOUT = os.getenv('LOG_STDOUT', True)
    if LOG_STDOUT == 'False':
        LOG_STDOUT = False
    T2T_DATA_DIR = os.getenv('T2T_DATA_DIR', '/app/t2t_data')
    ZH2EN_SERVER = os.getenv('ZH2EN_SERVER', '127.0.0.1:9082')
    EN2ZH_SERVER = os.getenv('EN2ZH_SERVER', '127.0.0.1:9083')

    EN2CS_SERVER = os.getenv('EN2CS_SERVER', '')
    CS2EN_SERVER = os.getenv('CS2EN_SERVER', '')

    EN2DE_SERVER = os.getenv('EN2DE_SERVER', '')
    DE2EN_SERVER = os.getenv('DE2EN_SERVER', '')

    EN2ES_SERVER = os.getenv('EN2ES_SERVER', '')
    ES2EN_SERVER = os.getenv('ES2EN_SERVER', '')

    MYSQL_HOST = os.getenv('MYSQL_HOST', 'rm-uf67jlfy9n338fqa5.mysql.rds.aliyuncs.com')
    MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD', 'jUOcnRR6ZoZ5')
    MYSQL_DATABASE = os.getenv('MYSQL_DATABASE', 'rt')
    MYSQL_USER = os.getenv('MYSQL_USER', 'rt')
    LOG_LEVEL = os.getenv('LOG_LEVEL')
    if LOG_LEVEL == 'debug':
        LOG_LEVEL = logging.DEBUG
    else:
        LOG_LEVEL = logging.INFO



def get_config_obj():
    ENV = os.getenv('ENV')
    if ENV == 'prod':
        return ProductionConfig
    else:
        return DevelopmentConfig


def gen_config():
    ENV = os.getenv('ENV')
    if ENV == 'prod':
        return ProductionConfig()
    else:
        return DevelopmentConfig()

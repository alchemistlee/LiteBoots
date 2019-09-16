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

    EN2ET_SERVABLE_NAME = 'transformer_enet'
    EN2ET_PROBLEM = 'translate_enet_wmt32k'

    ET2EN_SERVABLE_NAME = 'transformer_eten'
    ET2EN_PROBLEM = 'translate_eten_wmt32k'

    EN2FR_SERVABLE_NAME = 'transformer_enfr'
    EN2FR_PROBLEM = 'translate_enfr_wmt32k'

    FR2EN_SERVABLE_NAME = 'transformer_fren'
    FR2EN_PROBLEM = 'translate_fren_wmt32k'

    EN2HI_SERVABLE_NAME = 'transformer_enhi'
    EN2HI_PROBLEM = 'translate_enhi_wmt32k'

    HI2EN_SERVABLE_NAME = 'transformer_hien'
    HI2EN_PROBLEM = 'translate_hien_wmt32k'

    EN2ID_SERVABLE_NAME = 'transformer_enid'
    EN2ID_PROBLEM = 'translate_enid_iwslt32k'

    ID2EN_SERVABLE_NAME = 'transformer_iden'
    ID2EN_PROBLEM = 'translate_iden_iwslt32k'

    EN2JP_SERVABLE_NAME = 'transformer_enjp'
    EN2JP_PROBLEM = 'translate_enjp_wmt32k'

    JP2EN_SERVABLE_NAME = 'transformer_jpen'
    JP2EN_PROBLEM = 'translate_jpen_wmt32k'

    EN2KO_SERVABLE_NAME = 'transformer_enko'
    EN2KO_PROBLEM = 'translate_enko_wmt32k'

    KO2EN_SERVABLE_NAME = 'transformer_koen'
    KO2EN_PROBLEM = 'translate_koen_wmt32k'

    EN2RO_SERVABLE_NAME = 'transformer_enro'
    EN2RO_PROBLEM = 'translate_enro_wmt32k'

    RO2EN_SERVABLE_NAME = 'transformer_roen'
    RO2EN_PROBLEM = 'translate_roen_wmt32k'

    EN2MK_SERVABLE_NAME = 'transformer_enmk'
    EN2MK_PROBLEM = 'translate_enmk_setimes32k'

    MK2EN_SERVABLE_NAME = 'transformer_mken'
    MK2EN_PROBLEM = 'translate_mken_setimes32k'

    EN2PT_SERVABLE_NAME = 'transformer_enpt'
    EN2PT_PROBLEM = 'translate_enpt_wmt32k'

    PT2EN_SERVABLE_NAME = 'transformer_pten'
    PT2EN_PROBLEM = 'translate_pten_wmt32k'

    EN2RU_SERVABLE_NAME = 'transformer_enru'
    EN2RU_PROBLEM = 'translate_enru_wmt32k'

    RU2EN_SERVABLE_NAME = 'transformer_ruen'
    RU2EN_PROBLEM = 'translate_ruen_wmt32k'

    EN2TH_SERVABLE_NAME = 'transformer_enth'
    EN2TH_PROBLEM = 'translate_enth_wmt32k'

    TH2EN_SERVABLE_NAME = 'transformer_then'
    TH2EN_PROBLEM = 'translate_then_wmt32k'

    EN2TN_SERVABLE_NAME = 'transformer_entn'
    EN2TN_PROBLEM = 'translate_entn_rma'

    TN2EN_SERVABLE_NAME = 'transformer_tnen'
    TN2EN_PROBLEM = 'translate_tnen_rma'

    EN2TR_SERVABLE_NAME = 'transformer_entr'
    EN2TR_PROBLEM = 'translate_entr_wmt32k'

    TR2EN_SERVABLE_NAME = 'transformer_tren'
    TR2EN_PROBLEM = 'translate_tren_wmt32k'

    EN2VI_SERVABLE_NAME = 'transformer_envi'
    EN2VI_PROBLEM = 'translate_envi_iwslt32k'

    VI2EN_SERVABLE_NAME = 'transformer_vien'
    VI2EN_PROBLEM = 'translate_vien_iwslt32k'

    EN2AR_SERVABLE_NAME = 'transformer_enar'
    EN2AR_PROBLEM = 'translate_enar_wmt32k'

    AR2EN_SERVABLE_NAME = 'transformer_aren'
    AR2EN_PROBLEM = 'translate_aren_wmt32k'

    EN2IT_SERVABLE_NAME = 'transformer_enit'
    EN2IT_PROBLEM = 'translate_enit_wmt32k'

    IT2EN_SERVABLE_NAME = 'transformer_iten'
    IT2EN_PROBLEM = 'translate_iten_wmt32k'


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
    T2T_DATA_DIR = os.getenv('T2T_DATA_DIR', '/data/translate/models/v13/t2t_data')
    ZH2EN_SERVER = os.getenv('ZH2EN_SERVER', '127.0.0.1:9082')
    EN2ZH_SERVER = os.getenv('EN2ZH_SERVER', '127.0.0.1:9083')

    EN2CS_SERVER = os.getenv('EN2CS_SERVER', '10.0.3.125:9000')
    CS2EN_SERVER = os.getenv('CS2EN_SERVER', '10.0.3.125:9001')
    EN2DE_SERVER = os.getenv('EN2DE_SERVER', '10.0.3.125:9002')
    DE2EN_SERVER = os.getenv('DE2EN_SERVER', '10.0.3.125:9003')
    EN2ES_SERVER = os.getenv('EN2ES_SERVER', '10.0.3.125:9004')
    ES2EN_SERVER = os.getenv('ES2EN_SERVER', '10.0.3.125:9005')
    EN2ET_SERVER = os.getenv('EN2ET_SERVER', '10.0.3.125:9006')
    ET2EN_SERVER = os.getenv('ET2EN_SERVER', '10.0.3.125:9007')
    EN2FR_SERVER = os.getenv('EN2FR_SERVER', '10.0.3.125:9008')
    FR2EN_SERVER = os.getenv('FR2EN_SERVER', '10.0.3.125:9009')
    EN2HI_SERVER = os.getenv('EN2HI_SERVER', '10.0.3.125:9010')
    HI2EN_SERVER = os.getenv('HI2EN_SERVER', '10.0.3.125:9011')
    EN2ID_SERVER = os.getenv('EN2ID_SERVER', '10.0.3.125:9012')
    ID2EN_SERVER = os.getenv('ID2EN_SERVER', '10.0.3.125:9013')
    EN2JP_SERVER = os.getenv('EN2JP_SERVER', '10.0.3.125:9014')
    JP2EN_SERVER = os.getenv('JP2EN_SERVER', '10.0.3.125:9015')
    EN2KO_SERVER = os.getenv('EN2KO_SERVER', '10.0.3.125:9016')
    KO2EN_SERVER = os.getenv('KO2EN_SERVER', '10.0.3.125:9017')
    EN2RO_SERVER = os.getenv('EN2RO_SERVER', '10.0.3.125:9018')
    RO2EN_SERVER = os.getenv('RO2EN_SERVER', '10.0.3.125:9019')
    EN2MK_SERVER = os.getenv('EN2MK_SERVER', '10.0.3.125:9020')
    MK2EN_SERVER = os.getenv('MK2EN_SERVER', '10.0.3.125:9021')
    EN2PT_SERVER = os.getenv('EN2PT_SERVER', '10.0.3.125:9022')
    PT2EN_SERVER = os.getenv('PT2EN_SERVER', '10.0.3.125:9023')
    EN2RU_SERVER = os.getenv('EN2RU_SERVER', '10.0.3.125:9024')
    RU2EN_SERVER = os.getenv('RU2EN_SERVER', '10.0.3.125:9025')
    EN2TH_SERVER = os.getenv('EN2TH_SERVER', '10.0.3.125:9026')
    TH2EN_SERVER = os.getenv('TH2EN_SERVER', '10.0.3.125:9027')
    EN2TN_SERVER = os.getenv('EN2TN_SERVER', '10.0.3.125:9028')
    TN2EN_SERVER = os.getenv('TN2EN_SERVER', '10.0.3.125:9029')
    EN2TR_SERVER = os.getenv('EN2TR_SERVER', '10.0.3.125:9030')
    TR2EN_SERVER = os.getenv('TR2EN_SERVER', '10.0.3.125:9031')
    EN2VI_SERVER = os.getenv('EN2VI_SERVER', '10.0.3.125:9032')
    VI2EN_SERVER = os.getenv('VI2EN_SERVER', '10.0.3.125:9033')
    EN2AR_SERVER = os.getenv('EN2AR_SERVER', '10.0.3.125:9034')
    AR2EN_SERVER = os.getenv('AR2EN_SERVER', '10.0.3.125:9035')
    EN2IT_SERVER = os.getenv('EN2IT_SERVER', '10.0.3.125:9036')
    IT2EN_SERVER = os.getenv('IT2EN_SERVER', '10.0.3.125:9037')

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

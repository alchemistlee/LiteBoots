# coding = utf-8

# @time    : 2019/4/9 10:04 AM
# @author  : alchemistlee
# @fileName: config.py
# @abstract:

EN2ZH_GET_ALL='select id,ent_keys,ent_val,type from en_zh_ent where is_delete=0;'
EN2ZH_GET_MAX='select update_time from en_zh_ent order by update_time desc limit 1;'

ZH2EN_GET_ALL='select id,ent_keys,ent_val,type from zh_en_ent where is_delete=0;'
ZH2EN_GET_MAX='select update_time from zh_en_ent order by update_time desc limit 1;'
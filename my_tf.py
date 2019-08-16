#!/usr/bin/env python
# coding = utf-8

# @time    : 2018/8/26 下午9:01
# @author  : alchemistlee
# @fileName: my_tf.py
# @abstract:

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import json

import my_query

from flask import Flask
from flask import request
from flask import render_template

from util.langconv import *
from util.pre_post_mapper import *
from config import get_config_obj, gen_config

config = gen_config()
app = Flask(__name__)
app.config.from_object(get_config_obj())


@app.route('/translate/en2cs/', methods=['GET'])
def tran_en2cs_interface():
    inputs = request.args.get('in')
    return trans_en2cs(inputs)


def trans_en2cs(inputs):
    server = config.EN2CS_SERVER
    servable_name = config.EN2CS_SERVABLE_NAME
    problem = config.EN2CS_PROBLEM
    data_dir = config.T2T_DATA_DIR

    # # dealt_with zh2en mapper
    # en2csMapper = PrePostMapper(MysqlUtil(config.EN2CS_GET_ALL, config.EN2CS_GET_MAX),
    #                             name='en2csMapper', tpl=config.EN2CS_REPLACE_TPL)
    # dealt_input, mark_dict = en2csMapper.pre_replace_v2(inputs, is_enzh=False)
    #
    # log.logger.info('[en2cs] pre-res = %s ' % dealt_input)
    # log.logger.info('[en2cs] mark-dict = %s ' % str(mark_dict))
    # model_res = my_query.entry(dealt_input, data_dir, problem, servable_name, server)
    #
    # log.logger.info('[en2cs] model-res = %s ' % model_res)
    #
    # is_all_right, post_dealt_res = en2csMapper.post_replace(model_res['output'], mark_dict, is_zhen=True)
    #
    # log.logger.info('[zh2en] is_all_right = %s , post-res = %s ' % (str(is_all_right), post_dealt_res))
    #
    # if is_all_right:
    #     model_res['output'] = post_dealt_res
    #     return model_res
    # else:
    return my_query.entry(inputs, data_dir, problem, servable_name, server)


@app.route('/translate/cs2en/', methods=['GET'])
def tran_cs2en_interface():
    inputs = request.args.get('in')
    return trans_cs2en(inputs)


def trans_cs2en(inputs):
    server = config.CS2EN_SERVER
    servable_name = config.CS2EN_SERVABLE_NAME
    problem = config.CS2EN_PROBLEM
    data_dir = config.T2T_DATA_DIR

    return my_query.entry(inputs, data_dir, problem, servable_name, server)


@app.route('/translate/en2de/', methods=['GET'])
def tran_en2de_interface():
    inputs = request.args.get('in')
    return trans_en2de(inputs)


def trans_en2de(inputs):
    server = config.EN2DE_SERVER
    servable_name = config.EN2DE_SERVABLE_NAME
    problem = config.EN2DE_PROBLEM
    data_dir = config.T2T_DATA_DIR

    return my_query.entry(inputs, data_dir, problem, servable_name, server)


@app.route('/translate/de2en/', methods=['GET'])
def tran_de2en_interface():
    inputs = request.args.get('in')
    return trans_de2en(inputs)


def trans_de2en(inputs):
    server = config.DE2EN_SERVER
    servable_name = config.DE2EN_SERVABLE_NAME
    problem = config.DE2EN_PROBLEM
    data_dir = config.T2T_DATA_DIR

    return my_query.entry(inputs, data_dir, problem, servable_name, server)


@app.route('/translate/en2es/', methods=['GET'])
def tran_en2es_interface():
    inputs = request.args.get('in')
    return trans_en2es(inputs)


def trans_en2es(inputs):
    server = config.EN2ES_SERVER
    servable_name = config.EN2ES_SERVABLE_NAME
    problem = config.EN2ES_PROBLEM
    data_dir = config.T2T_DATA_DIR

    return my_query.entry(inputs, data_dir, problem, servable_name, server)


@app.route('/translate/es2en/', methods=['GET'])
def tran_es2en_interface():
    inputs = request.args.get('in')
    return trans_es2en(inputs)


def trans_es2en(inputs):
    server = config.ES2EN_SERVER
    servable_name = config.ES2EN_SERVABLE_NAME
    problem = config.ES2EN_PROBLEM
    data_dir = config.T2T_DATA_DIR

    return my_query.entry(inputs, data_dir, problem, servable_name, server)


@app.route('/translate/zh2en/', methods=['GET'])
def tran_zh2en_interface():
    inputs = request.args.get('in')
    return trans_zh2en(inputs)


def trans_zh2en(inputs):
    server = config.ZH2EN_SERVER
    servable_name = config.ZH2EN_SERVABLE_NAME
    problem = config.ZH2EN_PROBLEM
    data_dir = config.T2T_DATA_DIR

    # dealt_with zh2en mapper
    zh2enMapper = PrePostMapper(MysqlUtil(config.ZH2EN_GET_ALL, config.ZH2EN_GET_MAX),
                                name='zh2enMapper', tpl=config.ZH2EN_REPLACE_TPL)
    dealt_input, mark_dict = zh2enMapper.pre_replace_v2(inputs, is_enzh=False)

    log.logger.info('[zh2en] pre-res = %s ' % dealt_input)
    log.logger.info('[zh2en] mark-dict = %s ' % str(mark_dict))

    model_res = my_query.entry(dealt_input, data_dir, problem, servable_name, server)

    log.logger.info('[zh2en] model-res = %s ' % model_res)

    is_all_right, post_dealt_res = zh2enMapper.post_replace(model_res['output'], mark_dict, is_zhen=True)

    log.logger.info('[zh2en] is_all_right = %s , post-res = %s ' % (str(is_all_right), post_dealt_res))

    if is_all_right:
        model_res['output'] = post_dealt_res
        return model_res
    else:
        return my_query.entry(inputs, data_dir, problem, servable_name, server)
    # return my_query.entry(inputs,data_dir,problem,servable_name,server)


@app.route('/translate/en2zh/', methods=['GET'])
def trans_en2zh_interface():
    inputs = request.args.get('in')
    return trans_en2zh(inputs)


def trans_en2zh(inputs):
    server = config.EN2ZH_SERVER
    servable_name = config.EN2ZH_SERVABLE_NAME
    problem = config.EN2ZH_PROBLEM
    data_dir = config.T2T_DATA_DIR

    # dealt_with en2zh mapper
    en2zhMapper = PrePostMapper(MysqlUtil(config.EN2ZH_GET_ALL, config.EN2ZH_GET_MAX),
                                name='en2zhMapper', tpl=config.EN2ZH_REPLACE_TPL)
    dealt_input, mark_dict = en2zhMapper.pre_replace_v2(inputs, is_enzh=True)

    log.logger.info('[en2zh] pre-res = %s ' % dealt_input)
    log.logger.info('[en2zh] mark-dict = %s ' % str(mark_dict))

    model_res = my_query.entry(dealt_input, data_dir, problem, servable_name, server)

    log.logger.info('[en2zh] model-res = %s ' % model_res)

    is_all_right, post_dealt_res = en2zhMapper.post_replace(model_res['output'], mark_dict)

    log.logger.info('[en2zh] is_all_right = %s , post-res = %s ' % (str(is_all_right), post_dealt_res))

    if is_all_right:
        model_res['output'] = post_dealt_res
        return model_res
    else:
        return my_query.entry(inputs, data_dir, problem, servable_name, server)


@app.route("/translate/tr2zh/", methods=['GET'])
def trans_tr2zh_interface():
    inputs = request.args.get('in')
    return trans_tr2zh(inputs)


def trans_tr2zh(inputs):
    sentence = Converter('zh-hans').convert(inputs)
    res = {
        "output": sentence,
        "input": inputs,
        "score": 1.0
    }
    return res


@app.route("/translate/zh2tr/")
def trans_zh2tr_interface():
    inputs = request.args.get('in')
    return trans_zh2tr(inputs)


def trans_zh2tr(inputs):
    sentence = Converter('zh-hant').convert(inputs)
    res = {
        "output": sentence,
        "input": inputs,
        "score": 1.0
    }
    return res


@app.route("/", methods=['GET', 'POST'])
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
                    "output": input,
                    "input": input,
                    "score": 1.0
                }
        elif in_language == 'en':

            if out_language == 'zh':
                res = trans_en2zh(input)
            elif out_language == 'tr':
                res = trans_en2zh(input)
                en2zh_out = res['output']
                res = trans_zh2tr(en2zh_out)
            elif out_language == 'de':
                res =  trans_en2de(input)
            elif out_language == 'es':
                res = trans_en2es(input)
            elif out_language == 'cs':
                res = trans_en2cs(input)
            else:
                res = {
                    "output": input,
                    "input": input,
                    "score": 1.0
                }
        elif in_language == 'de' :
            if out_language == 'en':
                res = trans_de2en(input)
            else:
                res = {
                    "output": input,
                    "input": input,
                    "score": 1.0
                }
        elif in_language == 'es':
            if out_language =='en':
                res = trans_es2en(input)
            else:
                res = {
                    "output": input,
                    "input": input,
                    "score": 1.0
                }
        elif in_language == 'cs':
            if out_language == 'en':
                res = trans_cs2en(input)
            else:
                res = {
                    "output": input,
                    "input": input,
                    "score": 1.0
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
    app.debug = config.DEBUG
    # handler = logging.FileHandler("/data/logs/my-tf-flask.log",encoding="UTF-8")
    # handler.setLevel(logging.DEBUG)
    # logging_format = logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s')
    # handler.setFormatter(logging_format)
    # app.logger.addHandler(handler)
    app.run(host='0.0.0.0')

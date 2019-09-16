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
from flask import jsonify


from util.langconv import *
from util.pre_post_mapper import *
from config import get_config_obj, gen_config

config = gen_config()
app = Flask(__name__)
app.config.from_object(get_config_obj())


@app.route('/translate/en2cs/', methods=['GET'])
def tran_en2cs_interface():
    inputs = request.args.get('in')
    server = config.EN2CS_SERVER
    servable_name = config.EN2CS_SERVABLE_NAME
    problem = config.EN2CS_PROBLEM
    data_dir = config.T2T_DATA_DIR
    print('server = {} , name = {} , problem = {} , data-dir = {}'.format(server, servable_name, problem, data_dir))
    res = my_query.entry(inputs, data_dir, problem, servable_name, server)
    return jsonify(res)


@app.route('/translate/cs2en/', methods=['GET'])
def tran_cs2en_interface():
    inputs = request.args.get('in')
    server = config.CS2EN_SERVER
    servable_name = config.CS2EN_SERVABLE_NAME
    problem = config.CS2EN_PROBLEM
    data_dir = config.T2T_DATA_DIR
    print('server = {} , name = {} , problem = {} , data-dir = {}'.format(server, servable_name, problem, data_dir))
    res = my_query.entry(inputs, data_dir, problem, servable_name, server)
    return jsonify(res)


@app.route('/translate/en2de/', methods=['GET'])
def tran_en2de_interface():
    inputs = request.args.get('in')
    server = config.EN2DE_SERVER
    servable_name = config.EN2DE_SERVABLE_NAME
    problem = config.EN2DE_PROBLEM
    data_dir = config.T2T_DATA_DIR
    print('server = {} , name = {} , problem = {} , data-dir = {}'.format(server, servable_name, problem, data_dir))
    res = my_query.entry(inputs, data_dir, problem, servable_name, server)
    return jsonify(res)


@app.route('/translate/de2en/', methods=['GET'])
def tran_de2en_interface():
    inputs = request.args.get('in')
    server = config.DE2EN_SERVER
    servable_name = config.DE2EN_SERVABLE_NAME
    problem = config.DE2EN_PROBLEM
    data_dir = config.T2T_DATA_DIR
    print('server = {} , name = {} , problem = {} , data-dir = {}'.format(server, servable_name, problem, data_dir))
    res = my_query.entry(inputs, data_dir, problem, servable_name, server)
    return jsonify(res)


@app.route('/translate/en2es/', methods=['GET'])
def tran_en2es_interface():
    inputs = request.args.get('in')
    server = config.EN2ES_SERVER
    servable_name = config.EN2ES_SERVABLE_NAME
    problem = config.EN2ES_PROBLEM
    data_dir = config.T2T_DATA_DIR
    print('server = {} , name = {} , problem = {} , data-dir = {}'.format(server, servable_name, problem, data_dir))
    res = my_query.entry(inputs, data_dir, problem, servable_name, server)
    return jsonify(res)


@app.route('/translate/es2en/', methods=['GET'])
def tran_es2en_interface():
    inputs = request.args.get('in')
    server = config.ES2EN_SERVER
    servable_name = config.ES2EN_SERVABLE_NAME
    problem = config.ES2EN_PROBLEM
    data_dir = config.T2T_DATA_DIR
    print('server = {} , name = {} , problem = {} , data-dir = {}'.format(server, servable_name, problem, data_dir))
    res = my_query.entry(inputs, data_dir, problem, servable_name, server)
    return jsonify(res)


@app.route('/translate/en2et/', methods=['GET'])
def tran_en2et_interface():
    inputs = request.args.get('in')
    server = config.EN2ET_SERVER
    servable_name = config.EN2ET_SERVABLE_NAME
    problem = config.EN2ET_PROBLEM
    data_dir = config.T2T_DATA_DIR
    print('server = {} , name = {} , problem = {} , data-dir = {}'.format(server, servable_name, problem, data_dir))
    res = my_query.entry(inputs, data_dir, problem, servable_name, server)
    return jsonify(res)


@app.route('/translate/et2en/', methods=['GET'])
def tran_et2en_interface():
    inputs = request.args.get('in')
    server = config.ET2EN_SERVER
    servable_name = config.ET2EN_SERVABLE_NAME
    problem = config.ET2EN_PROBLEM
    data_dir = config.T2T_DATA_DIR
    print('server = {} , name = {} , problem = {} , data-dir = {}'.format(server, servable_name, problem, data_dir))
    res = my_query.entry(inputs, data_dir, problem, servable_name, server)
    return jsonify(res)


@app.route('/translate/en2fr/', methods=['GET'])
def tran_en2fr_interface():
    inputs = request.args.get('in')
    server = config.EN2FR_SERVER
    servable_name = config.EN2FR_SERVABLE_NAME
    problem = config.EN2FR_PROBLEM
    data_dir = config.T2T_DATA_DIR
    print('server = {} , name = {} , problem = {} , data-dir = {}'.format(server, servable_name, problem, data_dir))
    res = my_query.entry(inputs, data_dir, problem, servable_name, server)
    return jsonify(res)


@app.route('/translate/fr2en/', methods=['GET'])
def tran_fr2en_interface():
    inputs = request.args.get('in')
    server = config.FR2EN_SERVER
    servable_name = config.FR2EN_SERVABLE_NAME
    problem = config.FR2EN_PROBLEM
    data_dir = config.T2T_DATA_DIR
    print('server = {} , name = {} , problem = {} , data-dir = {}'.format(server, servable_name, problem, data_dir))
    res = my_query.entry(inputs, data_dir, problem, servable_name, server)
    return jsonify(res)


@app.route('/translate/en2hi/', methods=['GET'])
def tran_en2hi_interface():
    inputs = request.args.get('in')
    server = config.EN2HI_SERVER
    servable_name = config.EN2HI_SERVABLE_NAME
    problem = config.EN2HI_PROBLEM
    data_dir = config.T2T_DATA_DIR
    print('server = {} , name = {} , problem = {} , data-dir = {}'.format(server, servable_name, problem, data_dir))
    res = my_query.entry(inputs, data_dir, problem, servable_name, server)
    return jsonify(res)


@app.route('/translate/hi2en/', methods=['GET'])
def tran_hi2en_interface():
    inputs = request.args.get('in')
    server = config.HI2EN_SERVER
    servable_name = config.HI2EN_SERVABLE_NAME
    problem = config.HI2EN_PROBLEM
    data_dir = config.T2T_DATA_DIR
    print('server = {} , name = {} , problem = {} , data-dir = {}'.format(server, servable_name, problem, data_dir))
    res = my_query.entry(inputs, data_dir, problem, servable_name, server)
    return jsonify(res)


@app.route('/translate/en2id/', methods=['GET'])
def tran_en2id_interface():
    inputs = request.args.get('in')
    server = config.EN2ID_SERVER
    servable_name = config.EN2ID_SERVABLE_NAME
    problem = config.EN2ID_PROBLEM
    data_dir = config.T2T_DATA_DIR
    print('server = {} , name = {} , problem = {} , data-dir = {}'.format(server, servable_name, problem, data_dir))
    res = my_query.entry(inputs, data_dir, problem, servable_name, server)
    return jsonify(res)


@app.route('/translate/id2en/', methods=['GET'])
def tran_id2en_interface():
    inputs = request.args.get('in')
    server = config.ID2EN_SERVER
    servable_name = config.ID2EN_SERVABLE_NAME
    problem = config.ID2EN_PROBLEM
    data_dir = config.T2T_DATA_DIR
    print('server = {} , name = {} , problem = {} , data-dir = {}'.format(server, servable_name, problem, data_dir))
    res = my_query.entry(inputs, data_dir, problem, servable_name, server)
    return jsonify(res)


@app.route('/translate/en2jp/', methods=['GET'])
def tran_en2jp_interface():
    inputs = request.args.get('in')
    server = config.EN2JP_SERVER
    servable_name = config.EN2JP_SERVABLE_NAME
    problem = config.EN2JP_PROBLEM
    data_dir = config.T2T_DATA_DIR
    print('server = {} , name = {} , problem = {} , data-dir = {}'.format(server, servable_name, problem, data_dir))
    res = my_query.entry(inputs, data_dir, problem, servable_name, server)
    return jsonify(res)


@app.route('/translate/jp2en/', methods=['GET'])
def tran_jp2en_interface():
    inputs = request.args.get('in')
    server = config.JP2EN_SERVER
    servable_name = config.JP2EN_SERVABLE_NAME
    problem = config.JP2EN_PROBLEM
    data_dir = config.T2T_DATA_DIR
    print('server = {} , name = {} , problem = {} , data-dir = {}'.format(server, servable_name, problem, data_dir))
    res = my_query.entry(inputs, data_dir, problem, servable_name, server)
    return jsonify(res)


@app.route('/translate/en2ko/', methods=['GET'])
def tran_en2ko_interface():
    inputs = request.args.get('in')
    server = config.EN2KO_SERVER
    servable_name = config.EN2KO_SERVABLE_NAME
    problem = config.EN2KO_PROBLEM
    data_dir = config.T2T_DATA_DIR
    print('server = {} , name = {} , problem = {} , data-dir = {}'.format(server, servable_name, problem, data_dir))
    res = my_query.entry(inputs, data_dir, problem, servable_name, server)
    return jsonify(res)


@app.route('/translate/ko2en/', methods=['GET'])
def tran_ko2en_interface():
    inputs = request.args.get('in')
    server = config.KO2EN_SERVER
    servable_name = config.KO2EN_SERVABLE_NAME
    problem = config.KO2EN_PROBLEM
    data_dir = config.T2T_DATA_DIR
    print('server = {} , name = {} , problem = {} , data-dir = {}'.format(server, servable_name, problem, data_dir))
    res = my_query.entry(inputs, data_dir, problem, servable_name, server)
    return jsonify(res)


@app.route('/translate/en2ro/', methods=['GET'])
def tran_en2ro_interface():
    inputs = request.args.get('in')
    server = config.EN2RO_SERVER
    servable_name = config.EN2RO_SERVABLE_NAME
    problem = config.EN2RO_PROBLEM
    data_dir = config.T2T_DATA_DIR
    print('server = {} , name = {} , problem = {} , data-dir = {}'.format(server, servable_name, problem, data_dir))
    res = my_query.entry(inputs, data_dir, problem, servable_name, server)
    return jsonify(res)


@app.route('/translate/ro2en/', methods=['GET'])
def tran_ro2en_interface():
    inputs = request.args.get('in')
    server = config.RO2EN_SERVER
    servable_name = config.RO2EN_SERVABLE_NAME
    problem = config.RO2EN_PROBLEM
    data_dir = config.T2T_DATA_DIR
    print('server = {} , name = {} , problem = {} , data-dir = {}'.format(server, servable_name, problem, data_dir))
    res = my_query.entry(inputs, data_dir, problem, servable_name, server)
    return jsonify(res)


@app.route('/translate/en2mk/', methods=['GET'])
def tran_en2mk_interface():
    inputs = request.args.get('in')
    server = config.EN2MK_SERVER
    servable_name = config.EN2MK_SERVABLE_NAME
    problem = config.EN2MK_PROBLEM
    data_dir = config.T2T_DATA_DIR
    print('server = {} , name = {} , problem = {} , data-dir = {}'.format(server, servable_name, problem, data_dir))
    res = my_query.entry(inputs, data_dir, problem, servable_name, server)
    return jsonify(res)


@app.route('/translate/mk2en/', methods=['GET'])
def tran_mk2en_interface():
    inputs = request.args.get('in')
    server = config.MK2EN_SERVER
    servable_name = config.MK2EN_SERVABLE_NAME
    problem = config.MK2EN_PROBLEM
    data_dir = config.T2T_DATA_DIR
    print('server = {} , name = {} , problem = {} , data-dir = {}'.format(server, servable_name, problem, data_dir))
    res = my_query.entry(inputs, data_dir, problem, servable_name, server)
    return jsonify(res)


@app.route('/translate/en2pt/', methods=['GET'])
def tran_en2pt_interface():
    inputs = request.args.get('in')
    server = config.EN2PT_SERVER
    servable_name = config.EN2PT_SERVABLE_NAME
    problem = config.EN2PT_PROBLEM
    data_dir = config.T2T_DATA_DIR
    print('server = {} , name = {} , problem = {} , data-dir = {}'.format(server, servable_name, problem, data_dir))
    res = my_query.entry(inputs, data_dir, problem, servable_name, server)
    return jsonify(res)


@app.route('/translate/pt2en/', methods=['GET'])
def tran_pt2en_interface():
    inputs = request.args.get('in')
    server = config.PT2EN_SERVER
    servable_name = config.PT2EN_SERVABLE_NAME
    problem = config.PT2EN_PROBLEM
    data_dir = config.T2T_DATA_DIR
    print('server = {} , name = {} , problem = {} , data-dir = {}'.format(server, servable_name, problem, data_dir))
    res = my_query.entry(inputs, data_dir, problem, servable_name, server)
    return jsonify(res)


@app.route('/translate/en2ru/', methods=['GET'])
def tran_en2ru_interface():
    inputs = request.args.get('in')
    server = config.EN2RU_SERVER
    servable_name = config.EN2RU_SERVABLE_NAME
    problem = config.EN2RU_PROBLEM
    data_dir = config.T2T_DATA_DIR
    print('server = {} , name = {} , problem = {} , data-dir = {}'.format(server, servable_name, problem, data_dir))
    res = my_query.entry(inputs, data_dir, problem, servable_name, server)
    return jsonify(res)


@app.route('/translate/ru2en/', methods=['GET'])
def tran_ru2en_interface():
    inputs = request.args.get('in')
    server = config.RU2EN_SERVER
    servable_name = config.RU2EN_SERVABLE_NAME
    problem = config.RU2EN_PROBLEM
    data_dir = config.T2T_DATA_DIR
    print('server = {} , name = {} , problem = {} , data-dir = {}'.format(server, servable_name, problem, data_dir))
    res = my_query.entry(inputs, data_dir, problem, servable_name, server)
    return jsonify(res)


@app.route('/translate/en2th/', methods=['GET'])
def tran_en2th_interface():
    inputs = request.args.get('in')
    server = config.EN2TH_SERVER
    servable_name = config.EN2TH_SERVABLE_NAME
    problem = config.EN2TH_PROBLEM
    data_dir = config.T2T_DATA_DIR
    print('server = {} , name = {} , problem = {} , data-dir = {}'.format(server, servable_name, problem, data_dir))
    res = my_query.entry(inputs, data_dir, problem, servable_name, server)
    return jsonify(res)


@app.route('/translate/th2en/', methods=['GET'])
def tran_th2en_interface():
    inputs = request.args.get('in')
    server = config.TH2EN_SERVER
    servable_name = config.TH2EN_SERVABLE_NAME
    problem = config.TH2EN_PROBLEM
    data_dir = config.T2T_DATA_DIR
    print('server = {} , name = {} , problem = {} , data-dir = {}'.format(server, servable_name, problem, data_dir))
    res = my_query.entry(inputs, data_dir, problem, servable_name, server)
    return jsonify(res)


@app.route('/translate/en2tn/', methods=['GET'])
def tran_en2tn_interface():
    inputs = request.args.get('in')
    server = config.EN2TN_SERVER
    servable_name = config.EN2TN_SERVABLE_NAME
    problem = config.EN2TN_PROBLEM
    data_dir = config.T2T_DATA_DIR
    print('server = {} , name = {} , problem = {} , data-dir = {}'.format(server, servable_name, problem, data_dir))
    res = my_query.entry(inputs, data_dir, problem, servable_name, server)
    return jsonify(res)


@app.route('/translate/tn2en/', methods=['GET'])
def tran_tn2en_interface():
    inputs = request.args.get('in')
    server = config.TN2EN_SERVER
    servable_name = config.TN2EN_SERVABLE_NAME
    problem = config.TN2EN_PROBLEM
    data_dir = config.T2T_DATA_DIR
    print('server = {} , name = {} , problem = {} , data-dir = {}'.format(server, servable_name, problem, data_dir))
    res = my_query.entry(inputs, data_dir, problem, servable_name, server)
    return jsonify(res)


@app.route('/translate/en2tr/', methods=['GET'])
def tran_en2tr_interface():
    inputs = request.args.get('in')
    server = config.EN2TR_SERVER
    servable_name = config.EN2TR_SERVABLE_NAME
    problem = config.EN2TR_PROBLEM
    data_dir = config.T2T_DATA_DIR
    print('server = {} , name = {} , problem = {} , data-dir = {}'.format(server, servable_name, problem, data_dir))
    res = my_query.entry(inputs, data_dir, problem, servable_name, server)
    return jsonify(res)


@app.route('/translate/tr2en/', methods=['GET'])
def tran_tr2en_interface():
    inputs = request.args.get('in')
    server = config.TR2EN_SERVER
    servable_name = config.TR2EN_SERVABLE_NAME
    problem = config.TR2EN_PROBLEM
    data_dir = config.T2T_DATA_DIR
    print('server = {} , name = {} , problem = {} , data-dir = {}'.format(server, servable_name, problem, data_dir))
    res = my_query.entry(inputs, data_dir, problem, servable_name, server)
    return jsonify(res)


@app.route('/translate/en2vi/', methods=['GET'])
def tran_en2vi_interface():
    inputs = request.args.get('in')
    server = config.EN2VI_SERVER
    servable_name = config.EN2VI_SERVABLE_NAME
    problem = config.EN2VI_PROBLEM
    data_dir = config.T2T_DATA_DIR
    print('server = {} , name = {} , problem = {} , data-dir = {}'.format(server, servable_name, problem, data_dir))
    res = my_query.entry(inputs, data_dir, problem, servable_name, server)
    return jsonify(res)


@app.route('/translate/vi2en/', methods=['GET'])
def tran_vi2en_interface():
    inputs = request.args.get('in')
    server = config.VI2EN_SERVER
    servable_name = config.VI2EN_SERVABLE_NAME
    problem = config.VI2EN_PROBLEM
    data_dir = config.T2T_DATA_DIR
    print('server = {} , name = {} , problem = {} , data-dir = {}'.format(server, servable_name, problem, data_dir))
    res = my_query.entry(inputs, data_dir, problem, servable_name, server)
    return jsonify(res)


@app.route('/translate/en2ar/', methods=['GET'])
def tran_en2ar_interface():
    inputs = request.args.get('in')
    server = config.EN2AR_SERVER
    servable_name = config.EN2AR_SERVABLE_NAME
    problem = config.EN2AR_PROBLEM
    data_dir = config.T2T_DATA_DIR
    print('server = {} , name = {} , problem = {} , data-dir = {}'.format(server, servable_name, problem, data_dir))
    res = my_query.entry(inputs, data_dir, problem, servable_name, server)
    return jsonify(res)


@app.route('/translate/ar2en/', methods=['GET'])
def tran_ar2en_interface():
    inputs = request.args.get('in')
    server = config.AR2EN_SERVER
    servable_name = config.AR2EN_SERVABLE_NAME
    problem = config.AR2EN_PROBLEM
    data_dir = config.T2T_DATA_DIR
    print('server = {} , name = {} , problem = {} , data-dir = {}'.format(server, servable_name, problem, data_dir))
    res = my_query.entry(inputs, data_dir, problem, servable_name, server)
    return jsonify(res)


@app.route('/translate/en2it/', methods=['GET'])
def tran_en2it_interface():
    inputs = request.args.get('in')
    server = config.EN2IT_SERVER
    servable_name = config.EN2IT_SERVABLE_NAME
    problem = config.EN2IT_PROBLEM
    data_dir = config.T2T_DATA_DIR
    print('server = {} , name = {} , problem = {} , data-dir = {}'.format(server, servable_name, problem, data_dir))
    res = my_query.entry(inputs, data_dir, problem, servable_name, server)
    return jsonify(res)


@app.route('/translate/it2en/', methods=['GET'])
def tran_it2en_interface():
    inputs = request.args.get('in')
    server = config.IT2EN_SERVER
    servable_name = config.IT2EN_SERVABLE_NAME
    problem = config.IT2EN_PROBLEM
    data_dir = config.T2T_DATA_DIR
    print('server = {} , name = {} , problem = {} , data-dir = {}'.format(server, servable_name, problem, data_dir))
    res = my_query.entry(inputs, data_dir, problem, servable_name, server)
    return jsonify(res)


@app.route('/translate/zh2en/', methods=['GET'])
def tran_zh2en_interface():
    inputs = request.args.get('in')
    res = trans_zh2en(inputs)
    return jsonify(res)


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
    res = trans_en2zh(inputs)
    return jsonify(res)


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
            else:
                res = {
                    "output": input,
                    "input": input,
                    "score": 1.0
                }
        log.logger.info(str(res))
        # return str(res)
        return json.dumps(res)
    return render_template('index.html')


if __name__ == '__main__':
    app.debug = config.DEBUG
    app.run(host='0.0.0.0')

# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 配置切词器
"""

import jieba

jieba.setLogLevel(log_level="ERROR")


def jieba_tokenize(sentence):
    """
    jieba分词
    """
    return list(jieba.tokenize(sentence))


def hanlp_tokenize(sentence):
    """
    hanlp分词
    """
    import os
    import hanlp

    os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
    hanlp_parser = hanlp.load(hanlp.pretrained.mtl.CLOSE_TOK_POS_NER_SRL_DEP_SDP_CON_ELECTRA_SMALL_ZH)  # 中文语料库
    sent_list = hanlp_parser(sentence, tasks='tok/fine').get('tok/fine')
    res = []
    start_idx = 0
    for word in sent_list:
        end_idx = start_idx + len(word)
        res.append((word, start_idx, end_idx))
        start_idx = end_idx
    return res


if __name__ == '__main__':
    text = "阿联酋阿斯迪拉电子贸易公司"
    print(jieba_tokenize(text))
    print(hanlp_tokenize(text))

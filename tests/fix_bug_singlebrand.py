# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""
import os
import sys

sys.path.append('..')
import companynameparser
import jieba

a = [
    "合肥杰迈特汽车新材料有限公司",
    "中节能秦皇岛环保有限公司",
    "玉田县鸦鸿桥镇凯翔商店",
    "成都好房屋网络科技有限公司",
    "天津曰新塑料制品有限公司",
    "天津港源国际船舶代理有限公司",
    "大厂回族自治县祁各庄镇宝艺大唐艺术行",
    "永安市燕南街扶晴梅百货商行",
    "武陟县大唛副食门市部",
]


def load_file(file_path):
    subs = []
    if file_path and os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as fr:
            for line in fr:
                i = line.strip().split()[0]
                subs.append(i)
    return subs


if __name__ == '__main__':
    # for i in a:
    #     r = m.parse(i)
    #     print(i, r['brand'])
    #
    # print()

    for i in a:
        r = companynameparser.parse(i)
        print(i, jieba.lcut(i), r['brand'], ' ---- ', r['place'], r['brand'], r['trade'], r['suffix'])

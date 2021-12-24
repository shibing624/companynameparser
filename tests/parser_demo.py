# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""
import sys

sys.path.append('..')

from companynameparser import parser

if __name__ == '__main__':
    m = parser.Parser()
    with open('company_demo.txt', 'r', encoding='utf-8') as fr, \
            open('company_names_result.txt', 'w', encoding='utf-8') as fw:
        count = 0
        for line in fr:
            i = line.strip()
            count += 1
            r = m.parse(i)
            b = r['brand']
            print(i, r['place'], r['brand'], r['trade'], r['suffix'])
            fw.write(i + '\t' + b + '\n')

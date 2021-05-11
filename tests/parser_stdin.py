# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""
import sys

sys.path.append('..')
from companynameparser import parser

m = parser.Parser()
if __name__ == '__main__':
    for line in sys.stdin:
        i = line.strip()
        r = m.parse(i)
        b = r['brand']
        # print(i + ' ' + r['brand'] + ' ' + r['trade'] + ' ' + r['suffix'])
        print(i + '\t' + r['brand'])

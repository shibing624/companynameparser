# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""

import sys

import jieba


def cut_stdin():
    """切词"""
    for line in sys.stdin:
        i = line.strip()
        r = jieba.lcut(i)
        print(r[-1])


if __name__ == '__main__':
    cut_stdin()

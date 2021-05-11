# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""
import sys

sys.path.append('..')
import companynameparser

if __name__ == '__main__':
    company_strs = [
        "武汉海明智业电子商务有限公司",
        "泉州益念食品有限公司",
        "常州途畅互联网科技有限公司合肥分公司",
        "昆明享亚教育信息咨询有限公司",
        "深圳光明区三晟股份有限公司",
    ]
    for name in company_strs:
        r = companynameparser.parse(name)
        print(r)

    print("*" * 42, ' enable word segment')
    for name in company_strs:
        r = companynameparser.parse(name, pos_sensitive=False, enable_word_segment=True)
        print(r)

    print("*" * 42, ' pos sensitive')
    for name in company_strs:
        r = companynameparser.parse(name, pos_sensitive=True, enable_word_segment=False)
        print(r)

    print("*" * 42, 'enable word segment and pos')
    for name in company_strs:
        r = companynameparser.parse(name, pos_sensitive=True, enable_word_segment=True)
        print(r)

    print("*" * 42, 'use custom name')
    companynameparser.set_custom_split_file('./custom_name_split.txt')
    for i in company_strs:
        r = companynameparser.parse(i)
        print(r)

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
        "昆明享亚教育信息咨询有限公司",
        "郑州市管城回族区咔悠化妆品商行",
        "武汉海明智业电子商务有限公司",
    ]
    for name in company_strs:
        r = companynameparser.parse(name)
        print(r)

    print("*" * 42)
    for name in company_strs:
        r = companynameparser.parse(name, enable_word_segment=True)
        print(r)
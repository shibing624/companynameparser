# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""

import sys

sys.path.append('..')
from companynameparser import Parser
from companynameparser import parser


def test_eng_name():
    """测试EnglishName类"""
    company_strs = [
        "chinese武汉海明智业电子商务有限公司",
        "01泉州益念食品有限公司",
        "english company",
        "Eng Company",
    ]
    m = Parser()
    for name in company_strs:
        for i in name:
            k = parser.is_chinese(i)
            print(i, k)

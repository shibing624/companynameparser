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
        "武汉蓝天医院",
    ]
    for i in company_strs:
        r = companynameparser.parse(i)
        print(r)

        print(i, r['place'], r['brand'], r['trade'], r['suffix'])

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
        "沧州嘉诺温室大棚设施有限公司",
        "深圳光明区三晟有限公司",
        "深圳光明区三晟股份有限公司",
        "山西安健堂健康管理有限公司",
        "西咸新区沣东新城未科诚百货店",
        "昆明享亚教育信息咨询有限公司",
        "北京华颜健康咨询有限公司",
    ]
    for i in company_strs:
        r = companynameparser.parse(i)
        print(r)

    print("*" * 42)
    companynameparser.set_custom_split_file('./custom_name_split.txt')
    for i in company_strs:
        r = companynameparser.parse(i)
        print(r)

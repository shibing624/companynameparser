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
        "朝阳县大山苗圃",
        "海宁市海昌思诚贸易商行",
        "昆山千灯镇南野智能科技店",
        "武陟县大唛副食门市部",
        "贵州民族酒业（集团）销售有限公司",
        "玉田县鸦鸿桥镇凯翔商店",
        "桐乡市梧桐卓继宇文贸易商行",
        "大厂回族自治县祁各庄镇宝艺大唐艺术行",
    ]
    for i in company_strs:
        r = companynameparser.parse(i)
        print(r)

    print("*" * 42)
    companynameparser.set_custom_split_file('./my_custom_name_split.txt')
    for i in company_strs:
        r = companynameparser.parse(i)
        print(r)

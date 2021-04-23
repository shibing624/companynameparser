# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""

import companyparser

if __name__ == '__main__':
    company_strs = ["泉州益念食品有限公司",
                    "武汉蓝天医院",
                    "武汉海明智业电子商务有限公司",
                    ]
    df = companyparser.parse(company_strs)
    print(df)

    for map_key in zip(df["place"], df["brand"], df["trade"], df['suffix']):
        print(map_key)

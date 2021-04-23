# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""

import companyparser

if __name__ == '__main__':
    company_strs = ["泉州益念食品有限公司",
                    "武汉蓝天医院",
                    "宁波澜格网络科技有限公司常州第一分公司",
                    "武汉海明智业电子商务有限公司",
                    "成都高保真生物技术有限公司",
                    "河南省冠食源食品有限公司",
                    "兰州壹玖壹玖电子商务有限公司",
                    "陕西山有枢生物科技有限公司",
                    ]
    df = companyparser.parse(company_strs)
    print(df)

    for map_key in zip(df["place"], df["brand"], df["trade"], df['suffix']):
        print(map_key)

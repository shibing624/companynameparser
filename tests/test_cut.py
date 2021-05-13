# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""
import os
import unittest

import jieba

pwd_path = os.path.abspath(os.path.dirname(__file__))


class TestCut(unittest.TestCase):
    def test_cut1(self):
        """切词"""
        location_str = [
            "徐州九州通医药公司",
        ]
        for i in location_str:
            o = jieba.lcut(i)
            print(o)

    def test_cut_with_dict(self):
        """加入自定义词典，切词"""
        d = {'上海': 1000, '上海市': 1000, '浦东新区': 1000, '祥和小区': 200}
        d_path = 'my.dict'
        with open(d_path, 'w', encoding='utf-8') as f:
            for k, v in d.items():
                f.write(k + ' ' + str(v) + '\n')

        location_str = [
            "上海市浦东新区东方路1365号5号楼24B",
            "上海浦东东方路1365号5号楼24B",
            "上海市浦东东方路1365号5号楼24B",
            "上海市浦东区东方路1365号5号楼24B",
            "湖北武汉复兴路111号",
            "天津滨海祥和小区",
            "天津滨海新区祥和小区111号",
        ]
        for i in location_str:
            o = jieba.lcut(i)
            print(i, o)

        print('-' * 42)
        jieba.set_dictionary(d_path)
        for i in location_str:
            o = jieba.lcut(i)
            print(i, o)
        os.remove(d_path)


if __name__ == '__main__':
    unittest.main()

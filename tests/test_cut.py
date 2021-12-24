# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""
import os
import unittest

import jieba
from companynameparser.tokenizer import hanlp_tokenize, jieba_tokenize
pwd_path = os.path.abspath(os.path.dirname(__file__))


class TestCut(unittest.TestCase):
    def test_cut_jieba(self):
        """jieba切词"""
        location_str = [
            "徐州九州通医药公司",
            "深圳光明区三晟电子商务中心"
        ]
        for i in location_str:
            o = jieba_tokenize(i)
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

    def test_hanlp(self):
        import hanlp
        import os
        os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
        HanLP = hanlp.load(hanlp.pretrained.mtl.CLOSE_TOK_POS_NER_SRL_DEP_SDP_CON_ELECTRA_SMALL_ZH)  # 世界最大中文语料库
        HanLP('商品和服务', tasks='tok')
        HanLP(['2021年HanLPv2.1为生产环境带来次世代最先进的多语种NLP技术。', '阿婆主来到北京立方庭参观自然语义科技公司。'])
        print(HanLP('商品和服务项目', tasks=['tok/fine',"pos/pku"]))
        print(HanLP("商品和服务项目")["tok/fine"])
        print(HanLP(['2021年HanLPv2.1为生产环境带来次世代最先进的多语种NLP技术。', '阿婆主来到北京立方庭参观自然语义科技公司。']))

    def test_cut_hanlp(self):
        """hanlp切词"""
        location_str = [
            "徐州九州通医药公司",
            "深圳光明区三晟电子商务中心",
            "佛山市立业思医疗用品有限公司"
        ]
        for i in location_str:
            o = hanlp_tokenize(i)
            print(o)


if __name__ == '__main__':
    unittest.main()

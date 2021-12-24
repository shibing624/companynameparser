# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""
import sys
import unittest

sys.path.append('..')
import companynameparser


class TestCus(unittest.TestCase):
    def test_custom_split(self):
        """测试公司名自定义切分文件"""
        company_strs = [
            "沧州嘉诺温室大棚设施有限公司",
            "深圳光明区三晟有限公司",
            "深圳光明区三晟股份有限公司",
            "山西安健堂健康管理有限公司",
            "西咸新区沣东新城未科诚百货店",
            "朝阳县大山苗圃",
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

        print("-" * 42)
        companynameparser.set_custom_split_file('../examples/custom_name_split.txt')
        res = []
        for i in company_strs:
            r = companynameparser.parse(i)
            print(r)
            res.append(r)

        def _assert_line(linenum, p, b, t, s, sy):
            assert res[linenum]['place'] == p
            assert res[linenum]['brand'] == b
            assert res[linenum]['trade'] == t
            assert res[linenum]['suffix'] == s
            assert res[linenum]['symbol'] == sy

        _assert_line(0, '沧州', '嘉诺', '温室大棚设施', '有限公司', '')
        _assert_line(1, '深圳光明区', '三晟', '', '有限公司', '')
        _assert_line(2, '深圳光明区', '三晟', '', '股份有限公司', '')
        _assert_line(3, '山西', '安健堂', '健康管理', '有限公司', '')
        _assert_line(4, '西咸新区沣东新城', '未科诚', '', '百货店', '')
        _assert_line(5, '朝阳县', '大山', '苗圃', '', '')
        _assert_line(6, '昆山千灯镇', '南野', '智能科技', '店', '')
        _assert_line(7, '武陟县', '大唛', '副食', '门市部', '')
        _assert_line(8, '贵州', '', '民族酒业,销售', '集团,有限公司', '（,）')
        _assert_line(9, '玉田县鸦鸿桥镇', '凯翔', '', '商店', '')
        _assert_line(10, '桐乡市梧桐', '卓继宇文', '', '贸易商行', '')
        _assert_line(11, '大厂回族自治县祁各庄镇', '宝艺大唐', '艺术', '行', '')


if __name__ == '__main__':
    unittest.main()

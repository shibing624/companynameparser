# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""

import os

import pandas as pd

from companyparser.logger import logger
from companyparser.tokenizer import segment

pwd_path = os.path.abspath(os.path.dirname(__file__))
# 地址文件
place_path = os.path.join(pwd_path, 'data/china_place.txt')
# 商标文件
brand_path = os.path.join(pwd_path, 'data/brand.txt')
# 行业文件
trade_path = os.path.join(pwd_path, 'data/trade.txt')
# 后缀文件
suffix_path = os.path.join(pwd_path, 'data/suffix.txt')


def load_dict(file_path):
    res = dict()
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            terms = line.split()
            if len(terms) == 2:
                key = terms[0]
                val = terms[1]
            elif len(terms) == 1:
                key = terms[0]
                val = '1'
            else:
                continue
            res[key] = val
    return res


def findall(string, s):
    """
    Find all str index
    :param string:
    :param s:
    :return: indies
    """
    res = []
    index = 0
    while True:
        index = string.find(s, index)
        if index != -1:
            res.append(index)
            index += len(s)
        else:
            break
    return res


class NameParser:
    """
    Name Parser for Company Name
    """

    def __init__(self,
                 place_file=place_path,
                 brand_file=brand_path,
                 trade_file=trade_path,
                 suffix_file=suffix_path
                 ):
        self.name = 'company_name_parser'
        self.place_file = place_file
        self.brand_file = brand_file
        self.trade_file = trade_file
        self.suffix_file = suffix_file
        self.places = None
        self.brands = None
        self.trades = None
        self.suffixes = None
        self.symbols = ['《', '》', '（', '）', '(', ')']
        self.inited = False

    def init(self):
        if not self.inited:
            self.places = load_dict(self.place_file)
            self.brands = load_dict(self.brand_file)
            self.trades = load_dict(self.trade_file)
            self.suffixes = load_dict(self.suffix_file)
            self.inited = True
            logger.debug('dict load ok.')

    @staticmethod
    def is_english_char(ch):
        if ord(ch) not in (97, 122) and ord(ch) not in (65, 90):
            return False
        return True

    def _extract_token(self, words, data_dict):
        """
        Extract token words
        :param words: query segmented words
        :return: tuple(token, left_words)
        """
        self.init()
        res = [w for w in words if w in data_dict]
        left_words = [w for w in words if w not in res]
        return res, left_words

    def _extract_brand(self, words):
        """
        Extract Company name brand words
        :param words: query segmented words
        :return: tuple(brand, left_words)
        """
        self.init()
        return words

    def parse_one(self, name):
        name = name.strip()
        res = {'input': name, 'place': '', 'brand': '', 'trade': '', 'suffix': '', 'symbol': ''}
        # English company name
        if not name or self.is_english_char(name[0]):
            return res

        self.init()
        words = segment(name, pos=False, cut_type='word')

        symbols, left_words = self._extract_token(words, self.symbols)
        places, left_words = self._extract_token(left_words, self.places)
        suffixes, left_words = self._extract_token(left_words, self.suffixes)
        trades, left_words = self._extract_token(left_words, self.trades)
        brands = self._extract_brand(left_words)
        res['place'] = ','.join(places)
        res['brand'] = ''.join(brands)
        res['trade'] = ''.join(trades)
        res['suffix'] = ','.join(suffixes)
        res['symbol'] = ','.join(symbols)

        return res

    def parse(self, names):
        """
        Parse Company Names
        :param names:
        :return: DataFrame
        """
        result = pd.DataFrame([self.parse_one(name) for name in names])
        return result


if __name__ == '__main__':
    m = NameParser()
    a = [
        "灵动生物科技（舟山）有限公司（北京）分公司",
        "北京华颜健康咨询有限公司",
        "南通市崇川区百媚美容生活馆",
        "吉林省美华生物科技有限公司",
        "京口区恒湶钻井工程施工服务部",
        "南京漫天美容服务有限公司",
        "天津利亚科技有限公司",
        "南京诺申网络科技有限公司",
        "温县甘淳电子商务有限公司",
        "安徽陛颜祛斑技术研究有限公司",
        "佛山市顺德信元生物科技有限公司",
        "昆明享亚教育信息咨询有限公司",
        " 淮安迈捷生物科技有限公司",
        "南京佰达隆电子科技有限公司",
        "成都锤子科技有限公司",
        "上海览康贸易有限公司",
    ]
    w = m.parse(a)
    print(a)
    print(w)

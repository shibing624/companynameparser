# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""

import os

from companynameparser.logger import logger
from companynameparser.tokenizer import jieba_tokenize

pwd_path = os.path.abspath(os.path.dirname(__file__))
# 地址文件
place_path = os.path.join(pwd_path, 'data/china_place.txt')
# 地址补充文件，单字类
place_single_path = os.path.join(pwd_path, 'data/place_single.txt')
# 商标文件
brand_path = os.path.join(pwd_path, 'data/brand.txt')
# 行业文件
trade_path = os.path.join(pwd_path, 'data/trade.txt')
# 行业补充文件，单字类
trade_single_path = os.path.join(pwd_path, 'data/trade_single.txt')
# 后缀文件
suffix_path = os.path.join(pwd_path, 'data/suffix.txt')
# 后缀补充文件，单字类
suffix_single_path = os.path.join(pwd_path, 'data/suffix_single.txt')
# 词语分隔符，split word by comma
split_sep = ','


class Parser:
    """
    Name Parser for Company Name
    """

    def __init__(self,
                 place_file=place_path,
                 brand_file=brand_path,
                 trade_file=trade_path,
                 suffix_file=suffix_path,
                 place_single_file=place_single_path,
                 trade_single_file=trade_single_path,
                 suffix_single_file=suffix_single_path,
                 custom_name_split_file='',
                 ):
        self.name = 'company_name_parser'
        self.place_file = place_file
        self.brand_file = brand_file
        self.trade_file = trade_file
        self.suffix_file = suffix_file
        self.place_single_file = place_single_file
        self.trade_single_file = trade_single_file
        self.suffix_single_file = suffix_single_file
        self.custom_name_split_file = custom_name_split_file
        self.places = None
        self.brands = None
        self.trades = None
        self.suffixes = None
        self.place_single = None
        self.trade_single = None
        self.suffix_single = None
        self.custom_name_split = None
        self.symbols = ['《', '》', '（', '）', '(', ')']
        self.inited = False

    def init(self):
        if not self.inited:
            self.places = self.load_dict(self.place_file)
            self.brands = self.load_dict(self.brand_file)
            self.trades = self.load_dict(self.trade_file)
            self.suffixes = self.load_dict(self.suffix_file)
            self.place_single = self.load_dict(self.place_single_file)
            self.trade_single = self.load_dict(self.trade_single_file)
            self.suffix_single = self.load_dict(self.suffix_single_file)
            self.custom_name_split = self.load_name_split(self.custom_name_split_file)
            self.inited = True
            logger.debug('dict load ok.')

    def set_custom_split_file(self, file_path):
        self.custom_name_split_file = file_path
        self.custom_name_split = self.load_name_split(self.custom_name_split_file)
        logger.debug('set_custom_split_file done, custom_name_split size: {}'.format(len(self.custom_name_split)))

    @staticmethod
    def load_dict(file_path):
        res = dict()
        if file_path and os.path.exists(file_path):
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

    @staticmethod
    def load_name_split(file_path):
        res = dict()
        if file_path and os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    terms = line.split(' ')
                    if line.startswith('#') or len(terms) <= 1:
                        continue
                    # Company_name place brand trade suffix symbol
                    name = terms[0]
                    place = terms[1] if len(terms) >= 2 else ''
                    brand = terms[2] if len(terms) >= 3 else ''
                    trade = terms[3] if len(terms) >= 4 else ''
                    suffix = terms[4] if len(terms) >= 5 else ''
                    symbol = terms[5] if len(terms) >= 6 else ''
                    res[name] = {'place': place,
                                 'brand': brand,
                                 'trade': trade,
                                 'suffix': suffix,
                                 'symbol': symbol}
        return res

    @staticmethod
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

    @staticmethod
    def is_english_char(ch):
        if ord(ch) not in (97, 122) and ord(ch) not in (65, 90):
            return False
        return True

    @staticmethod
    def _extract_token(tokens, data_dict):
        """
        Extract token words
        :param tokens: query segmented words
        :param data_dict: dict
        :return: tuple(token, left_words)
        """
        res = []
        left_words = []
        for w, p, q in tokens:
            if w in data_dict:
                res.append((w, p, q))
            else:
                left_words.append((w, p, q))
        return res, left_words

    @staticmethod
    def link_near_words(tokens):
        new_tokens = []
        if not tokens:
            return new_tokens
        i = 0
        w, p, q = tokens[i]
        while i < len(tokens):
            i += 1
            if i == len(tokens):
                new_tokens.append((w, p, q))
            else:
                w_i, p_i, q_i = tokens[i]
                # next word near before word
                if p_i == q:
                    w = w + w_i
                    p = p
                    q = q_i
                else:
                    new_tokens.append((w, p, q))
                    w, p, q = tokens[i]
        return new_tokens

    def _extract_brand(self, left_words, places, trades, suffixes):
        """
        Extract Company name brand words
        :param left_words: query segmented words
        :param places: places
        :param trades: trades
        :param suffixes: suffixes
        :return: tuple(brand, left_words)
        """
        brands = []
        brand_tokens, left_tokens = self._extract_token(left_words, self.brands)

        lefts = []
        for w, p, q in left_tokens:
            if len(w) == 1:
                # Single word
                if w in self.trade_single:
                    trades.append((w, p, q))
                elif w in self.place_single:
                    places.append((w, p, q))
                elif w in self.suffix_single:
                    suffixes.append((w, p, q))
                else:
                    lefts.append((w, p, q))
            else:
                if w[-1] in self.place_single:
                    places.append((w, p, q))
                else:
                    lefts.append((w, p, q))
        brands.extend(brand_tokens)
        brands.extend(lefts)
        if len(brands) > 1:
            # Deal with link near words
            brands.sort(key=lambda k: k[1])
            brands = self.link_near_words(brands)
        return brands, places, trades, suffixes

    @staticmethod
    def _get_leave_tokens(tokens, start, end):
        """
        String out of [start, end]
        :param tokens: list, [(word, start_idx, end_idx),...]
        :param start: int, start_idx
        :param end: int, end_idx
        :return: list, < start_idx || > end_idx
        """
        res = []
        for w, p, q in tokens:
            if p < start:
                res.append((w, p, q))
            elif p >= end:
                res.append((w, p, q))
        return res

    def parse(self, name, pos_sensitive=False, enable_word_segment=False, **kwargs):
        """
        Parse One Record
        :param name: Company name
        :param pos_sensitive: if True, output position index; default False
        :param enable_word_segment: if True, output word split by comma, else no comma; default False
        :return: dict
        """
        name = name.strip()
        res = {'place': '', 'brand': '', 'trade': '', 'suffix': '', 'symbol': ''}
        # English company name
        if not name or self.is_english_char(name[0]):
            return res

        self.init()
        places, brands, trades, suffixes, symbols = [], [], [], [], []
        # Tokens: [(word, start_index, end_index), ...]
        tokens = jieba_tokenize(name)

        if self.custom_name_split:
            # Custom name split
            for k, v in self.custom_name_split.items():
                start = name.find(k)
                if start > -1:
                    end = start + len(k)
                    tokens = self._get_leave_tokens(tokens, start, end)
                    place_len = len(v['place'])
                    brand_len = len(v['brand'])
                    trade_len = len(v['trade'])
                    suffix_len = len(v['suffix'])
                    c_places = [(v['place'], start, start + place_len)] if place_len > 0 else []
                    c_brands = [(v['brand'], start + place_len, start + place_len + brand_len)] if brand_len > 0 else []
                    c_trades = [(v['trade'], start + place_len + brand_len,
                                 start + place_len + brand_len + trade_len)] if trade_len > 0 else []
                    c_suffixes = [(v['suffix'], start + place_len + brand_len + trade_len,
                                   start + place_len + brand_len + trade_len + suffix_len)] if suffix_len > 0 else []
                    places.extend(c_places)
                    brands.extend(c_brands)
                    trades.extend(c_trades)
                    suffixes.extend(c_suffixes)
                    break

        if tokens:
            # Extract token order: symbol, place, suffix, trade, brand
            t_symbols, left_words = self._extract_token(tokens, self.symbols)
            t_places, left_words = self._extract_token(left_words, self.places)
            t_suffixes, left_words = self._extract_token(left_words, self.suffixes)
            t_trades, left_words = self._extract_token(left_words, self.trades)
            t_brands, t_places, t_trades, t_suffixes = self._extract_brand(left_words, t_places, t_trades, t_suffixes)
            places.extend(t_places)
            brands.extend(t_brands)
            trades.extend(t_trades)
            suffixes.extend(t_suffixes)
            symbols.extend(t_symbols)

        # Sort token idx
        if len(places) > 1:
            places.sort(key=lambda k: k[1])
        if len(brands) > 1:
            brands.sort(key=lambda k: k[1])
        if len(trades) > 1:
            trades.sort(key=lambda k: k[1])
        if len(suffixes) > 1:
            suffixes.sort(key=lambda k: k[1])

        # Link split tokens
        if not enable_word_segment:
            places = self.link_near_words(places)
            brands = self.link_near_words(brands)
            trades = self.link_near_words(trades)
            suffixes = self.link_near_words(suffixes)

        # Pos Sensitive Enable
        res['place'] = places if pos_sensitive else split_sep.join([w[0] for w in places])
        res['brand'] = brands if pos_sensitive else split_sep.join([w[0] for w in brands])
        res['trade'] = trades if pos_sensitive else split_sep.join([w[0] for w in trades])
        res['suffix'] = suffixes if pos_sensitive else split_sep.join([w[0] for w in suffixes])
        res['symbol'] = symbols if pos_sensitive else split_sep.join([w[0] for w in symbols])

        return res

# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""
from companynameparser import parser
import os
company_name_file = 'Company-Names-Corpus-480W-shuf.txt'
organ_name_file = 'Organization-Names-Corpus-110w-shuf.txt'
domain_name_file = '../data/company_demo.txt'


def load_file(file_path, limit_size=2000):
    subs = []
    count = 0
    if not os.path.exists(file_path):
        return subs
    with open(file_path, 'r', encoding='utf-8') as fr:
        for line in fr:
            i = line.strip()
            subs.append(i)
            count += 1
            if 0 < limit_size < count:
                break
    return subs


def main():
    c1 = load_file(company_name_file, limit_size=0)
    c2 = load_file(organ_name_file, limit_size=0)
    c3 = load_file(domain_name_file, limit_size=10)

    # c = c3 + c1
    c = c3
    m = parser.Parser()
    horizontal_file = 'hor_train.txt'
    vertical_file = 'ver_train.txt'

    horizontal_bio(m, c, horizontal_file)
    vertical_bio(horizontal_file, vertical_file)


def horizontal_bio(model, input_list, horizontal_file):
    with open(horizontal_file, 'w', encoding='utf-8') as fw:
        # for i, p, b, t, s, sy in zip(c, df['place'], df['brand'], df['trade'], df['suffix'], df['symbol']):
        for i in input_list:
            r = model.parse(i, pos_sensitive=False)
            b = r['brand'].split(",")[0]
            if not b:
                continue
            brand_idx = i.index(b)
            if brand_idx > -1:
                brand_start = brand_idx
                brand_len = len(b)
                if brand_len == 1:
                    continue
                out = ' '.join(['O'] * brand_start + ['B'] + ['I'] * (brand_len - 1) + ['O'] * (
                        len(i) - brand_start - brand_len))
            else:
                out = ' '.join(['O'] * len(i))
            fw.write(i + '\t' + out + '\n')
            print(i + '\t' + ' '.join([r['place'], r['brand'], r['trade'], r['suffix']]))
            print(i + '\t' + out)


def vertical_bio(horizontal_file, out_vertical_file):
    with open(horizontal_file, 'r', encoding='utf-8') as f, open(out_vertical_file, 'w', encoding='utf-8') as fw:
        for line in f:
            line = line.strip()
            terms = line.split('\t')
            chars = list(terms[0])
            tags = terms[1].split(' ')
            if len(chars) != len(tags):
                continue
            for i in range(len(chars)):
                fw.write(chars[i] + '\t' + tags[i] + '\n')
            fw.write('\n')


if __name__ == '__main__':
    main()

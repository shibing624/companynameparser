# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""
import os

from companynameparser import parser


def predict_tags(input_list, predict_file):
    model = parser.Parser()
    with open(predict_file, 'w', encoding='utf-8') as f:
        for line in input_list:
            r = model.parse(line, pos_sensitive=False)
            b = r['brand']
            f.write(line + '\t' + b + '\n')


def load_file(file_path, limit_size=20):
    subs = []
    count = 0
    if not os.path.exists(file_path):
        return subs
    with open(file_path, 'r', encoding='utf-8') as fr:
        for line in fr:
            i = line.strip().split()[0]
            if i:
                count += 1
                subs.append(i)
            if 0 < limit_size <= count:
                break
    return subs


def horizontal_bio(predict_result_file, horizontal_file):
    with open(predict_result_file, 'r', encoding='utf-8') as fr, open(horizontal_file, 'w', encoding='utf-8') as fw:
        for line in fr:
            terms = line.split()
            i = terms[0]
            b = terms[1].strip().split(',')[0] if len(terms) == 2 else ''
            if b:
                brand_idx = i.index(b)
                if brand_idx > -1:
                    brand_start = brand_idx
                    brand_len = len(b)
                    if brand_len == 1:
                        continue
                    out = ' '.join(['O'] * brand_start + ['B-ORG'] + ['I-ORG'] * (brand_len - 1) + ['O'] * (
                            len(i) - brand_start - brand_len))
            else:
                out = ' '.join(['O'] * len(i))
            fw.write(i + '\t' + out + '\n')
            print(i + '\t' + out)


def vertical_bio(horizontal_file, out_vertical_file):
    with open(horizontal_file, 'r', encoding='utf-8') as fr, open(out_vertical_file, 'w', encoding='utf-8') as fw:
        for line in fr:
            line = line.strip()
            terms = line.split('\t')
            chars = list(terms[0])
            tags = terms[1].split(' ')
            if len(chars) != len(tags):
                continue
            for i in range(len(chars)):
                fw.write(chars[i] + '\t' + tags[i] + '\n')
            fw.write('\n')


def main():
    domain_name_file = '../data/company_demo.txt'
    # predict_file format: sentence '\t' brand1,brand2
    predict_file = 'sentence_brands.txt'
    horizontal_file = 'hor_train.txt'
    vertical_file = 'ver_train.txt'
    c = load_file(domain_name_file, limit_size=10)
    # predict, output brand name
    predict_tags(c, predict_file)
    # to bio
    horizontal_bio(predict_file, horizontal_file)
    # to vertical bio
    vertical_bio(horizontal_file, vertical_file)


if __name__ == '__main__':
    main()

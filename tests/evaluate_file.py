# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""
import sys

sys.path.append('..')

import companynameparser

if __name__ == '__main__':
    right = 0
    wrong = 0
    count = 0
    right_all = 0
    right_right = 0
    with open('groundtruth.txt', 'r', encoding='utf-8') as fr:
        for line in fr:
            terms = line.split()
            count += 1
            name = terms[0]
            ground = terms[1] if len(terms) == 2 else ''
            r = companynameparser.parse(name)
            predict = r['brand']
            if ground:
                right_all += 1
                if predict == ground:
                    right_right += 1
            if predict == ground:
                right += 1
            else:
                wrong += 1
                print('[wrong]', line.strip() + ' Predict: ' + predict)
    acc = right / count
    recall = right_right / right_all
    print('count: ', count, 'acc:', acc, ' recall:', recall)

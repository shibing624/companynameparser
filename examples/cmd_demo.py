# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""
import os

import companynameparser


def parse(names):
    """
    Turns address list into province, city, country and street.
    :param names: list of address
    :return: list of place, brand, trade, suffix
    """
    result = []
    df = companynameparser.parse(names)

    for map_key in zip(df["place"], df["brand"], df["trade"], df["suffix"]):
        result.append('\t'.join([map_key[0], map_key[1], map_key[2], map_key[3]]))
    return result



if __name__ == '__main__':
    origin_path = os.path.join(os.path.dirname(__file__), '../tests/company_demo.txt')

    lines = []
    with open(origin_path, 'r', encoding='utf-8') as f:
        for line in f:
            lines.append(line.strip())

    print('{} lines in input'.format(len(lines)))
    parsed = parse(lines)
    count = 0
    with open('name_processed.txt', 'w', encoding='utf-8') as f:
        for i, o in zip(lines, parsed):
            count += 1
            f.write(i + '\t' + o + '\n')
    print('{} lines in output'.format(count))

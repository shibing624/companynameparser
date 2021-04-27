# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""
import argparse

import companynameparser


def parse(names):
    """
    Turns address list into province, city, country and street.
    :param names: list of address
    :return: list of place, brand, trade, suffix
    """
    result = []
    for name in names:
        r = companynameparser.parse(name)
        result.append('\t'.join([r['place'], r['brand'], r['trade'], r['suffix']]))
    return result


def main(**kwargs):
    """
    Cmd script of addressparser. Input address file, output extracted province, city country and street.
    :param kwargs: input, a text file object that will be read from. Should contain address data, one address per line
    :param output: a text file object where parsed output will be written. Parsed output will be similar to CSV data
    :type input: text file object in read mode
    :type output: text file object in write mode
    :return:
    """
    lines = []
    with open(kwargs['input'], 'r', encoding='utf-8') as f:
        for line in f:
            lines.append(line.strip())

    print('{} lines in input'.format(len(lines)))
    parsed = parse(lines)
    count = 0
    with open(kwargs['output'], 'w', encoding='utf-8') as f:
        for i, o in zip(lines, parsed):
            count += 1
            f.write(i + '\t' + o + '\n')
    print('{} lines in output'.format(count))


def run():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input', type=str,
                        help='the input file path, file encode need utf-8.')
    parser.add_argument('-o', '--output', type=str, required=True,
                        help='the output file path.')
    args = parser.parse_args()
    main(**vars(args))


if __name__ == '__main__':
    run()

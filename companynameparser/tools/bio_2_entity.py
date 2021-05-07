# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""
import sys


def get_entity_from_bio(chars, tags):
    """
    从BIO结果中获取brand
    """
    chunks = []
    current = None
    if len(chars) != len(tags):
        return chunks
    for i, tag in enumerate(tags):
        if tag == 'B-ORG':
            if current is not None and len(current) > 1:
                chunks.append(''.join(current))
            current = [chars[i]]
        elif tag == 'I-ORG':
            if current is not None:
                current.append(chars[i])
        elif tag == 'O':
            if current is not None and len(current) > 1:
                chunks.append(''.join(current))
            current = None
    if current is not None and len(current) > 1:
        chunks.append(''.join(current))
    return chunks


if __name__ == "__main__":
    for line in sys.stdin:
        line = line.strip()
        terms = line.split('\t')
        chars = terms[0]
        tags = terms[1].split(" ")
        chunks = get_entity_from_bio(list(chars), tags)
        print(chars + " " + " ".join(chunks))

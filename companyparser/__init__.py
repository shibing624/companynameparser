# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""

from companyparser import nameparser
from companyparser.nameparser import NameParser

__version__ = "0.1.1"

np = NameParser()
parse = np.parse
parse_one = np.parse_one

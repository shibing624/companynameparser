# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""

from companynameparser import parser
from companynameparser.parser import Parser

__version__ = "0.1.5"

np = Parser()
parse = np.parse
set_custom_split_file = np.set_custom_split_file

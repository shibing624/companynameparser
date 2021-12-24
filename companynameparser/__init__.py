# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""

from companynameparser import parser
from companynameparser.parser import Parser

__version__ = "0.1.7"

par = Parser()
parse = par.parse
set_custom_split_file = par.set_custom_split_file

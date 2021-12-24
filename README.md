# companynameparser
[![PyPI version](https://badge.fury.io/py/companynameparser.svg)](https://badge.fury.io/py/companynameparser)
[![Contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![License Apache 2.0](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)
![Language](https://img.shields.io/badge/Language-Python-blue.svg)
![Python3](https://img.shields.io/badge/Python-3.X-red.svg)

company name parser, extract company name brand. 中文公司名称分词工具，支持公司名称中的地名，品牌名（主词），行业词，公司名后缀提取。

**Guide**

- [Feature](#Feature)
- [Install](#Install)
- [Usage](#usage)
- [Command Line Usage](#command-line-usage)
- [Contribute](#contribute)
- [Reference](#Reference)

# Feature

对公司名文本解析，识别并提取地名、品牌名、行业词、公司名后缀词。

# Evaluate

运行评估脚本[evaluate_file.py](./tests/evaluate_file.py)，使用预测结果与GroundTruth完成相等才为算对的保守评估方法，
评估结果：
- 准确率：97.0%
- 召回率：96.7%

# Install

- 全自动安装：pip install companynameparser
- 半自动安装：
```
git clone https://github.com/shibing624/companynameparser.git
cd companynameparser
python setup.py install
```
通过以上两种方法的任何一种完成安装都可以。如果不想安装，可以下载github源码包，安装依赖[requirements.txt](./requirements.txt)再使用。

# Usage

- Extract Company Name

公司名称各元素提取功能[base_demo.py](./examples/base_demo.py)

```python
import companynameparser

company_strs = [
    "武汉海明智业电子商务有限公司",
    "泉州益念食品有限公司",
    "常州途畅互联网科技有限公司合肥分公司",
    "昆明享亚教育信息咨询有限公司",
]
for name in company_strs:
    r = companynameparser.parse(name)
    print(r)
```

output:
```
{'place': '武汉', 'brand': '海明智业', 'trade': '电子商务', 'suffix': '有限公司', 'symbol': ''}
{'place': '泉州', 'brand': '益念', 'trade': '食品', 'suffix': '有限公司', 'symbol': ''}
{'place': '常州,合肥', 'brand': '途畅', 'trade': '互联网科技', 'suffix': '有限公司,分公司', 'symbol': ''}
{'place': '昆明', 'brand': '享亚', 'trade': '教育信息咨询', 'suffix': '有限公司', 'symbol': ''}
```
> `parse`方法的此处输入`name`是str;

> 输出的是一个包括place(地名)，brand(品牌名)，trade(行业词名)，suffix(后缀名)，symbol(标点符号)的dict; 多个地名词、品牌、行业词之间用`,`间隔，如`'常州,合肥'`。

- All Demo

一个demo演示所有示例[all_demo.py](./examples/all_demo.py)，包括：
1. 公司名称各元素提取
2. 元素名称结果带分词
3. 显示各元素的位置
4. 用户自定义分词词典，用于解决部分误杀和漏召回

```python

import companynameparser

company_strs = [
    "武汉海明智业电子商务有限公司",
    "泉州益念食品有限公司",
    "常州途畅互联网科技有限公司合肥分公司",
    "昆明享亚教育信息咨询有限公司",
    "深圳光明区三晟股份有限公司",
]
for name in company_strs:
    r = companynameparser.parse(name)
    print(r)

print("*" * 42, ' enable word segment')
for name in company_strs:
    r = companynameparser.parse(name, pos_sensitive=False, enable_word_segment=True)
    print(r)

print("*" * 42, ' pos sensitive')
for name in company_strs:
    r = companynameparser.parse(name, pos_sensitive=True, enable_word_segment=False)
    print(r)

print("*" * 42, 'enable word segment and pos')
for name in company_strs:
    r = companynameparser.parse(name, pos_sensitive=True, enable_word_segment=True)
    print(r)

print("*" * 42, 'use custom name')
companynameparser.set_custom_split_file('./custom_name_split.txt')
for i in company_strs:
    r = companynameparser.parse(i)
    print(r)
```

output:
```
{'place': '武汉', 'brand': '海明智业', 'trade': '电子商务', 'suffix': '有限公司', 'symbol': ''}
{'place': '泉州', 'brand': '益念', 'trade': '食品', 'suffix': '有限公司', 'symbol': ''}
{'place': '常州,合肥', 'brand': '途畅', 'trade': '互联网科技', 'suffix': '有限公司,分公司', 'symbol': ''}
{'place': '昆明', 'brand': '享亚', 'trade': '教育信息咨询', 'suffix': '有限公司', 'symbol': ''}
{'place': '深圳光明', 'brand': '区三晟', 'trade': '', 'suffix': '股份有限公司', 'symbol': ''}
******************************************  enable word segment
{'place': '武汉', 'brand': '海明智业', 'trade': '电子商务', 'suffix': '有限公司', 'symbol': ''}
{'place': '泉州', 'brand': '益念', 'trade': '食品', 'suffix': '有限公司', 'symbol': ''}
{'place': '常州,合肥', 'brand': '途畅', 'trade': '互联网,科技', 'suffix': '有限公司,分公司', 'symbol': ''}
{'place': '昆明', 'brand': '享亚', 'trade': '教育,信息,咨询', 'suffix': '有限公司', 'symbol': ''}
{'place': '深圳,光明', 'brand': '区三晟', 'trade': '', 'suffix': '股份,有限公司', 'symbol': ''}
******************************************  pos sensitive
{'place': [('武汉', 0, 2)], 'brand': [('海明智业', 2, 6)], 'trade': [('电子商务', 6, 10)], 'suffix': [('有限公司', 10, 14)], 'symbol': []}
{'place': [('泉州', 0, 2)], 'brand': [('益念', 2, 4)], 'trade': [('食品', 4, 6)], 'suffix': [('有限公司', 6, 10)], 'symbol': []}
{'place': [('常州', 0, 2), ('合肥', 13, 15)], 'brand': [('途畅', 2, 4)], 'trade': [('互联网科技', 4, 9)], 'suffix': [('有限公司', 9, 13), ('分公司', 15, 18)], 'symbol': []}
{'place': [('昆明', 0, 2)], 'brand': [('享亚', 2, 4)], 'trade': [('教育信息咨询', 4, 10)], 'suffix': [('有限公司', 10, 14)], 'symbol': []}
{'place': [('深圳光明', 0, 4)], 'brand': [('区三晟', 4, 7)], 'trade': [], 'suffix': [('股份有限公司', 7, 13)], 'symbol': []}
****************************************** enable word segment and pos
{'place': [('武汉', 0, 2)], 'brand': [('海明智业', 2, 6)], 'trade': [('电子商务', 6, 10)], 'suffix': [('有限公司', 10, 14)], 'symbol': []}
{'place': [('泉州', 0, 2)], 'brand': [('益念', 2, 4)], 'trade': [('食品', 4, 6)], 'suffix': [('有限公司', 6, 10)], 'symbol': []}
{'place': [('常州', 0, 2), ('合肥', 13, 15)], 'brand': [('途畅', 2, 4)], 'trade': [('互联网', 4, 7), ('科技', 7, 9)], 'suffix': [('有限公司', 9, 13), ('分公司', 15, 18)], 'symbol': []}
{'place': [('昆明', 0, 2)], 'brand': [('享亚', 2, 4)], 'trade': [('教育', 4, 6), ('信息', 6, 8), ('咨询', 8, 10)], 'suffix': [('有限公司', 10, 14)], 'symbol': []}
{'place': [('深圳', 0, 2), ('光明', 2, 4)], 'brand': [('区三晟', 4, 7)], 'trade': [], 'suffix': [('股份', 7, 9), ('有限公司', 9, 13)], 'symbol': []}
****************************************** use custom name
{'place': '武汉', 'brand': '海明智业', 'trade': '电子商务', 'suffix': '有限公司', 'symbol': ''}
{'place': '泉州', 'brand': '益念', 'trade': '食品', 'suffix': '有限公司', 'symbol': ''}
{'place': '常州,合肥', 'brand': '途畅', 'trade': '互联网科技', 'suffix': '有限公司,分公司', 'symbol': ''}
{'place': '昆明', 'brand': '享亚', 'trade': '教育信息咨询', 'suffix': '有限公司', 'symbol': ''}
{'place': '深圳光明区', 'brand': '三晟', 'trade': '', 'suffix': '股份有限公司', 'symbol': ''}

```

## Command Line Usage

<details>
<summary>命令行模式</summary>

支持批量提取地址的省市区信息：
```
python3 -m companynameparser company_demo.txt -o out.csv

usage: python3 -m companynameparser [-h] -o OUTPUT input
@description:

positional arguments:
  input                 the input file path, file encode need utf-8.

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        the output file path.
```
> 输入文件：`company_demo.txt`；输出文件：`out.csv`，地名、品牌名、行业名、后缀名以`\t`间隔

</details>

## Todo
- [x] 补充中国三级地名，优化地名提取效果
- [ ] 优化品牌名边界问题
- [ ] 多个行业词提取



## Contact

- Issue(建议)：[![GitHub issues](https://img.shields.io/github/issues/shibing624/companynameparser.svg)](https://github.com/shibing624/companynameparser/issues)
- 邮件我：xuming: xuming624@qq.com
- 微信我：加我*微信号：xuming624*, 进Python-NLP交流群，备注：*姓名-公司名-NLP*

<img src="docs/wechat.jpeg" width="200" />


## Citation

如果你在研究中使用了companynameparser，请按如下格式引用：

```latex
@software{companynameparser,
  author = {Xu Ming},
  title = {companynameparser: Company Name parser Tool},
  year = {2021},
  url = {https://github.com/shibing624/companynameparser},
}
```

## License

**Apache License 2.0**

## Contribute

项目代码还很粗糙，如果大家对代码有所改进，欢迎提交回本项目
，在提交之前，注意以下两点：

 - 在`tests`添加相应的单元测试
 - 使用`python setup.py test`来运行所有单元测试，确保所有单测都是通过的

之后即可提交PR。

## Reference

* [addressparser](https://github.com/shibing624/addressparser)

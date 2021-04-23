# companynameparser
company name parser, extract company name brand. 中文公司名称分词工具，支持公司名称中的地名，品牌名（主词），行业词，公司名后缀提取。

# Feature

对公司名文本解析，识别并提取地名、品牌名、行业词、公司名后缀词。

# Evaluate

评估结果：
- 准确率：
- 召回率：

# Install

- 全自动安装：pip install companynameparser
- 半自动安装：
```
git clone https://github.com/shibing624/companynameparser.git
cd companynameparser
python setup.py install
```
通过以上两种方法的任何一种完成安装都可以。如果不想安装，可以下载github源码包，安装下面依赖再使用。

# Usage

- Extract Company Name

```python
import companynameparser

company_strs = ["泉州益念食品有限公司",
                "武汉蓝天医院",
                "武汉海明智业电子商务有限公司",
                ]
df = companynameparser.parse(company_strs)
print(df)
```

output:
```
            input place brand trade suffix symbol
0      泉州益念食品有限公司    泉州    益念    食品   有限公司
1          武汉蓝天医院    武汉    蓝天           医院
2  武汉海明智业电子商务有限公司    武汉  海明智业  电子商务   有限公司
```
> 程序的此处输入`company_strs`可以是任意的可迭代类型，如list，tuple，set，pandas的Series类型等;

> 输出的`df`是一个Pandas的DataFrame类型变量，DataFrame可以非常轻易地转化为csv或者excel文件，Pandas的官方文档：http://pandas.pydata.org/pandas-docs/version/0.20/dsintro.html#dataframe


## Command line usage
- 命令行模式

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


## Todo
- [x] 补充中国三级地名，优化地名提取效果
- [ ] 优化品牌名边界问题
- [ ] 多个行业词提取


## Contribute

项目代码还很粗糙，如果大家对代码有所改进，欢迎提交回本项目
，在提交之前，注意以下两点：

 - 在`tests`添加相应的单元测试
 - 使用`python setup.py test`来运行所有单元测试，确保所有单测都是通过的

之后即可提交PR。

## Reference

* [addressparser](https://github.com/shibing624/addressparser)

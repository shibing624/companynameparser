# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""

# 兰州壹玖壹玖电子商务有限公司 壹玖壹
# 北京华颜健康咨询有限公司 北京华
# 河北新合作网络科技有限公司 新
# 山西安健堂健康管理有限公司 山健堂
# 山西安运安环科技有限公司 山运安环
# 邢台万生大药房 万生大
# 常州途畅互联网科技有限公司合肥分公司 途畅互联
# 钟楼区北港可诺丹婷美容院 北港可诺
# 南京市江北新区春之燕美容店 江北新区

from companynameparser import parser

a = [
    "合肥经济技术开发区妍丽雅服装店",
    "西咸新区沣东新城未科诚百货店",
    "信阳市羊山新区沐香干果食品店",
    "巴马寿夫人健康产业有限公司",
    "庄浪县域起土特产批发零售店",
    "唯尚品百货商场（杭州）淘宝店",
    "潍坊综合保税区御见名匠专业护肤中心",
    "观途（上海）旅游服务中心（有限合伙）",

    "山西安健堂健康管理有限公司",
    "邢台万生大药房",
    "常州途畅互联网科技有限公司合肥分公司",
    "钟楼区北港可诺丹婷美容院",
    "南京市江北新区春之燕美容店",
    "西安运安环科技有限公司",
    "北新合作网络科技有限公司",
    "波澜格网络科技有限公司常州第一分公司",
    " 淮安迈捷生物科技有限公司",
    "河北新合作网络科技有限公司",
    "南京佰达隆电子科技有限公司",
    "成都锤子科技有限公司",
    "上海览康贸易有限公司",
    "兰州壹玖壹玖电子商务有限公司",
    "北京华颜健康咨询有限公司",
]


def load_file(file_path):
    subs = []
    with open(file_path, 'r', encoding='utf-8') as fr:
        for line in fr:
            i = line.strip()
            subs.append(i)
    return subs


if __name__ == '__main__':
    bug_file = 'bug_0425.txt'
    b = load_file(bug_file)
    a = a + b
    m = parser.Parser()
    df = m.parse(a)
    for p, i, b, t, s in zip(a, df['place'], df['brand'], df['trade'], df['suffix']):
        print(p, i, b, t, s)

    print()
    df = m.parse(a, pos_sensitive=True)
    for p, i, b, t, s in zip(a, df['place'], df['brand'], df['trade'], df['suffix']):
        print(p, i, b, t, s)
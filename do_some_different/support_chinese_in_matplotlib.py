#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Time: 2020-01-01 16:09
# @Software: python
# @File: support_chinese_in_matplotlib.py
# @Author: Peter Ren
# @Contact: cnprogrammer@126.com
# @Site: 
# @IDE: PyCharm


import pandas as pd
import matplotlib.pyplot as plt

# 支持中文
import matplotlib.font_manager as fm
fonts = fm.FontProperties(fname=r'simsun.ttc')  # 设置字体，纯属测试
plt.title('纯属测试中文，从网络下载使用了simsun.tcc中文字体', fontproperties=fonts)
plt.xlabel('横轴', fontproperties=fonts)
plt.ylabel('纵轴', fontproperties=fonts)
plt.xticks(fontproperties=fonts)

data_dic = {
    'origin': [1, 2, 3, 4],
    'power 2': [1, 4, 9, 16]
}

df = pd.DataFrame(data_dic, index=['a-中文', 'b', 'c', 'd'])

print(df)

plt.plot(df.index.values, df['origin'])
plt.show()

# 我的测试，也许速度还是不太理想


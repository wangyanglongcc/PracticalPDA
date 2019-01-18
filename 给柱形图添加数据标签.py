# -*- coding: UTF-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
%matplotlib inline
plt.rcParams['font.sans-serif'] = ['SimHei'] # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号显示为方块的问题

plt.subplots(figsize=(16,6))
g = sns.barplot(x='cut',y='tmitemid',data=data)
# 利用循环添加数据标签
for i,j in enumerate(list(data['tmitemid'])):
    g.text(i,j*1.02,j)
g.set_title('R^2分布图');

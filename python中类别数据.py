
'''
好处：
1. 有层级顺序，比如铜<银<金,可以用来自定义排序。
2. 比普通的文本更节省空间，从而可以带来程序性能的优化改善。
'''

import pandas as pd
from pandas.api.types import CategoricalDtype
import random as rd
# 创建数据
areas = ['全部','华中','华南','华北']
custs = ['全部','进口水果','国产水果','水产']
codes = ['全部','樱桃','车厘子','花生']
df = pd.DataFrame([(area,cust,code) for area in areas for cust in custs for code in codes],
                  columns=['area','cust','code'])
df['rand'] = 1
df['rand'] = df['rand'].map(lambda x:x*rd.random())
df = df.sort_values(by='rand').drop('rand',axis='columns')# 乱序
df.sort_values(by=['area','cust','code'])
print(df.head())
# 	area	cust	code
# 42	华南	国产水果	车厘子
# 19	华中	全部	花生
# 32	华南	全部	全部
# 58	华北	国产水果	车厘子
# 50	华北	全部	车厘子
print(df.info())# 注意这里memory usage是2.0+ KB
# <class 'pandas.core.frame.DataFrame'>
# Int64Index: 64 entries, 42 to 29
# Data columns (total 3 columns):
# area    64 non-null object
# cust    64 non-null object
# code    64 non-null object
# dtypes: object(3)
# memory usage: 2.0+ KB
# None
for i in df.columns:
    cates = list(df[i].unique())
    try:
        cates.remove('全部')
    except:
        pass
    cates =['全部'] + cates
    cate_rank = CategoricalDtype(categories=cates, ordered=True)
    df[i] = df[i].astype(cate_rank)
df.sort_values(by=['area','cust','code']).head()
# 注意到这里是进行了排序
# 	area	cust	code
# 0	全部	全部	全部
# 2	全部	全部	车厘子
# 3	全部	全部	花生
# 1	全部	全部	樱桃
print(df.info())# 注意这里的memory usage变成了1.2 KB
# <class 'pandas.core.frame.DataFrame'>
# Int64Index: 64 entries, 42 to 29
# Data columns (total 3 columns):
# area    64 non-null category
# cust    64 non-null category
# code    64 non-null category
# dtypes: category(3)
# memory usage: 1.2 KB

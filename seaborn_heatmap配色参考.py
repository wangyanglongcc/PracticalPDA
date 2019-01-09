import pandas as pd
import matplot.pyplot as plt
import seaborn as sns
%matplotlib inline
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

f, ax = plt.subplots(figsize=(16, 6))
goods = set(items.loc[items['cor']>0,'tmitemid'])
corr = df.loc[df['tmitemid'].isin(goods),[y]+X].corr()
hm = sns.heatmap(round(corr,2), annot=True, ax=ax, cmap="coolwarm",fmt='.2f',vmin=-1,vmax=1,
                  linewidths=.05)
f.subplots_adjust(top=0.93)

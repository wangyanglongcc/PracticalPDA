import pandas as pd
import numpy as np
import seaborn as sns
import datetime as dt
import glob
import os
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import association_rules, apriori
# %matplotlib inline
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

# pre for mba
def mba(df):
    df['c'] = 1
    df = df.pivot_table(index=['orderid'],columns=['commodityname'],values='c',aggfunc='count').\
    fillna(0).reset_index(drop=True)
    for i in df.columns:
        df[i] = df[i].map(lambda x:1 if x>0 else 0)
    frequent_itemsets = apriori(df, min_support=0.01, use_colnames=True)
    result = association_rules(frequent_itemsets, metric='lift', min_threshold=1.0).\
    sort_values(by=['antecedents','lift'],ascending=False)
    return result
if __name__ == '__main__':
    # reach data
    path = r'E:\RFM'
    df = pd.read_pickle(os.path.join(path,'rfm_3cols.pickle'))
    # df['month'] = df['sk_createdateid'].map(lambda x:str(x)[:6])
    print(df.shape)
    # calucate
    res = pd.DataFrame()
    for idate in np.sort(df['sk_createdateid'].unique()):
        file = mba(df[df['sk_createdateid']==idate])
        file['sk_createdateid'] = idate
        res = res.append(file)
        print(idate,file.shape,res.shape)
    res.to_csv(os.path.join(path,'mba_res.txt'),sep='\t',index=False,encoding='utf-8')

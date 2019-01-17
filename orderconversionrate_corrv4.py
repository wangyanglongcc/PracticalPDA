# -*- coding: UTF-8 -*-
import pandas as pd
import numpy as np
import os
import statsmodels.api as sm
import warnings
import time
warnings.filterwarnings('ignore')
# -*- coding: UTF-8 -*-
import pandas as pd
import numpy as np
import os
import statsmodels.api as sm
import warnings
warnings.filterwarnings('ignore')
def linear_regression(file):
    X_value,y_value = file[X],file[y].values
    X_value = sm.add_constant(X_value)
    est = sm.OLS(y_value, X_value)
    est = est.fit()
    return est
def reg(df):
    try:
        # 相关系数
        for x in X:
            df['{}_corr'.format(x)] = np.corrcoef(df[y],df[x])[0,1]
        # 回归方程参数
        est = linear_regression(df)
        df['rsquared'] = est.rsquared if est.rsquared else None
        df['rsquared_adj'] = est.rsquared_adj if est.rsquared_adj else None
        df['const_param'] = est.params.loc['const'] if est.params.loc['const'] else None
        for x in X:
            df['{}_param'.format(x)] = est.params.loc[x] if est.params.loc[x] else None
    # cannot fit model
    except:
        pass
        # 相关系数
        # for x in X:
        #     df['{}_corr'.format(x)] = 'cannot fit model'
        # # 回归方程参数
        # est = linear_regression(df)
        # df['rsquared'] = 'cannot fit model'
        # df['rsquared_adj'] = 'cannot fit model'
        # df['const_param'] = 'cannot fit model'
        # for x in X:
        #     df['{}_param'.format(x)] = 'cannot fit model'
    return df
def load_and_clean(inputfile):
    print('-'*10 + 'start' + '-'*10)
    try:
        df = pd.read_pickle(inputfile)
    except:
        f = open(inputfile,'r+',encoding='utf-8')
        df = pd.read_csv(f,sep='\t')
        f.close()
    print('-'*10 + 'data was loaded!' + '-'*10)
    print('-'*10 + 'clean' + '-'*10)
    for i in [y] + X:
        try:
            df[i] = df[i].astype('float')
        except:
            print(i)
    return df
def main(inputfile):
    df = load_and_clean(inputfile)
    result = df.groupby(['warehousename','customcategoryname','highcategoryname','categoryname','tmitemid','tmname'],\
               group_keys=False,sort=False).apply(reg)
    # add predict value
    # result = result[result['rsquared']!='cannot fit model']
    result = result[result['rsquared'].notnull()]
    XP = ['{}_param'.format(i) for i in X]
    result['predict'] = np.sum(result[X].values * result[XP].values,axis=1) + result['const_param'].values
    result['cut'] = pd.cut(result['rsquared'],bins=[i/10 for i in range(11)])
    result.to_csv(os.path.join('\\'.join(inputfile.split('\\')[:-1]),'相关性计算结果V4.txt'),sep='\t',index=False,encoding='utf-8')
    return result

 
if __name__ == '__main__':
    tt = time.time()
    y = 'orderconversionrate'
    X = ['staytime','profit','discount','temp_max', 'temp_min', 'olduser_rate']#'amount', 'qty',
    inputfile = r'D:\PycharmProjects\转化率\data\zhl_after_clean.pickle'
    main(inputfile)
    print('All Done!共耗时{}s'.format(time.time()-tt))
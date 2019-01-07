# -*- coding: UTF-8 -*-
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression

def load_data():
    '''
    '''
    return df 

def reg(X,y):
    reg = LinearRegression()
    reg.fit(X, y)
    # 评估回归模型
    res = sm.add_constant(X)
    est = sm.OLS(y, res)
    est = est.fit()
    return est

def main():
    df = load_data()
    X,y = df['y'].values,df[['x1','x2','x3']]
    est = reg(X,y)
    print(est)
if __name__ == '__main__':
    main()

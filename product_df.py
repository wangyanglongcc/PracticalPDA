from itertools import product
import pandas as pd
from tabulate import tabulate


def product_df(df1, df2):
    columns = list(df1.columns) + list(df2.columns)
    ii = product(df1.values, df2.values)
    df = pd.DataFrame(((x for row in i for x in row) for i in ii), columns=columns)
    return df


if __name__ == '__main__':
    df1 = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
    df2 = pd.DataFrame({'c': [7, 8], 'd': [9, 10]})
    df = product_df(df1, df2)
    print(tabulate(df, headers=df.columns))

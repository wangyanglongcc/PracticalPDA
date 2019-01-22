import pandas as pd
# 从github上获取数据
url = 'https://raw.githubusercontent.com/wangyanglongcc/pandas_basic/master/data/iris.csv'
df = pd.read_csv(url)
# 使用列表生成式统计每列唯一值个数
ii = [(col,df[col].unique().size) for col in df.columns]
print(ii)
# [('sepal_length', 35), ('sepal_width', 23), ('petal_length', 43), ('petal_width', 22), ('class', 3)]
# 将生成的结果直接转成DataFrame
res = pd.DataFrame([(col, df[col].nunique()) for col in df.columns],columns=['col_name','value_unique'])
# col_name	value_unique
# 0	sepal_length	35
# 1	sepal_width	23
# 2	petal_length	43
# 3	petal_width	22
# 4	class	3

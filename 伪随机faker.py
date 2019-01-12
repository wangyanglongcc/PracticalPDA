from faker import Faker
fake = Faker(locale='zh_CN')

for i in range(100):
    print(i+1,fake.profile(fields=None, sex='M'),fake.phone_number())

# print(fake.chrome(version_from=13, version_to=63, build_from=800, build_to=899))
# import itertools
# words = ['A','B','C','D','E']
# ii = ['*' + '*'.join(i) + '*' for i in itertools.combinations(words,3)]
# print(ii)

# import pandas as pd

# df = pd.DataFrame({'name':'A B C D','value':[1]})
# # print(df)
# print('111',df['name'].str.split(' '))
# print()
# print('222',type(df['name'].str.split(' ',expand=True)))
# print()
# print('333',df['name'].str.split(' ',expand=True).stack())
# print()
# print(type(df['name'].str.split(' ',expand=True).stack()))
# print()
# print('4',df['name'].str.split(' ',expand=True).stack().reset_index(level=1,drop=True))
# print('5',df['name'].str.split(' ',expand=True).stack().reset_index(level=1,drop=True).rename('name'))
# print('6',df.drop('name',1).join(df['name'].str.split(' ',expand=True).stack().reset_index(level=1,drop=True).rename('name')))
# 这里注意df['name'].str.split(' ',expand=True).stack().reset_index(level=1,drop=True).rename('name')得到的是一个series，无法用join，
# series无法与一个DataFrame做join,但DataFrame可以与series做join，两者顺序很重要
# print('6',df['name'].str.split(' ',expand=True).stack().reset_index(level=1,drop=True).rename('name').join(df.drop('name',1)))

# print(df['name'].str.split(' ',expand=True).stack().reset_index(level=0).rename(columns={0:'name'}))
# print(df['name'].str.split(' ',expand=True).stack().reset_index(level=0).set_index('level_0').rename(columns={0:'name'}))
#
# print(df['name'].str.split(' ',expand=True).stack().reset_index(level=0).set_index('level_0').rename(columns={0:'name'}).join(df.drop('name',1)))
#
# print(df['name'].str.split(' ',expand=True).stack().reset_index(level=0).rename(columns={0:'name'}).join(df.drop('name',1)))
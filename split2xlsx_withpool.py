import pandas as pd
import os
import math
import threading
from multiprocessing import Pool


def int_range(x):
    x = int(x)
    if x <= 10:
        return '1'
    elif x <= 20:
        return '2'
    else:
        return '3'


def df2xlsx(df, outputfile):
    print(outputfile,df.shape)
    writer = pd.ExcelWriter(outputfile, engine='xlsxwriter', options={'strings_to_urls': False})
    max_rows = 1000000
    pages = math.ceil(df.shape[0] / max_rows)
    if pages == 1:
        df.to_excel(writer, index=False)
    else:
        for page in range(pages):
            start = max_rows * page
            end = max_rows * (page + 1)
            df[start:end].to_excel(writer, sheet_name=str(page + 1), index=False)
    writer.save()


def split2xlsx_withpool(path, filename):
    file = os.path.join(path, filename)
    with open(file, 'r+', encoding='utf-8') as f:
        df = pd.read_csv(f, dtype={'sites_id': str, 'channel_id': str})
    print('文件{}已读入...,共{}行'.format(file,len(df)))
    cols = list(df.columns)
    df['month'] = df['datelabel'].map(lambda x: str(x).split('-')[1])
    df['days'] = df['datelabel'].map(lambda x: str(x).split('-')[-1])
    df['days'] = df['days'].apply(int_range)
    core_num = 6
    pool = Pool(core_num)
    for m, d in df[['month', 'days']].drop_duplicates().values:
        pool.apply_async(func=df2xlsx, args=(df.loc[(df['month'] == m) & (df['days'] == d),cols], os.path.join(path, '{}-{}-{}.xlsx'.format(filename.strip('.txt'), m, d)).replace('190102_190601', '190101_190531'),))
    pool.close()
    pool.join()

def split2xlsx(path, filename):
    file = os.path.join(path, filename)
    with open(file, 'r+', encoding='utf-8') as f:
        df = pd.read_csv(f, dtype={'sites_id': str, 'channel_id': str})
    print('文件{}已读入...'.format(file))
    cols = list(df.columns)
    df['month'] = df['datelabel'].map(lambda x: str(x).split('-')[1])
    df['days'] = df['datelabel'].map(lambda x: str(x).split('-')[-1])
    df['days'] = df['days'].apply(int_range)
    for m, d in df[['month', 'days']].drop_duplicates().values:
        label = (df['month'] == m) & (df['days'] == d)
        tmp = df[label]
        outputfile = os.path.join(path, '{}-{}-{}.xlsx'.format(filename.strip('.txt'), m, d))
        outputfile = outputfile.replace('190102_190601', '190101_190531')
        print(m, d, outputfile)
        df2xlsx(tmp[cols], outputfile)


if __name__ == '__main__':
    import time

    path = os.getcwd()
    filename = 'volume190102_190601.txt'
    t0 = time.time()
    # split2xlsx(path, filename)
    t1 = time.time()
    # print('>>>>>> All Done!,{:.4f}s'.format(t1 - t0))
    split2xlsx_withpool(path, filename)
    t2 = time.time()
    print('>>>>>> All Done!,{:.4f}s'.format(t2 - t1))

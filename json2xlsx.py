import pandas as pd
import math
import json
def json2xlsx(jsonfile,xlsxfile,encoding='utf-8',max_rows=10):
    '''
    该程序仅适用于单层的json格式，如有多层，则不适合。
    {键1:值1,键2:值2,键3:值3......}
    '''
    try:
        with open(jsonfile,'r+',encoding=encoding) as f:
            df = pd.read_json(f,lines=True)
    except:
        df = pd.DataFrame()
        with open(jsonfile,'r+',encoding=encoding) as f:
            lines = iter(f.readlines())
            for line in lines:
                tmp = pd.DataFrame([json.loads(line.strip())])
                df = df.append(tmp)
    print(df.shape)
    df = df.drop_duplicates()
    pages = math.ceil(df.shape[0]/max_rows)
    print('共有{}行{}列数据，将会写出{}个文件'.format(df.shape[0],df.shape[1],pages))
    writer = pd.ExcelWriter(xlsxfile,engine='xlsxwriter', options={'strings_to_urls': False})
    for page in range(1,pages+1):
        start,end = page * max_rows - max_rows + 1,page * max_rows
        tmp = df.iloc[start:end,:]
        tmp.to_excel(writer,sheet_name = '{}-{}'.format(str(page),str(pages)),index=False)
    writer.save()
if __name__ == '__main__':
    jsonfile = r'D:\PycharmProjects\tongyong_history\model_package\101_20170501_autohome_forum-3.json'
    xlsxfile = r'D:\PycharmProjects\tongyong_history\model_package\101_20170501_autohome_forum-3.xlsx'

    json2xlsx(jsonfile,xlsxfile)
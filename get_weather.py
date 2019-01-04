import pandas as pd 
from pypinyin import lazy_pinyin
import sys,argparse
import os

def parse_input_args():
    if len(sys.argv) == 1:
        sys.argv.append('-h')
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', dest = 'city')
    parser.add_argument('-m', dest = 'month')
    args = vars(parser.parse_args())
    return args['city'],args['month']

def get_weather(city,month):
    city_pinyin = ''.join(lazy_pinyin(city)).strip("'")
    url = 'http://www.tianqihoubao.com/lishi/{city_pinyin}/month/{month}.html'.format(city_pinyin=city_pinyin,month = month)
    print(url)
    file = pd.read_html(url,encoding='gbk')[0]
    cols = list(file.loc[0,:])
    # print(cols)
    file.columns = cols
    file = file[file['日期']!='日期']
    file['城市'] = city
    file['月份'] = month
    file = file[['城市','月份'] + cols]
    return file,city_pinyin

if __name__ == '__main__':
    # city,month = parse_input_args()
    result = pd.DataFrame()
    for city in ['beijing','shanghai','chengdu','wuhan','foshan']:
        for month in [201701,201702,201703,201704,201705,201706,201707,201708,201709,201710,201711,201712,
        201801,201802,201803,201804,201805,201806,201807,201808,201809,201810,201811,201812,]:
            try:
                df,city_pinyin = get_weather(city,month)
                result = result.append(df)
            except:
                print('wrong!',city,month)
    result.to_excel('5city_weather.xlsx',index=False)
    df,city_pinyin = get_weather(city,month)
    # filepath = os.path.join(os.getcwd(),'{}-{}.xlsx'.format(city_pinyin,month))
    # df.to_excel(filepath,index=False)
    
    print('执行完成，文件已输出，路径为：{}'.format(filepath))
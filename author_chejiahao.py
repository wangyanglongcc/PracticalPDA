import requests
from bs4 import BeautifulSoup
import pandas as pd
import time # 添加延时

def get_page(page):
    url = F'https://chejiahao.autohome.com.cn/Authors/AuthorListMore?orderType=3&page={page}&userCategory=13'
    data = {
        'orderType': 3,
        'page': page,
        'userCategory': 13
    }
    headers = {
        'user-agent':'xxxx',
        'cookie':'xxxx'
    } # 添加headers
    wb_data = requests.post(url, data,headers = headers)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    titles = soup.select('div.list-title')
    descs = soup.select('div.list-mes')
    nums = soup.select('div.list-num')
    for title, desc, num in zip(titles, descs, nums):
        data = {
            'article_author': title.get_text(),
            'desc': desc.get_text(),
            'flowers': num.get_text().split('｜')[0].strip().strip('\xa0粉丝'),
            'works': num.get_text().split('｜')[-1].strip().strip('\xa0作品'),
        }
        yield data

def get_all_page(max_pages):
    df = pd.DataFrame()
    rows = {0: 0}
    for i in range(1, max_pages + 1):
        tmp = pd.DataFrame(get_page(i))
        df = df.append(tmp).drop_duplicates()
        time.sleep(2) # 休息2秒
        rows[i] = df.shape[0]
        if rows[i] <= rows[i - 1]:
            print('爬取完成，共有{}页'.format(i-1))
            break
    return df
def strip_m(num):
    try:
        num = str(num)
        if '万' in num:
            num = int(float(num.strip('万'))*10000)
        elif '千' in num:
            num = int(float(num.strip('千')) * 1000)
        else:
            pass
    except:
        pass
    return num

def data_clean(df):
    df = df[['author', 'desc', 'flowers', 'works']]
    for i in ['flowers', 'works']:
        df[i] = df[i].apply(strip_m)
    return df

if __name__ == '__main__':
    df = get_all_page(10000)
    df = data_clean(df)
    df.to_csv('author_chejiahao.txt',sep='\t',index=False,encoding='utf-8')

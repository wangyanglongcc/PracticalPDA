import pandas as pd
import math
import json
import os
import glob


def perjson2xlsx(jsonfile, xlsxfile=None, encoding='utf-8', max_rows=1000000, is_remove=False):
    try:
        with open(jsonfile, 'r+', encoding=encoding) as f:
            df = pd.read_json(f, lines=True)
    except:
        df = pd.DataFrame()
        with open(jsonfile, 'r+', encoding=encoding) as f:
            lines = iter(f.readlines())
            for line in lines:
                tmp = pd.DataFrame([json.loads(line.strip())])
                df = df.append(tmp)
    df = df.drop_duplicates()
    pages = math.ceil(df.shape[0] / max_rows)
    print('文件{}共有{}行{}列数据，将会写出{}个文件'.format(jsonfile, df.shape[0], df.shape[1], pages))
    if xlsxfile is None:
        xlsxfile = jsonfile.strip('.json') + '.xlsx'
    writer = pd.ExcelWriter(xlsxfile, engine='xlsxwriter', options={'strings_to_urls': False})
    for page in range(1, pages + 1):
        start, end = page * max_rows - max_rows + 1, page * max_rows
        tmp = df.iloc[start:end, :]
        tmp.to_excel(writer, sheet_name='{}-{}'.format(str(page), str(pages)), index=False)
    writer.save()
    if is_remove:
        os.remove(jsonfile)
    return jsonfile


def json2xlsx(jsonfile_or_jsonpath, xlsxfile=None, encoding='utf-8', max_rows=1000000, is_remove=False):
    '''
    :param jsonfile_or_jsonpath: 输入一个文件或文件夹路径，文件后缀名为.json，当为路径时，该参数指定无效，只能以原文件名进行输出
    :param xlsxfile: 输出文件，默认为None,此时与json文件同路径，且文件名一致，仅后缀名改为.xlxs。
    :param encoding: json文件的编码方式，默认为utf-8
    :param max_rows: 分工作表的页数，默认为100万，即每100万行数据防止一个工作表中
    :param is_remove: 是否删除原json文件，默认为False，即不删除
    :return: 转换完成的文件列表
    '''
    jsonfiles = []
    if os.path.isdir(jsonfile_or_jsonpath):
        xlsxfile = None
        for file in glob.glob(os.path.join(jsonfile_or_jsonpath, '*.json')):
            jsonfile = perjson2xlsx(file, xlsxfile, encoding, max_rows, is_remove)
            jsonfiles.append(jsonfile)
    elif os.path.isfile(jsonfile_or_jsonpath):
        assert os.path.basename(jsonfile_or_jsonpath).endswith('.json'), '文件{}后缀名应为.json'.format(jsonfile_or_jsonpath)
        jsonfile = perjson2xlsx(jsonfile_or_jsonpath, xlsxfile, encoding, max_rows, is_remove)
        jsonfiles.append(jsonfile)
    else:
        print('输入错误，请输入一个正确的路径或文件')
    return jsonfiles


if __name__ == '__main__':
    jsonfile = r'D:\PycharmProjects\tongyong_history\model_package\101_20170501_autohome_forum-3.json'
    res = json2xlsx(jsonfile, max_rows=10)
    # print(res)

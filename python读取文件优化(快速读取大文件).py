# encoding=utf-8
import os
import pandas as pd

def read_csv(filepath_or_buffer,sep=',',encoding='utf-8'):
    '''
    Desc
    ----------
    读取文本文件，当文件超过2G则使用get_chunk方式。
    
    Params
    ----------
    filepath_or_buffer:完整的文件路径
    sep:文件分隔符,如'\\t',','；默认为','
    encoding:文件编码方式，如utf-8,gbk；默认为utf-8
    '''
    assert os.path.isfile(filepath_or_buffer),"File '{}' does not exist".format(filepath_or_buffer)
    if os.path.getsize(filepath_or_buffer)/(1024*1024*1000) < 2:
        df = pd.read_csv(filepath_or_buffer=filepath_or_buffer,sep=sep,encoding=encoding,iterator=False)
        return df
    else:
        # pandas.io.parsers.TextFileReader
        tfr = pd.read_csv(filepath_or_buffer=filepath_or_buffer,sep=sep,encoding=encoding,iterator = True)
        loop =True
        dflst = []
        while loop:
            try:
                dfc = tfr.get_chunk(1000000)
                dflst.append(dfc)
    #             print(len(dflst))
            except StopIteration as e:
                loop = False
                print(e)
        df = pd.concat(dflst,ignore_index =True)
#         del dflst,dfc
        return df

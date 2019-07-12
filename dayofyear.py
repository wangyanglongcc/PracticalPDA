import datetime as dt

def dayofyear(yyyymmdd):
    '''如果需要指定从周一或周日或其他周次开始计算，可使用dt.timedelta通过日期的增减来变换'''
    return dt.datetime.strptime(str(yyyymmdd), '%Y%m%d').isocalendar()[1]


if __name__ == '__main__':
    print(dayofyear(20190101))
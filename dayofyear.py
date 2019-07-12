import datetime as dt

def dayofyear(yyyymmdd):
    return dt.datetime.strptime(str(yyyymmdd), '%Y%m%d').isocalendar()[1]


if __name__ == '__main__':
    print(dayofyear(20190101))
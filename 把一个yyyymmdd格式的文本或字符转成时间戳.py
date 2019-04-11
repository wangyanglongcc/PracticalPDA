import time
def mktime(yyyymmdd):
    '''
    把一个yyyymmdd格式的文本或字符转成时间戳
    '''
    t = time.strptime(str(yyyymmdd),'%Y%m%d')
    t = int(time.mktime(t))
    return t

# -*- coding：utf-8 -*-
import time
def mktime(yyyymmdd):
    '''
    把一个yyyymmdd格式的文本或字符转成时间戳
    '''
    t = time.strptime(str(yyyymmdd),'%Y%m%d')
    t = int(time.mktime(t))
    return t
if __name__ == '__main__':
    print(mktime(20190702)) # 1561996800
    print(mktime(20190703)) # 1562083200
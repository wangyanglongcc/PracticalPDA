# -*- coding: UTF-8 -*-
import datetime as dt
from dateutil.relativedelta import relativedelta
def add_month(start_month,n):
    x = dt.datetime.strptime(start_month,'%Y%m') + relativedelta(months=n)
    return dt.datetime.strftime(x,'%Y%m')
start_month = '201704'
current_ms = [add_month(start_month,i) for i in range(12)]
history_ms = [add_month(start_month,i) for i in range(-12,0)]
print(current_ms)
print(history_ms)
# ['201704', '201705', '201706', '201707', '201708', '201709', '201710', '201711', '201712', '201801', '201802', '201803']
# ['201604', '201605', '201606', '201607', '201608', '201609', '201610', '201611', '201612', '201701', '201702', '201703']
from itertools import zip_longest
import pandas as pd
import datetime as dt


def conse_date_range(part_dates, full_dates):
    '''
    get consecutive date range
    :param part_dates:中间断层的日期
    :param full_dates:全日期字段
    :return:分段连续的日期
    '''
    part_dates = [str(i) for i in part_dates]
    full_dates = [str(i) for i in full_dates]
    for part, full in zip_longest(part_dates, full_dates):
        if part != full:
            index = full_dates.index(full)
            part_dates.insert(index, 'loss')

    part_dates = ','.join(part_dates).split(",loss,")
    part_dates = (i.strip("loss,") for i in part_dates if i != 'loss')
    part_dates = (i for i in part_dates if i != '')
    date_range = (i.split(',')[0] + '_' + i.split(',')[-1] for i in part_dates)
    return '|'.join(date_range)


if __name__ == '__main__':
    full_dates = pd.date_range('20190101', '20190201')
    full_dates = [dt.datetime.strftime(i, '%Y%m%d') for i in full_dates]
    part_dates = ['20190115', '20190116', '20190117', '20190118', '20190122', '20190123', '20190124', '20190127',
                  '20190129']
    print(conse_date_range(part_dates, full_dates))

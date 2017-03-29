'''
生成
beginDate:开始日期
endDate  结束日期
'''

import datetime
def dateRange(beginDate, endDate):
    dates = []
    dt = datetime.datetime.strptime(beginDate, "%Y%m%d")
    date = beginDate[:]
    while date <= endDate:
        dates.append(date+'\n')
        dt = dt + datetime.timedelta(1)
        date = dt.strftime("%Y%m%d")
    return dates
if __name__ == '__main__':
    datelisk=dateRange("19700101", "20100101")
    file=open('password.txt','w')
    for i in datelisk:
        file.write(i)
    file.close()
#-------------------------------------------------------------------------------
# Name:        ??1
# Purpose:
#
# Author:      zhaojian
#
# Created:     22/03/2017
# Copyright:   (c) zhaojian 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import datetime
import os
def dateRange(beginDate, endDate):
    dates = []
    dt = datetime.datetime.strptime(beginDate, "%Y%m%d")
    date = beginDate[:]
    while date <= endDate:
        dates.append(date)
        dt = dt + datetime.timedelta(1)
        date = dt.strftime("%Y%m%d")
    return dates
if __name__ == '__main__':
    datelisk=dateRange("20160101", "20160501")
    file=open('password.txt','w')
    file.write('23232323')
    for i in datelisk:
    #    file.write(i)
    file.close()
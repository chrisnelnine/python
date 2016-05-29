#!/usr/bin/python
import time;
import datetime;

localtime = time.localtime(time.time())
now = time.asctime( localtime )
date = localtime.tm_mday
year = localtime.tm_year
month = localtime.tm_mon
print "Local current time :", now
print "Date:", str(year) + str(month) + str(date)


print time.strftime('%Y%m%d%H%M')

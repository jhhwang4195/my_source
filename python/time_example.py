# -*- coding: utf-8 -*-
#!/usr/bin/python

from datetime import datetime
import time

print ">>> example1"
print datetime.now()

print "\n>>> example2"
now = datetime.now()
print ("%04d/%02d/%02d %02d:%02d:%02d" % (now.year, now.month, now.day, now.hour, now.minute, now.second))

print "\n>>> example3"
time_data = time.strftime("%Y/%m/%d %H:%M:%S")
print time_data
time_data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print time_data

print "\n>>> example4"
year, month, day, hour, minute, second = time.strftime("%Y,%m,%d,%H,%M,%S").split(',')
print ("%s/%s/%s %s:%s:%s" % (year, month, day, hour, minute, second))

print "\n>>> example5"
print time.time()

print "\n>>> example6"
print time.ctime(time.time())

"""
########################################
# Result
########################################
>>> example1
2018-01-09 15:02:54.891897

>>> example2
2018/01/09 15:02:54

>>> example3
2018/01/09 15:02:54
2018-01-09 15:02:54

>>> example4
2018/01/09 15:02:54

>>> example5
1515477774.89

>>> example6
Tue Jan  9 15:02:54 2018
"""

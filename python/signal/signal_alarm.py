# -*- coding: utf-8 -*-
#!/usr/bin/python
#Reference: https://pymotw.com/2/signal/index.html

import signal
import time


def receive_alarm(signum, stack):
    print 'Alarm :', time.ctime()

# Call receive_alarm in 2 seconds
signal.signal(signal.SIGALRM, receive_alarm)
signal.alarm(2)

print 'Before:', time.ctime()
time.sleep(4)
print 'After :', time.ctime()

"""
########################################
# Result
########################################
Before: Tue Jan  9 15:27:00 2018
Alarm : Tue Jan  9 15:27:02 2018
After : Tue Jan  9 15:27:02 2018
"""

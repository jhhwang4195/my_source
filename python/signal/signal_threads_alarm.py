# -*- coding: utf-8 -*-
#!/usr/bin/python
#Reference: https://pymotw.com/2/signal/index.html

import signal
import time
import threading


def signal_handler(num, stack):
    print time.ctime(), 'Alarm in', threading.currentThread()

signal.signal(signal.SIGALRM, signal_handler)


def use_alarm():
    print time.ctime(), 'Setting alarm in', threading.currentThread()
    signal.alarm(1)
    print time.ctime(), 'Sleeping in', threading.currentThread()
    time.sleep(3)
    print time.ctime(), 'Done with sleep'

# Start a thread that will not receive the signal
alarm_thread = threading.Thread(target=use_alarm, name='alarm_thread')
alarm_thread.start()
time.sleep(0.1)

# Wait for the thread to see the signal (not going to happen!)
print time.ctime(), 'Waiting for', alarm_thread
alarm_thread.join()

print time.ctime(), 'Exiting normally'

"""
########################################
# Result
########################################
Tue Jan  9 15:29:25 2018 Setting alarm in <Thread(alarm_thread, started 140591839737600)>
Tue Jan  9 15:29:25 2018 Sleeping in <Thread(alarm_thread, started 140591839737600)>
Tue Jan  9 15:29:25 2018 Waiting for <Thread(alarm_thread, started 140591839737600)>
Tue Jan  9 15:29:28 2018 Done with sleep
Tue Jan  9 15:29:28 2018 Alarm in <_MainThread(MainThread, started 140591860627264)>
Tue Jan  9 15:29:28 2018 Exiting normally
"""

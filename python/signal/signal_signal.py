# -*- coding: utf-8 -*-
#!/usr/bin/python
#Reference: https://pymotw.com/2/signal/index.html

import signal
import os
import time


def receive_signal(signum, stack):
    print 'Received:', signum

signal.signal(signal.SIGUSR1, receive_signal)
signal.signal(signal.SIGUSR2, receive_signal)

print 'My PID is:', os.getpid()

while True:
    print 'Waiting...'
    time.sleep(3)


"""
########################################
# Result
########################################
My PID is: 887
Waiting...
Waiting...
^CTraceback (most recent call last):
File "signal_signal.py", line 20, in <module>
time.sleep(3)
KeyboardInterrupt
"""

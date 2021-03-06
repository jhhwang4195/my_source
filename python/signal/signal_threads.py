# -*- coding: utf-8 -*-
#!/usr/bin/python
#Reference: https://pymotw.com/2/signal/index.html

import signal
import threading
import os
import time


def signal_handler(num, stack):
    print 'Received signal %d in %s' % (num, threading.currentThread())

signal.signal(signal.SIGUSR1, signal_handler)


def wait_for_signal():
    print 'Waiting for signal in', threading.currentThread()
    signal.pause()
    print 'Done waiting'

# Start a thread that will not receive the signal
receiver = threading.Thread(target=wait_for_signal, name='receiver')
receiver.start()
time.sleep(0.1)


def send_signal():
    print 'Sending signal in', threading.currentThread()
    os.kill(os.getpid(), signal.SIGUSR1)

sender = threading.Thread(target=send_signal, name='sender')
sender.start()
sender.join()

# Wait for the thread to see the signal (not going to happen!)
print 'Waiting for', receiver
signal.alarm(2)
receiver.join()


"""
########################################
# Result
########################################
Waiting for signal in <Thread(receiver, started 140222707390208)>
Sending signal in <Thread(sender, started 140222629148416)>
Received signal 10 in <_MainThread(MainThread, started 140222728279872)>
Waiting for <Thread(receiver, started 140222707390208)>
Alarm clock
"""

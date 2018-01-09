# -*- coding: utf-8 -*-
#!/usr/bin/python
#Reference: https://stackoverflow.com/questions/1112343/how-do-i-capture-sigint-in-python

import signal
import sys


def signal_handler(signal, frame):
    print("You pressed Ctrl+C!")
    print("signal=%s, frame=%s" % (signal, frame))
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
print('Press Ctrl+C')
signal.pause()

# -*- coding: utf-8 -*-
#!/usr/bin/python

import threading


def printit():
    threading.Timer(5.0, printit).start()
    print "Hello, World!"

printit()

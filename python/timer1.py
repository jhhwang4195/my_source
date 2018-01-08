# -*- coding: utf-8 -*-
#!/usr/bin/python

from threading import Timer


def hello():
    print "hello, world"

if __name__ == '__main__':
    t = Timer(10.0, hello)
    t.start()  # after 10 seconds, "hello, world" will be printed

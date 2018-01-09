# -*- coding: utf-8 -*-
#!/usr/bin/python
#Reference:

import threading


def sum(low, high):
    total = 0
    for i in range(low, high):
        total += i
    print("Subthread = %s\n" % total)

t = threading.Thread(target=sum, args=(1, 100))
t.start()

print("Main Thread\n")

# -*- coding: utf-8 -*-
#!/usr/bin/python
# Reference: http://stackabuse.com/pythons-os-and-subprocess-popen-commands/
import os

p = os.popen('ls -la')
print(p.read())

vin, out, err = os.popen3('ls -la')
print(out.read())

"""
########################################
# Result
########################################
total 76
drwxr-xr-x 7 root root 4096 Jan  9 15:08 .
drwxr-xr-x 4 root root 4096 Jan  8 21:56 ..
-rw-r--r-- 1 root root  118 Jan  8 21:56 basic.py
-rw-r--r-- 1 root root  541 Jan  8 21:56 color.py
-rw-r--r-- 1 root root  883 Jan  9 15:05 elapsed_time.py

total 76
drwxr-xr-x 7 root root 4096 Jan  9 15:08 .
drwxr-xr-x 4 root root 4096 Jan  8 21:56 ..
-rw-r--r-- 1 root root  118 Jan  8 21:56 basic.py
-rw-r--r-- 1 root root  541 Jan  8 21:56 color.py
-rw-r--r-- 1 root root  883 Jan  9 15:05 elapsed_time.py
"""

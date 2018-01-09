# -*- coding: utf-8 -*-
#!/usr/bin/python
# Reference: http://stackabuse.com/pythons-os-and-subprocess-popen-commands/
import subprocess
subprocess.Popen('ls -la', shell=True)

p1 = subprocess.Popen('free -m', shell=True, stdin=None, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
p2 = subprocess.Popen('df -h', shell=True, stdin=p1.stdout)

p1.stdout.close()
out, err = p2.communicate()


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
Filesystem      Size  Used Avail Use% Mounted on
udev            2.0G  4.0K  2.0G   1% /dev
tmpfs           396M  476K  395M   1% /run
/dev/vda1        26G  5.1G   20G  21% /
none            4.0K     0  4.0K   0% /sys/fs/cgroup
none            5.0M     0  5.0M   0% /run/lock
none            2.0G  4.0K  2.0G   1% /run/shm
none            100M     0  100M   0% /run/user
"""

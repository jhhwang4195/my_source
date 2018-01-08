# -*- coding: utf-8 -*-
#!/usr/bin/python
# Reference: http://stackabuse.com/pythons-os-and-subprocess-popen-commands/
import subprocess
subprocess.Popen('ls -la', shell=True)

p1 = subprocess.Popen('free -m', shell=True, stdin=None, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
p2 = subprocess.Popen('df -h', shell=True, stdin=p1.stdout)

p1.stdout.close()
out, err = p2.communicate()

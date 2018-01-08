#!/usr/bin/python
# Reference: http://stackabuse.com/pythons-os-and-subprocess-popen-commands/
import os

p = os.popen('ls -la')  
print(p.read()) 

vin, out, err = os.popen3('ls -la')  
print(out.read())

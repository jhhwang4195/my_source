# -*- coding: utf-8 -*-
#!/usr/bin/python
#Reference: https://stackoverflow.com/questions/287871/print-in-terminal-with-colors
def printr(prt): print("\033[91m {}\033[00m" .format(prt))
def printg(prt): print("\033[92m {}\033[00m" .format(prt))
def printy(prt): print("\033[93m {}\033[00m" .format(prt))
def printb(prt): print("\033[94m {}\033[00m" .format(prt))
def printt(prt): print("\033[30;47m {}\033[00m" .format(prt))

printr("Hello World!!")
printg("Hello World!!")
printb("Hello World!!")
printy("Hello World!!")
printt("Hello World!!")

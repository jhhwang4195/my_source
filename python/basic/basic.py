# -*- coding: utf-8 -*-
#!/usr/bin/python

import signal
import sys
import time

def printr(prt): print("\033[91m{}\033[00m" .format(prt))
def printg(prt): print("\033[92m{}\033[00m" .format(prt))
def printy(prt): print("\033[93m{}\033[00m" .format(prt))
def printb(prt): print("\033[94m{}\033[00m" .format(prt))
def printt(prt): print("\033[30;47m{}\033[00m" .format(prt))


def signal_handler(signal, frame):
    print("You pressed Ctrl+C!")
    print("signal=%s, frame=%s" % (signal, frame))
    sys.exit(0)


class Calculator:
    def __init__(self):
        self.result = 0

    def adder(self, num):
        self.result += num
        return self.result


class Rectangle:
    count = 0

    def __init__(self, width, height):
        self.width = width
        self.height = height
        Rectangle.count += 1

    def calcArea(self):
        area = self.width * self.height
        return area

    @staticmethod
    def isSquare(rectWidth, rectHeight):
        return rectWidth == rectHeight

    @classmethod
    def printCount(cls):
        printb(cls.count)


def test_func():
    printr("print main")

if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)

    test_func()

    c = Calculator()
    printg("Calculator::adder(): %d" % c.adder(10))
    printg("Calculator::adder(): %d" % c.adder(20))

    r = Rectangle(10, 10)
    r.printCount()
    Rectangle.printCount()

    printb("Rectangle::count %d" % r.count)
    printb("Rectangle::count %d" % Rectangle.count)
    printb("Rectangle::calcArea(): %d" % r.calcArea())
    printb("Rectangle::isSquare(): %s" % Rectangle.isSquare(5, 5))

    printr("\n>>>> vars(r)")
    printg(vars(r))
    printr("\n>>>> dir(r)")
    printg(dir(r))

    while True:
        time.sleep(1)
        printr("main loop... You pressed Ctrl+C!")

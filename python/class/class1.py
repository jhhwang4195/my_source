# -*- coding: utf-8 -*-
#!/usr/bin/python


class Calculator:
    def __init__(self):
        self.result = 0

    def adder(self, num):
        self.result += num
        return self.result

if __name__ == '__main__':
    cal1 = Calculator()
    cal2 = Calculator()

    print(cal1.adder(3))
    print(cal1.adder(4))
    print(cal2.adder(3))
    print(cal2.adder(7))


"""
########################################
# Result
########################################
3
7
3
10
"""

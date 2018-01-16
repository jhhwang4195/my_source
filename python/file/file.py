# -*- coding: utf-8 -*-
#!/usr/bin/python

# file write
print("\n>>>>> TEST1")
file = open('hello.txt', 'w')
file.write('Hello, world!')
file.close()

# file read
print("\n>>>>> TEST2")
file = open('hello.txt', 'r')
s = file.read()
print(s)
file.close()

# file write using with as
print("\n>>>>> TEST3")
with open('hello.txt', 'w') as file:
    for i in range(3):
        file.write('Hello, world! {0}\n'.format(i))

# file read example1
print("\n>>>>> TEST4")
with open('hello.txt', 'r') as file:
    s = file.read()
    print(s)

# file read example2
print("\n>>>>> TEST5")
with open('hello.txt', 'r') as file:
    lines = file.readlines()
    print(lines)

# file read example3
print("\n>>>>> TEST6")
with open('hello.txt', 'r') as file:
    line = file.readline()
    print(line.strip('\n'))
    while line != '':
        line = file.readline()
        print(line.strip('\n'))

"""
########################################
# Result
########################################
>>>>> TEST1

>>>>> TEST2
Hello, world!

>>>>> TEST3

>>>>> TEST4
Hello, world! 0
Hello, world! 1
Hello, world! 2


>>>>> TEST5
['Hello, world! 0\n', 'Hello, world! 1\n', 'Hello, world! 2\n']

>>>>> TEST6
Hello, world! 0
Hello, world! 1
Hello, world! 2
"""

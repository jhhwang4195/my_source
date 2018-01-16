# -*- coding: utf-8 -*-
#!/usr/bin/python

print('>>>TEST1')
for i in range(5):
    print('Hello, world!')

print('\n>>>TEST2')
for i in range(5, 10):
    print('Hello, world!', i)

print('\n>>>TEST3')
for i in range(0, 10, 2):
    print('Hello, world!', i)

print('\n>>>TEST4')
for i in range(5, 0, -1):
    print('Hello, world!', i)

print('\n>>>TEST5')
for i in reversed(range(5)):
    print('Hello, world!', i)

print('\n>>>TEST6')
i = 0
while i < 5:
    print('Hello, world!')
    i += 1

print('\n>>>TEST7')
i = 5
while i > 0:
    print('Hello, world!', i)
    i -= 1

print('\n>>>TEST8')
i = 0
while True:
    print('Hello, world!')
    i += 1
    if i == 5:
        break

print('\n>>>TEST9')
for i in range(1, 5):
    if i % 2 != 0:
        continue
    print(i)

print('\n>>>TEST10')
for i in range(5):
    for j in range(5):
        print('*', end='')
    print()

"""
########################################
# Result
########################################
>>>TEST1
Hello, world!
Hello, world!
Hello, world!
Hello, world!
Hello, world!

>>>TEST2
Hello, world! 5
Hello, world! 6
Hello, world! 7
Hello, world! 8
Hello, world! 9

>>>TEST3
Hello, world! 0
Hello, world! 2
Hello, world! 4
Hello, world! 6
Hello, world! 8

>>>TEST4
Hello, world! 5
Hello, world! 4
Hello, world! 3
Hello, world! 2
Hello, world! 1

>>>TEST5
Hello, world! 4
Hello, world! 3
Hello, world! 2
Hello, world! 1
Hello, world! 0

>>>TEST6
Hello, world!
Hello, world!
Hello, world!
Hello, world!
Hello, world!

>>>TEST7
Hello, world! 5
Hello, world! 4
Hello, world! 3
Hello, world! 2
Hello, world! 1

>>>TEST8
Hello, world!
Hello, world!
Hello, world!
Hello, world!
Hello, world!

>>>TEST9
2
4

>>>TEST10
*****
*****
*****
*****
*****
"""

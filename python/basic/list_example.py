# -*- coding: utf-8 -*-
#!/usr/bin/python
#Reference: https://dojang.io/mod/page/view.php?id=1001

# tuple
print (">>>>> tuple test")
test_tuple = ('one', 'two', 'three')
print("tuple_count: %d" % len(test_tuple))
for i in test_tuple:
    print(i)

print(test_tuple.index("three"))

a = tuple(i for i in range(10) if i % 2 == 0)
print(a)

# list
print ("\n>>>>> list test")
test_list = ['one', 'two', 'three']
print("list_count: %d" % len(test_list))
for i in test_list:
    print(i)

for i in range(len(test_list)):
    print(test_list[i])

for idx, value in enumerate(test_list):
    print(idx, value)

# list method
print ("\n>>>>> list method")

print(test_list.index("three"))

test_list.append("four")
print(test_list)

test_list.append(["five", "six"])
print(test_list)

test_list.insert(0, "zero")
print(test_list)

test_list.remove("zero")
print(test_list)

test_list.reverse()
print(test_list)

test_list.reverse()
print(test_list)

# list comprehension
print ("\n>>>>> list comprehension")
a = [i for i in range(10)]
print(a)

b = list(i for i in range(10))
print(b)

c = [i + 5 for i in range(5)]
print(c)

d = [i for i in range(10) if i % 2 == 0]
print(d)

# list & map
print ("\n>>>>> list & map")
a = [1.2, 2.5, 3.7, 4.6]
a = list(map(int, a))
print(a)

a = list(map(str, range(10)))
print(a)

# Two-dimensional list
print ("\n>>>>> Two-dimensional list")
a = [[10, 20], [30, 40], [50, 60]]
for x, y in a:
    print(x,y)

for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=' ')
    print()

a = []
for i in range(3):
    line = []
    for j in range(3):
        line.append(j)
    a.append(line)
print(a)

"""
########################################
# Result
########################################
>>>>> tuple test
tuple_count: 3
one
two
three
2
(0, 2, 4, 6, 8)

>>>>> list test
list_count: 3
one
two
three
one
two
three
0 one
1 two
2 three

>>>>> list method
2
['one', 'two', 'three', 'four']
['one', 'two', 'three', 'four', ['five', 'six']]
['zero', 'one', 'two', 'three', 'four', ['five', 'six']]
['one', 'two', 'three', 'four', ['five', 'six']]
[['five', 'six'], 'four', 'three', 'two', 'one']
['one', 'two', 'three', 'four', ['five', 'six']]

>>>>> list comprehension
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[5, 6, 7, 8, 9]
[0, 2, 4, 6, 8]

>>>>> list & map
[1, 2, 3, 4]
['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

>>>>> Two-dimensional list
10 20
30 40
50 60
10 20
30 40
50 60
[[0, 1, 2], [0, 1, 2], [0, 1, 2]]
"""

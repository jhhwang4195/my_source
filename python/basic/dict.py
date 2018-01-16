# -*- coding: utf-8 -*-
#!/usr/bin/python
#Reference: https://dojang.io/mod/page/view.php?id=1039

# initialize
print("\n>>>>> TEST1")
x = {}
y = dict()
print(x)
print(y)

# access
print("\n>>>>> TEST2")
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50}
print(x)
print(x['a'])
x['a'] = 100
print(x['a'])
print("len=%d" % len(x))

print("\n>>>>> TEST3")
x = dict(a=10, b=20, c=30)
print(x)
print(x['a'])
x['a'] = 100
print(x['a'])
print("len=%d" % len(x))

print("\n>>>>> TEST4")
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50}
print(x.get('a'))
print(x.get('z'))

print("\n>>>>> TEST5")
x.update(a=100, b=100)
print(x)
print(x['a'], x['b'])

print("\n>>>>> TEST6")
print(x.pop('a'))
print(x)

del x['b']
print(x)

print("\n>>>>> TEST7")
x.setdefault('e')
x.setdefault('f', 100)
print(x)

print("\n>>>>> TEST8")
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
print(x.items())
print(x.keys())
print(x.values())

print("\n>>>>> TEST9")
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
for key in x.keys():
    print(key, end=' ')

for value in x.values():
    print(value, end=' ')

for key, value in x.items():
    print(key, value)

print("\n>>>>> TEST10")
print('a' in x)
print('a' not in x)
print('z' in x)
print('z' not in x)

print("\n>>>>> TEST11")
terrestrial_planet = {
        'Mercury': {
            'mean_radius': 2439.7,
            'mass': 3.3022E+23,
            'orbital_period': 87.969
            },
        'Venus': {
            'mean_radius': 6051.8,
            'mass': 4.8676E+24,
            'orbital_period': 224.70069,
            }
}
print(terrestrial_planet['Venus']['mean_radius'])
terrestrial_planet['Venus']['mean_radius'] = 1111.99

print(terrestrial_planet)
print(terrestrial_planet['Venus']['mean_radius'])


"""
########################################
# Result
########################################
>>>>> TEST1
{}
{}

>>>>> TEST2
{'c': 30, 'e': 50, 'a': 10, 'b': 20, 'd': 40}
10
100
len=5

>>>>> TEST3
{'c': 30, 'a': 10, 'b': 20}
10
100
len=3

>>>>> TEST4
10
None

>>>>> TEST5
{'d': 40, 'c': 30, 'e': 50, 'a': 100, 'b': 100}
100 100

>>>>> TEST6
100
{'d': 40, 'c': 30, 'e': 50, 'b': 100}
{'d': 40, 'c': 30, 'e': 50}

>>>>> TEST7
{'f': 100, 'd': 40, 'c': 30, 'e': 50}

>>>>> TEST8
dict_items([('c', 30), ('a', 10), ('b', 20), ('d', 40)])
dict_keys(['c', 'a', 'b', 'd'])
dict_values([30, 10, 20, 40])

>>>>> TEST9
c a b d 30 10 20 40 c 30
a 10
b 20
d 40

>>>>> TEST10
True
False
False
True

>>>>> TEST11
6051.8
{'Mercury': {'mass': 3.3022e+23, 'orbital_period': 87.969, 'mean_radius': 2439.7}, 'Venus': {'mass': 4.8676e+24, 'orbital_period': 224.70069, 'mean_radius': 1111.99}}
1111.99
"""

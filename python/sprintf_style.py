# Reference: https://stackoverflow.com/questions/5309978/sprintf-like-functionality-in-python
# -*- coding: utf-8 -*-
#!/usr/bin/python

# Example1
a = "Hello"
b = "World"
buf = "%s %s" % (a, b)
print buf

# Example2
buf = "{} {}".format("Hello", "world")
print buf

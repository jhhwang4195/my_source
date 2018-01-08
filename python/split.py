# -*- coding: utf-8 -*-
#!/usr/bin/python

text = "This is random text we are going to split apart"

print ("#### split test1 ####")
words = text.split(" ")
for word in words:
    print word

print ("#### split test2 ####")
words = text.split(" ", 3)
for word in words:
    print word

# -*- coding: utf-8 -*-
#!/usr/bin/python

text = "This is random text we are going to split apart"

print ("#### split test1 ####")
words = text.split(" ")
for word in words:
    print word

print ("#### join test ####")
print words
org = "-".join(words)
print org

"""
########################################
# Result
########################################
#### split test1 ####
This
is
random
text
we
are
going
to
split
apart

#### join test ####
['This', 'is', 'random', 'text', 'we', 'are', 'going', 'to', 'split', 'apart']
This-is-random-text-we-are-going-to-split-apart
"""

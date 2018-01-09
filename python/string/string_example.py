# -*- coding: utf-8 -*-
#!/usr/bin/python
import string

text = "Monty Python's Flying Circus"
print("===========================================")
print("upper   -> %s" % text.upper())
print("lower   -> %s" % text.lower())
print("split   -> %s" % text.split())
print("join    -> %s" % "+".join(text.split()))
print("replace -> %s" % text.replace("Python", "Perl"))
print("find    -> %s %s" % (text.find("Python"), text.find("Perl")))
print("count   -> %s" % text.count("n"))
print("===========================================")


"""
########################################
# Result
########################################
===========================================
upper   -> MONTY PYTHON'S FLYING CIRCUS
lower   -> monty python's flying circus
split   -> ['Monty', "Python's", 'Flying', 'Circus']
join    -> Monty+Python's+Flying+Circus
replace -> Monty Perl's Flying Circus
find    -> 6 -1
count   -> 3
===========================================
"""

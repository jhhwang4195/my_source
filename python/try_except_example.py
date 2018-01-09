#!/usr/bin/python
import os
import sys
import traceback


def test_envrion_except():
    try:
        var = os.environ['GITHUB_USERNAME_TEST']
        print var
    except Exception as err:
        print ("[Error] %s" % (str(err)))
        print (">>>>>>>>>>>>>>> traceback.print_exc")
        print (traceback.print_exc())
        print (">>>>>>>>>>>>>>> traceback.format_exc")
        print (traceback.format_exc())
        print (">>>>>>>>>>>>>>> traceback.print_stack")
        print (traceback.print_stack())
        #sys.exit(1)


def test_file_open_except():
    try:
        fp = open("test.txt", "r")
        try:
            lines = fp.readlines()
            print(lines)
        finally:
            fp.close()
    except IOError as err:
        print ("[Error] %s" % (str(err)))
        print (">>>>>>>>>>>>>>> traceback.print_exc")
        print ("%s" % traceback.print_exc())
        #sys.exit(1)


if __name__ == '__main__':
    test_envrion_except()
    test_file_open_except()


"""
########################################
# Result
########################################
[Error] 'GITHUB_USERNAME_TEST'
>>>>>>>>>>>>>>> traceback.print_exc
Traceback (most recent call last):
File "try_except_example.py", line 9, in test_envrion_except
var = os.environ['GITHUB_USERNAME_TEST']
File "/usr/lib/python2.7/UserDict.py", line 23, in __getitem__
raise KeyError(key)
KeyError: 'GITHUB_USERNAME_TEST'
None

>>>>>>>>>>>>>>> traceback.format_exc
Traceback (most recent call last):
File "try_except_example.py", line 9, in test_envrion_except
var = os.environ['GITHUB_USERNAME_TEST']
File "/usr/lib/python2.7/UserDict.py", line 23, in __getitem__
raise KeyError(key)
KeyError: 'GITHUB_USERNAME_TEST'

>>>>>>>>>>>>>>> traceback.print_stack
File "try_except_example.py", line 38, in <module>
test_envrion_except()
File "try_except_example.py", line 18, in test_envrion_except
print (traceback.print_stack())
None

[Error] [Errno 2] No such file or directory: 'test.txt'
>>>>>>>>>>>>>>> traceback.print_exc
Traceback (most recent call last):
File "try_except_example.py", line 24, in test_file_open_except
fp = open("test.txt", "r")
IOError: [Errno 2] No such file or directory: 'test.txt'
None
"""

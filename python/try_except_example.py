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

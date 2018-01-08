# -*- coding: utf-8 -*-
#!/usr/bin/python
#Reference: https://pymotw.com/3/getopt/
#Reference: http://www.dreamincode.net/forums/topic/53240-using-getopt-in-python/
#Reference: https://raw.githubusercontent.com/dougsland/python-by-examples/master/getOpt.py

import getopt
import sys

version = '1.0'
verbose = False
output_filename = 'default.out'

try:
    options, remainder = getopt.getopt(sys.argv[1:],
                                       'o:v',
                                       ['output=', 'verbose', 'version='])
except getopt.GetoptError as err:
        print('ERROR:', err)
        sys.exit(1)

print ("ARGV: %s" % sys.argv[1:])
print ("OPTIONS: %s" % options)

for opt, arg in options:
    if opt in ('-o', '--output'):
        output_filename = arg
    elif opt in ('-v', '--verbose'):
        verbose = True
    elif opt == '--version':
        version = arg

print ("VERSION:%s" % version)
print ("VERBOSE:%s" % verbose)
print ("OUTPUT:%s" % output_filename)
print ("REMAINING:%s" % remainder)

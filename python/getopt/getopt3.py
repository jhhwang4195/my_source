# -*- coding: utf-8 -*-
#!/usr/bin/python
#Reference: https://pymotw.com/3/getopt/
#Reference: http://www.dreamincode.net/forums/topic/53240-using-getopt-in-python/
#Reference: https://raw.githubusercontent.com/dougsland/python-by-examples/master/getOpt.py

import sys
import getopt

VERSION = "1.0"


def usage():
    print "Usage: " + sys.argv[0] + " [OPTIONS]"
    print "\t--car      Car name"
    print "\t--model    Model name"
    print "\t--year     Year of car"
    print "\t--version  List version release"
    print "\t--help     This help menu\n"

    print "Example:"
    print "\t" + sys.argv[0] + " --car palio --model basic --year 2012"
    sys.exit(1)


if __name__ == "__main__":
    car = None
    model = None
    year = None
    try:
        opts, args = getopt.getopt(sys.argv[1:], "c:m:y:hv", ["car=", "model=", "year=", "help", "version"])
    except getopt.GetoptError, err:
        # print help information and exit:
        print(err)
        sys.exit(-1)

    for o, a in opts:
        if o in ("-c", "--car"):
            car = a
        elif o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-m", "--model"):
            model = a
        elif o in ("-y", "--year"):
            year = a
        elif o in ("-V", "--version"):
            print VERSION
            sys.exit(0)
        else:
            assert False, "unhandled option"
            sys.exit(-1)

    argc = len(sys.argv)
    if argc != 7:
        usage()

    print "car [%s] model [%s] year [%s]" % (car, model, year)


"""
########################################
# Result
########################################
$ python getopt3.py --car palio --model basic --year 2012
car [palio] model [basic] year [2012]
"""

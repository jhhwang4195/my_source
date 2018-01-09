# -*- coding: utf-8 -*-
#!/usr/bin/python
#Reference: https://pymotw.com/3/getopt/
#Reference: http://www.dreamincode.net/forums/topic/53240-using-getopt-in-python/
#Reference: https://raw.githubusercontent.com/dougsland/python-by-examples/master/getOpt.py

import getopt
import sys
import os


def main(argv):
    try:
        opt, args = getopt.getopt(argv,
                                  "he:da:",
                                  ["help", "execute=", "dothis", "argument="])
    except getopt.GetoptError, err:
        print str(err)
        usage()
        sys.exit(2)

    output = None
    verbose = False

    for o, a in opt:
        if o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-e", "--execute"):
            os.system(a)
        elif o in ("-d", "--dothis"):
            print "dothis"
        elif o in ("-a", "--argument"):
            print str(a)
        else:
            assert False, "unhandled option"


def usage():
    usage = """
        -h --help                 Prints this
        -e --execute (cmd)        Execute a system command
        -d --dothis               Print dothis
        -a --argument (argument   Print (argument)
    """
    print usage


if __name__ == "__main__":
    main(sys.argv[1:])


"""
########################################
# Result
########################################
$ python getopt2.py -e free -d -a test
total       used       free     shared    buffers     cached
Mem:       4046644    3900220     146424      44812     115744     516888
-/+ buffers/cache:    3267588     779056
Swap:      4191228     529816    3661412
dothis
test
"""

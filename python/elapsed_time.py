# -*- coding: utf-8 -*-
#!/usr/bin/python

import time
from datetime import datetime

start_time = time.time()
time.sleep(2.22)
elapsed_time = time.time() - start_time
print ("elapsed_time: %s" % elapsed_time)


start_time = datetime.now()
time.sleep(2.22)
time_elapsed = datetime.now() - start_time
print("Time elapsed (hh:mm:ss.ms): %s" % format(time_elapsed))


start_time = datetime.now()
print("My Start Time: %s" % start_time)
time.sleep(2.22)
stop_time = datetime.now()
print("My Stop Time: %s" % stop_time)
elapsed_time = stop_time - start_time
print("My Elapsed Time: %s" % elapsed_time)

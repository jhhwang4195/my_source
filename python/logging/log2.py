# -*- coding: utf-8 -*-
#!/usr/bin/python
#Reference: http://hamait.tistory.com/880

"""
import logging

if __name__ == '__main__':
    logging.error("something wrong!!")
"""

"""
import logging

if __name__ == '__main__':
    mylogger = logging.getLogger("my")
    mylogger.setLevel(logging.INFO)

    stream_hander = logging.StreamHandler()
    mylogger.addHandler(stream_hander)

    mylogger.info("server start!!!")
"""

"""
import logging

if __name__ == '__main__':
    mylogger = logging.getLogger("my")
    mylogger.setLevel(logging.INFO)

    stream_hander = logging.StreamHandler()
    mylogger.addHandler(stream_hander)

    file_handler = logging.FileHandler('my.log')
    mylogger.addHandler(file_handler)

    mylogger.info("server start!!!")
"""

"""
import logging

if __name__ == '__main__':
    mylogger = logging.getLogger("my")
    mylogger.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    stream_hander = logging.StreamHandler()
    stream_hander.setFormatter(formatter)
    mylogger.addHandler(stream_hander)

    file_handler = logging.FileHandler('my.log')
    mylogger.addHandler(file_handler)

    mylogger.info("server start!!!")
"""

import logging
import threading
import time

def worker(arg):
    while not arg['stop']:
        logging.debug('Hi from myfunc')
        time.sleep(0.5)

def main():
    logging.basicConfig(level=logging.DEBUG, format='%(relativeCreated)6d %(threadName)s %(message)s')
    info = {'stop': False}
    thread = threading.Thread(target=worker, args=(info,))
    thread.start()
    while True:
        try:
            logging.debug('Hello from main')
            time.sleep(0.75)
        except KeyboardInterrupt:
            info['stop'] = True
            break
    thread.join()

if __name__ == '__main__':
    main()

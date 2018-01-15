# -*- coding: utf-8 -*-
#!/usr/bin/python
#Reference: http://gyus.me/?p=418

"""
import logging

logging.info("I told you so")
logging.warning("Watch out!")
"""

"""
import logging
logging.basicConfig(level=logging.DEBUG)

logging.debug("디버깅용 로그~~")
logging.info("도움이 되는 정보를 남겨요~")
logging.warning("주의해야되는곳!")
logging.error("에러!!!")
logging.critical("심각한 에러!!")
"""

"""
import logging
logging.basicConfig(filename='./test.log',level=logging.DEBUG)

logging.info("=========================================")
logging.info("파일에다가 남겨봐요~")
logging.info("=========================================")
logging.debug("디버깅용 로그~~")
logging.info("도움이 되는 정보를 남겨요~")
logging.warning("주의해야되는곳!")
logging.error("에러!!!")
logging.critical("심각한 에러!!")
"""


"""
import logging
import logging.handlers

# 1. 로거 인스턴스를 만든다
logger = logging.getLogger('mylogger')

# 2. 스트림과 파일로 로그를 출력하는 핸들러를 각각 만든다.
fileHandler = logging.FileHandler('./myLoggerTest.log')
streamHandler = logging.StreamHandler()

# 3. 1번에서 만든 로거 인스턴스에 스트림 핸들러와 파일핸들러를 붙인다.
logger.addHandler(fileHandler)
logger.addHandler(streamHandler)

# 4. 로거 인스턴스로 로그를 찍는다.
logger.setLevel(logging.DEBUG)
logger.debug("===========================")
logger.info("TEST START")
logger.warning("스트림으로 로그가 남아요~")
logger.error("파일로도 남으니 안심이죠~!")
logger.critical("치명적인 버그는 꼭 파일로 남기기도 하고 메일로 발송하세요!")
logger.debug("===========================")
logger.info("TEST END!")
"""

import logging
import logging.handlers

# 로거 인스턴스를 만든다
logger = logging.getLogger('mylogger')

# 포매터를 만든다
#fomatter = logging.Formatter('[%(levelname)s|%(filename)s:%(lineno)s] %(asctime)s > %(message)s')
fomatter = logging.Formatter('%(asctime)s [%(levelname)8s] [%(filename)s:%(lineno)s] %(message)s')

# 스트림과 파일로 로그를 출력하는 핸들러를 각각 만든다.
fileHandler = logging.FileHandler('./myLoggerTest.log')
streamHandler = logging.StreamHandler()

# 각 핸들러에 포매터를 지정한다.
fileHandler.setFormatter(fomatter)
streamHandler.setFormatter(fomatter)

# 로거 인스턴스에 스트림 핸들러와 파일핸들러를 붙인다.
logger.addHandler(fileHandler)
logger.addHandler(streamHandler)

# 로거 인스턴스로 로그를 찍는다.
logger.setLevel(logging.DEBUG)
logger.debug("===========================")
logger.info("TEST START")
logger.warning("스트림으로 로그가 남아요~")
logger.error("파일로도 남으니 안심이죠~!")
logger.critical("치명적인 버그는 꼭 파일로 남기기도 하고 메일로 발송하세요!")
logger.debug("===========================")
logger.info("TEST END!")

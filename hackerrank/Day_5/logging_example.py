import logging

logging.basicConfig(level=logging.DEBUG) # default level(warning) ko change kerke any level ko set kerte hai ese
logging.debug("This is a debug message") #10
logging.info("module2 got completed and module3 started") #20
logging.warning("The warning message is displaying") #30
logging.error("The error message is displaying") #40
logging.critical("The critical message is displaying") #50

# default level is warning()

# bar bar logging na likh ke hum direct ese likh sakte hai -

from logging import *

basicConfig(level=DEBUG)
basicConfig(level=20) # we can put the level's numeric value also
debug("This is a debug message")
info("module2 got completed and module3 started")
warning("The warning message is displaying")
error("The error message is displaying")
critical("The critical message is displaying")

# CRITICAL:root:The critical message is displaying
# levelname:loggername:message - by default format of log message & by default loggername is root


# then we have to store the log messages into the log file

from logging import *

basicConfig(filename="app.log", level=DEBUG) # log file by default append mode me create hoga. later you can change to R/W both mode

# app.log file created in the same directory where python script is running.
# if you want to create log file in different directory then you have to specify the full path of the log file.
# basicConfig(filename="/home/user/app.log", level=DEBUG)

basicConfig(filename="hackerrank/Day_5/app.log", level=DEBUG)
debug("This is a debug message")
info("module2 got completed and module3 started")
warning("The warning message is displaying")
error("The error message is displaying")
critical("The critical message is displaying")


# How to change format of log messages?

# change file mode
from logging import *

basicConfig(filename="app.log", level=DEBUG, filemode="w")

debug("This is a debug message")
info("module2 got completed and module3 started")
warning("The warning message is displaying")
error("The error message is displaying")
critical("The critical message is displaying")

# change format of log messages
from logging import *

basicConfig(filename="app.log", level=DEBUG, filemode="w", format="%(name)s:%(levelname)s:%(message)s") # s represents string
debug("This is a debug message")
info("module2 got completed and module3 started")
warning("The warning message is displaying")
error("The error message is displaying")
critical("The critical message is displaying")

# log process id & line no

from logging import *

basicConfig(filename="app.log",
             level=DEBUG,
               filemode="w",
                 format="%(name)s:%(levelname)s:%(message)s:%(process)s:%(lineno)s")
debug("This is a debug message")
info("module2 got completed and module3 started")
warning("The warning message is displaying")
error("The error message is displaying")
critical("The critical message is displaying")

# log date & time
from logging import *

basicConfig(filename="app.log",
             level=DEBUG,
               filemode="w",
                 format="%(asctime)s:%(name)s:%(levelname)s:%(message)s:%(process)s:%(lineno)s",
                 datefmt="%d-%b-%y %H:%M:%S")
debug("This is a debug message")
info("module2 got completed and module3 started")
warning("The warning message is displaying")
error("The error message is displaying")
critical("The critical message is displaying")

# changing style of formatting
from logging import *

basicConfig(filename="app.log",
             level=DEBUG,
               filemode="w",
                 format="{asctime}|{name}|{levelname}|{message}|{process}|{lineno}",
                 datefmt="%d-%b-%y %H:%M:%S",
                 style="{")
debug("This is a debug message")
info("module2 got completed and module3 started")
warning("The warning message is displaying")
error("The error message is displaying")
critical("The critical message is displaying")


# creating logger object

from logging import *
import sys

basicConfig(filename="app.log",
               filemode="w",
                 format="{asctime}|{name}|{levelname}|{message}|{process}|{lineno}",
                 datefmt="%d-%b-%y %H:%M:%S",
                 style="{")

# logger = getLogger(sys.argv[0]) 
logger = getLogger(__name__) # It is a special attribute where it will store the current file name
logger.setLevel(DEBUG) # we can put the numeric value of debug

logger.debug("This is a debug message")
logger.info("module2 got completed and module3 started")
logger.warning("The warning message is displaying")
logger.error("The error message is displaying")
logger.critical("The critical message is displaying")

# If this program is not imported anywhere then the root(current file) name will be __main__. 
# If it is imported then instead of __main__ there is the imported file name(logging_example) you can see.

# from logging import *

# basicConfig(filename="app1.log",
#                filemode="w",
#                  format="{asctime}|{levelname}|{message}",
#                  datefmt="%d-%b-%y %H:%M:%S",
#                  style="{")

# logger = getLogger()
# logger.setLevel(DEBUG)

# try:
#     age = int(input("Enter your age: "))
# except Exception as obj:
#     # print(obj)
#     # error(obj)
#     # error("Exception details: ", exc_info=True)
#     exception("Exception details: ")


# Example -- 1 

from logging import *

basicConfig(filename="app1.log", filemode="a", level=10, format="{process}|{asctime}|{levelname}|{message}", 
            datefmt="%d-%b-%y %H:%M:%S",
            style="{")

class AccessDenied(Exception):
    pass

try:
    age = int(input("Enter your age: "))
    if age < 18:
        raise AccessDenied("Access Denied!")
    info(f"a user having age {age} has logged in")
except AccessDenied as obj:
    exception("Exception Occured")

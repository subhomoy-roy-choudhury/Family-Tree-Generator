# import re
# #
# # txt = 'Member<anil,0> -> Member<sad,1>'
# # x = re.findall(r"Member<*[a-z]{1,4},[0-9]>",txt)
# # print(x)
#
# def tree_command_parser(func):
#     def wrapper(*args, **kwargs):
#         print(args[0])
#         x = re.findall(r"Member<*[a-z]{1,4},[0-9]>",args[0])
#         return func(x,0)
#     return wrapper
#
# @tree_command_parser
# def parser(x,y):
#     print('sdlkhfgdsk',x)
#     return x
#
# if __name__ == '__main__':
#     txt = 'Member<anil,0> -> Member<sad,1>'
#     x1 = parser(txt,'q')
#     print(x1)

from pynput.keyboard import Key, Listener
import os
import logging

from threading import *
import time

def fun():
    while True :
        time.sleep(0.1)
        print("Geeks For Geeks")

def on_press(key):
    global keys , count
    logging.info(str(key))
    keys.append(str(key))
    count += 1
    print("{0} pressed ".format(key))

def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press , on_release = on_release) as listener:
    listener.join()

T = Thread(target = fun)

print("GFG")
print(T.isDaemon())

# set thread as Daemon
T.setDaemon(True)

# check status
print(T.isDaemon())
T.start()
T.join()
time.sleep(2)
print("skbdkb")

# from pynput.keyboard import Key, Listener
# import os
# import logging
#
# logging.basicConfig(filename = ("keyLog.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')
#
# count =0
# keys = []
# if os.path.exists("logs.txt"):
#     os.remove("logs.txt")
# open("keyLog.txt", 'a').close()
#
# def on_press(key):
#     global keys , count
#     logging.info(str(key))
#     keys.append(str(key))
#     count += 1
#     print("{0} pressed ".format(key))
#
# def on_release(key):
#     if key == Key.esc:
#         return False
#
#
# with Listener(on_press=on_press , on_release = on_release) as listener:
#     listener.join()

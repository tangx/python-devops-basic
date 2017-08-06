#!/usr/bin/env python
# encoding: utf-8
#

"""
@version:  0.0.1
@author: TangHsin
@license: Apache Licence
@mailto: octowhale@github
@site: 
@software: PyCharm Community Edition
@python ver: Python 2.7.12
@python ver: Python 3.6
@FILE: 09事件_events.py
@time: 2017/8/5 13:49
"""
"""
An event is a simple synchronization object;

the event represents an internal flag, and threads can wait for the flag to be set,
or set or clear the flag themseleves.

event=threading.Event()

# a client thread can wait for the flag to be set
event.wati()

# a server thread can set or reset it
event.set()
event.clear()

If the flag is set, the wait method doesn't do anything.
If the flag is cleared, wait will block until it becomes set again.
Any number of threads may wait for the same event.
"""

import os
import sys
import time
from random import randint
import threading

event = threading.Event()


def lighter():
    counter = 0
    event.set()  # 初始化为绿灯
    while True:
        if counter < 10:
            print("\033[32m %s 绿灯亮了，车辆可以通过\033[0m" % counter)
            event.set()  # 设置为绿灯
        elif counter < 18:
            print("\033[31m %s 红灯亮了，车辆禁止通行\033[0m" % counter)
            event.clear()  # 设置为红灯
        else:
            counter = 0  # 置零

        counter += 1
        time.sleep(1)


def car(name):
    """红灯停，绿灯行"""

    while True:

        # print("event.is_set() = ", event.is_set())
        if event.is_set():
            event.wait()
            print("现在是绿灯， car[%s] \033[32m可以通行\033[0m" % name)
        else:
            print("现在是红灯， car[%s] \033[31m等待通行\033[0m" % name)
            event.wait()        # 当红灯的时候，这里只会执行一次，因为 wait() 一直在等待。

        time.sleep(1)


def main():
    """这是一个红绿灯的案例，规则很简单： 红灯停，绿灯行"""

    l = threading.Thread(target=lighter)
    l.start()
    car1 = threading.Thread(target=car, args=(("volvo",)))
    car2 = threading.Thread(target=car, args=(("benz",)))
    car3 = threading.Thread(target=car, args=(("bmw",)))

    car1.start()
    # car2.start()
    # car3.start()


if __name__ == "__main__":
    main()

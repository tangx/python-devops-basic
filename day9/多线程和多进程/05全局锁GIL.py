#!/usr/bin/env python
# encoding: utf-8

"""
@author: tangxin@haowan123.com
@python_version: python2.7
@file: 05全局锁GIL.py
@time: 2017/8/4 17:25
"""

import os
import sys
import threading
import time
from random import randint

num = 0


def run():
    global num
    time.sleep(randint(0, 3))
    num += 1
    # print("num in rum = ", num)


def without_thread_lock():
    thread_list = []

    for i in range(50):
        t = threading.Thread(target=run)
        t.start()
        thread_list.append(t)

    for t in thread_list:
        t.join()

        # time.sleep(1)
        # print("inner num = ", num)

    print("outer num = ", num)  # 在 ubuntu 或者 mac 下的 python2.x 中，可能会出现少于 50 的值。


if __name__ == '__main__':
    without_thread_lock()

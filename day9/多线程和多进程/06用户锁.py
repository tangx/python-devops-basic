#!/usr/bin/env python
# encoding: utf-8

"""
@author: tangxin@haowan123.com
@python_version: python2.7
@file: 06用户锁.py
@time: 2017/8/4 17:25
"""

import os
import sys
import threading
import time
from random import randint

num = 0
lock = threading.Lock()


def run():
    global num

    # 用户锁的原则是，尽量减少锁时间
    lock.acquire()  # 申请锁
    num += 1
    lock.release()  # 释放锁

    # print("num in rum = ", num)

    # time.sleep(randint(0, 3))
    time.sleep(1)   # 将 sleep 放在 lock 外面。



def without_thread_lock():
    start_time = time.time()
    thread_list = []

    for i in range(50):
        t = threading.Thread(target=run)
        t.start()
        thread_list.append(t)

    for t in thread_list:
        t.join()

        # time.sleep(1)
        # print("inner num = ", num)

    print("outer num = ", num)  # 在 ubuntu 或者 mac 下的 python 中，可能会出现少于 50 的值。

    print("total cost:", (time.time() - start_time))


if __name__ == '__main__':
    without_thread_lock()

#!/usr/bin/env python
# encoding: utf-8

"""
@author: tangxin@haowan123.com
@python_version: python2.7
@file: 04守护线程.py
@time: 2017/8/4 16:39
"""

import os
import sys
import threading
import time
import random

"""
当将子线程被设置为守护线程之后，主线程的退出将不在依赖该线程的执行结果。
+ 主线程只需要等待非守护线程结束后，即可退出。
+ 主线程不需要等待守护线程结束，也可以退出。
"""


def daemon_thread(n):
    print("start daemon subprocess -> %s " % n)
    time.sleep(random.randint(10, 20))
    print("stop daemon subprocess -> %s " % n)


def common_thread(n):
    print("start common subprocess -> %s " % n)
    time.sleep(random.randint(1, 2))
    print("stop common subprocess -> %s " % n)


def main():
    start_time = time.time()

    t1 = threading.Thread(target=daemon_thread, args=(1,))
    t2 = threading.Thread(target=common_thread, args=(2,))
    t1.setDaemon(daemonic=True)     # `setDaemon` 必须存在于 `start` 之前
    t1.start()
    t2.start()

    # t2.join()
    # t1.join()     # 但是，主线程依旧是可以使用 t.join() 等待守护线程的结束。
    # print("time spend: %s" % (time.time() - start_time))


if __name__ == '__main__':
    main()

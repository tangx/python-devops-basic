#!/usr/bin/env python
# encoding: utf-8

"""
@author: tangxin@haowan123.com
@python_version: python2.7
@file: 03主线程等待子线程结束_join.py
@time: 2017/8/4 15:53
"""

import os
import sys
import threading
import time
from random import randint


# 使用 `threading.current_thread()` 显示当前线程 PID
# 使用 `threading.currentThread` 显示当前线程的内存地址
# 使用 `threading.active_count()` 显示当前线程的个数


def sayhello(n):
    print("start subprocess OK -> %s " % n, threading.current_thread())
    print("start subprocess OK -> %s " % n, threading.currentThread)
    time.sleep(randint(1, 5))
    print("stop  subprocess OK -> %s " % n)


def main():
    print("start main thread OK ->  ", threading.current_thread())
    print("start main thread OK ->  ", threading.currentThread)

    # # 使用 `t.join()` 等待线程执行结果。
    # #   + 使用了 `join()` 之后，进程一定会等待该线程结束之后，再继续执行。

    start_time = time.time()

    t1 = threading.Thread(target=sayhello, args=(1,))
    t2 = threading.Thread(target=sayhello, args=(2,))

    t1.start()
    # t1.join()

    t2.start()
    t2.join()
    stop_time = time.time()

    print("total cost: %s" % (stop_time - start_time))

    # # 主线程在默认情况下，会有一个 `join()`。 主线程会在子线程全部结束之后再结束。

    print(threading.active_count())


if __name__ == '__main__':
    main()

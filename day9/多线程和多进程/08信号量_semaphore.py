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
@FILE: 08信号量_semaphore.py
@time: 2017/8/5 13:20
"""

"""
同一时间允许多个线程在锁内工作
"""

import os
import sys
import threading
import time
from random import randint

num = 0

semaphore = threading.BoundedSemaphore(5)   # 同时允许 N 个线程调用锁


def run(n):
    semaphore.acquire()

    print("in run: subporcess: %s; all threads number = %s " % (n, threading.active_count()))

    time.sleep(randint(2, 5))

    semaphore.release()


def main():
    # semaphore.acquire()
    for i in xrange(20):
        # time.sleep(0.1)
        t = threading.Thread(target=run, args=(i,))
        t.start()


if __name__ == "__main__":
    main()

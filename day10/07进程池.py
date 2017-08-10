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
@FILE: 07进程池.py
@time: 2017/8/10 21:13
"""

import os
import sys
import time
from multiprocessing import Process, Pool


def foo(i):
    time.sleep(1)
    print("in the subprocess %s: %s " % (i, os.getpid()))


def bar(i):
    print("  --> in callback %s: %s" % (i, os.getpid()))


def main():
    pool = Pool(processes=3)  # 声明可以同时最多有三个子进程

    print("main process : %s " % (os.getpid(),))

    for i in range(10):
        """
           pool 有两个方法
             + apply : 串行
             + apply_async: 异步并行
               + apply_async 可以使用回调函数，回调函数在主进程中被调用
        """
        # pool.apply(func=foo, args=(i,))           # 串行
        # pool.apply_async(func=foo, args=(i,))     # 并行
        # pool.apply(func=foo, args=(i,), callable=bar)      # wrong: pool.apple 没有回调函数
        pool.apply_async(func=foo, args=(i,), callback=bar)  # 回调函数是通过主进程执行的。

    """
        在使用 apply_async 的时候，必须使用 pool.close() 和 pool.join()。
        并且 pool.close() 必须在 pool.join() 之前被使用，否则会报错。
    """
    pool.close()    # 异步并行的时候必须存在，否则会报错
    pool.join()     # 必须存在，否则程序直接退出。


if __name__ == "__main__":
    main()

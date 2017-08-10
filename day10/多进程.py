#!/usr/bin/env python
# encoding: utf-8

"""
@author: tangxin@haowan123.com
@python_version: python3.6
@file: 多进程.py
@time: 2017/8/10 16:26
"""

"""
进程之间的数据相互独立，不能共享。
每一个子进程都是由其父进程启动的


多进程的语法与多线程差不多
"""

import os
import sys
import multiprocessing
import time


def run(name):
    print("\033[31min child process.\033[0m")
    print("parent process pid:", os.getppid())
    print("current process pid:", os.getpid())
    print("\n==== \n")
    time.sleep(2)

    # info()
    # print("hello, %s " % name)


def info():
    print("\033[31min child process.\033[0m")
    print("parent process pid:", os.getppid())
    print("current process pid:", os.getpid())
    print("\n==== \n")


def main():
    info()
    p = multiprocessing.Process(target=run, args=("world",))
    p.start()

    p_list = []
    start_time = time.time()
    for i in range(2):
        p = multiprocessing.Process(target=run, args=('Max -> %s' % i,))
        p.start()

        p_list.append(p)

    for p in p_list:
        p.join()

    print("total cost: ", time.time() - start_time)


if __name__ == '__main__':
    main()

#!/usr/bin/env python
# encoding: utf-8

"""
@author: tangxin@haowan123.com
@python_version: python2.7
@file: 01多线程写法01.py
@time: 2017/8/4 15:12
"""

import os
import sys
import threading
import time


def run(n):
    print("in sub process -> %s" % n)
    time.sleep(3)


def sayhello():
    print("hello, my love")
    time.sleep(3)


def main():
    # # 使用 `target` 指定目标函数。
    #   + 目标函数名称可以是任意值
    #   + 目标函数只需要函数名，不需要括号
    # # 使用 `args` 传入参数。参数必须是一个元组。
    t1 = threading.Thread(target=run, args=(1,))
    t2 = threading.Thread(target=sayhello)

    t1.start()
    t2.start()


if __name__ == '__main__':
    main()

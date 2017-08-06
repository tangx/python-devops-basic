#!/usr/bin/env python
# encoding: utf-8

"""
@author: tangxin@haowan123.com
@python_version: python2.7
@file: 02多线程写法02_类继承式调用.py
@time: 2017/8/4 15:38
"""

import os
import sys
import threading
import time


class MyThread(threading.Thread):
    def __init__(self, n):
        super(MyThread, self).__init__()
        # threading.Thread.__init__(self)
        self.n = n

    def run(self):
        # # 这里的函数名称必须是 `run`。
        # #   + 因为这里重构了父类的方法。

        print("running subprocess task -> %s " % self.n)
        time.sleep(3)


def main():
    t1 = MyThread("t1")
    t2 = MyThread('t2')

    t1.start()
    t2.start()


if __name__ == '__main__':
    main()

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
@FILE: 装饰器.py
@time: 2017/6/9 10:25
"""

import os
import sys
import time


def timer(func):
    # *args, **kwargs 传入非固定参数
    # *args: 字符串、数字、列表、函数 等
    # **kwargs: 字典
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        stop_time = time.time()

        print "func cost time: %s" % (stop_time - start_time)

    # 注意这里要返回 wrapper 而非返回 wrapper()
    return wrapper


# 注意这里要调用『 @timmer 』 以 『@』开头
# @ 被称为语法糖
@timer
def test1():
    time.sleep(3)
    print "line in test1"


@timer
def test2(name):
    time.sleep(2)
    print "line in test2: %s" % name


if __name__ == "__main__":
    test1()
    test2("barbosa")
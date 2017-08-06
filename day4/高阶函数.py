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
@FILE: 高阶函数.py
@time: 2017/6/9 11:33
"""

import os
import sys
import time

"""
2. 高阶函数
  2.1 把函数名作为实参传入另外一个函数
  2.2 返回值中包含函数名
"""


def bar():
    time.sleep(3)
    print "in the bar"


def fun_2_1(x, y, func):
    """ 把函数名作为实参传入另外一个函数 ， 不改变装饰函数源代码"""
    print func(x) + func(y)


def func_2_2(func):
    """ 返回值中包含函数名 ， 不改变函数调用方式"""
    print func
    return func


if __name__ == "__main__":

    # 2_1
    fun_2_1(-1, 5, abs)

    # 2_2
    bar = func_2_2(bar)
    bar()

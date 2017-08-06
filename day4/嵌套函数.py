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
@FILE: 嵌套函数.py
@time: 2017/6/9 14:15
"""

import os
import sys

"""在一个函数体内使用 def 声明另一个函数"""


def foo():
    print "in the foo"

    def bar():
        print "in the bar"

    # bar 可以理解为局部变量，只存在于 foo 内。因此不能在 foo 外部调用
    bar()


def test1():
    print "in the test1"


def test2():
    print "in the test2"
    # 函数调用
    test1()


def grandpa():
    """
    # 作用域
    只能从内网外找
    """
    x = 1

    def dad():
        x = 2

        def son():
            x = 3
            print x

        son()

    dad()


if __name__ == "__main__":
    # 嵌套函数
    foo()

    # 调用函数
    test2()

    # 作用域
    grandpa()

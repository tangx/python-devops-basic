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
@FILE: 生成器构建斐波那契函数.py
@time: 2017/6/10 11:45
"""

import os
import sys

"""
使用 yield 构建生成器
"""

def fib(max):
    n, a, b = 0, 0, 1

    while n < max:
        a, b = b, a + b

        # 使用 yield 生成返回值
        yield b
        # print b
        n += 1
    # while 退出处罚条件
    else:
        yield "done"

        # python versions < 3.3 do not allow 'return' with argument inside generator.
        # python 版本小于 3.3 不允许在生成器中使用return
        # return "fib generator done"


if __name__ == "__main__":
    # print fib(10)

    # for f in fib(10):
    #     print f

    f = fib(10)

    # 在 python 3.3 以后可以使用错误捕获return的值
    while True:
        try:
            print f.next()
        except StopIteration as e:
            print "Generator return value:", e
            break

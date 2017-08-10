#!/usr/bin/env python
# encoding: utf-8
#

"""
@license: Apache Licence
@python ver: Python 2.7.12
@python ver: Python 3.6
@FILE: 10_gevent协程IO切换.py
@time: 2017/8/10 23:24
"""

import os
import sys
import gevent


def foo():
    print("\033[31min foo header \033[0m")
    gevent.sleep(2)
    print("\033[31min foo footer \033[0m")



def bar():

    print("\033[32min bar header \033[0m")
    gevent.sleep(1)
    print("\033[32min bar footer \033[0m")

def func():
    print("\033[33min func header \033[0m")
    gevent.sleep(0.1)     # 触发 IO 切换，但是由于 IO 时间最短，因此继续执行下面
    print("\033[33min func footer \033[0m")



if __name__ == "__main__":
    gevent.joinall([
        gevent.spawn(foo),
        gevent.spawn(bar),
        gevent.spawn(func)
    ])

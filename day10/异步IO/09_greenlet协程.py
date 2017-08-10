#!/usr/bin/env python
# encoding: utf-8
#

"""
@license: Apache Licence
@python ver: Python 2.7.12
@python ver: Python 3.6
@FILE: 09_greenlet协程.py
@time: 2017/8/10 23:18
"""

import os
import sys
from greenlet import greenlet


def test1():
    print(12)
    gl2.switch()    # 协程切换
    print(34)
    gl2.switch()


def test2():
    print(56)
    gl1.switch()
    print(78)


if __name__ == "__main__":
    gl1 = greenlet(test1)   # 启动一个协程
    gl2 = greenlet(test2)
    gl1.switch()

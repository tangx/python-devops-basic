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
@FILE: 生成器应用协程.py
@time: 2017/6/10 15:04
"""

import os
import sys
import time

"""
串行代码下的并行效果
"""


def consumer(name):
    print "%s 进入餐馆，准备吃包子了" % name

    while True:
        # 当程序运行到 yield 的时候，跳出。
        # 并保存当前状态，下次进入后继续运行
        baozi = yield

        print "包子 [%s] 被 [%s] 吃了" % (baozi, name)


# c = consumer('tangx')
#
# c.next()
# c.next()


def producer():
    c1 = consumer('tang')
    c2 = consumer('xin')

    c1.next()
    c2.next()

    for i in xrange(1, 10):
        print "厨师做好了2个包子"
        c1.send(i)
        c2.send(i)

        # send 为生成器方法之一
        # 作用是激活生成器，并将传入变量发送到生成器。
        # 生成器将传入的值作为当前返回表达式的值。
        # 即『传入即结果』
        # '''Resumes the generator and "sends" a value that becomes
        # the result of the current yield-expression.'''

        time.sleep(1)

if __name__ == "__main__":
    producer()

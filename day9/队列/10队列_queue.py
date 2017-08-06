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
@python ver: Python 3.6
@FILE: 10队列_queue.py
@time: 2017/8/5 14:17
"""

import os
import sys
import time
import queue
import threading
from random import randint

# q = queue.Queue()     ## FIFO  # 先进先出
q = queue.LifoQueue()  ## LIFO  # 后进先出
q = queue.PriorityQueue()  ## 带有优先级的 FIFO 队列


def producer():
    for i in range(10):
        priority_int = randint(1, 10)

        time.sleep(randint(1, 2))
        print("Producer 生产了一个包子 ->  baozi %s" % i)
        # q.put("baozi %s " % i)

        # queue.PriorityQueue()  ## 带有优先级的 FIFO 队列
        # priority_int = randint(1, 10)
        q.put((priority_int, "baozi %s" % i))  # 由于 q 只能接受一个参数，因此需要使用元组传参
        # q.put("pro %s : baozi %s" % (priority_int, i))


def consumer():
    while True:
        time.sleep(1)
        try:
            # (p, b) = q.get(timeout=3)  # 当使用优先级队列的时候，取出来的值为排序的优先值
            b = q.get(timeout=3)  # 当使用优先级队列的时候，取出来的值为排序的优先值
            # b = q.get_nowait()
            print("狗吃了 -> p:%s %s" % b)

            # print(b)

        except queue.Empty as e:
            print("包子都被狗吃完了")
            break


def main():
    p = threading.Thread(target=producer)
    p.start()

    time.sleep(5)

    c = threading.Thread(target=consumer)
    c.start()


if __name__ == "__main__":
    main()

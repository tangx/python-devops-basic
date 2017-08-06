#!/usr/bin/env python
# encoding: utf-8
#

"""
@version:  0.0.1
@author: TangHsin
@license: Apache Licence
@mailto: octowhale@github
@software: PyCharm Community Edition
@python ver: Python 3.6
@FILE: 优先级队列_银行排号系统.py
@time: 2017/8/5 14:17
"""

"""
q = queue.PriorityQueue()  ## 带有优先级的 FIFO 队列

  + 由于 q.get() 只能接受一个参数，因此需要使用元组传参
    + q.get((priority, descript))
    + q.get(number)
    + q.get("string")

  + 数字越小，队列优先级越高
    + 队列优先级比较中， 数字不能与字母比较
    + 数字比较按照 a-z 的数序
    + 字符串数字 "11" 比 "2" 的优先级高
"""

import time
import queue
import threading
from random import randint

# q = queue.Queue()     ## FIFO  # 先进先出
# q = queue.LifoQueue()  ## LIFO  # 后进先出
q = queue.PriorityQueue()  ## 带有优先级的 FIFO 队列


def banker(name):
    """银行柜员"""
    print("%s 柜台准备就绪" % name)
    while True:
        try:
            priority, c_name = q.get(timeout=10)
            # print("%s banker waiting" % name)
            if "vip" in c_name:
                print("\033[32m请 %s 到 %s 柜台办理业务\033[0m" % (c_name, name))
            else:
                print("请 %s 到 %s 柜台办理业务" % (c_name, name))

            time.sleep(randint(1, 15))  # 随机办理业务时间
        except queue.Empty:
            print("%s 柜台所有业务都办理完成" % name)
            break


def customer():
    """普通客户叫号系统"""
    for cus_num in range(1, 10):
        time.sleep(randint(1, 3))
        q.put((10, "cus_%s" % cus_num))
        print("cus_%s 进入队列" % cus_num)


def vipCustomer():
    """vip 叫号系统"""
    for vip_num in range(1, 5):
        time.sleep(randint(1, 8))  # vip 随机进入
        q.put((1, "vip_%s" % vip_num))
        print("\033[32mvip_%s 进入队列\033[0m" % vip_num)


def main():
    b1 = threading.Thread(target=banker, args=(1,))
    b2 = threading.Thread(target=banker, args=(2,))
    b3 = threading.Thread(target=banker, args=(3,))

    b1.start()
    b2.start()
    b3.start()

    c = threading.Thread(target=customer)
    c.start()

    vc = threading.Thread(target=vipCustomer)
    vc.start()


if __name__ == "__main__":
    main()

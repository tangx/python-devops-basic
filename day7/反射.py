#!/usr/bin/env python
# encoding: utf-8

"""
@author: tangxin@haowan123.com
@python_version: python2.7
@file: 反射.py
@time: 2017/7/21 10:21
"""

import os
import sys

'''
# 反射
  通过字符串映射或修改程序运行时的状态、属性、方法，也偶一下4个方法
  + hasattr(object, name_string): 判断 object 对象中， 是否还有 name_string 对应的方法或属性。如果有则返回 True，反之 返回 False。
  + getattr(object, name_string): 获取 object 对象中 ，name_string 对应方法的内存地址或属性的值
  + setattr(object, key , value): 为 object 新建一个方法或属性，或修改一个已存在的方法或属性的值。 相当于 object.key = value。
  + delattr(object ,name_string): 删除 object 中的一个方法或属性。
'''


class Dog(object):
    def __init__(self, name):
        self.name = name
        self.talk = "%s can talk" % self.name

    def eat(self):
        print("%s is eating ..." % self.name)


def bulk(self):
    """
    这里必须传入 self ，否则再外面调用的时候，会提示缺少参数
    TypeError: bulk() takes 0 positional arguments but 1 was given
    """
    print("%s is bulking ... wang wang wang" % self.name)


def buuulk(self):
    print("%s is buuulking ... waff waff waff " % self.name)


if __name__ == '__main__':

    d = Dog("nyh")

    while True:

        choice = input(">>: ").strip()

        if choice == ";exit" or choice == "":
            sys.exit(0)

        # hasattr(obj,key)
        if hasattr(d, choice):
            print("hasattr(d, choice) = ", hasattr(d, choice))
            try:
                # getattr(obj,key)
                getattr(d, choice)()

            except:
                print(getattr(d, choice))

        if not hasattr(d, choice):
            # setattr(obj, key, value)
            print("==== try to get %s in d ====" % choice)
            try:
                getattr(d, choice)(d)
            except:
                print("d has no attribute of %s" % choice)

            print("==== add %s to d ====" % choice)
            setattr(d, choice, bulk)
            getattr(d, choice)(d)

            # reset a attribute of object

            print("==== reset %s in d ====" % choice)
            setattr(d, choice, buuulk)
            getattr(d, choice)(d)

            # delete a attribute of object
            print("==== delete %s in d ====" % choice)
            delattr(d, choice)
            try:
                getattr(d, choice)(d)
            except:
                print("d has no attribute of %s" % choice)

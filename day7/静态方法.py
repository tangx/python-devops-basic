#!/usr/bin/env python
# encoding: utf-8

"""
@author: tangxin@haowan123.com
@python_version: python2.7
@file: 静态方法.py
@time: 2017/7/20 10:27
"""

import os
import sys

'''
# 静态方法
  @staticmethod
  静态方法实际上是取消 类方法与类的关联。将类方法变成一个单纯的函数。
  类中的函数只是名义上属于类，但是不能访问内中的任何东西。
'''

class Dog(object):
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print("%s is eating %s" % (self.name, food))

    @staticmethod
    def eat_static(food):
        print("somebody is eating %s" % food)


if __name__ == '__main__':
    d = Dog("Chengronghua")

    d.eat("baozi")
    d.eat_static("mantou")

#!/usr/bin/env python
# encoding: utf-8

"""
@author: tangxin@haowan123.com
@python_version: python2.7
@file: 属性方法.py
@time: 2017/7/20 14:37
"""

import os
import sys


class People(object):
    def __init__(self, name):
        self.name = name
        self.__food = None

    # 设置一个属性方法
    @property
    def eat(self):
        print("%s is eating %s" % (self.name, self.__food))

    # 对属性方法赋值
    # 这里的方法名应该与属性方法的函数名一样。
    @eat.setter
    def eat(self, food):
        print("set to food:", food)
        self.__food = food

    @eat.setter
    def Eat(self, food):
        print("set to food in Eat: ", food)
        self.__food = food

    @eat.deleter
    def eat(self):
        del self.__food


if __name__ == '__main__':
    d = People('chengronghua')
    # d.eat('baozi')

    # d.eat = 'mantou'

    d.eat
    ## eat.setter
    d.eat = 'baozi'

    d.eat

    ## eat.deleter
    del d.eat
    d.eat

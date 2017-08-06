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
@FILE: 列表操作.py
@time: 2017/6/9 8:27
"""

import os
import sys


def list_copy():
    list1 = ["a", "b", "c", ["e_1", "e_2"], "d"]

    # 浅复制
    list2 = list1[:]
    """
    python 3

    list1.copy() # 浅copy
    """

    list1[2] = "initial_C"
    list1[3][0] = "E_1"

    print list1
    print list2


def list_deep_copy():
    import copy

    list1 = ["a", "b", "c", ["e_1", "e_2"], "d"]

    # 浅复制
    list2 = copy.copy(list1)

    list1[2] = "initial_C"
    list1[3][0] = "E_1"

    print list1
    print list2

    list1 = ["a", "b", "c", ["e_1", "e_2"], "d"]

    # 深复制 完全独立
    list2 = copy.deepcopy(list1)

    list1[2] = "initial_C"
    list1[3][0] = "E_1"

    print list1
    print list2


if __name__ == "__main__":
    # list_copy()
    list_deep_copy()
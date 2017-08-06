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
@FILE: 文件替换.py
@time: 2017/6/8 22:35
"""

import os
import sys


def main():
    f = open('lyric', mode='r')
    f_new = open('lyric.new', mode='w')

    for line in f:
        if '毛主席' in line:
            line = line.replace('毛主席', ' chairman mao')
            # print line
        f_new.write(line)

    f.close()
    f_new.close()


if __name__ == "__main__":
    main()

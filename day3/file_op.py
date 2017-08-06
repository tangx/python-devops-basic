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
@FILE: file_op.py
@time: 2017/6/8 15:46

http://www.cnblogs.com/alex3714/category/770733.html
http://www.cnblogs.com/alex3714/articles/5717620.html

"""

import os
import sys


def read_file():
    '''读取文件所有内容'''
    f = open('lyric', mode='r')  # 文件句柄
    data = f.read()
    data2 = f.read()

    print (data)

    print ('---------data2 ------------%s---', data2)

    print f.read()

    f.close()


def write_file():
    """创建一个文件，并覆盖原有文件"""
    f = open('lyric', mode='w')  # mode='w', 创建一个文件，覆盖已有文件

    f.write('我爱北京天安门，\n')
    f.write('天安门上台上升。。。。。\n')
    f.close()


def append_file():
    """在原有文件中追加内容"""
    f = open('lyric', mode='a')  # mode='a', 在原有文件中追加内容

    f.write('伟大领袖毛主席。')

    f.close()


def readline_file():
    """ 读取文本一行信息 """
    f = open('lyric2')

    for i in xrange(5):
        print (f.readline())

    f.close()


def readlines_file():
    """读取所有行到内存中，返回一个列表
    只适合读小文件
    """
    f = open('lyric2')

    # for line in f.readlines():
    #     print (line.strip())

    for index, line in enumerate(f.readlines()):
        if index == 9:
            print "========="
        else:
            print line

    f.close()


def xreadlines_file():
    """ 生成器 ，返回列表"""
    f = open('lyric2')

    for index, line in enumerate(f.xreadlines()):
        print type(f.xreadlines())
        if index == 9:
            print "========="
        else:
            print line.strip()


def readline_file_02():
    """ 迭代器 , 按行读取文件"""
    f = open('lyric2')
    for line in f:
        print line

    f.close()


def tell_seek_file():
    """
        f.tell() 返回光标位置，按字符计数
        f.seek(num) 将光标移动到指定位置

    """
    f = open('lyric2')

    print (f.tell())
    print f.readline()

    print (f.tell())

    # 移动光标
    f.seek(3)

    print f.readline()

    f.close()


def other_function_file():
    f = open('lyric2', 'w')

    f.fileno()  # 返回文件编号。 python 使用操作系统的io维护文件
    print f.name  # 文件名
    f.isatty()  # 是否是一个终端（例如打印机）

    f.flush()  # 将缓存中的数据写入硬盘，与 'w' 搭配

    f.truncate()  # 清空文件
    f.truncate(size=10)  # 从 0 开始，保留 size 大小之前的数据。 与 mode='a' 搭配
    f.close()


def stdout_write():
    # sys.stdout.write("#")     # 标准输出
    # sys.stdout.flush()
    import time
    for i in xrange(10):
        sys.stdout.write(" # ")
        sys.stdout.flush()
        time.sleep(0.4)


def read_write_file():
    # f = open('lyric2', 'r+')  # """读写文件 读和追加模式"""
    # f = open('lyric3', 'a+')  # """写读文件 覆盖追加模式"""
    f = open('lyric3', 'w+')  # """写读文件 覆盖追加读写模式"""

    f.write("------------1\n")
    f.write("------------1\n")
    f.write("------------1\n")
    f.write("------------1\n")
    print f.tell()
    f.seek(5)

    print f.tell()

    f.write("-something-")


    f.close()

def read_write_binary_file():
    """ 读二进制
    在 python2.7 中，socket 可以使用字符串传文件
    在 python3.x 中，socket 只能使用二进制串文件，即使是文本文件
    """
    f = open('lyric', mode='rb')  # 读二进制文件


    f.close()


    f = open('lyric', mode='wb')  # 写二进制文件
    f.write("hello. binary\n".encode()) # 转换编码
    f.close()


if __name__ == "__main__":
    # write_file()
    # append_file()
    # read_file()
    # readline_file()
    # readlines_file()
    # xreadlines_file()
    # readline_file_02()
    # tell_seek_file()
    # other_function_file()
    # stdout_write()
    read_write_file()
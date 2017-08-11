#!/usr/bin/env python
# encoding: utf-8

"""
@author: tangxin@haowan123.com
@python_version: python3.6
@file: 11_使用gevent并发爬网页.py
@time: 2017/8/11 8:44
"""

import os
import sys
from urllib.request import urlopen
from gevent import monkey
import gevent
import time

"""
    `monkey.patch_all()` : 把当前进程及子进程的 IO 单独做标记。并提供给 gevent 做切换。
    如果不使用 `monkey.patch_all()` 的话， gevent 不能发现 urllib 的 IO 操作。那么主进程将会变成串行模式。因为无法进行 IO 切换。
"""

monkey.patch_all()  # 把当前进程及子进程的 IO 单独做标记。并提供给 gevent 做切换。


def crawler(url):
    print("start to crawl : ", url)
    resp = urlopen(url)
    data = resp.read()

    print(len(data), url)


if __name__ == '__main__':
    # crawler('http://www.python.org')
    # crawler('http://www.sina.com.cn')

    url_list1 = ['http://www.sina.com.cn/', 'http://www.163.com/', 'http://www.qq.com/']
    url_list2 = ['http://github.com/', 'http://www.yahoo.com/', 'http://www.python.org/']

    url_list = url_list1
    # url1 = url_list[0]
    # url2 = url_list[1]
    # url3 = url_list[2]

    start_time = time.time()
    for url in url_list:
        crawler(url)
    print("串行消耗时间：", time.time() - start_time)

    g_spawn_list = []
    for url in url_list:
        g_spawn_list.append(gevent.spawn(crawler, url))

    async_start_time = time.time()
    # gevent.joinall([
    #     gevent.spawn(crawler, url1),
    #     gevent.spawn(crawler, url2),
    #     gevent.spawn(crawler, url3)
    # ])

    gevent.joinall(g_spawn_list)
    print("并行消耗时间：", time.time() - async_start_time)

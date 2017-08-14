#!/usr/bin/env python
# encoding: utf-8

"""
@author: tangxin@haowan123.com
@python_version: python2.7
@python_version: python3.6
@file: 02_redis操作.py
@time: 2017/8/14 12:51
"""

"""
> http://www.cnblogs.com/wupeiqi/articles/5132791.html
"""

import os
import sys
import redis

redis_host = '192.168.56.201'
redis_port = 6379

pool = redis.ConnectionPool(host=redis_host, port=redis_port)

r = redis.Redis(connection_pool=pool)


def string_mode():
    """字符串

    在Redis中设置值，默认，不存在则创建，存在则修改
    参数：
         ex，过期时间（秒）
         px，过期时间（毫秒）
         nx，如果设置为True，则只有name不存在时，当前set操作才执行
         xx，如果设置为True，则只有name存在时，当前set操作才执行

    setnx(name, value)
    setex(name, value, time)
    psetex(name, time_ms, value)
    """

    pass


def hash_mode():
    """哈希"""
    pass


def list_mode():
    """列表"""
    pass


def set_mode():
    """无序集合"""
    pass


def sort_set_mode():
    """有序集合"""
    pass


def pipe_mode():
    """管道"""
    pass


def subscribe_mode():
    """发布订阅"""
    pass


def main():
    pass


if __name__ == '__main__':
    main()

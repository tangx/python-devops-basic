#!/usr/bin/env python
# encoding: utf-8

"""
@author: tangxin@haowan123.com
@python_version: python2.7
@python_version: python3.6
@file: 01_redis连接与连接池.py
@time: 2017/8/14 9:00
"""

import os
import sys
import redis
import time

redis_host = '192.168.56.201'
redis_port = 6379


def redis_conn():
    """（短连接） 连接redis"""
    r = redis.Redis(host=redis_host, port=redis_port)
    r.set('foo', 'bar')
    # time.sleep(3)
    print(r.get('foo'))


def redis_conn_pool():
    """（长连接） 使用连接池连接 redis 避免每次操作都重新建立连接。"""
    pool = redis.ConnectionPool(host=redis_host, port=redis_port)

    r = redis.Redis(connection_pool=pool)

    r.set('foo2', 'bar2')
    print(r.get('foo2'))


if __name__ == '__main__':
    redis_conn_pool()

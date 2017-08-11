#!/usr/bin/env python
# encoding: utf-8

"""
@author: tangxin@haowan123.com
@python_version: python2.7
@python_version: python3.6
@file: socket_server.py
@time: 2017/8/11 11:37
"""

import os
import sys
import gevent
import time
import socket
# from gevent import socket, monkey       # 这里也导入 socket？ 到底用那个？
from gevent import monkey  # 这里也导入 socket？ 到底用那个？

monkey.patch_all()


def server(ip='0.0.0.0', port=30086):
    s = socket.socket()
    s.bind((ip, port))

    s.listen(500)  # ??

    while True:
        cli, addr = s.accept()  # ??
        gevent.spawn(handle_request, cli)  # 开始阻塞


def handle_request(conn):
    try:
        while True:
            data = conn.recv(1024)      # 接收 1024 字节
            print("recv: ", data)       # 打印接收内容
            conn.send(data)             # 将接收内容发送回去

            if not data:
                conn.shutdown(socket.SHUT_WR)
    except Exception as e:
        print(e)
    finally:
        conn.close()


if __name__ == '__main__':
    server()

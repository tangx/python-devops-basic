#!/usr/bin/env python
# encoding: utf-8
#

"""
@license: Apache Licence
@python ver: Python 2.7.12
@python ver: Python 3.6
@FILE: 14_selectors实现IO多路复用.py
@time: 2017/8/13 14:47
"""

"""
> https://docs.python.org/3/library/selectors.html#classes
"""

import os
import sys
import selectors
import socket

host = '127.0.0.1'
port = 9999


def server_active(server, mask):
    conn, addr = server.accept()
    print('accept', conn, 'from', addr)
    conn.setblocking(False)

    # register(fileobj, events, data=None)
    sel.register(conn, selectors.EVENT_READ, conn_active)


def conn_active(conn, mask):
    data = conn.recv(1024)
    if data:
        print('echoing', repr(data), 'to', conn)
        conn.send(data)
    else:
        print('closing', conn)
        sel.unregister(conn)
        conn.close()



#############

# 注册 selectors，
# 默认使用 epoll，当不支持epoll时使用 select
sel = selectors.DefaultSelector()

server = socket.socket()        # 实例化一个 server
server.bind((host, port))
server.setblocking(False)
server.listen(100)

# 向 selectors 中注册监听 server 的活动。
# 当 server 有活动的时候，则调用 server_active 函数
sel.register(server, selectors.EVENT_READ, server_active)

while True:
    events = sel.select()       # 默认使用 epoll，当不支持epoll时使用 select
    # print("event: ", events)
    for key, mask in events:
        # print("key: ", key)
        # print("mask:", mask)

        # callback 回调函数
        # 此处为 sel.register 注册时填入的 server_active, 或 conn_active
        callback = key.data
        callback(key.fileobj, mask)  # key.fileobj 为 server的句柄

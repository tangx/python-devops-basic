#!/usr/bin/env python
# encoding: utf-8
#

"""
@license: Apache Licence
@python ver: Python 2.7.12
@python ver: Python 3.6
@FILE: 13_select实现IO多路复用.py
@time: 2017/8/11 21:33
"""

import os
import sys
import time
import select
import socket
import queue

host = '0.0.0.0'
port = 9999
server = socket.socket()
server.bind((host, port))

server.listen(500)

server.setblocking(False)  # 设置非阻塞模式

inputs = [server, ]  # 监控输入的活动队列
outputs = []  # 监控输出的活动队列
queue_dict = {}  # 为了实现单独输出，新建 outputs 队列的链接消息字典

while True:

    # readable : 有输入活动的链接队列
    # writeable: 有输出活动的链接队列
    # exceptional: 出错的活动的链接队列
    # rlist: 监控具有输入活动的队列
    # wlist: 监控需要输出活动的队列
    # xlist: 监控出错的链接队列
    # readable, writeable, exceptional = select.select(rlist=inputs, wlist=outputs, xlist=inputs)
    readable, writeable, exceptional = select.select(inputs, outputs, inputs)
    # print(readable, writeable, exceptional)

    for r in readable:
        # print(r)

        if r is server:
            conn, addr = server.accept()  # 建立连接
            inputs.append(conn)  # 将新建立的链接放入 select 监控列表
            queue_dict[conn] = queue.Queue()  # 新建输出消息队列
        else:
            try:
                data = r.recv(10)  # 接收数据
                print(data)
                queue_dict[r].put(data)  # 向输出队列中加入消息
                outputs.append(r)  # 将输出链接放入 select 监控列表
            except ConnectionResetError as e:
                inputs.remove(r)
                del queue_dict[r]
                print("用户关闭了一个链接")

    for w in writeable:
        w.send(queue_dict[w].get())  # 发送输出
        outputs.remove(w)  # 将已经完成消息发送的链接移除监控列表

    for e in exceptional:  # 异常处理
        if e in outputs:  # 移除发送监控列表
            outputs.remove(e)
        if e in inputs:  # 移除接收监控列表
            inputs.remove(e)
        del queue_dict[e]  # 移除消息队列

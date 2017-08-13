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

host = '127.0.0.1'
port = 9999
server = socket.socket()
server.bind((host, port))

server.listen(500)

server.setblocking(False)

inputs = [server]
outputs = []

readable, writeable, exceptional = select.select(inputs, outputs, inputs)

for r in readable:
    # if r is server:
        conn, addr = r.accpet()
        inputs.append(conn)
    # else:
    #     r.recv(1024)

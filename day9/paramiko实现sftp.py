#!/usr/bin/env python
# encoding: utf-8

"""
@author: tangxin@haowan123.com
@python_version: python2.7
@file: paramiko实现sftp.py
@time: 2017/8/4 10:50
"""

import os
import sys
import paramiko


def para_sftp():
    transport = paramiko.Transport('192.168.56.201', 22)
    transport.connect(username='root', password='eibbor')

    sftp_client = paramiko.SFTPClient.from_transport(transport)

    # 上传本地文件到远程目录，路径必须精确到文件名
    sftp_client.put('bear.png',
                    '/tmp/bear.png')

    # 下载远程文件到本地目录，路径必须精确到文件名
    sftp_client.get(remotepath='/tmp/bear.png', localpath=r'C:\Users\admin\Desktop\bear.png')


if __name__ == '__main__':
    para_sftp()

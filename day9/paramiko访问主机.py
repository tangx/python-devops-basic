#!/usr/bin/env python
# encoding: utf-8

"""
@author: tangxin@haowan123.com
@python_version: python2.7
@file: paramiko访问主机.py
@time: 2017/8/4 10:03
"""

import paramiko

import os
import sys

hostname = '192.168.56.201'
port = 22
username = 'root'
password = 'eibbor'
timeout = 3

pkey_name = 'bastion_201.id_rsa'


def para_ssh():
    # 创建一个 client 实例
    client = paramiko.SSHClient()

    # 忽略 know_hosts 中 不存在主机 key 提示
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # 连接 主机
    client.connect(hostname=hostname, port=port, username=username, password=password, timeout=timeout)

    # stdin  标准输入
    # stdout 标准输出
    # stderr 标准错误输出
    stdin, stdout, stderr = client.exec_command('ls')

    for line in stdout:
        print(line.strip('\n'))
        # print(line)

    client.close()


def para_pkey_ssh():
    # 使用 private key 登录验证有两种方式
    #  + 一种是使用 private key 文件
    #  + 一种是使用 private key 文件的 file_obj。即open文件的的内容
    # > 注意： pkey 的值不能是明文的字符串。


    # # 使用 file
    # pkey = paramiko.RSAKey.from_private_key_file('bastion_201.id_rsa', password="")

    # # 使用 file_obj
    with open(pkey_name, 'r') as file_obj:
        pkey = paramiko.RSAKey.from_private_key(file_obj=file_obj)

    client = paramiko.SSHClient()

    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    client.connect(hostname=hostname, port=port, username=username, pkey=pkey)

    stdin, stdout, stderr = client.exec_command('ls')

    for line in stdout:
        print(line.strip('\n'))

    client.close()


if __name__ == '__main__':
    para_pkey_ssh()

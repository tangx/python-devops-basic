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
@FILE: haproxy_config_operate.py
@time: 2017/6/8 22:47
"""

import os
import sys
import json


def main():
    pass


def search(s):
    f = open('haproxy.cfg', mode='r')
    start_to_print = 0
    for line in f:
        if 'backend %s\n' % s in line:
            # print line
            start_to_print = 1
            continue

        if start_to_print == 1:
            if 'server' in line:
                print line.strip()
            else:
                start_to_print = 0

    f.close()


def add(s):
    """
            arg = {
            'backend': 'www.oldboy.org',
            'record':{
                'server': '100.1.7.9',
                'weight': 20,
                'maxconn': 30
            }
        }
    """
    f = open('haproxy.cfg', mode='a')

    f.write('%s %s\n' % ('backend', s['backend']))
    f.write('        server %s %s weight %s maxconn %s\n' % (s['record']['server'],
                                                             s['record']['server'],
                                                             s['record']['weight'],
                                                             s['record']['maxconn']
                                                             ))
    f.close()


def delete(s):
    f = open('haproxy.cfg', mode='r')
    f_tmp = open('haproxy.cfg.tmp', mode='w')

    start_to_delete = 0
    for line in f:
        if 'backend %s\n' % s['backend'] in line:
            start_to_delete = 1
            continue
        if start_to_delete == 1:
            if 'server' in line:
                continue
            else:
                start_to_delete = 0
        f_tmp.write(line)

    f.close()
    f_tmp.close()

    os.remove('haproxy.cfg')
    os.rename('haproxy.cfg.tmp', 'haproxy.cfg')


def update(s):
    f = open('haproxy.cfg', 'r')
    f_tmp = open('haproxy.cfg.tmp', 'w')

    start_to_update = 0

    for line in f:
        if 'backend %s\n' in line:
            start_to_update = 1
            continue


if __name__ == "__main__":
    # search('www.oldboy.org')
    #
    # arg = {
    #     'backend': 'www.oldboy.org',
    #     'record': {
    #         'server': '100.1.7.9',
    #         'weight': 20,
    #         'maxconn': 30
    #     }
    # }

    # add(arg)
    # delete(arg)

    # update(arg)

    if len(sys.argv) != 3:
        sys.exit(1)

    if sys.argv[1] == 'search':
        search(eval(sys.argv[2]))

    if sys.argv[1] == 'add':
        add(eval(sys.argv[2]))

    if sys.argv[1] == 'delete':
        delete(eval(sys.argv[2]))

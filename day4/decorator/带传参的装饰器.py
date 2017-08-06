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
@FILE: 带传参的装饰器.py
@time: 2017/6/9 16:55
"""

import os
import sys

user = 'tangx'
passwd = 'xin'


def auth(func):
    def wrapper(*args, **kwargs):

        _user = raw_input("Username: ")
        _pass = raw_input("Password: ")

        if user == _user and passwd == _pass:
            print "auth passed"
            func(*args, **kwargs)
        else:
            print "auth failed"
            sys.exit(1)

    return wrapper


def multi_auth(auth_type):
    # print auth_type

    def out_wrapper(func):

        # 基本上来说, 最底层的 wrapper 就是最 func 进行封装的了。
        # 传参都是用不定参数 *args,**kwargs
        def wrapper(*args, **kwargs):

            if auth_type == 'local':
                _user = raw_input("Username: ")
                _pass = raw_input("Password: ")

                if user == _user and passwd == _pass:
                    print "auth passed"

                    func(*args, **kwargs)

                    # return func(*args, **kwargs)

                    print "------ 分割线 ------"
                else:
                    print "auth failed"
                    sys.exit(1)
            elif auth_type == 'ldap':
                return func(*args, **kwargs)

        return wrapper

    return out_wrapper


def index():
    print "welcome index page"


@multi_auth(auth_type='local')
# @auth
def home():
    print "welcome home  page"


@multi_auth(auth_type='ldap')
# @auth
def bbs():
    print "welcome bbs   page"


if __name__ == "__main__":
    index()

    home()

    bbs()

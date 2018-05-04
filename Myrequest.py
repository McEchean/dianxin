#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/27 9:58
# @Author  : Echean
# @File    : Myrequest.py
# @Software: PyCharm

import requests
from http import cookiejar


def My_session():
    my_session = requests.Session()
    my_session.cookies = cookiejar.LWPCookieJar('cookies.txt')

    Headers = {
        'Host': 'login.189.cn',
        'Connection': 'keep-alive',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Origin': 'http://login.189.cn',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/65.0.3325.181 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Referer': 'http://login.189.cn/web/login',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',

    }

    my_session.headers = Headers.copy()
    return my_session

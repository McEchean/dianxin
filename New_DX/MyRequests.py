#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/4 14:49
# @Author  : Echean
# @File    : MyRequests.py
# @Software: PyCharm

import requests
from http import cookiejar


class My_request(object):
    def _get_session(self):
        self.session = requests.session()
        self.session.cookies = cookiejar.LWPCookieJar('cookies.txt')
        return self.session
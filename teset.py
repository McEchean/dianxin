#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/27 14:56
# @Author  : Echean
# @File    : teset.py
# @Software: PyCharm

import requests
import logging
logging.basicConfig(level=logging.INFO)

session = requests.session()


_get_init_url1 = 'http://zj.189.cn/common_v2/login.html'
session.headers.update({
    'Host': 'zj.189.cn',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/65.0.3325.181 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Referer': 'http://zj.189.cn/shouji/17342071372/service/queryorder/',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
})
_get_init_resp1 = session.get(url=_get_init_url1, headers=session.headers)
logging.info('_get_init_resp1: %s %s' % (_get_init_resp1.status_code,_get_init_resp1.text))
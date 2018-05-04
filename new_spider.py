#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/28 13:54
# @Author  : Echean
# @File    : new_spider.py
# @Software: PyCharm

import logging
import requests

logging.basicConfig(level=logging.INFO)
# session = requests.session()


class NewSpider(object):
    def __init__(self, start_url, my_session):
        self.start_url = start_url
        self.session = my_session

    def _get_ssolink(self):
        _get_ssolink_url = self.start_url
        Headers = {
            'Host': 'www.189.cn',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/66.0.3359.139 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Referer': 'http://www.189.cn/zj/',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }
        _get_ssolink_resp = self.session.get(url=_get_ssolink_url, headers=Headers, allow_redirects=False)
        logging.info('_get_ssolink_resp: %s' % _get_ssolink_resp.status_code)
        _get_ecsdo_url = _get_ssolink_resp.headers['Location']
        Headers = {
            'Host': 'www.189.cn',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/66.0.3359.139 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Referer': 'http://www.189.cn/zj/',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }
        _get_ecsdo_resp = self.session.get(url=_get_ecsdo_url, headers=Headers, allow_redirects=False)
        logging.info('_get_ecsdo_resp: %s' % _get_ecsdo_resp.status_code)
        _get_redirect_url = _get_ecsdo_resp.headers['Location']
        Headers = {
            'Host': 'login.189.cn',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/66.0.3359.139 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Referer': 'http://www.189.cn/zj/',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }
        _get_redirect_resp = self.session.get(url=_get_redirect_url, headers=Headers, allow_redirects=False)
        logging.info('_get_redirect_resp: %s' % _get_redirect_resp.status_code)


    def _get_login_sso(self):
        self._get_ssolink()

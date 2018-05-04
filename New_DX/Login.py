#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/4 11:35
# @Author  : Echean
# @File    : Login.py
# @Software: PyCharm


import requests
import logging
import json
import random
import execjs
import re
import time
from scrapy import Selector
from PIL import Image

logging.basicConfig(level=logging.INFO)
# session = requests.session()


class Login_first(object):
    def __init__(self, my_session):
        self.session = my_session

    def _get_checkphone(self, phone_num):
        _get_checkphone_url = 'http://login.189.cn/web/login/ajax'
        Datas = {
            'm': 'checkphone',
            'phone': phone_num,
        }
        Headers = {
            'Host': 'login.189.cn',
            'Connection': 'keep-alive',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Origin': 'http://login.189.cn',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/66.0.3359.139 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Referer': 'http://login.189.cn/web/login',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }
        _get_checkphone_resp = self.session.post(url=_get_checkphone_url, data=Datas, headers=Headers)
        logging.info('_get_checkphone_resp: %s %s' % (_get_checkphone_resp.status_code,
                                                      _get_checkphone_resp.text))
        return json.loads(_get_checkphone_resp.text)['provinceId']

    def _get_intface_captcha(self, phone_num, pid):
        _get_intface_captcha_url = 'http://login.189.cn/web/login/ajax'
        Datas = {
            'm': 'captcha',
            'account': phone_num,
            'uType': '201',
            'ProvinceID': pid,
            'areaCode': '',
            'cityNo': '',
        }
        Headers = {
            'Host': 'login.189.cn',
            'Connection': 'keep-alive',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Origin': 'http://login.189.cn',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/66.0.3359.139 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Referer': 'http://login.189.cn/web/login',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }
        _get_intface_captcha_resp = self.session.post(url=_get_intface_captcha_url, data=Datas, headers=Headers)
        logging.info('_get_intface_captcha_resp: %s %s' % (_get_intface_captcha_resp.status_code,
                                                           _get_intface_captcha_resp.text))

    def _get_captcha(self):
        _get_captcha_url = 'http://login.189.cn/web/captcha'
        query_string = {
            'undefined	': '',
            'source': 'login',
            'width': '100',
            'height': '37',
            random.random(): '',
        }
        Headers = {
            'Host': 'login.189.cn',
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/66.0.3359.139 Safari/537.36',
            'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
            'Referer': 'http://login.189.cn/web/login',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }
        _get_captcha_resp = self.session.get(url=_get_captcha_url, params=query_string, headers=Headers)
        with open('captcha.jpg', 'wb') as f:
            f.write(_get_captcha_resp.content)
        img = Image.open('captcha.jpg')
        img.show()
        captcha_code = input('请输入验证码：')
        return captcha_code

    def _get_pwdvalidate(self, phone_num, pwd, isRandom):
        _get_pwdvalidate_url = 'http://login.189.cn/web/pwd/validate'
        Datas = {
            'uName': phone_num,
            'uType': '201',
            'uPwd': pwd,
            'isRandomPwd': isRandom,
        }
        Headers = {
            'Host': 'login.189.cn',
            'Connection': 'keep-alive',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Origin': 'http://login.189.cn',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/66.0.3359.139 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Referer': 'http://login.189.cn/web/login',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }
        _get_pwdvalidate_resp = self.session.post(url=_get_pwdvalidate_url, data=Datas, headers=Headers)
        logging.info('_get_pwdvalidate_resp: %s %s' % (_get_pwdvalidate_resp.status_code,
                                                       _get_pwdvalidate_resp.text))

    def _get_js(self):
        f = open("ase.js", 'r', encoding='utf-8')
        line = f.readline()
        htmlstr = ''
        while line:
            htmlstr = htmlstr + line
            line = f.readline()
        return htmlstr

    def _get_pwd(self, pwd):
        jsstr = self._get_js()
        ctx = execjs.compile(jsstr)
        return ctx.call('valAesEncryptSet', pwd)

    def _get_login_turn(self, phone_num, pid, isRandom, password, captcha_code):
        _get_login_turn_url = 'http://login.189.cn/web/login'
        Datas = {
            'Account': phone_num,
            'UType': '201',
            'ProvinceID': pid,
            'AreaCode': '',
            'CityNo': '',
            'RandomFlag': isRandom,
            'Password': password,
            'Captcha': captcha_code,
        }
        Headers = {
            'Host': 'login.189.cn',
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'Origin': 'http://login.189.cn',
            'Upgrade-Insecure-Requests': '1',
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/66.0.3359.139 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Referer': 'http://login.189.cn/web/login',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }
        _get_login_turn_resp = self.session.post(url=_get_login_turn_url, data=Datas, headers=Headers, allow_redirects=False)
        logging.info('_get_login_turn_resp: %s' % _get_login_turn_resp.status_code)
        _get_login_ecsdo_url = _get_login_turn_resp.headers['Location']
        Headers = {
            'Host': 'www.189.cn',
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/66.0.3359.139 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Referer': 'http://login.189.cn/web/login',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }
        _get_login_ecsdo_resp = self.session.get(url=_get_login_ecsdo_url, headers=Headers, allow_redirects=False)
        logging.info('_get_login_ecsdo_resp: %s' % _get_login_ecsdo_resp.status_code)
        _get_login_location_url = _get_login_ecsdo_resp.headers['Location']
        Headers = {
            'Host': 'www.189.cn',
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/66.0.3359.139 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Referer': 'http://login.189.cn/web/login',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }
        _get_login_location_resp = self.session.get(url=_get_login_location_url, headers=Headers)
        logging.info('_get_login_location_resp: %s' % _get_login_location_resp.status_code)
        sel = Selector(_get_login_location_resp)
        return sel.css('.fl.tc.lh26.w67 .a_img ::attr(href)').extract()[4]

    def _get_ssolink(self, start_url):
        _get_ssolink_url = start_url
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
        _get_verify_center_url = _get_redirect_resp.headers['Location']
        time.sleep(10)
        Headers = {
            'Host': 'zj.189.cn',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/66.0.3359.139 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Referer': 'http://www.189.cn/zj/',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }
        _get_verify_center_resp = self.session.get(url=_get_verify_center_url, headers=Headers)
        logging.info('_get_verify_center_resp: %s' % _get_verify_center_resp.status_code)
        intaid = re.match(r'.*?intaid=(.*?)".*', _get_verify_center_resp.text, re.DOTALL).group(1)
        _get_accountnew_url = 'http://zj.189.cn/service/accountnew'
        query_string = {
            'intaid': intaid,
        }
        Headers = {
            'Host': 'zj.189.cn',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/66.0.3359.139 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Referer': _get_verify_center_url,
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }
        _get_accountnew_resp = self.session.get(url=_get_accountnew_url, params=query_string, headers=Headers)
        logging.info('_get_accountnew_resp: %s' % _get_accountnew_resp.status_code)

    def login(self):
        phone_num = input('请输入手机号:')
        pwd = input('请输入服务密码:')
        pid = self._get_checkphone(phone_num)
        self._get_intface_captcha(phone_num, pid)
        captcha_code = self._get_captcha()
        self._get_intface_captcha(phone_num, pid)
        self._get_pwdvalidate(phone_num, pwd, '1')
        pwd_encrypt = self._get_pwd(pwd)
        start_url = self._get_login_turn(phone_num, pid, '0', pwd_encrypt, captcha_code)
        self._get_ssolink(start_url)
        return phone_num


if __name__ == '__main__':
    user = Login_first()
    user.login()
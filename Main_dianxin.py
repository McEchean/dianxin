#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/25 15:39
# @Author  : Echean
# @File    : Main_dianxin.py
# @Software: PyCharm

import json
import execjs
from PIL import Image
import logging

from scrapy import Selector

logging.basicConfig(level=logging.INFO)


class Login_dianxin(object):
    def __init__(self,phone_num, my_session):
        self.phone_num = phone_num
        self.session = my_session
        self.Headers = {
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

    def _get_init(self):
        _get_init_url = 'http://login.189.cn/web/login'
        self.session.headers.update({
            'Upgrade-Insecure-Requests': '1',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        })
        _get_init_resp = self.session.get(url=_get_init_url, headers=self.session.headers)
        logging.info('_get_init_resp: %s' % _get_init_resp.status_code)
        _get_init_url2 = 'http://www.189.cn/jt/loginpic/'
        self.session.headers.update({
            'Host': 'www.189.cn',
        })
        _get_init_resp2 = self.session.get(url=_get_init_url2, headers=self.session.headers)
        logging.info('_get_init_resp2: %s' % _get_init_resp2.status_code)

    def _check_phone_num(self, phone_num):
        check_phonenum_url = 'http://login.189.cn/web/login/ajax'
        post_param = {
            'm': 'checkphone',
            'phone': phone_num,
        }
        _check_resp = self.session.post(url=check_phonenum_url, data=post_param, headers=self.Headers)
        logging.info('_check_resp: %s' % _check_resp.text)
        return json.loads(_check_resp.text)

    def _get_intface_captcha(self, phone_num, pid):
        # session.headers.update({
        # })
        _get_captha_url = 'http://login.189.cn/web/login/ajax'
        post_param = {
            'm': 'captcha',
            'account': phone_num,
            'uType': '201',
            'ProvinceID': pid,
            'areaCode': None,
            'cityNo': None,
        }
        _get_captha_resp = self.session.post(url=_get_captha_url, data=post_param, headers=self.Headers)
        logging.info('_get_captha_resp: %s' % _get_captha_resp.text)
        return json.loads(_get_captha_resp.text)

    def _send_message(self, phone_num, pid):
        # session.headers.update({
        # })
        _send_message_url = 'http://login.189.cn/web/login/ajax'
        post_param = {
            'm': 'sendrandompwd',
            'account': phone_num,
            'uType': '201',
            'pid': pid,
        }
        _send_message_resp = self.session.post(url=_send_message_url, data=post_param, headers=self.Headers)
        logging.info('_send_message_resp: %s' % _send_message_resp.text)
        return json.loads(_send_message_resp.text)

    def _get_captcha_img(self):
        self.session.headers.update({
            'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
        })
        _get_captcha_img_url = 'http://login.189.cn/web/captcha?undefined&' \
                               'source=login&width=100&height=37&0.8290304597800164 '
        _get_captcha_img_resp = self.session.get(url=_get_captcha_img_url, headers=self.session.headers)
        with open('captcha.jpg', 'wb') as f:
            f.write(_get_captcha_img_resp.content)
        img = Image.open('captcha.jpg')
        img.show()

    def _check_pwd_valdate(self, phonw_number, password, isRandom):
        if isRandom.lower() == 'y':
            isRandom = 'true'
        else:
            isRandom = 'false'
        _check_pwd_url = 'http://login.189.cn/web/pwd/validate'
        post_param = {
            'uName': phonw_number,
            'uType': '201',
            'uPwd': password,
            'isRandomPwd': isRandom,
        }
        _check_pwd_resp = self.session.post(url=_check_pwd_url, data=post_param, headers=self.Headers)
        logging.info('_check_pwd_resp: %s' % _check_pwd_resp.text)

    def _login(self, phone_num, password, captcha_num, pid, isRandom):
        if isRandom.lower() == 'y':
            isRandom = '1'
        else:
            isRandom = '0'
        self.session.headers.update({
            'Upgrade-Insecure-Requests': '1',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        })
        _login_url = 'http://login.189.cn/web/login'
        post_param = {
            'Account': phone_num,
            'UType': '201',
            'ProvinceID': pid,
            'AreaCode': None,
            'CityNo': None,
            'RandomFlag': isRandom,
            'Password': self._get_pwd(password),
            'Captcha': captcha_num,
        }
        _login_resp = self.session.post(url=_login_url, data=post_param, headers=self.session.headers,
                                        allow_redirects=False)
        logging.info('_login_resp: %s' % _login_resp.status_code)
        return _login_resp.headers['Location']

    def _get_ecsdo(self, match_http):
        self.session.headers.update({
            'Host': 'www.189.cn',
        })
        _get_ecsdo_url = match_http
        _get_ecsdo_resp = self.session.get(url=_get_ecsdo_url, headers=self.session.headers, allow_redirects=False)
        logging.info('_get_ecsdo_resp: %s' % _get_ecsdo_resp.status_code)
        _get_main_url = _get_ecsdo_resp.headers['Location']
        _get_main_resp = self.session.get(url=_get_main_url, headers=self.session.headers)
        logging.info('_get_main_resp: %s' % _get_main_resp.status_code)
        sel = Selector(_get_main_resp)
        return sel.css('.down_ul_a.f12.bb1_a.pt10.h.ov .span_font_a a::attr(href)').extract()[56]

    def _get_login_json(self):
        _get_login_json_url = 'http://www.189.cn/login/ttfaces.do?channel=WEB&locationType=1'
        self.session.headers.update({
            'Host': 'www.189.cn',
            'Connection': 'keep-alive',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/65.0.3325.181 Safari/537.36',
            'Referer': 'http://www.189.cn/zj/',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        })
        _get_login_json_resp = self.session.get(url=_get_login_json_url, headers=self.session.headers)
        logging.info('_get_login_json_resp: %s' % _get_login_json_resp.text)

        _get_login_info_url = 'http://www.189.cn/login/index.do'
        self.session.headers.update({
            'Referer': 'http://www.189.cn/html/login/right.html',
        })
        _get_login_info_resp = self.session.get(url=_get_login_info_url, headers=self.session.headers)
        logging.info('_get_login_info_resp: %s' % _get_login_info_resp.text)

        _get_login_info_url2 = 'http://www.189.cn/login/index.do'
        self.session.headers.update({
            'Referer': 'http://www.189.cn/html/login/index.html',
        })
        _get_login_info_resp2 = self.session.get(url=_get_login_info_url2, headers=self.session.headers)
        logging.info('_get_login_info_resp2: %s' % _get_login_info_resp2.text)

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

    def login_last(self):
        self._get_init()
        phone_num = self.phone_num
        info = self._check_phone_num(phone_num)
        pid = info['provinceId']
        self._get_intface_captcha(phone_num, pid)
        self._get_captcha_img()
        captcha_num = input('请输入图片验证码:')
        self._get_intface_captcha(phone_num, pid)
        isRandom = input('是否使用随机码（y/n）：').strip()
        if isRandom.lower() == 'y':
            self._send_message(phone_num, pid)
            self._get_intface_captcha(phone_num, pid)
            password = input('请输入手机验证码：')
        else:
            password = input('请输入服务密码：')
        self._check_pwd_valdate(phone_num, password, isRandom)
        x = self._login(phone_num, password, captcha_num, pid, isRandom)
        y = self._get_ecsdo(x)
        self._get_login_json()
        return y


if __name__ == '__main__':
    login_n = Login_dianxin('177xxxxxxxx')
    login_n.login_last()

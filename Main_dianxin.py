#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/25 15:39
# @Author  : Echean
# @File    : Main_dianxin.py
# @Software: PyCharm

import requests
import json
import execjs
from PIL import Image
import logging
import re
from http import cookiejar

session = requests.session()
session.cookies = cookiejar.LWPCookieJar('cookies.txt')
logging.basicConfig(level=logging.INFO)

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
Headers1 = {
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

session.headers = Headers.copy()


def _get_init():
    _get_init_url = 'http://login.189.cn/web/login'
    session.headers.update({
        'Upgrade-Insecure-Requests': '1',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    })
    _get_init_resp = session.get(url=_get_init_url, headers=session.headers)
    logging.info('_get_init_resp: %s' % _get_init_resp.status_code)
    _get_init_url2 = 'http://www.189.cn/jt/loginpic/'
    session.headers.update({
       'Host': 'www.189.cn',
    })
    _get_init_resp2 = session.get(url=_get_init_url2, headers=session.headers)
    logging.info('_get_init_resp2: %s' % _get_init_resp2.status_code)


def _check_phone_num(phone_num):
    check_phonenum_url = 'http://login.189.cn/web/login/ajax'
    post_param = {
        'm': 'checkphone',
        'phone': phone_num,
    }
    _check_resp = session.post(url=check_phonenum_url, data=post_param, headers=Headers)
    logging.info('_check_resp: %s' % _check_resp.text)
    return json.loads(_check_resp.text)


def _get_intface_captcha(phone_num, pid):
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
    _get_captha_resp = session.post(url=_get_captha_url, data=post_param, headers=Headers)
    logging.info('_get_captha_resp: %s' % _get_captha_resp.text)
    return json.loads(_get_captha_resp.text)


def _send_message(phone_num, pid):
    # session.headers.update({
    # })
    _send_message_url = 'http://login.189.cn/web/login/ajax'
    post_param = {
        'm': 'sendrandompwd',
        'account': phone_num,
        'uType': '201',
        'pid': pid,
    }
    _send_message_resp = session.post(url=_send_message_url, data=post_param, headers=Headers)
    logging.info('_send_message_resp: %s' % _send_message_resp.text)
    return json.loads(_send_message_resp.text)


def _get_captcha_img():
    session.headers.update({
        'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    })
    _get_captcha_img_url = 'http://login.189.cn/web/captcha?undefined&' \
                           'source=login&width=100&height=37&0.8290304597800164 '
    _get_captcha_img_resp = session.get(url=_get_captcha_img_url, headers=session.headers)
    with open('captcha.jpg', 'wb') as f:
        f.write(_get_captcha_img_resp.content)
    img = Image.open('captcha.jpg')
    img.show()


def _check_pwd_valdate(phonw_number, password):
    _check_pwd_url = 'http://login.189.cn/web/pwd/validate'
    post_param = {
        'uName': phonw_number,
        'uType': '201',
        'uPwd': password,
        'isRandomPwd': 'true',
    }
    _check_pwd_resp = session.post(url=_check_pwd_url, data=post_param, headers=Headers)
    logging.info('_check_pwd_resp: %s' % _check_pwd_resp.text)


def _login(phone_num, password, captcha_num, pid):
    session.headers.update({
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
        'RandomFlag': '1',
        'Password': _get_pwd(password),
        'Captcha': captcha_num,
    }
    _login_resp = session.post(url=_login_url, data=post_param, headers=session.headers, allow_redirects=True)
    logging.info('_login_resp: %s' % _login_resp.text)

    # match_http = re.match(r'.*?PlatNO=(\d+).*?ResultCode=(\d+).*?Ticket=(\w+).*?TxID=(\w+).*',
    #                       _login_resp.text, re.DOTALL).group(1, 2, 3, 4)
    # match_http = _login_resp.headers.get('Location', '')
    # return match_http


def _get_ecsdo(match_http):
    session.headers.update({
        'Host': 'www.189.cn',
    })
    _get_ecsdo_url = 'http://www.189.cn/login/ecs.do?PlatNO={0}&ResultCode={1}&Ticket={2}&TxID={3}'.format(*match_http)
    _get_ecsdo_resp = session.get(url=_get_ecsdo_url, headers=session.headers)
    logging.info('_get_ecsdo_resp: %s' % _get_ecsdo_resp.status_code)


def _get_js():
    f = open("ase.js", 'r', encoding='utf-8')
    line = f.readline()
    htmlstr = ''
    while line:
        htmlstr = htmlstr + line
        line = f.readline()
    return htmlstr


def _get_pwd(pwd):
    jsstr = _get_js()
    ctx = execjs.compile(jsstr)
    return ctx.call('valAesEncryptSet', pwd)

# 10036201804261110109dc31dd30fd04917cadcb0c1442d8f14
# def get_runntime(path):
#     """
#     :param path: 加密js的路径,注意js中不要使用中文！估计是pyexecjs处理中文还有一些问题
#     :return: 编译后的js环境，不清楚pyexecjs这个库的用法的请在github上查看相关文档
#     """
#     phantom = execjs.get('PhantomJS')  # 这里必须为phantomjs设置环境变量，否则可以写phantomjs的具体路径
#     with open(path, 'r') as f:
#         source = f.read()
#     return phantom.compile(source)
#
# def get_encodename(pwd, runntime):
#     return runntime.call('valAesEncryptSet', pwd)

# runntime = get_runntime('ase.js')
# su = get_encodename('123456', runntime)
# print(_check_phone_num())
# print(_get_intface_captcha())
# # print(_send_message())
# _get_captcha_img()
# print(_get_pwd('564184'))


_get_init()
phone_num = input('请输入手机号：')
info = _check_phone_num(phone_num)
pid = info['provinceId']
_get_intface_captcha(phone_num, pid)
_get_captcha_img()
captcha_num = input('请输入图片验证码:')
_get_intface_captcha(phone_num, pid)
_send_message(phone_num, pid)
_get_intface_captcha(phone_num, pid)
password = input('请输入手机验证码：')
_check_pwd_valdate(phone_num, password)
_login(phone_num, password, captcha_num, pid)
# _get_ecsdo(match_http)

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

session = requests.session()

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
session.headers = Headers.copy()


def _check_phone_num():
    check_phonenum_url = 'http://login.189.cn/web/login/ajax'
    post_param = {
        'm': 'checkphone',
        'phone': '17342071372',
    }
    _check_resp = session.post(url=check_phonenum_url, data=post_param, headers=session.headers)
    return json.loads(_check_resp.text)


def _get_intface_captcha():
    # session.headers.update({
    # })
    _get_captha_url = 'http://login.189.cn/web/login/ajax'
    post_param = {
        'm': 'captcha',
        'account': '17342071372',
        'uType': '201',
        'ProvinceID': '12',
        'areaCode': None,
        'cityNo': None,
    }
    _get_captha_resp = session.post(url=_get_captha_url, data=post_param, headers=session.headers)
    return json.loads(_get_captha_resp.text)


def _send_message():
    # session.headers.update({
    # })
    _send_message_url = 'http://login.189.cn/web/login/ajax'
    post_param = {
        'm': 'sendrandompwd',
        'account': '17342071372',
        'uType': '201',
        'pid': '12',
    }
    _send_message_resp = session.post(url=_send_message_url, data=post_param, headers=session.headers)
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


def _login():
    session.headers.update({
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    })
    _login_url = 'http://login.189.cn/web/login'
    post_param = {
        'Account': '17342071372',
        'UType': '201',
        'ProvinceID': '12',
        'AreaCode': None,
        'CityNo': None,
        'RandomFlag': '1',
        'Password': 'NrX37cwtBJ4HzWheMlaUMQ==',
        'Captcha': 'j4j4',
    }


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


def get_runntime(path):
    """
    :param path: 加密js的路径,注意js中不要使用中文！估计是pyexecjs处理中文还有一些问题
    :return: 编译后的js环境，不清楚pyexecjs这个库的用法的请在github上查看相关文档
    """
    phantom = execjs.get('PhantomJS')  # 这里必须为phantomjs设置环境变量，否则可以写phantomjs的具体路径
    with open(path, 'r') as f:
        source = f.read()
    return phantom.compile(source)

def get_encodename(pwd, runntime):
    return runntime.call('valAesEncryptSet', pwd)

runntime = get_runntime('ase2.js')
su = get_encodename('123456', runntime)
# print(_check_phone_num())
# print(_get_intface_captcha())
# # print(_send_message())
# _get_captcha_img()

print('su',su)

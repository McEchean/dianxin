#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/27 11:00
# @Author  : Echean
# @File    : dianxin_main.py
# @Software: PyCharm

from Main_dianxin import Login_dianxin
from spider import _Spider
from Myrequest import my_session

phone_num = input('请输入手机号：')
login_n = Login_dianxin(phone_num, my_session)
new_url = login_n.login_last()
my_spider = _Spider(my_session, new_url)
my_spider._get_init(phone_num)
my_spider._send_second_message(phone_num)
message_code = input('请输入二次短信验证码：')
my_spider._check_message(phone_num, message_code)

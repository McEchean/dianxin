#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/4 14:51
# @Author  : Echean
# @File    : Login_Main.py
# @Software: PyCharm

from New_DX.MyRequests import My_request
from New_DX.Login import Login_first
from New_DX.SpiderNew import Spider_New

if __name__ == '__main__':
    myrequest = My_request()
    my_session = myrequest._get_session()
    user = Login_first(my_session)
    phone_num = user.login()
    user_spider = Spider_New(my_session)
    user_spider.parse(phone_num)
    my_session.cookies.save()

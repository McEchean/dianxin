#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/25 17:03
# @Author  : Echean
# @File    : test.py
# @Software: PyCharm

# import base64
# #
# #
# # s = b'123456'
# # print(base64.b64encode(s))

# from scrapy import Selector
#
# doc = ''
# sel = Selector()
# sel.css(login_response,)


# import requests
# from scrapy import Selector
#
# Headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)'
#                   ' Chrome/65.0.3325.181 Safari/537.36'
# }
#
# url = 'https://www.baidu.com/'
# session = requests.session()
#
# resp = session.get(url,headers=Headers)
# sel = Selector(resp)
# print(sel.css('script::text').extract_first(''))


import re
_login_resp = '''
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<HTML>
<HEAD>
    <META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=gbk">
    <TITLE>´íÎó£ºÄúËùÇëÇóµÄÍøÖ·£¨URL£©ÎÞ·¨»ñÈ¡</TITLE>
    <STYLE type="text/css"><!--
    BODY {
        background-color: #ffffff;
        font-family: verdana, sans-serif
    }

    PRE {
        font-family: sans-serif
    }

    --></STYLE>
</HEAD>
<BODY>
<H1>´íÎó</H1>
<H2>ÄúËùÇëÇóµÄÍøÖ·£¨URL£©ÎÞ·¨»ñÈ¡</H2>
<HR noshade size="1px">
<P>
    µ±³¢ÊÔ¶ÁÈ¡ÒÔÏÂÍøÖ·£¨URL£©Ê±£º
    <A HREF="http://login.189.cn/login/ecs.do?PlatNO=90000&amp;ResultCode=0&amp;Ticket=900000035138b169f9b8498242b598fd256b1b446540&amp;TxID=10036900006420180426120034000012">http://login.189.cn/login/ecs.do?PlatNO=90000&amp;ResultCode=0&amp;Ticket=900000035138b169f9b8498242b598fd256b1b446540&amp;TxID=10036900006420180426120034000012</A>
<P>
    ·¢ÉúÁËÏÂÁÐµÄ´íÎó£º
    <UL>
        <LI>
            <STRONG>
                Access Denied.
                <BR>¾Ü¾ø·ÃÎÊ
            </STRONG>
<P>
    Access control configuration prevents your request from
    being allowed at this time. Please contact your service provider if
    you feel this is incorrect.
    <BR>
    µ±Ç°µÄ´æÈ¡¿ØÖÆÉè¶¨½ûÖ¹ÄúµÄÇëÇó±»½ÓÊÜ£¬
    Èç¹ûÄú¾õµÃÕâÊÇ´íÎóµÄ£¬ÇëÓëÄúÍøÂ··þÎñµÄÌá¹©ÕßÁªÏµ¡£
    </UL>
</P>
<P>±¾»º´æ·þÎñÆ÷¹ÜÀíÔ±£º<A HREF="mailto:support@chinacache.com">support@chinacache.com</A>
'''
# match_http = re.search(r'^>http://[^;]+<$', _login_resp, re.S)
match_http = re.findall(r'>http://.*?<', _login_resp, re.DOTALL)
print(match_http)
match_http = re.findall(r'PlatNO=\d{4}?', _login_resp, re.DOTALL)
match_http = re.match(r'.*?PlatNO=(\d+).*?ResultCode=(\d+).*?Ticket=(\w+).*?TxID=(\w+).*', _login_resp, re.DOTALL).group(1,2,3,4)


print(match_http)

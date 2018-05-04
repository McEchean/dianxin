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


# import re
# _login_resp = '''
# <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
# <HTML>
# <HEAD>
#     <META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=gbk">
#     <TITLE>´íÎó£ºÄúËùÇëÇóµÄÍøÖ·£¨URL£©ÎÞ·¨»ñÈ¡</TITLE>
#     <STYLE type="text/css"><!--
#     BODY {
#         background-color: #ffffff;
#         font-family: verdana, sans-serif
#     }
#
#     PRE {
#         font-family: sans-serif
#     }
#
#     --></STYLE>
# </HEAD>
# <BODY>
# <H1>´íÎó</H1>
# <H2>ÄúËùÇëÇóµÄÍøÖ·£¨URL£©ÎÞ·¨»ñÈ¡</H2>
# <HR noshade size="1px">
# <P>
#     µ±³¢ÊÔ¶ÁÈ¡ÒÔÏÂÍøÖ·£¨URL£©Ê±£º
#     <A HREF="http://login.189.cn/login/ecs.do?PlatNO=90000&amp;ResultCode=0&amp;Ticket=900000035138b169f9b8498242b598fd256b1b446540&amp;TxID=10036900006420180426120034000012">http://login.189.cn/login/ecs.do?PlatNO=90000&amp;ResultCode=0&amp;Ticket=900000035138b169f9b8498242b598fd256b1b446540&amp;TxID=10036900006420180426120034000012</A>
# <P>
#     ·¢ÉúÁËÏÂÁÐµÄ´íÎó£º
#     <UL>
#         <LI>
#             <STRONG>
#                 Access Denied.
#                 <BR>¾Ü¾ø·ÃÎÊ
#             </STRONG>
# <P>
#     Access control configuration prevents your request from
#     being allowed at this time. Please contact your service provider if
#     you feel this is incorrect.
#     <BR>
#     µ±Ç°µÄ´æÈ¡¿ØÖÆÉè¶¨½ûÖ¹ÄúµÄÇëÇó±»½ÓÊÜ£¬
#     Èç¹ûÄú¾õµÃÕâÊÇ´íÎóµÄ£¬ÇëÓëÄúÍøÂ··þÎñµÄÌá¹©ÕßÁªÏµ¡£
#     </UL>
# </P>
# <P>±¾»º´æ·þÎñÆ÷¹ÜÀíÔ±£º<A HREF="mailto:support@chinacache.com">support@chinacache.com</A>
# '''
# # match_http = re.search(r'^>http://[^;]+<$', _login_resp, re.S)
# match_http = re.findall(r'>http://.*?<', _login_resp, re.DOTALL)
# print(match_http)
# match_http = re.findall(r'PlatNO=\d{4}?', _login_resp, re.DOTALL)
# match_http = re.match(r'.*?PlatNO=(\d+).*?ResultCode=(\d+).*?Ticket=(\w+).*?TxID=(\w+).*', _login_resp, re.DOTALL).group(1,2,3,4)
#
#
# print(match_http)
#
# import random
#
# print(random.random())

import re

# s = '''
# <html>
# <head>
# <meta http-equiv="Content-Type" content="text/html; charset=gbk">
# <title>中国电信网上营业厅·浙江|为您提供电信业务办理、充值交费、费用查询等全方位电子自助服务</title>
# <script language="javascript">
#               location.href = "/service/accountnew?&intaid=zj-sy-hxfw-05-";
# </script>
# </head>
# '''
# resp = re.match(r'.*?intaid=(.*?)".*', s, re.DOTALL).group(1)
# print(resp)
#

x = '<buffalo-reply><map><type>java.util.HashMap</type><string>cdrlevel</string><string>2</string><string>logininfo</string><map><type>com.zjhcsoft.zjpr.product.domain.Pr_productDomain</type><string>product_id</string><long>13953108</long><string>product_nbr</string><string>17342071372</string><string>contract_nbr</string><string>2711059478433</string><string>cust_id</string><string>171100041692471</string><string>cust_identifier_id</string><null></null><string>cust_reg_type</string><string>身份证</string><string>cust_reg_nbr</string><string>230183199503200013</string><string>serv_type_id</string><string>18</string><string>area_id</string><long>571</long><string>city_id</string><long>571001</long><string>sts</string><string>A</string><string>create_date</string><date>20171214T210932Z</date><string>modify_date</string><date>20180504T145921Z</date><string>product_password</string><null></null><string>integration_id</string><string>1-HCAA1033099</string><string>cust_name</string><string>金咏泽</string><string>serv_type_name</string><string>移动电话</string><string>product_login_cnt</string><long>50</long><string>product_last_login_date</string><date>20180504T142413Z</date><string>groupcount</string><null></null><string>pass_validate</string><null></null><string>bizdislist</string><null></null><string>insurance_level</string><int>0</int><string>ctzjtype</string><null></null><string>level</string><null></null><string>isCampusNet</string><null></null><string>serv_type_crm</string><string>PHY-MAN-0022</string><string>is_weak_password</string><string>N</string><string>firstrownum</string><int>0</int><string>lastrownum</string><int>0</int><string>order</string><null></null><string>sort</string><null></null></map></map></buffalo-reply>'

from scrapy import Selector
import re

s = {}
s['product_id'] = re.match(r'.*?<string>product_id</string><long>(.*?)</long>.*', x).group(1)
s['product_nbr'] = re.match(r'.*?<string>product_nbr</string><string>(.*?)</string>.*', x).group(1)
s['contract_nbr'] = re.match(r'.*?<string>contract_nbr</string><string>(.*?)</string>.*', x).group(1)
s['cust_id'] = re.match(r'.*?<string>cust_id</string><string>(.*?)</string>.*', x).group(1)
s['cust_identifier_id'] = re.match(r'.*?<string>cust_identifier_id</string><null>(.*?)</null>.*', x).group(1)
s['cust_reg_type'] = re.match(r'.*?<string>cust_reg_type</string><string>(.*?)</string>.*', x).group(1)
s['cust_reg_nbr'] = re.match(r'.*?<string>cust_reg_nbr</string><string>(.*?)</string>.*', x).group(1)
s['serv_type_id'] = re.match(r'.*?<string>serv_type_id</string><string>(.*?)</string>.*', x).group(1)
s['area_id'] = re.match(r'.*?<string>area_id</string><long>(.*?)</long>.*', x).group(1)
s['city_id'] = re.match(r'.*?<string>city_id</string><long>(.*?)</long>.*', x).group(1)
s['sts'] = re.match(r'.*?<string>sts</string><string>(.*?)</string>.*', x).group(1)
s['create_date'] = re.match(r'.*?<string>create_date</string><date>(.*?)</date>.*', x).group(1)
s['modify_date'] = re.match(r'.*?<string>modify_date</string><date>(.*?)</date>.*', x).group(1)
s['product_password'] = re.match(r'.*?<string>product_password</string><null>(.*?)</null>.*', x).group(1)
s['integration_id'] = re.match(r'.*?<string>integration_id</string><string>(.*?)</string>.*', x).group(1)
s['cust_name'] = re.match(r'.*?<string>cust_name</string><string>(.*?)</string>.*', x).group(1)
s['serv_type_name'] = re.match(r'.*?<string>serv_type_name</string><string>(.*?)</string>.*', x).group(1)
s['product_login_cnt'] = re.match(r'.*?<string>product_login_cnt</string><long>(.*?)</long>.*', x).group(1)
s['product_last_login_date'] = re.match(r'.*?<string>product_last_login_date</string><date>(.*?)</date>.*', x).group(1)
s['serv_type_name'] = re.match(r'.*?<string>serv_type_name</string><string>(.*?)</string>.*', x).group(1)
s['serv_type_name'] = re.match(r'.*?<string>serv_type_name</string><string>(.*?)</string>.*', x).group(1)



print(s)

# sel = Selector(text=x)
# s = sel.css('map map ::text').extract()
# l = {}
# l['phone_num'] = s[4]
# l['type'] = s[11]
# l['ID_num'] = s[13]
# l['area_id'] = s[17]
# l['city_id'] = s[19]
# l['productid'] = s[28]
# l['name'] = s[30]
# l['phone_type'] = s[32]
# print(l)
# print(s)
#
# print(b'\xd2\xc6\xb6\xaf\xb5\xe7\xbb\xb0'.decode('gbk'))

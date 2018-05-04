#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/4 14:21
# @Author  : Echean
# @File    : SpiderNew.py
# @Software: PyCharm

import requests
import logging
from scrapy import Selector
import re

logging.basicConfig(level=logging.INFO)
# session = requests.session()


class Spider_New(object):
    def __init__(self, my_session):
        self.session = my_session

    def _get_buff(self):
        _get_buff_url = 'http://zj.189.cn/bfapp/buffalo/cdrService'
        xml = '''
        <buffalo-call>
        <method>querycdrasset</method>
        </buffalo-call>
        '''
        Headers = {
            'Host': 'zj.189.cn',
            'Connection': 'keep-alive',
            'X-Buffalo-Version': '2.0',
            'Origin': 'http://zj.189.cn',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/66.0.3359.139 Safari/537.36',
            'Content-Type': 'text/xml;charset=UTF-8',
            'Accept': '*/*',
            # 'Referer': 'http://zj.189.cn/zjpr/service/query/query_order.html?menuFlag=1',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }
        _get_buff_resp = self.session.post(url=_get_buff_url, data=xml, headers=Headers)
        logging.info('_get_buff_resp: %s' % _get_buff_resp.status_code)
        x = _get_buff_resp.text
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
        s['product_last_login_date'] = re.match(r'.*?<string>product_last_login_date</string><date>(.*?)</date>.*',
                                                x).group(1)
        s['serv_type_name'] = re.match(r'.*?<string>serv_type_name</string><string>(.*?)</string>.*', x).group(1)
        s['serv_type_name'] = re.match(r'.*?<string>serv_type_name</string><string>(.*?)</string>.*', x).group(1)
        return s

    def _get_Vcode(self, phone_num):
        _get_Vcode_url = 'http://zj.189.cn/bfapp/buffalo/VCodeOperation'
        xml = '''
        <buffalo-call>
        <method>SendVCodeByNbr</method>
        <string>{0}</string>
        </buffalo-call>
        '''.format(phone_num)
        Headers = {
            'Host': 'zj.189.cn',
            'Connection': 'keep-alive',
            'X-Buffalo-Version': '2.0',
            'Origin': 'http://zj.189.cn',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/66.0.3359.139 Safari/537.36',
            'Content-Type': 'text/xml;charset=UTF-8',
            'Accept': '*/*',
            # 'Referer': 'http://zj.189.cn/zjpr/service/query/query_order.html?menuFlag=1',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }
        _get_Vcode_resp = self.session.post(url=_get_Vcode_url, data=xml, headers=Headers)
        logging.info('_get_Vcode_resp: %s' % _get_Vcode_resp.text)
        sms_code = input('请输入二次验证码：')
        return sms_code

    def _get_parse(self, message_code, params):
        month = input('请输入要查询的月份(近六个月，格式如：201803):')
        type = input('请输入要查询的详单类型（11：通话 21：短信 31：综合信息服务费 41：流量）：')
        _check_message_url = 'http://zj.189.cn/zjpr/cdr/getCdrDetail.htm'
        Datas = {
            'flag': '1',
            'cdrCondition.pagenum': '1',
            'cdrCondition.pagesize': '100',
            'cdrCondition.productnbr	': params['product_nbr'],
            'cdrCondition.areaid': params['area_id'],
            'cdrCondition.cdrlevel': None,
            'cdrCondition.productid': params['integration_id'],
            'cdrCondition.product_servtype': '18',
            'cdrCondition.recievenbr	': params['serv_type_name'],
            'cdrCondition.cdrmonth': month,
            'cdrCondition.cdrtype': type,
            'cdrCondition.usernameyanzheng': params['cust_name'],
            'cdrCondition.idyanzheng	': params['cust_reg_nbr'],
            'cdrCondition.randpsw': message_code,
        }
        _check_message_resp = self.session.post(url=_check_message_url, data=Datas, headers=self.session.headers)
        logging.info('_check_message_resp: %s %s' % (_check_message_resp.status_code, _check_message_resp.text))

    def parse(self, phone_num):
        params = self._get_buff()
        sms_code = self._get_Vcode(phone_num)
        while True:
            self._get_parse(sms_code, params)
            s = input('是否还需要查询（y/n）：').strip()
            if s.lower() != 'y':
                break





















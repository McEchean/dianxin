#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/27 10:12
# @Author  : Echean
# @File    : spider.py
# @Software: PyCharm

import logging
import re

logging.basicConfig(level=logging.INFO)


class _Spider(object):
    def __init__(self, my_session, start_url):
        self.session = my_session
        self.start_url = start_url
        self.Header = {
        }

    def _get_init(self, phone_num):
        time = 0
        while time < 10:
            _get_start_url = self.start_url
            self.session.headers.update({
                'Host': 'www.189.cn',
                'Connection': 'keep-alive',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                'Referer': 'http://www.189.cn/zj/',
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'zh-CN,zh;q=0.9',
            })
            _get_start_resp = self.session.get(url=_get_start_url, headers=self.session.headers)
            if re.findall(r'出错提示信息', _get_start_resp.text, re.S) or re.findall(r'很抱歉，页面它', _get_start_resp.text, re.S):
                print(time)
                time += 1
                continue
            else:
                break
        next_url = _get_start_resp.url
        logging.info('_get_start_resp: %s %s' % (_get_start_resp.status_code, _get_start_resp.text))

        _get_next_url = re.match(r'.*?toStUrl=(.*)', self.start_url).group(1)
        self.session.headers.update({
            'Host': 'zj.189.cn',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Referer': next_url,
        })

        _get_next_resp = self.session.get(url=_get_next_url, headers=self.session.headers)
        logging.info('_get_next_resp: %s %s' % (_get_next_resp.status_code, _get_next_resp.text))

        _get_shouji_url = 'http://zj.189.cn/shouji/{0}/service/queryorder/'.format(phone_num)
        self.session.headers.update({
            'Host': 'zj.189.cn',
            'Upgrade-Insecure-Requests': '1',
            'Referer': 'http://zj.189.cn/service/accountnew?&intaid=zj-sy-hxfw-05-',
        })
        _get_shouji_resp = self.session.get(url=_get_shouji_url, headers=self.session.headers)
        logging.info('_get_shouji_resp: %s %s' % (_get_shouji_resp.status_code, _get_shouji_resp.text))

        _get_init_url1 = 'http://zj.189.cn/common_v2/login.html'
        self.session.headers.update({
            'Referer': 'http://zj.189.cn/shouji/{0}/service/queryorder/'.format(phone_num),
        })
        _get_init_resp1 = self.session.get(url=_get_init_url1, headers=self.session.headers)
        logging.info('_get_init_resp1: %s' % (_get_init_resp1.status_code,))

        _get_info_url1 = 'http://zj.189.cn/zjpr/servicenew/queryAccountInfo.htm'
        self.session.headers.update({
            'Accept': '*/*',
            'Origin': 'http://zj.189.cn',
            'X-Requested-With': 'XMLHttpRequest',
        })
        _get_info_resp1 = self.session.post(url=_get_info_url1, headers=self.session.headers)
        logging.info('_get_info_resp1: %s' % _get_info_resp1.text)

        _get_init_url4 = 'http://zj.189.cn/zjpr/service/query/query_order.html?menuFlag=1'
        self.session.headers.update({
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Referer': 'http://zj.189.cn/shouji/17342071372/service/queryorder/',
        })
        _get_init_resp4 = self.session.get(url=_get_init_url4, headers=self.session.headers)
        logging.info('_get_init_resp4: %s' % (_get_init_resp4.status_code,))

        _get_init_url2 = 'http://zj.189.cn/bfapp/buffalo/demoService'
        self.session.headers.update({
            'X-Buffalo-Version': '2.0',
            'Origin': 'http://zj.189.cn',
            'Content-Type': 'text/xml;charset=UTF-8',
            'Accept': '*/*',
            'Referer': 'http://zj.189.cn/zjpr/service/query/query_order.html?menuFlag=1',
        })
        xml_2 = '<buffalo-call><method>getAllProductWithCustId_D</method></buffalo-call>'
        _get_init_resp2 = self.session.post(url=_get_init_url2, data=xml_2, headers=self.session.headers)
        logging.info('_get_init_resp2: %s %s' % (_get_init_resp2.status_code, _get_init_resp2.text))

        _get_init_url3 = 'http://zj.189.cn/bfapp/buffalo/cdrService'
        xml_3 = '<buffalo-call><method>querycdrasset</method></buffalo-call>'
        _get_init_resp3 = self.session.post(url=_get_init_url3, data=xml_3, headers=self.session.headers)
        logging.info('_get_init_resp3: %s %s' % (_get_init_resp3.status_code, _get_init_resp3.text))

    def _send_second_message(self, phone_num):
        _send_second_message_url = 'http://zj.189.cn/bfapp/buffalo/VCodeOperation'
        xml = '<buffalo-call><method>SendVCodeByNbr</method><string>{0}</string></buffalo-call>'.format(phone_num)
        _send_second_message_resp = self.session.post(url=_send_second_message_url, data=xml,
                                                      headers=self.session.headers)
        logging.info('_send_second_message_resp: %s %s' % (_send_second_message_resp.status_code,
                                                           _send_second_message_resp.text))

    def _check_message(self, phone_num, message_code):
        _check_message_url = 'http://zj.189.cn/zjpr/cdr/getCdrDetail.htm'
        self.session.headers.update({
            'Upgrade-Insecure-Requests': '1',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Referer': 'http://zj.189.cn/zjpr/service/query/query_order.html?menuFlag=1',
        })
        post_param = {
            'flag': '1',
            'cdrCondition.pagenum': '1',
            'cdrCondition.pagesize': '100',
            'cdrCondition.productnbr	': phone_num,
            'cdrCondition.areaid': '571',
            'cdrCondition.cdrlevel': None,
            'cdrCondition.productid': '1-HCAA1033099',
            'cdrCondition.product_servtype': '18',
            'cdrCondition.recievenbr	': '移动电话'.encode('gbk'),
            'cdrCondition.cdrmonth': '201803',
            'cdrCondition.cdrtype': '11',
            'cdrCondition.usernameyanzheng': '金咏泽'.encode('gbk'),
            'cdrCondition.idyanzheng	': '230183199503200013',
            'cdrCondition.randpsw': message_code,
        }
        _check_message_resp = self.session.post(url=_check_message_url, data=post_param, headers=self.session.headers)
        logging.info('_check_message_resp: %s %s' % (_check_message_resp.status_code, _check_message_resp.text))

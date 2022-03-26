# -*- coding: utf-8 -*-
"""
@Description : 
@File        : test_global_search_ybxy.py
@Project     : SYProject
@Time        : 2021/9/18 下午4:59
@Author      : dj
@Software    : PyCharm
"""
import unittest
from base.my_logger import Logger
from data.globalogin import GlobalLogin
import requests


class Global_Match_XY(unittest.TestCase):

    def setUp(self):
        self.log = Logger()
        self.log.logger.info("测试用例执行前的初始化操作========")
        # warnings.simplefilter("ignore", ResourceWarning)
        gl = GlobalLogin(log=self.log)
        self.headers = gl.login()
        self.path = gl.base + '/api/global-platform-extend/national/sku/drugsRelation/matchingData'
        self.body = {}

    def tearDown(self):
        self.log.logger.info("测试用例执行完之后的收尾操作=====")

    def test_match_xy(self):
        res = requests.post(url=self.path, json= self.body, headers=self.headers)
        self.assertIn('{"errCode":0', res.text)
        self.log.logger.info(res.text)


if __name__ == '__main__':
    unittest.main()

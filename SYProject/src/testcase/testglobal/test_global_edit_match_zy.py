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


class Global_Edit_Match_ZY(unittest.TestCase):

    def setUp(self):
        self.log = Logger()
        self.log.logger.info("测试用例执行前的初始化操作========")
        # warnings.simplefilter("ignore", ResourceWarning)
        gl = GlobalLogin(log=self.log)
        self.headers = gl.login()
        self.path = gl.base + '/api/global-platform-extend/national/sku/chineseMedicineRelation/edit'
        self.body = {"id":2,"piecesCode":"[\"zy123234a12312\"]"}

    def tearDown(self):
        self.log.logger.info("测试用例执行完之后的收尾操作=====")

    def test_edit_match_zy(self):
        res = requests.post(url=self.path, json= self.body, headers=self.headers)
        self.assertIn('{"errCode":0', res.text)
        self.log.logger.info(res.text)


if __name__ == '__main__':
    unittest.main()

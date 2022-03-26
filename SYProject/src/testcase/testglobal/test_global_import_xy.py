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
import json


class Global_Import_XY(unittest.TestCase):

    def setUp(self):
        self.log = Logger()
        self.log.logger.info("测试用例执行前的初始化操作========")
        # warnings.simplefilter("ignore", ResourceWarning)
        gl = GlobalLogin(log=self.log)
        self.headers = gl.login()
        self.path = gl.base + '/api/global-platform-extend/national/sku/drugs/save'
        self.body = [
    {
        "approvalcode": "国药准字H20067255",
        "unit": "盒",
        "materialname": "铝塑",
        "goodscode": "XA01ABD075A002010100483",
        "registeredmedicinemodel": "片剂(口含)",
        "registeredproductname": "地喹氯铵含片",
        "goodsname": "无",
        "registeredoutlook": "0.25mg",
        "factor": 24,
        "companynamesc": "汕头经济特区明治医药有限公司",
        "goodsstandardcode": "86900483000019",
        "minunit": "片"
    }]

    def tearDown(self):
        self.log.logger.info("测试用例执行完之后的收尾操作=====")

    def test_import_xy(self):
        res = requests.post(url=self.path, data= json.dumps(self.body), headers=self.headers)
        self.assertIn('{"errCode":0', res.text)
        self.log.logger.info(res.text)


if __name__ == '__main__':
    unittest.main()

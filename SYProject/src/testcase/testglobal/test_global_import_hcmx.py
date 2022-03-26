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


class Global_Import_HCMX(unittest.TestCase):

    def setUp(self):
        self.log = Logger()
        self.log.logger.info("测试用例执行前的初始化操作========")
        # warnings.simplefilter("ignore", ResourceWarning)
        gl = GlobalLogin(log=self.log)
        self.headers = gl.login()
        self.path = gl.base + '/api/global-platform-extend/national/sku/consumablesDetail/save'
        self.body = [
            {
                "registrant": "常州华森医疗器械有限公司",
                "id": "0000189e-c4b2-11e9-953f-fa163e0a8baf",
                "specificationCode": "C0311160800200706410",
                "catalogname1": "03-骨科材料",
                "catalogname2": "11-接骨板",
                "catalogname3": "16-小儿接骨板",
                "commonname": "080-固定板",
                "matrial": "02-纯钛",
                "characteristic": "007-肱骨/普通",
                "regcardnm": "国械注准20153460353",
                "regcardName": None,
                "productName": "金属接骨板 (三叶草型接骨板)",
                "companyName": "常州华森医疗器械有限公司",
                "releaseVersion": 20210626,
                "ggxhCount": "7",
                "specification": None,
                "model": None,
                "udiCode": None
            }
        ]

    def tearDown(self):
        self.log.logger.info("测试用例执行完之后的收尾操作=====")

    def test_import_HCMX(self):
        res = requests.post(url=self.path, data= json.dumps(self.body), headers=self.headers)
        self.assertIn('{"errCode":0', res.text)
        self.log.logger.info(res.text)


if __name__ == '__main__':
    unittest.main()

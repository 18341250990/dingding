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


class Global_Import_HC(unittest.TestCase):

    def setUp(self):
        self.log = Logger()
        self.log.logger.info("测试用例执行前的初始化操作========")
        # warnings.simplefilter("ignore", ResourceWarning)
        gl = GlobalLogin(log=self.log)
        self.headers = gl.login()
        self.path = gl.base + '/api/global-platform-extend/national/sku/consumables/save'
        self.body = [
            {
                "registrant": None,
                "id": None,
                "specificationCode": "C0101010010100104744",
                "catalogname1": "01-非血管介入治疗类材料",
                "catalogname2": "01-呼吸介入材料",
                "catalogname3": "01-气管支气管支架",
                "commonname": "001-支架",
                "matrial": "01-镍钛合金",
                "characteristic": "001-全覆膜",
                "regcardnm": None,
                "regcardName": None,
                "productName": None,
                "companyName": "麦瑞通医疗器械（北京）有限公司",
                "releaseVersion": 20210626,
                "ggxhCount": None,
                "specification": None,
                "model": None,
                "udiCode": None
            }
        ]

    def tearDown(self):
        self.log.logger.info("测试用例执行完之后的收尾操作=====")

    def test_import_HC(self):
        res = requests.post(url=self.path, data= json.dumps(self.body), headers=self.headers)
        self.assertIn('{"errCode":0', res.text)
        self.log.logger.info(res.text)


if __name__ == '__main__':
    unittest.main()

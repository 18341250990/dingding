import unittest
from data.login import Login
from tools.HandleRequests import HandleRequests
import warnings
import json
from base.my_logger import Logger
import requests


class Case(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.log = Logger()
        # warnings.simplefilter("ignore", ResourceWarning)
        cls.headers = Login(log=cls.log).get_headers()

    @classmethod
    def tearDownClass(cls):
        pass

    def test11_getSupplierLocalByClini(self):
        data = '{"name":"西药房","codesMatchValues":[{"value":"西药房"}],"page":1,"offset":0,"pagesize":20}'
        self.url = 'https://test2a.everjiankang.cn/api/warehouse/storageRoom/getStorageRoomList/'
        res = HandleRequests(log=self.log).call(method='post',url=self.url, data = data, headers = json.loads(self.headers))
        print(res)


if __name__ == '__main__':
    unittest.main()

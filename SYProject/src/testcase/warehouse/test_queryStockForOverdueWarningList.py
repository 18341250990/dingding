import unittest
from data.login import Login
from tools.HandleRequests import HandleRequests
import json
from base.my_logger import Logger
from data.url_path import URL
from base.config import Config
from data.requests_body import queryInventoryWarningList_body
from data.search_base_data import Base_Data


class QueryStockForOverdueWarningList(unittest.TestCase):

    def setUp(self):
        self.log = Logger()
        self.log.logger.info("测试用例执行前的初始化操作========")
        # warnings.simplefilter("ignore", ResourceWarning)
        self.headers = Login(log=self.log).get_tenant_headers()
        self.path = URL.warehosue_getSupplierLocalByClinic_path
        self.config = Config(log=self.log, file_name='tenant.config').config

    def tearDown(self):
        self.log.logger.info("测试用例执行完之后的收尾操作=====")

    def test_getSupplierLocalByClini(self):
        bd = Base_Data(self.log,self.headers)
        resultList = bd.getStorageRoomList()['data']['resultList']
        storageRoomid = resultList[0]['id']
        # for oject in resultList:
        #     name = oject['name']
        #     id = oject['id']
        #     if '西药房' in name:
        #         storageRoomid = id
        #         break
        #     else:
        #         continue
        queryInventoryWarningList_body['storageRoomId'] = storageRoomid
        data = queryInventoryWarningList_body
        self.url = f'{self.config["BASE_URL"]}/{self.path}'

        res = HandleRequests(log=self.log).call(method='post', url=self.url, data=data,
                                                headers=json.loads(self.headers))
        obj = json.loads(res.text)['data']['resultList']
        if obj:
            self.log.logger.info(str(obj))
            self.assertIsNotNone(obj)
        else:
            self.assertIn('没有查询到预警信息', res.text)


if __name__ == '__main__':
    unittest.main()

# -*- coding: utf-8 -*-
"""
@Description : 
@File        : suppliercontactsdetail.py
@Project     : SYProject
@Time        : 2022/1/26 下午2:26
@Author      : dj
@Software    : PyCharm
"""
import unittest
import requests
from base.config import Config
from base.report_config import report_body,suppliercontactsdetail_path
from base.my_logger import Logger
import time
import datetime
import json
from data.login import Login


class Suppliercontactsdetail(unittest.TestCase):

    def setUp(self):
        self.log = Logger()
        self.log.logger.info("测试用例执行前的初始化操作------")
        self.config = Config(log=self.log, file_name='tenant.config').config
        # warnings.simplefilter("ignore", ResourceWarning)
        self.path = suppliercontactsdetail_path
        self.report = report_body
        dt= datetime.datetime.now()
        self.end_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.start_time = (dt + datetime.timedelta(days=-30)).strftime('%Y-%m-%d %H:%M:%S')
        self.headers = Login(log=self.log).get_tenant_headers()
        self.tenantid = self.config['TENTANTID']
        self.flag = self.config.get('flag')
        if self.flag =='test':
            self.base_url = self.config['BASE_URL']
        else:
            self.base_url = self.config['pre_url']
        self.url = self.base_url + self.path

    def tearDown(self):
        self.log.logger.info("测试用例执行完之后的收尾操作------")

    def test_suppliercontactsdetail(self):
        self.report['type'] = 1
        self.report['startDate'] = self.start_time
        self.report['endDate'] = self.end_time
        self.report['clinicIds'] = [self.tenantid]
        stime = time.time()
        self.log.logger.info(f'访问url地址：{self.url}')
        res = requests.post(url=self.url, data=json.dumps(self.report).encode('utf-8'),
                            headers=json.loads(self.headers))
        if res.status_code == 200 and ('供应商往来明细' in res.text):
            etime = time.time()
            self.log.logger.info(res.text)
            self.log.logger.info(f'供应商往来明细表查询耗时:{etime-stime} s')
        else:
            self.log.logger.info('查询报表数据异常')



if __name__ == '__main__':
    unittest.main()

# -*- coding: utf-8 -*-
"""
@Description : 用于获取基础信息的接口备用
@File        : search_base_data.py
@Project     : SYProject
@Time        : 2021/8/16 下午3:25
@Author      : dj
@Software    : PyCharm
"""
from base.config import Config
from base.my_logger import Logger
import requests
from data.login import Login
import json


class Base_Data:

    def __init__(self, log=None, headers=None):
        if not log:
            self.log = Logger()
        else:
            self.log = log
        self.headers = headers
        self.config = Config(log=self.log, file_name='tenant.config').config
        # self.body = {"page": 1, "offset": 0, "pagesize": 20}

    # 查询库房列表
    def getStorageRoomList(self):
        body = {"page": 1, "offset": 0, "pagesize": 20}
        url = self.config['BASE_URL'] + '/api/warehouse/storageRoom/getStorageRoomList/'
        res = requests.post(url=url, json=body, headers=json.loads(self.headers))
        if res.status_code == 200:
            return json.loads(res.text)
        else:
            return '查询库房列表请求失败'

    # 查询当前用户信息
    def getCurrentUser(self):
        body = {}
        url = self.config['BASE_URL'] + '/api/thc-platform-core/unify/getCurrentUser'
        res = requests.post(url=url, data=json.dumps(body), headers=json.loads(self.headers))
        if res.status_code == 200:
            return json.loads(res.text)
        else:
            return '查询当前用户请求失败'

    # 获取结构的定价模式
    def selectSystemSettingByClinicId(self):
        body = {}
        url = self.config['BASE_URL'] + '/api/warehouse/clinic/selectSystemSettingByClinicId/'
        res = requests.post(url=url, data=json.dumps(body), headers=json.loads(self.headers))
        if res.status_code == 200:
            text = json.loads(res.text)
            pricingModel = text['pricingModel']
            return pricingModel
        else:
            return '获取定价模式请求失败'


if __name__ == '__main__':
    sbd = Base_Data()
    # print(sb.getStorageRoomList())
    # print(sb.getCurrentUser())

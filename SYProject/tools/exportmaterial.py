# -*- coding: utf-8 -*-
"""
@Description : 
@File        : build.py
@Project     : SYProject
@Time        : 2021/11/3 下午6:29
@Author      : dj
@Software    : PyCharm
"""
from base.my_logger import Logger
from data.login import Login
import requests
import json
import copy
from data.requests_body import export_zc_body, search_body, inStockItem


class ExportMaterial:

    def __init__(self):
        self.log = Logger()
        self.log.logger.info("开始批量暂存物资")
        self.headers = Login(log=self.log).get_tenant_headers()
        self.base_url = 'https://testdsskyy.everjiankang.cn'
        self.zc_url = self.base_url+'/api/warehouse/inStock/createPurchaseInStockAndItem/'
        self.search = self.base_url+'/api/warehouse/localSetting/getLocalSettingList/'
        self.search_body = search_body
        self.zc_body = export_zc_body
        self.inStockItem = inStockItem
        self.contractId= '9ab1cc52-a404-4d36-bd82-f01ae306d23e'
        self.supplierLocalId = '00d19a64-662e-49bb-b1f3-63bee5645399'
        self.storageRoomId = 'bfaa2df1-cc9a-4b03-b866-9f40cd0b9d92'

    def search_inStockItemList(self,name):
        inStockItemlist = []
        self.search_body['storageRoomId'] = self.storageRoomId
        self.search_body['supplierLocalId'] = self.supplierLocalId
        self.search_body['contractId'] = self.contractId
        self.search_body['name'] = name

        res = requests.post(url=self.search, data=json.dumps(self.search_body).encode('utf-8'),
                            headers=json.loads(self.headers))

        datas = json.loads(res.text)['data']
        leng = len(datas)
        for m in datas:
            inStockItem = copy.deepcopy(self.inStockItem)
            inStockItem['localMaterialId'] = m['localMaterialId']
            inStockItem['materialName'] = m['materialName']
            inStockItem['serviceId'] = m['serviceId']
            inStockItem['materialSkuId'] = m['materialSkuId']
            inStockItem['materialSpkuId'] = m['materialSpkuId']
            inStockItem['storageRoomId'] = self.storageRoomId
            inStockItem['supplierLocalId'] = self.supplierLocalId
            inStockItem['contractId'] = self.contractId
            inStockItemlist.append(inStockItem)
        # return json.dumps(inStockItemlist)
        return inStockItemlist,leng

    def temporary(self, name):
        inStockItemlist,totalprce = self.search_inStockItemList(name)
        self.zc_body['inStockItemList'] = inStockItemlist
        self.zc_body['totalPrice'] = totalprce
        self.zc_body['storageRoomId'] = self.storageRoomId
        self.zc_body['supplierLocalId'] = self.supplierLocalId

        res = requests.post(url=self.zc_url, data=json.dumps(self.zc_body).encode('utf-8'),
                                headers=json.loads(self.headers))
        if res.status_code == 200:
            self.log.logger.info("采购入库单据暂存成功")
            self.log.logger.info(res.text)
        else:
            self.log.logger.info("采购入库单据暂存失败")


if __name__ == '__main__':
    em = ExportMaterial()
    #暂存已xx开头的物资
    em.temporary('批量')
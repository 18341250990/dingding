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
from data.requests_body import buildMaterial_body,buildMaterial_xybody


class BuildMaterial:

    def __init__(self):
        self.log = Logger()
        self.log.logger.info("开始批量创建物资")
        self.headers = Login(log=self.log).get_tenant_headers()
        self.url = 'https://test2a.everjiankang.cn/api/warehouse/material/save/'
        self.hcbody = buildMaterial_body
        self.xybody = buildMaterial_xybody

    def buildhc(self, num, name):
        date_list = []
        for i in range(num):
            self.hcbody['ext']['SXX000005'] = name + str(i)
            res = requests.post(url=self.url, data=json.dumps(self.hcbody).encode('utf-8'),
                                headers=json.loads(self.headers))
            print(json.dumps(json.loads(res.text)['data']))
            if res.status_code == 200:
                date_list.append(json.loads(res.text)['data'])
                self.log.logger.info(f'创建{name}{str(i)}耗材物资成功')
            else:
                self.log.logger.info(f'创建{name}{str(i)}耗材物资失败')

        return date_list

    def buildxy(self, num, name):
        date_list = []
        for i in range(num):
            self.xybody['ext']['SXX000003'] = name + str(i)
            self.xybody['ext']['SXX000001'] = name + str(i)
            res = requests.post(url=self.url, data=json.dumps(self.xybody).encode('utf-8'),
                                headers=json.loads(self.headers))
            if res.status_code == 200:
                print(res.text)
                date_list.append(json.loads(res.text)['data'])
                self.log.logger.info(f'创建{name}{str(i)}西药物资成功')
            else:
                self.log.logger.info(f'创建{name}{str(i)}西药物资失败')

        return date_list


if __name__ == '__main__':
    bm = BuildMaterial()
    li = bm.buildxy(2, '批量西药')
    # print(li)

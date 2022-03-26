# -*- coding: utf-8 -*-
"""
@Description : 
@File        : login.py
@Project     : SYProject
@Time        : 2021/5/21 上午10:37
@Author      : dj
@Software    : PyCharm
"""
from base.config import Config, BASE_CONFIG_PAHT
from base.my_logger import Logger
from tools.HandleRequests import HandleRequests
from tools.md5Hex import MD5Hex
import json
from data.requests_body import login_body, headers
from ruamel import yaml
import requests


class Login:
    def __init__(self, log=None):
        if not log:
            self.log = Logger()
        else:
            self.log = log
        self.config = Config(file_name='tenant.config', log=self.log).config
        #切换登录测试环境或预上线环境token
        self.flag = self.config.get('flag')
        if self.flag == 'test':
            self.user = self.config.get('USER')
            self.password = self.config.get('PASSWORD')
            self.base = self.config.get('BASE_URL')
        else:
            self.user = self.config.get('admin')
            self.password = self.config.get('pw')
            self.base = self.config.get('test_url')

        self.login_path = self.config.get('LOGINPATH')
        self.replaceToken_path = self.config.get('ReplaceToken')
        self.url = self.base + self.login_path
        self.version = self.config.get("VERSION")
        self.dt = {"orgId": "", "tenantId": ""}

    def login(self):
        data = str(self.data())
        res = HandleRequests(log=self.log).call(method='post', url=self.url, data=data, is_json=True)

        return res

    def data(self):
        pw = MD5Hex(log=self.log).get_md5Hex(self.password)
        login_body['name'] = self.user
        login_body['password'] = pw
        # login_body['version'] = self.version
        self.log.logger.info(f'登录请求参数：{json.dumps(login_body)}')
        return json.dumps(login_body)

    def get_token(self):
        res = self.login()
        if res.status_code == 200:
            token = json.loads(res.text)
        else:
            self.log.logger.info('登录失败，未获取到token信息')

        return token['data']['token']

    def get_headers(self):
        headers['x-access-token'] = self.get_token()
        # with open(f"{BASE_CONFIG_PAHT}headers.yaml", "w", encoding="utf-8") as f:
        #     yaml.dump_all(headers, f, Dumper=yaml.RoundTripDumper)
        return json.dumps(headers)

    def login_with_session(self):
        data = str(self.data())
        h = HandleRequests(log=self.log)
        res = h.session_request(method='post', url=self.url, data=data, is_json=True)
        h.close_session()
        return res

    def switchOrgToReplaceToken(self):
        # data = {"orgId":"","tenantId":""}
        self.dt['orgId'] = self.config['ORGID']
        self.dt['tenantId'] = self.config['TENTANTID']
        url = self.base + self.replaceToken_path
        res = requests.post(url=url, json=self.dt, headers=json.loads(self.get_headers()))
        if res.status_code == 200:
            token = json.loads(res.text)['data']
        else:
            token = None
        return token

    # 获取登录机构的headers
    def get_tenant_headers(self):
        headers['x-access-token'] = self.switchOrgToReplaceToken()
        # with open(f"{BASE_CONFIG_PAHT}tenant_headers.yaml", "w", encoding="utf-8") as f:
        #     yaml.dump(headers, f, Dumper=yaml.RoundTripDumper)
        return json.dumps(headers)


if __name__ == '__main__':
    data = Login().get_tenant_headers()
    # print(data)
    # pass

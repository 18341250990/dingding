# -*- coding: utf-8 -*-
"""
@Description : 
@File        : globalogin.py
@Project     : SYProject
@Time        : 2021/9/18 下午4:39
@Author      : dj
@Software    : PyCharm
"""

from base.my_logger import Logger
from base.config import Config
import json
import requests


class GlobalLogin:

    def __init__(self, log = None):
        if not log:
            self.log = Logger()
        else:
            self.log = log
        self.config = Config(file_name='global.config', log=self.log).config
        self.user = self.config.get('USER')
        self.password = self.config.get('PASSWORD')
        self.base = self.config.get('BASE_URL')
        self.login_url_path = self.base+'/api/global-platform/sys/user/userLogin'
        self.body = '{"account":"admin","password":"admin"}'
        self.headers = {"Content-Type":"application/json;charset=UTF-8","x-access-token": ""}

    def login(self):
        res = requests.post(url=self.login_url_path, data=self.body, headers = self.headers)
        token = json.loads(res.text)['data']
        self.headers['x-access-token'] = token
        return self.headers


if __name__ == '__main__':
    GlobalLogin().login()
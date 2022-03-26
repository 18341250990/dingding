# -*- coding: utf-8 -*-
"""
@Description : 
@File        : md5Hex.py
@Project     : SYProject
@Time        : 2021/5/21 上午11:44
@Author      : dj
@Software    : PyCharm
"""
import hashlib
from base.my_logger import Logger


class MD5Hex:

    def __init__(self, log=None):
        if not log:
            self.log = Logger()
        else:
            self.log = log

    def get_md5Hex(self, password):
        pw = hashlib.md5(password.encode(encoding='UTF-8')).hexdigest()
        self.log.logger.info(f'登录密码为：{pw}')
        return pw


if __name__ == '__main__':
    pw = MD5Hex().get_md5Hex("admin@123")
    print(pw)

# -*- coding: utf-8 -*-
"""
@Description :
@File        : login.py
@Project     : SYProject
@Time        : 2021/4/21 上午10:37
@Author      : dj
@Software    : PyCharm
"""

import logging
from logging import handlers
import os
import threading

root_path = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),"../log"))
log_path = f'{root_path}/'


class Logger(object):
    _instance_lock = threading.Lock()
    level_relations = {
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARNING,
        'error': logging.ERROR,
        'crit': logging.CRITICAL
    }  # 日志级别关系映射

    def __new__(cls, *args, **kwargs):
        if not hasattr(Logger, "_instance"):
            with Logger._instance_lock:
                if not hasattr(Logger, "_instance"):
                    Logger._instance = object.__new__(cls)
        return Logger._instance

    def __init__(self, filename = 'log.log', level='debug', when='D', backCount=3,
                 fmt='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'):

        self.logger = logging.getLogger(log_path+filename)
        #判断logger是否存在handers
        if not self.logger.handlers:

            format_str = logging.Formatter(fmt)  # 设置日志格式
            self.logger.setLevel(self.level_relations.get(level))  # 设置日志级别
            sh = logging.StreamHandler()  # 往屏幕上输出
            sh.setFormatter(format_str)  # 设置屏幕上显示的格式
            th = handlers.TimedRotatingFileHandler(filename=log_path+filename, when=when, backupCount=backCount,
                                                   encoding='utf-8')  # 往文件里写入#指定间隔时间自动生成文件的处理器
            # 实例化TimedRotatingFileHandler
            # interval是时间间隔，backupCount是备份文件的个数，如果超过这个个数，就会自动删除，when是间隔的时间单位，单位有以下几种：
            # S 秒
            # M 分
            # H 小时、
            # D 天、
            # W 每星期（interval==0时代表星期一）
            # midnight 每天凌晨
            th.setFormatter(format_str)  # 设置文件里写入的格式
            self.logger.addHandler(sh)  # 把对象加到logger里
            self.logger.addHandler(th)


if __name__ == '__main__':
    log = Logger('all.log', level='error')
    log1 = Logger('all.log', level='error')


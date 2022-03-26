# -*- coding: utf-8 -*-
"""
@Description : 
@File        : Concurrency.py
@Project     : SYProject
@Time        : 2022/2/12 上午11:37
@Author      : dj
@Software    : PyCharm
"""

import threading
from base.my_logger import Logger
from src.testcase.wh_report.test_inventory import Inventory
import time


class Concurrency(threading.Thread):

    def __init__(self, timeout=30):
        self.log = Logger()
        threading.Thread.__init__(self)
        self.timeout = timeout

    def run(self):
        lock = threading.Lock()
        self.log.logger.info(f'第{i+1}次请求')
        lock.acquire()
        self.req()
        lock.release()

    def req(self):
        i = Inventory()
        i.setUp()
        i.test_inventory()
        time.sleep(3)

count = 10
threads = []
for i in range(count):
    thread = Concurrency(i)
    thread.start()
    threads.append(thread)
for t in threads:
    t.join()

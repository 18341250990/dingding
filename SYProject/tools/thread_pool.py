# -*- coding: utf-8 -*-
"""
@Description : 
@File        : thread_pool.py
@Project     : SYProject
@Time        : 2022/3/9 上午10:29
@Author      : dj
@Software    : PyCharm
"""

from threading import Thread, Semaphore, currentThread
import time, random

from twisted._threads import pool

sm = Semaphore(5)  # 运行的时候有5个人


def task():
    sm.acquire()
    print('[%s上厕所' % currentThread().getName())
    time.sleep(random.randint(1, 3))
    print('[%s上完厕所走了' % currentThread().getName())
    sm.release()


if __name__ == '__main__':
    # for i in range(20):  #开了20个线程 ，这20人都要上厕所
    #     t = Thread(target=task)
    #     t.start()
    pass

from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

import os, time, random


def task(n):
    print('%s is runing' % os.getpid())
    time.sleep(random.randint(1, 3))
    print(f'{os.getpid()} is finished')
    return n ** 2


if __name__ == '__main__':
    # executor=ProcessPoolExecutor(max_workers=3)  #生成3个进程

    executor = ThreadPoolExecutor(max_workers=3)  # 单个进程id 三个线程
    #
    # futures=[]
    # for i in range(11):
    #     future=executor.submit(task,i)
    #     futures.append(future)
    # executor.shutdown(True)
    # print('+++>')
    # for future in futures:
    #     print(future.result())

from concurrent.futures import ThreadPoolExecutor
import time
import random


def la(name):
    print('%s is laing' % name)
    time.sleep(random.randint(5, 7))
    res = random.randint(1, 13) * '#'
    return {'name': name, 'res': res}


def weigh(shit):
    shit = shit.result()
    name = shit['name']
    size = len(shit['res'])
    print('%s 拉了 《%s》kg' % (name, size))


if __name__ == '__main__':
    pool = ThreadPoolExecutor(13)

    # pool.submit(la,'alex').add_done_callback(weigh)
    #
    # pool.submit(la,'wupeiqi').add_done_callback(weigh)
    #
    # pool.submit(la,'yuanhao').add_done_callback(weigh)

from concurrent.futures import ThreadPoolExecutor


class Mypool:

    def __init__(self):
        pass

    def fun(name):
        print(f"{os.getpid()}--runing")
        time.sleep(3)
        print(f"{os.getpid()}--success")

        return name

    def getname(action):
        res = action.result()
        print(f'进程id: {res}')


if __name__ == '__main__':
    my = Mypool()
    pool = ProcessPoolExecutor(3)
    # pool = ThreadPoolExecutor(3)
    pool.submit(Mypool.fun, os.getpid()).add_done_callback(Mypool.getname)
    pool.submit(Mypool.fun, os.getpid()).add_done_callback(Mypool.getname)

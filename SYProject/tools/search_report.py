# -*- coding: utf-8 -*-
"""
@Description : 
@File        : search_report.py
@Project     : SYProject
@Time        : 2021/8/18 下午4:26
@Author      : dj
@Software    : PyCharm
"""
import os

BASE_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
CONFIG_PATH = os.path.join(BASE_PATH, 'report')


class Search_Report:

    def search(self):
        global files
        for root,dirs,files in os.walk(fr'{CONFIG_PATH}'):
            pass
        files.sort(reverse=True)
        if files:
            return files[0]
        else:
            return None


if __name__ == '__main__':
    sr = Search_Report()
    sr.search()

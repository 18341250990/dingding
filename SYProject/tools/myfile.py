# -*- coding: utf-8 -*-
"""
@Description : 
@File        : myfile.py
@Project     : SYProject
@Time        : 2021/9/27 上午11:08
@Author      : dj
@Software    : PyCharm
"""
import  requests
import re
import pandas as pd


class myfile:
    def __init__(self):
        self.url = 'https://wenku.baidu.com/view/25e35773f321dd36a32d7375a417866fb94ac0c5.html'
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'}

    def get(self):
        res =  requests.get(url = self.url)
        # print(res.text)
        pattern = "[\u4e00-\u9fa5]+"
        regex = re.compile(pattern)
        results = regex.findall(res.text)
        print(results)
        # pd.DataFrame(results)
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', None)
        pd.set_option('display.expand_frame_repr', False)
        pd.set_option('display.width', 1000)
        content = pd.DataFrame(results,columns=['content'])
        print(content)


if __name__ == '__main__':
    myfile().get()

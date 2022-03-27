# -*- coding: utf-8 -*-
"""
@Description :
@File        : send_msg.py
@Project     : SYProject
@Time        : 2021/8/17 下午6:06
@Author      : dj
@Software    : PyCharm
"""

import requests
import time
import os

from ruamel import yaml

from base.config import Config
from base.my_logger import Logger

BASE_CONFIG_PAHT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../config/'))


class ReadYaml:
    def read(self):
        file_path = f'{BASE_CONFIG_PAHT}/robot_config.yaml'
        with open(file_path,'r') as f:
            # res = yaml.safe_load(f)
            res = yaml.load(f,Loader=yaml.Loader)
        return res


class MSG:

    def __init__(self,log=None):
        ry = ReadYaml()
        if not log:
            self.log = Logger()
        else:
            self.log = log
        res = ry.read()
        self.robot_headers = res.get('robot_headers')
        self.robot_url = res.get("robot_url")
        self.host_url = res.get('host_url')
        self.config = Config(file_name='tenant.config', log=self.log).config

        self.flag = self.config.get('flag')
        if self.flag == 'test':
            self.base = str(self.config.get('BASE_URL')).split('//')[1]

        else:
            self.base = str(self.config.get('test_url')).split('//')[1]

    def send_msg(self, msg):
        data = {
            "msgtype": "markdown",
            "markdown": {
                "content": str(msg)
            }
        }
        res = requests.post(url=self.robot_url, headers=self.robot_headers, json=data)
        if res.status_code == 200:
            print('消息推送成功')
        else:
            print('消息推送成功')

    def send_new(self, title, url, picUrl):
        now = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
        data = {
            "touser": "@all",
            "msgtype": "news",  # 消息类型，此时固定为news
            "news": {
                "articles": [  # 图文消息，一个图文消息支持1到8条图文
                    {
                        "title": title,  # 标题，不超过128个字节，超过会自动截断
                        "description": f"执行人： admin \n"
                                       f"报告时间：{now} \n"
                                       f"执行环境：{self.base} ",  # 描述，不超过512个字节，超过会自动截断
                        "url": url,# 点击后跳转的链接。
                        "picurl": picUrl
                        # 图文消息的图片链接，支持JPG、PNG格式，较好的效果为大图 1068*455，小图150*150。
                    }
                ]
            }
        }
        res = requests.post(url=self.robot_url, headers=self.robot_headers, json=data)
        if res.status_code == 200:
            print('消息推送成功')
        else:
            print('消息推送成功')

    def send_text(self, content, mentioned_list = None, mentioned_mobile_list=None):
        now = time.asctime()
        data = {
        "msgtype": "text",  # 必填
        "text": {
            "content": content,
            "mentioned_list": mentioned_list,
            "mentioned_mobile_list": mentioned_mobile_list
        }
    }
        res = requests.post(url=self.robot_url, headers=self.robot_headers, json=data)
        if res.status_code == 200:
            print('消息推送成功')
        else:
            print('消息推送成功')

    def get_new_report(self,path):
       if os.path.isdir(path):
           lists = os.listdir(path)  # 列出目录的下所有文件和文件夹保存到lists
           lists.sort(key=lambda fn: os.path.getmtime(path + "\\" + fn))  # 按时间排序
           file_new = os.path.join(path, lists[-1])  # 获取最新的文件保存到file_new
           return file_new
       else:
           print('文件目录不正确，请重新输入')


if __name__ == '__main__':
    # msg = {'tip': '测试'}
    # MSG().send(msg)
    m = MSG()

    url = m.host_url
    picUrl = f'{m.host_url}/log.png'
    m.send_new(title='测试报告', url=url, picUrl=picUrl)
    # # MSG().send_text('for test')

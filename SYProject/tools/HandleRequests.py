"""
@Description : 
@File        : HandleRequests.py
@Project     : SYProject
@Time        : 2021/5/17 下午4:27
@Author      : dj
@Software    : PyCharm
"""
from base.my_logger import Logger
import requests
import json
from base.config import Config


class HandleRequests:

    def __init__(self, log=None):
        if not log:
            self.log = Logger()
        else:
            self.log = log
        self.config = Config(file_name='tenant.config',log=self.log).config
        self.session = requests.Session()

    def call(self, method, url, data, is_json=False, **kwargs):
        self.log.logger.info(f'请求url：{url}')
        global res
        method = method.lower()
        if len(data) > 0:
            if method == 'get':
                res = requests.request(method=method, url=url, params=data, **kwargs)
            elif method == "post":
                if is_json:
                    try:
                        data = json.loads(data)
                        res = requests.request(method=method, url=url, json=data, **kwargs)
                    except Exception as e:
                        self.log.logger.error(f'str字符串json数据处理异常:{str(e)}')
                else:

                    res = requests.request(method=method, url=url, data=str(data).encode('utf-8'), **kwargs)
            else:
                self.log.logger.info(f'{method}该请求方式暂不支持')
        else:
            res = requests.request(method=method, url=url)

        return res

    def session_request(self, method, url, data, is_json=False, **kwargs):
        self.log.logger.info(f'请求url：{url}')
        global res
        method = method.lower()
        if len(data) > 0:
            if method == 'get':
                res = self.session.request(method=method, url=url, params=data, **kwargs)
            elif method == "post":
                if is_json:
                    try:
                        data = json.loads(data)
                        res = self.session.request(method=method, url=url, json=data, **kwargs)
                    except Exception as e:
                        self.log.logger.error(f'str字符串json数据处理异常:{str(e)}')
                else:

                    res = self.session.request(method=method, url=url, data=str(data).encode('utf-8'), **kwargs)
            else:
                self.log.logger.info(f'{method}该请求方式暂不支持')
        else:
            res = self.session.request(method=method, url=url)

        return res

    def close_session(self):

        self.session.close()

    @staticmethod
    def get_headers(**kwargs):
        headers = {}
        for key in kwargs:
            headers[key] = kwargs[key]
        return json.dumps(headers)


if __name__ == '__main__':
    handle = HandleRequests()
    # h = header.get_headers(Content_type="application/json", Token=HandleRequests().token)
    h = handle.call(method='get', url='https://www.baidu.com/s?ie=UTF-8&wd=baidu')
    print(h)

# -*— coding:utf_8 -*-
import os
from base.my_logger import Logger
from tools.file_reader import YamlReader,ConfigReader
import json
BASE_CONFIG_PAHT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../config/'))


class Config:
    def __init__(self, file_name,log = None):
        if not log:
            self.log = Logger()
        else:
            self.log = log
        self.config = {}
        file_path = f'{BASE_CONFIG_PAHT}/{file_name}'
        if file_name:
            if str(file_name).endswith(".config"):
                list_ = ConfigReader(file_path).data()
                self.config = json.loads(json.dumps(dict(list_)))

            elif str(file_name).endswith('.yaml'):
                yml_path = BASE_CONFIG_PAHT + file_name
                text = YamlReader(yml_path).data
                self.config = json.loads(json.dumps(text[0]))
            else:
                self.log.logger.info("暂不支持文件类型")

        else:
            self.log.logger.info('传入文件名称为空')


if __name__ == '__main__':
    config = Config(file_name='tenant.config')

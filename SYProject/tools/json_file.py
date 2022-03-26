# -*- coding: utf-8 -*-
"""
@Description : 
@File        : json_file.py
@Project     : SYProject
@Time        : 2021/9/2 下午5:28
@Author      : dj
@Software    : PyCharm
"""

import requests
import json
import codecs


class JSON_FIle:

    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'}

    def get(self, rows, type, page=1):

        # 下载西药
        # url = f'https://code.nhsa.gov.cn/yp/getPublishGoodsDataInfo.html?batchNumber=%2020210730&sord=asc&rows={rows}&page={page}'
        # 下载耗材数据
        # url = f'https://code.nhsa.gov.cn/hc/stdPublishData/getStdPublicDataList.html?releaseVersion=20210626&sord=asc&rows={rows}&page={page}'
        # #下载耗材明细
        url = f'https://code.nhsa.gov.cn/hc/stdPublishData/getStdPublicDataListDetail.html?releaseVersion=20210626&sord=asc&rows={rows}&page={page}'
        # #下载中药颗粒
        # url= f'https://code.nhsa.gov.cn/yp/getPublishPiecesData.html?batchNumber=20210610&sord=asc&rows={rows}&page={page}'
        # #下载中药饮片
        # url = f'https://code.nhsa.gov.cn/yp/getPublishPiecesData.html?batchNumber=20210322&sord=asc&rows={rows}&page={page}'
        res = requests.get(url=url, headers=self.headers)
        file = json.loads(res.text)['rows']
        # print(file)
        try:
            # with open(f"../file/file_{type}.json", "w", encoding='utf-8') as f:
            #     # json.dump(file, f）
            #     f.write(str(file).replace("'", '"').replace('None','null'))
            #     print('文件写入成功')
            #
            # f = codecs.open(f"../file/file_{type}.json", "w",'utf-8')
            # f.write(str(file).replace("'", '"').replace('None','null'))

            with open(f"../file/file_{type}.json", "w", encoding='utf-8') as f:
                json.dump(file, f,ensure_ascii=False)
                print('写入成功')
        except Exception as e:
            print('文件写入失败' + str(e))
        finally:
            f.close()


if __name__ == '__main__':
    jf = JSON_FIle()
    # jf.get(40000, 'xy5',5)
    # jf.get(30000, 'hc2',2)
    jf.get(40000, 'hcmx1',1)
    # jf.get(2000, 'zykl')
    # jf.get(2000, 'zyyp')

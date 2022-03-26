import hashlib
import re
import json
import pandas as pd
import requests
import re

def get_md5(need_value):
    """
    获取md5值
    :param file:
    :return:
    """
    md = hashlib.md5()
    md.update(need_value.encode(encoding='utf-8'))
    md5 = md.hexdigest()
    return md5

print(get_md5('admin@123'))

pwd = 'abacaa1'
p = r'^([a-zA-Z])(?![0-9]+$)(?![a-zA-Z]+$)[0-9A-Za-z]{5,19}$'
p1= r'^(?![a-zA-Z]+$)(?![0-9]+$)[0-9A-Za-z]{6,20}$'
print(re.search(p, pwd))

def messagetype_markdown(content):

    robot_headers = {"Content-Type": "application/json"}
    robot_webhook = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=38bfc33f-f94e-401c-84f3-58290d209d04'
    data = {
            "msgtype": "markdown",
            "markdown": {
            "content": content
                        }
        }
    response = requests.post(url=robot_webhook,headers=robot_headers, json=data)
    print(response.text)


if __name__ == '__main__':
   # data = '{"tip":"测试"}'
   # messagetype_markdown(data)

   data = '''{
    "resultList": [
        {
            "id": "244c0e65-674f-40ef-bd52-1fd257676ee6",
            "code": "V1G100210806000010",
            "addNewCode": null,
            "purchaseType": 1,
            "summaryCode": null,
            "status": 812,
            "num": 1,
            "totalPrice": 3,
            "applicant": "7995a3bacf164eccb443e93d4c77bad5",
            "applyTime": "2021-08-06 18:02:48",
            "createTime": "2021-08-06 18:02:48",
            "isDelete": 0,
            "description": null,
            "lastUpdatedBy": null,
            "createBy": "7995a3bacf164eccb443e93d4c77bad5",
            "lastUpdatedDate": null,
            "clinicId": 5000100,
            "targetOrgId": null,
            "tenantId": "5000",
            "storageRoomId": "4198d47a-0f0f-4e52-81d1-eb8b9fe9b16c",
            "auditOpinion": null,
            "abolitionReason": null,
            "abolitionTime": null,
            "abolition": null,
            "confirmTime": null,
            "confirmer": null,
            "remark": null,
            "flag": null,
            "errorMessage": null,
            "items": null,
            "storageRoomName": "西药房_38",
            "applicantName": "丁杰",
            "confirmerName": null,
            "abolitionName": null,
            "logId": null,
            "purchaseOrders": null,
            "pageType": null,
            "statusName": null,
            "taskLogs": null,
            "taskInfos": null,
            "isExecute": null,
            "auditFlag": null,
            "auditRemark": null,
            "rejectId": null,
            "clinicName": null,
            "sortTime": "2021-08-19 17:09:39"
        }
    ]
}'''
   print(data.replace('\r','').replace('\n','').replace(' ',''))

   a = re.findall(r'\d+',data)
   for j in a:
     re.sub('\d+',j,data)

   print(data)
   data = data.replace("null","None")
   # print(data)
   data = json.dumps(data)
   print(data)
   d = json.loads(data,strict = False)
   print(type(d))
   # d2 = json.loads(d,strict=False)
   # print(type(d2))

   # resultList = d.get('resultList')
   # for i in resultList:
   #     if i.get('status') == 812:
   #         print('nihao')

import datetime
dt = datetime.datetime.now()

print(dt.strftime('%Y-%m-%d'))




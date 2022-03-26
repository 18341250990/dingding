# -*- coding: utf-8 -*-
"""
@Description : 
@File        : requests_body.py
@Project     : SYProject
@Time        : 2021/5/18 上午10:43
@Author      : dj
@Software    : PyCharm
"""

login_body = {"name": "", "password": ""}
headers = {"Content-Type": "application/json", "x-access-token": ""}
queryStockForOverdueWarning_body = {"validitySign":6,"storageRoomId":"a51c7642-1437-41db-9582-81cd2f79ada9","page":1,"offset":0,"pagesize":20}
queryInventoryWarningList_body = {"storageRoomId":"a05c0a9a-cd3a-47c4-a6a6-98e86d46fa8f","page":1,"offset":0,"pagesize":20}
buildMaterial_body = {"classifyId":"300","isClinic":True,"ext":{"SXX000005":"医疗耗材","SXX000006":"PLYLHC","materialBarCodes":[],"ifService":2,"SXX19030500001ATTD":{"name":"耗材","id":"37"},"SXX000047":{"name":"g","id":"11"},"classifyObject":{"id":"300","name":"医疗耗材"}},"skuDTOList":[{"ext":{"SXX000049":"1","SXX000048":{"name":"g","id":"11"},"price":"1","SXX000050":""},"ifService":2,"code":"","splitFlag":0,"ceilingPrice":""}],"isExpiryDate":1,"markupPercentage":0}
buildMaterial_xybody = {"classifyId":"301","isClinic":True,"ext":{"SXX000015":[],"SXX211103000017FAqi":{},"SXX22020800001AC86s":{},"SXX19061000001BmIMC":[],"SXX19061000002BmaAT":[],"SXX000003":"批量西药","SXX000004":"PLXY","SXX000001":"文号","materialBarCodes":[],"SXX000007":{"name":"微丸","id":"40108"},"SXX000008":"说明书","SXX000014":{},"SXX000013":{},"SXX000012":{},"SXX19030700002B0q3b":[],"SXX181002000037QiH":{},"SXX20021700001AFMaJ":{},"SXX21121100001zEpbj":{},"SXX19030500001ATTD":{"name":"西药费","id":"8"},"SXX000047":{"id":"11","name":"g"},"SXX000053":{},"SXX000054":{},"SXX000016":[],"SXX000017":{},"SXX19011500001zpMoy":{"name":"是","id":"1"},"SXX000011":{"id":"02","name":"制剂单位"},"ifService":2,"classifyObject":{"id":"301","name":"西药"}},"skuDTOList":[{"ext":{"SXX000049":"1","SXX000048":{"name":"袋","id":"5"},"price":"1","SXX000050":""},"code":"","ifService":2,"splitFlag":0,"ceilingPrice":""}],"markupPercentage":0}
export_zc_body = {
    "inStockItemList": [],
    "status": 9,
    "totalPrice": 1,
    "supplyMode": 1,
    "storageRoomId": "36233eba-f929-4b20-9b84-99da59b81528",
    "supplierLocalId": "82dcc661-e279-4e1b-aba1-e1a132b2ee48",
    "description": "caigourukuzancun",
    "cargoNo": "000"
}

inStockItem =  {
            "localMaterialId": "6d9f6dd3-18c7-4d5e-9d52-e350745da5ef",
            "materialName": "1112西药 - 23 - 批准文号",
            "price": 1,
            "add": True,
            "oldPrice": 1,
            "num": "1",
            "totalPrice": 1,
            "batchNum": "1",
            "isExpiryDate": 1,
            "produceDate": "2021-10-31 00:00:00",
            "unitId": "24",
            "salePrice": 1,
            "serviceId": "2795c928-07de-4676-abd2-8aeb678e3a02",
            "validityDate": "2021-11-30 00:00:00",
            "byNameEn": "1112XY",
            "code": "301005033",
            "materialSkuId": "4cf455c7-72d0-4f22-9060-6db93c3c4b6c",
            "materialSpkuId": "6e16740f-94dd-4edc-bdd3-3f00b64606f9",
            "classifyId": "300",
            "spec": "12盒/IU",
            "unitName": "IU",
            "packagUnitName": "IU",
            "isManageAlone": 0,
            "isNum": 1,
            "unitPrice": 1,
            "usableNum": 5,
            "packageToPrepareRatio": 12,
            "thisTableIndex": 0,
            "thisTableBatchNumIndex": 0,
            "thisTableCount": 1,
            "thisTableBatchNumCount": 1,
            "last": True,
            "oldproduceDate": "2021-10-31 00:00:00",
            "oldvalidityDate": "2021-11-30 00:00:00",
            "isbatch": True,
            "mark": 1,
            "priceSwit": 0,
            "expectNum": "1",
            "materialType": "300",
            "supplyMode": 1,
            "contractId": "370104ee-b0e2-4e81-a998-4cec8e2f58f9",
            "storageRoomId": "36233eba-f929-4b20-9b84-99da59b81528",
            "supplierLocalId": "82dcc661-e279-4e1b-aba1-e1a132b2ee48",
            "invoiceStatus": 1,
            "invoiceNo": ""
        }
search_body = {"offset":0,"isNeedFilterGz":True,"pagesize":100,"storageRoomId":"36233eba-f929-4b20-9b84-99da59b81528","splitFlag":0,"state":0,"isNeedFreightCode":True,"isNeedStock":True,"isNeedSalePrice":True,"isFilterStock":False,"supplierLocalId":"82dcc661-e279-4e1b-aba1-e1a132b2ee48","supplyMode":1,"contractId":"370104ee-b0e2-4e81-a998-4cec8e2f58f9","name":"pl"}
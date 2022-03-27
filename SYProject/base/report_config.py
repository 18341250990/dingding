# -*- coding: utf-8 -*-
"""
@Description : 
@File        : report_config.py
@Project     : SYProject
@Time        : 2022/1/26 下午2:16
@Author      : dj
@Software    : PyCharm
"""

report_body = {"offset":0,"pagesize":20,"page":1,"printCodeSetting":1,"clinicIds":["1067"],"startDate":"2022-01-01 00:00:00","endDate":"2022-01-26 23:59:59","viewAll":"y","type":1,"pricingModel":0}

supplier_report_body = {"offset":0,"pagesize":20,"page":1,"clinicIds":["1067"],"showTypes":["1","2","3","4"],"startDate":"2022-01-01 00:00:00","endDate":"2022-01-26 23:59:59","viewAll":"y","type":1,"pricingModel":0}

inventory_body = {"offset":0,"pagesize":20,"page":1,"clinicIds":["1067"],"startDate":"2022-01-01 00:00:00","endDate":"2022-01-26 23:59:59","flag":"num","viewAll":"n","type":1,"pricingModel":0,"storageRoomItemze":0}

dispensemedicinecount_path = '/api/warehouse/sellreportforms/dispensemedicinecount/'

dispensemedicinedetail_path = '/api/warehouse/sellreportforms/dispensemedicinedetail/'

returnmedicinecount_path = '/api/warehouse/sellreportforms/returnmedicinecount/'

returnmedicinedetail_path = '/api/warehouse/sellreportforms/returnmedicinedetail/'

instockcount_path = '/api/warehouse/procurement/instockcount/'

instockdetail_path = '/api/warehouse/procurement/instockdetail/'

salesreturncount_path = '/api/warehouse/procurement/salesreturncount/'

salesreturndetail_path = '/api/warehouse/procurement/salesreturndetail/'

suppliercontactscount_path = '/api/warehouse/procurement/suppliercontactscount/'

suppliercontactsdetail_path = '/api/warehouse/procurement/suppliercontactsdetail/'

stockMaterial_path = '/api/warehouse/stockReportforms/stockMaterial/'

stockMaterialByBatch_path = '/api/warehouse/stockReportforms/stockMaterialByBatch/'

inAndOutStockGather_path = '/api/warehouse/stockReportforms/inAndOutStockGather/'

inAndOutStockFlow_path = '/api/warehouse/stockReportforms/inAndOutStockFlow/'

paidButNotOutStockMaterial_path = '/api/warehouse/stockReportforms/paidButNotOutStockMaterial/'

inventory_path = '/api/warehouse/stockReportforms/inventory/'
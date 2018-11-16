# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 16:47:25 2018
ADDITION:【json方法不用get改成post实现爬去1,2,3,4...页数据】
@author: lenovo
"""

import requests
import json

need_datas = []

postData = {'pageSize':10, 'pageIndex':1}

page = 1
while page <=3:
    postData['pageIndex'] = page
    page = page + 1
    response = requests.post("https://job.alibaba.com/zhaopin/socialPositionList/doList.json",data=postData)
    data = json.loads(response.text)
    returnValue = data["returnValue"]
    datas = returnValue["datas"] # [ {},{},{},... ]
    for dic in datas:
        need_keys = {'name','workLocation', 'degree', 'firstCategory','requirement'}
        need_dict = {key: value for key, value in dic.items() if key in need_keys}
        need_datas.append(need_dict)
    
print(need_datas)
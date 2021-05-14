# coding utf-8
"""
    request data
"""
import requests
import base64
import os
import json

stzd_url = 'http://143.176.22.53:8080/ysj-service/api/sjjg/getStzd'
table_url = 'http://143.176.22.53:8080/ysj-service/api//ywst/getStflAndYwstTree'
folder = 'C:\\Users\\pojok\\Desktop\\table'


def request_data_get(url):
    response = requests.get(url)
    responseData = response.json()         data = responseData['data']
    return data

def request_data_post(url,**keywords):
    param_dict = keywords
    response = requests.post(url, json=param_dict)
    responseData = response.json()
    data = responseData['data']
    return data


# print(table_list)
table_list = request_data_get(table_url)
count = 0
for val in table_list:
    bm = val['bm']
    mc = val['mc']
    if bm.isdigit():
        continue
    data = request_data_post(stzd_url, stbm=bm)
    if data == None:
        continue
    f = open(os.path.join(folder, mc,) + '.json', 'w')
    json.dump(data,f)
    f.close()

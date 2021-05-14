#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

def
def test_hq_ysj_da():
    data = {
        "caseTypeName": "民事"
    }
    res = requests.post("http://10.1.2.34:8899/eleac/data/case-type/queryBeanList",
                        json=data)
    res1 = res.json()
    print(res1)

def test_index_sjtj():
    data ={
        "endDate": "2021-04-20",
        "startDate": "2021-04-01",
        "lookDept": "false",
        "statisticalUnitId": 1850,
        "statisticalUnitLevel": 3,
        "unitId": 1850
    }
    res = requests.post("http://10.1.2.34:8899/eleac/statis/statis",json=data)
    res1 =res.json()
    print(res1)
#!/usr/bin/env python
# -*- coding: utf-8 -*-


import requests


def test_hq_ysj():
    res = requests.get("http://143.176.22.53:8080/ysj-service/api//ywst/getStflAndYwstTree")
    re1 = res.json()
    print(re1)
    
    
def test_hq_ysj_da():
    data = {
        "stbm": "T_TYYW_GG_BZXRJJX"
    }
    res = requests.post("http://143.176.22.53:8080/ysj-service/api/sjjg/getStzd",
                        json=data)
    res1 = res.json()
    print(res1)

def test_bd():
    res = requests.get("http://143.176.22.53:8080/bd-service/api/form/getFormContent?xtbz=TYAK&bdbm=4028821f6b72c2d5016b8d91932e012a")
    print(res.json())
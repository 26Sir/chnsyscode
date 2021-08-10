#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from eleac.eleac_api.index_api import Index_sjtj

class TestEleac:
    
    def test_sjtj(self):
        self.postsjtj = Index_sjtj()
        res = self.postsjtj.sjtj("10.1.2.34:8989","2021-01-01","2021-05-20","false",1850,2,1850)
        # restext = res.text
        # print(restext)
        resjson = json.loads(res.text)
        assert res.status_code == 200
        # print(resjson)
        print(res.elapsed.total_seconds())
        print(resjson["data"][1]["statisticalUnitName"])
        assert resjson["data"][0]["statisticalUnitName"] == '山东省'
        assert resjson["count"] == 0
    
    def test_zysjtj(self):
        self.postsjtj = Index_sjtj()
        res = self.postsjtj.sjtj("10.1.2.34:8989","2021-01-01","2021-05-20","false",1851,3,1851)
        # restext = res.text
        # print(restext)
        resjson = json.loads(res.text)
        assert res.status_code == 200
        # print(resjson)
        print(res.elapsed.total_seconds())
        print(resjson["data"][0]["statisticalUnitName"])
        assert resjson["data"][0]["statisticalUnitName"] == '全市'
        assert resjson["count"] == 0
        
    def test_sy(self):
        self.getsy= Index_sjtj()
        res = self.getsy.syym("10.1.2.34:8989")
        print(res.text.title())
        res.text.title()
        # assert res.text.title == '电子卷宗巡查系统'
    
    def test_mrconfig(self):
        self.getconfig = Index_sjtj()
        res = self.getconfig.mrconfig("10.1.2.34:8989")
        assert res.status_code == 200
        res_json = json.loads(res.text)
        print(res_json)
        print(res_json["data"]["unitcode"])
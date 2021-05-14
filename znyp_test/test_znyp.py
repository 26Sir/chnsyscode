#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import requests
import json
from pyone.znyp_test.api.Api_ss import Login_on

class TestLogin:
    # def steup(self):
    #     self.login = Login_on()
    def test_login(self):
        self.login = Login_on()
        res = self.login.post_login("http://127.0.0.1:8087","admin","admin")
        # res.
        print(res.text)
        assert res.text == '{message: "登录成功"}'
        
    def test_mj_mindjude(self):
        self.login = Login_on()
        res = self.login.mj_mindjude("http://127.0.0.1:8087","0d3f920b-c1ab-454c-b06c-1fcda34f4240")
        print(res.text)
        res_one = json.loads(res.text)
        print('-----------')
        print(res_one['data'])
        assert res_one['message'] == 'ok'
         # assert res ==
    




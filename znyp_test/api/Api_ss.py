#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from pyone.znyp_test.api.znyp_api import BaseApi

class Login_on(BaseApi):
    # def __init__(self):
    #     return self.send(**data)
    
    
    def post_login(self,ip,userName,password):
        """
        请求地址IP、账号、密码参数化
        @param ip:
        @param userName:
        @param password:
        把请求的方法返回，方便在测试类中调用
        @return:
        """
        data = {
            "method": "post",
            "url": f"{ip}/acl/login",
            "json": {
                "userName": userName,
                "password": password
            }
        }
        return self.send(**data)
    
    def mj_mindjude(self,ip,id):
        data = {
            "method" : "get",
            "url": f"{ip}/mj/mindjudge/{id}",
            # "json" : {
            # "id" : id
            # }
        }
        return self.send(**data)
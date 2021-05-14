#!/usr/bin/env python
# -*- coding: utf-8 -*-

from jxjs.page.Login_jxjs import Login_jxjs

class Test_login():
    def setup(self):
        self.login = Login_jxjs()
    def test_login(self):
        self.login.login_jxjs('http://127.0.0.1:8080/#/login',u'马锐萍','11111111')
        # self.login.quit_browser()
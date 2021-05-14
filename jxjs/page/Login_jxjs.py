#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By

from time import sleep


class Login_jxjs():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.vars = {}
    
    def quit_browser(self):
        self.driver.quit()
    
    def login_jxjs(self,login_url,name,password):
        self.driver.get(login_url)
        self.driver.find_element(By.CSS_SELECTOR, ".userName .el-input__inner").send_keys(name)
        self.driver.find_element(By.CSS_SELECTOR, ".password .el-input__inner").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, ".el-button").click()
        sleep(3)

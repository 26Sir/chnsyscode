# coding utf-8

"""

"""
from automagica import *
import time
import uuid
import base64
import json

login_return = {
    "userInfo": {
        "dlfs": "3",
        "dwbm": "520191",
        "dwmc": "贵阳市筑城地区人民检察院",
        "xb": "1",
        "mc": "罗礼斌",
        "jcrysf_mc": "检察官",
        "zzdwmc": "贵阳市筑城地区人民检察院",
        "rybm": "5201910008",
        "zzzt": "1",
        "dhhm": "18786626059",
        "sfzh": "522522196801200034",
        "zzdwbm": "520191",
        "dlbm": "罗礼斌",
        "jcrysf_dm": "9979000000104",
    },
    "unit": {
        "dwjb": "4",
        "fdwbm": "520100",
        "dwlb": "null",
        "dwmc": "贵阳市筑城地区人民检察院",
        "dwsx": "0",
        "xh": 520191,
        "tyshxydm": "52019100000000",
        "dwqc": "贵阳市筑城地区人民检察院",
        "dwjc": "筑地检",
        "dwbm": "520191"
    },
    "xtxx": {
        "xtmc": "全国检察机关统一业务应用系统",
        "xtbm": "00000001"
    },
    "roles": [
        {
            "jsmc": "检察官",
            "jsbm": "001",
            "zjldbm": "5201910004",
            "jsxh": 1,
            "bmbm": "0002",
            "dwbm": "520191"
        }
    ],
    "isSuperAdmin": "SuperAdmin",
    "networkId": "3",
    "departments": [
        {
            "sfagbm": "N",
            "sflsbm": "N",
            "bmbm": "0002",
            "sfcbbm": "Y",
            "bmmc": "刑事执行检察部",
            "dwbm": "520191",
            "bmxh": 3,
            "bmlb": ["100002"],
            "bmjc": "执检部"
        }
    ]
}
browser = Chrome()

browser.get('http://tyyw.gz.jcy/')
cookie_dict = read_list_from_txt("C:\\Users\26Sir\\Desktop\\ywxt\\generated_text_file.txt")
time.sleep(1)
browser.delete_all_cookies()
for cookie in cookie_dict:
    cookie = eval(cookie)
    browser.add_cookie(cookie)

browser.add_cookie({'name': 'caLogin', 'value': 'true'})
# login_return_str = str(login_return)
login_return_str = json.dumps(login_return)
print(type(login_return_str))
print(login_return_str)
b = login_return_str.encode('utf-8')
print(b)
encode_str = base64.standard_b64encode(b)
print(encode_str)
print(encode_str.decode('utf-8'))
browser.add_cookie({'name': 'userInfo0', 'value': encode_str.decode('utf-8')})

script = "window.localStorage.setItem('zdShow','1')"
browser.execute_script(script)
script = "window.localStorage.setItem('dlrmc','罗礼斌')"
browser.execute_script(script)
script = "window.localStorage.setItem('dlbm','罗礼斌')"
browser.execute_script(script)
script = "window.localStorage.setItem('dwbm','520191')"
browser.execute_script(script)
time_ns = time.time_ns()
login_key = str(uuid.uuid4())
storage_dict = {"time": time_ns, "logout": 0, "collect": False, "exists": False, "pageTimeOut": False, "xxslNum": 0}
script = "var key = 'logout_'.concat(arguments[0]);" \
         "window.localStorage.setItem(key,JSON.stringify(arguments[1]))"
browser.execute_script(script, login_key, storage_dict)

# script = "var key = 'logout_'.concat(arguments[0]);" \
#          "window.sessionStorage.setItem('logout_key',key)"
# browser.execute_script(script, login_key)

# script = "return document.cookie"
# browser.execute_script(script)
# script = ""
# browser.execute_script(script, str(login_return))
time.sleep(1)
# browser.get('http://tyyw.gz.jcy/xtmh/rwgl/zbaj?91a220f4b7b274a59544cd1b7cddf7d9b66c15b896d63233b80d433dbea3e880fe9cf0b653c379e9b4fd500133f9560f77ee73c02e00d7fdcf')
# browser.get('http://143.176.22.54/xtmh/rwgl/ajjs?91a220f4b7b274a59544cd1b7cddf7d6bd6c15b896d63233b80d433dbea3e880fe9cf0b653c379e9b4fd500133f9560f77ee73c02e0334e84a')
# browser.get('http://143.176.22.54/xtmh/rwgl/ajjs?91a220f4b7b274a59544cd1b7cddf7d6bd6c15b896d63233b80d433dbea3e880fe9cf0b653c379e9b4fd500133f9560f77ee73c02e0553b58f')
# browser.get('http://143.176.22.54/zlpc/pcfk?       91a220f4b7b274a49544cd1b7cddf5dab86c15b896d63233b80d433dbea3e880fe9cf0b653c379e9b4fd500133f9560f77ee73c02e03834ad6')
# browser.get('http://143.3.214.54:3000/xiaoshu/zdsa?91a220f4b7b274a09744cd1b7cddf5deb96c15b896d63233b80d433dbea3e880fe9cf0b653c379e9b4fd500133f9560f77ee73c02ecd799358e6b7c89230b9808fb67a753c1a974c7947cc0989befa3d5f32a7ed64966ab68ca4298fd6bea1b2d401550e48')
browser.get("http://tyyw.gz.jcy/xtmh")
# script = "window.location.href = '/xtmh'"
# browser.execute_script(script)
print(browser.get_cookies())
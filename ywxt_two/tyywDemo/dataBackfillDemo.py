# coding utf-8

"""

    数据回填完整demo
"""

from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import json
import base64
import uuid
import time
import urllib.parse
import math
import random


def load_json(path):
    """
        加载指定json文件
    :param path: json文件路径
    :return: 加载后的对象，list或dict
    """
    f = open(path, 'r', encoding='utf-8')
    json_data = json.load(f)
    f.close()
    return json_data


form_mapping = load_json('config/formMapping.json')


def set_storage(browser, key, value):
    script = "window.localStorage.setItem(arguments[0],arguments[1])"
    browser.execute_script(script, key, value)


def read_text_as_list(path):
    """
        读取指定文本文件，按每行读取，每行为列表中的一个元素
    :param path: 文本文件路径
    :return: list
    """
    data = []
    f = open(path, 'r', encoding='utf-8')
    line = f.readline().strip('\n')
    while (line is not None) & (line != ''):
        data.append(line)
        line = f.readline().strip('\n')
    f.close()
    return data


def set_cookie(browser, cookies):
    """
        设置cookie信息
    :param browser: 浏览器对象
    :param cookies: cookie列表
    :return:
    """
    browser.delete_all_cookies()
    if cookies is None:
        return
    for cookie in cookies:
        print(type(cookie))
        cookie = eval(cookie)
        print(type(cookie))
        browser.add_cookie(cookie)


def change_login_info(login_info_dict):
    """
        将登录信息的json字符串转换为编码后的字符串
    :param: 登录信息dict
    :return: 编码后的字符串
    """
    login_info_str = json.dumps(login_info_dict)
    login_info_binary = login_info_str.encode('utf-8')
    login_info_base64 = base64.standard_b64encode(login_info_binary)
    return login_info_base64.decode('utf-8')


def KD(url_param):
    """
        对url后携带的参数进行编码
    :param url_param:
    :return:
    """
    if "" == url_param:
        return ""
    url = urllib.parse.quote(url_param)
    t = "ae8b516cbffde62a74b726c82eb6748ad41d251480d84ce2e96ebf57ebaa8b22"
    new_t = urllib.parse.quote(t)
    if None == new_t or (len(new_t) <= 0):
        return None
    n = ""
    for ch in new_t:
        n += str(ord(ch))

    o = math.floor(len(n) / 5)
    c = int(n[o] + n[2 * o] + n[3 * o] + n[4 * o] + n[5 * o])
    l = math.ceil(len(new_t) / 2)
    d = int(math.pow(2, 31) - 1)
    if c < 2:
        return None
    h = int(round(1e9 * random.random()) % 1e8)
    n += str(h)
    while len(n) > 10:
        n_before = n[0:10]
        n_after = n[10:len(n)]
        n = str(int(float(n_before)) + int(n_after[0: n_after.index('e') if "e" in n_after else len(n_after)]))
        if len(n) > 10:
            n = '{:.15e}'.format(int(n))
    n = (c * int(n) + l) % d
    m = ""
    for v in range(0, len(url)):
        f = int(ord(url[v]) ^ math.floor(n / d * 255))
        m += ('0' + (hex(f).replace('0x', ""))) if f < 16 else hex(f).replace('0x', '')
        n = (c * n + l) % d
    h = hex(h).replace("0x", "")
    while len(h) < 8:
        h = '0' + h
    m += h
    return m


def handle_url(url):
    """
        构造页面url访问规则
    :param url: 原访问url
    :return:
    """
    if 2 == len(url.split("?")):
        t = url.split("?")
        url = t[0] + "?" + KD(t[1])
    return url


def construct_url(url, gnbm, rybm, dwbm):
    return url + "?gnbm=" + gnbm + "&dwbm=" + dwbm + "&rybm=" + rybm


def switch_tag(browser, title):
    """
        切换浏览器标签页
    :param browser:
    :param title:
    :return:
    """

    handles = browser.window_handles
    for handle in handles:
        browser.switch_to.window(handle)
        if title == browser.title:
            break


def pick_case(browser, name):
    """
        根据指定案件名称筛选案件，并跳转进详情页
    :param name: 案件名称
    :return:
    """
    # 先对案件列表筛选
    time.sleep(1)
    case_page_div = browser.find_element_by_xpath('//div[@id="pane-zbaj"]')
    select_row_div = case_page_div.find_element_by_xpath('./div/div[1]')
    select_input = select_row_div.find_element_by_xpath('./div[4]/input')
    select_input.send_keys(name)
    select_button = select_row_div.find_element_by_xpath('./button')
    select_button.send_keys(Keys.ENTER)
    time.sleep(1)
    # 进入选中的案件
    case_spans = {}
    case_infos = browser.find_elements_by_xpath('//*[@id="zbaj_table"]/div/div[3]/table/tbody/tr')
    for case in case_infos:
        case_span = case.find_element_by_xpath('./td[2]/div/div/span')
        case_type = case.find_element_by_xpath('./td[3]/div/div').text
        case_spans[case_span] = case_type

    for case_span in case_spans.keys():
        print(case_span.text)
        if name == case_span.text:
            case_type = case_spans.get(case_span)
            time.sleep(1)
            case_span.click()
            time.sleep(1)
            switch_tag(browser, case_span.text + '-' + case_type)
            break


def pick_select(browser, key, values):
    selectEle = browser.find_element_by_xpath(
        '//*[@id="treeSelect_1571298041957_37429"]/div/span/div/div[2]/span/span/i')
    selectEle.click()
    selectEle.click()
    time.sleep(1)
    for value in values:
        span_ele = browser.find_element_by_xpath('//span[@title="' + value + '"]')
        span_ele = span_ele.find_element_by_xpath('./../label')
        print(span_ele.get_attribute('class'))
        time.sleep(1)
        span_ele.send_keys(Keys.SPACE)


def pick_radio(browser, key, value):
    """
        单选框选择
    :param browser:
    :param key: 要选择案件那个属性
    :param value: 单选框值
    :return:
    """
    label_eles = browser.find_elements_by_xpath("//*[contains(text(), '"
                                                + key.lower()
                                                + "')] | //*[@value='"
                                                + key.lower()
                                                + "']").pop().find_elements_by_xpath("./../../div/div/div/div/label")
    for labelEle in label_eles:
        radio = labelEle.find_element_by_xpath('./span[1]/input')
        if value == radio.get_attribute('value'):
            radio.send_keys(Keys.SPACE)


def input_textarea(browser, text, key):
    """
    文本框输入信息
    :param text:
    :return:
    """
    textarea = browser.find_elements_by_xpath('//textarea').pop(key)
    textarea.clear()
    textarea.send_keys(text)


def click_save(browser, xpath, quit):
    save_button = browser.find_element_by_xpath(xpath)
    save_button.send_keys(Keys.ENTER)
    if quit:
        time.sleep(3)
        browser.quit()


def click_handle_item(browser, value):
    """
    点击特定罪犯，对该罪犯信息进行编辑
    :param value:
    :return:
    """
    browser.find_element_by_xpath('//p[@title="' + value + '"]').find_element_by_xpath(
        './../../..').click()
    time.sleep(1)


def parse_table(browser, item_name):
    """
    解析罪犯信息中特定选项卡页的table信息
    :param item_name: 选项卡名称
    :return: 返回解析后的table信息
    """
    table_list = browser.find_element_by_xpath('//*[@id="pane-xyr"]/div/div/div/form/div/div[1]/div/div/div')
    tables = table_list.find_elements_by_xpath('./div')
    td_ele_dict = {}
    for divTable in tables:
        span_ele = divTable.find_element_by_xpath('./span')
        if item_name == span_ele.text:
            time.sleep(1)
            span_ele.find_element_by_xpath('./..').click()
            div_id = span_ele.find_element_by_xpath('./..').get_attribute('id')
            form_ele = browser.find_element_by_xpath('//div[@aria-labelledby="' + div_id + '"]')
            div_form_eles = form_ele.find_elements_by_xpath('./div/div')
            for divForm in div_form_eles:
                tr_eles = divForm.find_elements_by_xpath('./table/tbody/tr')
                for trEle in tr_eles:
                    td_eles = trEle.find_elements_by_xpath('./td')
                    for tdEle in td_eles:
                        try:
                            span_ele = tdEle.find_element_by_xpath('./div/label/span')
                        except:
                            pass
                        td_ele_dict[span_ele.text] = tdEle
    return td_ele_dict


def handle_span(browser, span_ele, key, value, repeat_handle_data):
    """
        针对table中的每个span，即每个输入项进行处理，判断类型，将值输入
    :param browser:
    :param span_ele: span项
    :param value: 待输入的值
    :param key: 待处理的数据项
    :param repeat_handle_data: 容器，存放需要重复处理的字段，解决其它字段约束第一次不能输入的问题
    :return:
    """
    div_eles = span_ele.find_elements_by_xpath('./div/div/div/div')
    if len(div_eles) > 1:
        repeat_handle_data.append(key)
        return
    aEle = span_ele.find_element_by_xpath('./div/div/div/div/div/*')
    if "input" == aEle.tag_name:
        print(aEle.get_attribute('type'))
        print(aEle.get_attribute('readonly'))
        if "true" != aEle.get_attribute('readonly'):
            aEle.clear()
            aEle.send_keys(value)
    elif "label" == aEle.tag_name:
        label_eles = aEle.find_elements_by_xpath('./../label')
        for label_ele in label_eles:
            radio = label_ele.find_element_by_xpath('./span[1]/input')
            if value == radio.get_attribute('value'):
                radio.send_keys(Keys.SPACE)
    elif "span" == aEle.tag_name:
        aEle.find_element_by_xpath('./div/div/span/span/i').click()
        time.sleep(1)
        div_id = aEle.find_element_by_xpath('./div').get_attribute('aria-describedby')
        tool_div = browser.find_element_by_xpath('//div[@id="' + div_id + '"]')
        tool_div.find_element_by_xpath('./div/input').send_keys(value)
        time.sleep(2)
        select_span = tool_div.find_element_by_xpath('//span[@title="' + value + '"]/..')
        time.sleep(1)
        select_span.click()
    elif "textarea" == aEle.tag_name:
        aEle.clear()
        aEle.send_keys(value)
    elif "div" == aEle.tag_name:
        div_eles = aEle.find_elements_by_xpath('./../div')
        year_div = div_eles[0].find_element_by_xpath('./input')
        month_div = div_eles[1].find_element_by_xpath('./input')
        day_div = div_eles[2].find_element_by_xpath('./input')
        year_div.clear()
        year_div.send_keys(split_date(value)[0])
        month_div.clear()
        month_div.send_keys(split_date(value)[1])
        day_div.clear()
        day_div.send_keys(split_date(value)[2])


def split_date(date):
    """
    将传入日期分割开，分成年、月、日三部分
    :param date: 日期
    :return: 元组 [年,月,日]
    """
    dates = date.split('-')
    return dates


def input_data(browser, data, td_ele_dict):
    """
    输入数据
    :param browser:
    :param data: 待输入数据
    :param td_ele_dict: 表单解析结果
    :return:
    """
    repeat_handle_data = []
    for key in td_ele_dict.keys():
        if key in form_mapping.keys():
            value_key = form_mapping[key]
            if value_key in data.keys():
                value = data[value_key]
            else:
                continue
        else:
            continue
        handle_span(browser, td_ele_dict[key], key, value, repeat_handle_data)
    if len(repeat_handle_data) > 0:
        for key in repeat_handle_data:
            handle_span(browser, td_ele_dict[key], key, data[key], repeat_handle_data)


def handle_base_case(browser, case):
    """
        处理基本信息
    :param case: 案件基本信息
    :return:
    """
    print(case)
    pick_select(browser, "审查阶段", case['reviewStage'])
    pick_radio(browser, "督办案件", case['superviseCase'])
    pick_radio(browser, "关注案件", case['focusCase'])
    pick_radio(browser, "专项活动", case['specialEvent'])
    pick_radio(browser, "交办案件", case['caseAssigned'])
    input_textarea(browser, case['summary'], 0)
    input_textarea(browser, case['note'], 1)
    click_save(browser, '//*[@id="pane-ak"]/div/div[2]/div[2]/div[1]/button[4]', False)


def handle_criminal_info(browser, criminal_info):
    """
        处理罪犯信息
    :param criminal_info: 罪犯信息
    :return:
    """
    print(criminal_info)
    td_ele_dict = parse_table(browser, "罪犯信息")
    input_data(browser, criminal_info['baseInfo'], td_ele_dict)
    td_ele_dict = parse_table(browser, "判决信息")
    input_data(browser, criminal_info['sentence'], td_ele_dict)
    click_save(browser, '//*[@id="pane-ak"]/div/div[2]/div[2]/div[1]/button[4]', True)


def start():
    # 读取文件信息
    configuration = load_json('config/config.json')
    login_info_dict = load_json('config/loginResult.json')
    user_info = login_info_dict['userInfo']
    urls = configuration['urls']
    cookies = read_text_as_list('config/generated_text_file.txt')
    case_info_dict = load_json('data/caseInfo.json')

    # 构造浏览器对象
    option = webdriver.ChromeOptions()
    option.binary_location = configuration['app_location']
    browser = webdriver.Chrome(configuration['webdriver'], options=option)

    # 访问网址
    browser.get(configuration['app_url'])

    # 设置cookie
    login_info_str = change_login_info(login_info_dict)
    set_cookie(browser, cookies)
    browser.add_cookie({'name': 'caLogin', 'value': 'true'})
    browser.add_cookie({'name': 'userInfo0', 'value': login_info_str})

    # 执行js脚本
    set_storage(browser, 'zdShow', '1')
    set_storage(browser, 'dlrmc', user_info['mc'])
    set_storage(browser, 'dlbm', user_info['dlbm'])
    set_storage(browser, 'dwbm', user_info['dwbm'])
    login_key = str(uuid.uuid4())
    timestamp = time.time_ns()
    # key = ''.join('logout_', login_key)
    key = 'logout_' + login_key
    value = json.dumps(
        {"time": timestamp, "logout": 0, "collect": False, "exists": False, "pageTimeOut": False, "xxslNum": 0})
    set_storage(browser, key, value)
    time.sleep(1)

    # 跳过登录,访问首页
    browser.get(configuration['index_url'])
    time.sleep(1)

    # 跳转案件列表页面
    case_list = urls['caseList']
    url = construct_url(case_list['url'], case_list['gnbm'], user_info['rybm'], user_info['dwbm'])
    url = handle_url(configuration['app_url'] + "/" + url)
    browser.get(url)
    time.sleep(1)

    # 选中指定案件进行处理
    pick_case(browser, case_info_dict['name'])
    handle_base_case(browser, case_info_dict['baseInfo'])
    time.sleep(2)
    criminal_info_list = case_info_dict['criminalInfo']
    for criminal_info in criminal_info_list:
        click_handle_item(browser, criminal_info['name'])
        handle_criminal_info(browser, criminal_info)


if __name__ == '__main__':
    start()

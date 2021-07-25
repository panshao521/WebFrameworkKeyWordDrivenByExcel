# -*- coding: utf-8 -*-
"""
Time:     2021/7/22 22:54
Author:   panyuangao@foxmail.com
File:     KeyWord.py
Describe: 
"""

from Conf.ProjVar import *
from Util.LocateElement import find_element, find_elements
from Util.ReadConfig import *
from selenium import webdriver
from selenium.common.exceptions import ElementNotVisibleException
import traceback

import time

driver = ""


def open_browser(browser_name):
    global driver
    if "chrome" in browser_name.lower():
        driver = webdriver.Chrome(executable_path=chrome_driver_path)
    elif "firefox" in browser_name.lower():
        driver = webdriver.Firefox(executable_path=firefox_driver_path)
    else:
        driver = webdriver.Safari()
    return driver


def visit(url):
    global driver
    driver.get(url)


def sleep(seconds):
    if isinstance(seconds, str):
        seconds = seconds.strip()
        try:
            time.sleep(float(seconds))
        except Exception as e:
            pass
            raise e
    else:
        time.sleep(seconds)


def switch_to(locate_method, locate_exp):
    global driver
    try:
        if locate_method.strip() not in ['id', 'xpath', 'name', "class_name", "link text", "partial link text",
                                         "tag_name"]:
            try:
                locate_info = read_ini_file_option(conf_file_path, locate_method, locate_exp)
                locate_method, locate_exp = locate_info.split(">")
            except Exception as e:
                print("读取配置文件的定位表达式信息出现异常", e)
                traceback.print_exc()
                raise e
        element = find_element(driver, locate_method, locate_exp)
        driver.switch_to.frame(element)
    except ElementNotVisibleException as e:
        print(locate_method, locate_exp, "没有找到页面元素")
        raise e
    except Exception as e:
        print(locate_method, locate_exp, "切换到frame出现异常")
        traceback.print_exc()
        raise e


def switch_out():
    global driver
    driver.switch_to.default_content()


def input(locate_method, locate_exp, input_value):
    global driver
    try:
        if locate_method.strip() not in ['id', 'xpath', 'name', "class_name", "link text", "partial link text",
                                         "tag_name"]:
            try:
                locate_info = read_ini_file_option(conf_file_path, locate_method, locate_exp)
                locate_method, locate_exp = locate_info.split(">")
            except Exception as e:
                print("读取配置文件的定位表达式信息出现异常", e)
                traceback.print_exc()
                raise e
        element = find_element(driver, locate_method, locate_exp)
        element.send_keys(input_value)
    except ElementNotVisibleException as e:
        print(locate_method, locate_exp, "没有找到页面元素")
        raise e
    except Exception as e:
        print(locate_method, locate_exp, "元素的输入操作出现异常")
        traceback.print_exc()
        raise e


def click(locate_method, locate_exp):
    global driver
    try:
        if locate_method.strip() not in ['id', 'xpath', 'name', "class_name", "link text", "partial link text",
                                         "tag_name"]:
            try:
                locate_info = read_ini_file_option(conf_file_path, locate_method, locate_exp)
                locate_method, locate_exp = locate_info.split(">")
            except Exception as e:
                print("读取配置文件的定位表达式信息出现异常", e)
                traceback.print_exc()
                raise e
        element = find_element(driver, locate_method, locate_exp)
        element.click()
    except ElementNotVisibleException as e:
        print(locate_method, locate_exp, "没有找到页面元素")
        raise e
    except Exception as e:
        print(locate_method, locate_exp, "元素的点击操作出现异常")
        traceback.print_exc()
        raise e

def clear(locate_method, locate_exp):
    global driver
    try:
        if locate_method.strip() not in ['id', 'xpath', 'name', "class_name", "link text", "partial link text",
                                         "tag_name"]:
            try:
                locate_info = read_ini_file_option(conf_file_path, locate_method, locate_exp)
                locate_method, locate_exp = locate_info.split(">")
            except Exception as e:
                print("读取配置文件的定位表达式信息出现异常", e)
                traceback.print_exc()
                raise e
        element = find_element(driver, locate_method, locate_exp)
        element.clear()
    except ElementNotVisibleException as e:
        print(locate_method, locate_exp, "没有找到页面元素")
        raise e
    except Exception as e:
        print(locate_method, locate_exp, "元素的清空操作出现异常")
        traceback.print_exc()
        raise e

def assert_word(keyword):
    global driver
    keyword = str(keyword)
    assert keyword in driver.page_source


def quit():
    global driver
    if (driver is not None) and (not isinstance(driver, str)):
        driver.quit()

"""
def login():
    visit("https://www.126.com")
    sleep(1)
    switch_to("xpath", "//iframe[contains(@id,'x-URS-iframe')]")
    input("xpath", '//input[@name="email"]', "testworker2020")
    input("xpath", '//input[@name="password"]', "Wy123456")
    click("id", "dologin")
    switch_out()
    sleep(3)
    assert_word("退出")
"""
def login(username,password):
    global driver
    driver = open_browser("chrome")
    visit("https://www.126.com")
    sleep(1)
    switch_to("126mail_indexPage", "indexPage.frame")
    clear("126mail_indexPage", 'indexPage.username')
    input("126mail_indexPage", 'indexPage.username', username)
    input("126mail_indexPage", 'indexPage.password', password)
    click("126mail_indexPage", "indexPage.loginbutton")
    switch_out()
    sleep(3)
    assert_word("退出")

def addContact(address_list): # 混合驱动：多组数据（数据驱动） + 测试过程（关键字驱动）
    global driver
    click("126mail_homePage", "homePage.addressLink")
    sleep(3)
    for address in address_list:
        click("126mail_contactPersonPage", "contactPersonPage.createButton")
        sleep(2)
        input("126mail_contactPersonPage", "contactPersonPage.name", address[0])
        input("126mail_contactPersonPage", "contactPersonPage.email", address[1])
        input("126mail_contactPersonPage", "contactPersonPage.phone", address[2])
        input("126mail_contactPersonPage", "contactPersonPage.otherinfo", address[3])
        click("126mail_contactPersonPage", "contactPersonPage.confirmButton")
        sleep(4)
        assert_word("张伟")
    quit()


if __name__ == "__main__":
    login_data_list = [
        ["testworker2020", "Wy123456"],
        ["youngboss2020", "Wy123456"]
    ]
    test_data_list = [
        ["张伟1","aa@126.com","13800000001","我是好人1号"],
        ["张伟2","bb@126.com","13800000002","我是好人2号"],
        ["张伟3","cc@126.com","13800000003","我是好人3号"]
    ]
    for login_data in login_data_list:
        login(login_data[0], login_data[1])
        addContact(test_data_list)





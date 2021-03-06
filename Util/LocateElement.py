# -*- coding: utf-8 -*-
"""
Time:     2021/7/21 21:34
Author:   panyuangao@foxmail.com
File:     LocateElement.py
Describe: 封装查找元素的方法
"""
import traceback

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait


# 传递driver，定位方式和定位表达式，来获取一个页面元素
def find_element(driver, locate_method, locate_exp):
    try:
        # 使用显示等待的方式定位元素，最大等待时间是10秒
        element = WebDriverWait(driver, 10).until(lambda x: x.find_element(locate_method, locate_exp))
    except TimeoutException as e:
        print("*******:", locate_method, locate_exp)
        # 捕获NoSuchElementException异常
        traceback.print_exc()
        raise e
    return element


# 传递driver，定位方式和定位表达式，来获取一个页面的多个元素，
def find_elements(driver, locate_method, locate_exp):
    try:
        elements = WebDriverWait(driver, 2).until(lambda x: x.find_elements(locate_method, locate_exp))
    except TimeoutException as e:
        # 捕获NoSuchElementException异常
        traceback.print_exc()
        raise e
    return elements


if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.get("https://www.sogou.com")
    print(find_element(driver, "id", "query"))
    print(find_elements(driver, "xpath", "//input"))

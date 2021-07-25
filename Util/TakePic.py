# -*- coding: utf-8 -*-
"""
Time:     2021/7/21 21:40
Author:   panyuangao@foxmail.com
File:     TakePic.py
Describe: 对浏览器当前页面截图，并存入项目的ScreenCapture目录下，文件以"时-分-秒.png"命名
"""
from Util.DirUtil import make_curdate_dir
from Util.DateStr import *
from Conf.ProjVar import pic_capture_dir

import os
from selenium import webdriver


def take_pic(driver):
    try:
        '''
        调用get_screenshot_as_file(filename)方法，对浏览器当前打开页面
        进行截图,并保存在项目的ScreenCapture目录下，文件以"时-分-秒.png"命名。
        '''
        file_path = make_curdate_dir(pic_capture_dir)
        pic_path = os.path.join(file_path, get_english_current_time() + ".png")
        print(pic_path)
        driver.get_screenshot_as_file(pic_path)
        return pic_path
    except IOError as e:
        print(e)


if __name__ == "__main__":
    driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
    driver.get("http://www.baidu.com")
    take_pic(driver)
    driver.quit()

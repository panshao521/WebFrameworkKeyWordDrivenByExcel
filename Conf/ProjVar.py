# -*- coding: utf-8 -*-
"""
Time:     2021/7/21 21:27
Author:   panyuangao@foxmail.com
File:     ProjVar.py
Describe: 项目常用变量，如各类项目路径及excel的列号
"""

import os
# print(__file__)
# print(os.path.abspath(__file__))
# print(os.path.dirname(os.path.abspath(__file__)))
# print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

#当前工程在硬盘上的绝对路径
proj_dir_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(proj_dir_path)

#配置文件的绝对路径
conf_file_path = os.path.join(proj_dir_path,"Conf","ElementsRepository.ini")
# print(conf_file_path)

#配置用什么浏览器跑case
browser_name = "chrome"

#浏览器驱动的位置
chrome_driver_path = "/usr/local/bin/chromedriver"
firefox_driver_path = "/usr/local/bin/geckodriver"

#测试数据文件的位置
test_data_file_path = os.path.join(proj_dir_path,"TestData","添加联系人测试用例.xlsx")

#截图目录
pic_capture_dir = os.path.join(proj_dir_path,"ScreenCapture")

#日志配置文件的目录
log_config_path = os.path.join(proj_dir_path,"Conf","Logger.conf")


if __name__ == '__main__':
    print(conf_file_path)
    print(log_config_path)

# -*- coding: utf-8 -*-
"""
Time:     2021/7/21 21:32
Author:   panyuangao@foxmail.com
File:     ReadConfig.py
Describe: 封装读取配置文件的方法
"""
import configparser


# 获取配置文件中的所有sections
def read_ini_file_all_sections(ini_file_path):
    cf = configparser.ConfigParser()
    cf.read(ini_file_path, encoding="utf-8-sig")
    return cf.sections()


# 获取sections下的所有选项（key:value的键值对）
def read_ini_file_section_all_options(ini_file_path, section_name):
    cf = configparser.ConfigParser()
    cf.read(ini_file_path, encoding="utf-8-sig")
    return cf.options(section_name)


# 读取某个section下的某个选项对应的value
def read_ini_file_option(ini_file_path, section_name, option_name):
    cf = configparser.ConfigParser()
    cf.read(ini_file_path, encoding="utf-8-sig")
    try:
        value = cf.get(section_name, option_name)
    except:
        print("the specific seciton or the specific option doesn't exit!")
        return None
    else:
        return value


if __name__ == '__main__':
    from Conf import ProjVar

    # file_path = r"D:\Software\pythonPlace\po_framework\Conf\ElementsRepository.ini"
    # print(read_ini_file_all_sections(file_path))
    # print(read_ini_file_section_all_options(file_path,"126mail_contactPersonPage"))
    print(read_ini_file_option(ProjVar.conf_file_path, "126mail_contactPersonPage", "contactpersonpage.createbutton"))

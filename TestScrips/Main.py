# -*- coding: utf-8 -*-
"""
Time:     2021/7/22 22:54
Author:   panyuangao@foxmail.com
File:     Main.py
Describe:
"""
from Util.Excel import *
from Util.TakePic import *
from Util.Log import *
from Action.KeyWord import *
import traceback


def get_all_test_data(wb, sheet_name):
    data = []
    if not isinstance(wb, ExcelUtil):
        print("没有传入正确的excel对象")
        return None

    if str(sheet_name) in wb.get_sheet_names():
        wb.set_sheet_by_name(sheet_name)
        data = wb.get_sheet_all_cell_values()
        return data
    else:
        print("测试数据sheet{}不存在".format(sheet_name))
        return None


def execute_test_case(test_data_file_path, sheet_name, head_line_flag=True):
    global driver
    global test_data_excel
    if not test_data_excel:
        test_data_excel = ExcelUtil(test_data_file_path)

    test_steps_data = get_all_test_data(test_data_excel, sheet_name)
    # print(test_steps_data)
    test_data_excel.set_sheet_by_name("测试结果")
    if head_line_flag:  # 避免重复写入表头
        test_data_excel.write_a_line_in_sheet(test_steps_data[0], fgcolor='FF9D6F')
        head_line_flag = False

    for line in test_steps_data[1:]:
        # print(line)
        key_word = line[2]
        locate_method = line[3]
        locate_exp = line[4]
        value = line[5]
        if locate_method and locate_exp:
            if value is None:
                command = "%s('%s', '%s')" % (key_word, locate_method, locate_exp)
            else:
                command = "%s('%s', '%s', '%s')" % (key_word, locate_method, locate_exp, value)
        if locate_method is None:
            if value is None:
                command = "%s()" % (key_word)
            else:
                command = "%s('%s')" % (key_word, value)
        info(command)
        test_result = True
        try:
            if key_word is None:  # 如果excel中关键字是空的时候，跳过该步骤
                continue
            elif "self_key_word" in key_word.lower() and value is not None and value in test_data_excel.get_sheet_names():
                print("----->> 执行sheet【%s】测试用例，用例路径：%s" %(value, test_data_file_path))
                test_result = execute_test_case(test_data_file_path, value, head_line_flag) # 递归调用execute_test_case()
            else:
                eval(command)
        except:
            line[8] = traceback.format_exc()
            line[9] = take_pic(driver)
            test_result = False
        if test_result:
            line[7] = "成功"
        else:
            line[7] = "失败"
        line[6] = get_english_current_datetime()
        test_data_excel.write_a_line_in_sheet(line)
        test_data_excel.save()
    return test_result


driver = open_browser("chrome")
test_data_excel = ""
execute_test_case(test_data_file_path, "登录+添加联系人")
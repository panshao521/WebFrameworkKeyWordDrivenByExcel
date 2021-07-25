# -*- coding: utf-8 -*-
"""
Time:     2021/7/21 21:38
Author:   panyuangao@foxmail.com
File:     DateStr.py
Describe: 获取日期字符串，用于创建文件夹
"""
import time

def get_chinese_current_date():
    year = time.localtime().tm_year
    #print(year)
    month = time.localtime().tm_mon
    #print(month)
    day = time.localtime().tm_mday
    #print(day)
    return "%s年%s月%s日" %(year,month,day)

def get_english_current_date():
    year = time.localtime().tm_year
    month = time.localtime().tm_mon
    day = time.localtime().tm_mday
    return "%s-%s-%s" %(year,month,day)

def get_chinese_current_time():
    hour = time.localtime().tm_hour
    min = time.localtime().tm_min
    sec = time.localtime().tm_sec
    return "%s时%s分%s秒" % (hour,min,sec)

def get_english_current_time():
    hour = time.localtime().tm_hour
    min = time.localtime().tm_min
    sec = time.localtime().tm_sec
    return "%s-%s-%s" % (hour,min,sec)

def get_chinese_datetime():
    return get_chinese_current_date()+get_chinese_current_time()

def get_english_datetime():
    return get_english_current_date()+" "+get_english_current_time()

def get_cur_hour(): #获取当前小时数
    return time.localtime().tm_hour

def get_chinese_current_datetime():
    return get_chinese_current_date() + " " + get_chinese_current_time()

def get_english_current_datetime():
    return get_english_current_date() + " " + get_english_current_time()


if __name__ == "__main__":
    print(get_chinese_current_date())
    print(get_english_current_date())
    print(get_chinese_current_time())
    print(get_english_current_time())
    print(get_chinese_current_datetime())
    print(get_english_current_datetime())

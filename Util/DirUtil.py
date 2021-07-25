# -*- coding: utf-8 -*-
"""
Time:     2021/7/21 21:38
Author:   panyuangao@foxmail.com
File:     DirUtil.py
Describe: 创建截图目录，第一级目录为当天日期，第二级目录为小时，一小时一个目录，便于查看。
"""
import os
from Util.DateStr import *

def make_curdate_dir(pic_dir_path):
    curdate = get_chinese_current_date()
    dir_path = os.path.join(pic_dir_path,curdate)
    print(dir_path)
    cur_hour = str(get_cur_hour())
    dir_path = os.path.join(dir_path,cur_hour)
    print(dir_path)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    return dir_path


if __name__ == "__main__":
    from Conf.ProjVar import pic_capture_dir
    make_curdate_dir(pic_capture_dir)
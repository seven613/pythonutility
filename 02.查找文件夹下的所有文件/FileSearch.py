#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件        :FileSearch.py
@说明        :文件夹下所有文件，返回一个列表
@时间        :2020/04/13 14:51:38
@作者        :张强
@版本        :1.0
'''
import os

def list_dir(text_list,dir_path):
    dir_files = os.listdir(dir_path)  # 得到该文件夹下所有的文件
    for file in dir_files:
        file_path = os.path.join(dir_path, file)  # 路径拼接成绝对路径
        if os.path.isfile(file_path):  # 如果是文件，就打印这个文件路径
            if file_path.endswith(".docx") or file_path.endswith(".doc") or file_path.endswith(".ppt") or file_path.endswith(".pptx") or file_path.endswith(".xls") or file_path.endswith(".xlsx"):
                text_list.append(file_path)
        if os.path.isdir(file_path):  # 如果目录，就递归子目录
            list_dir(text_list,file_path)
    return text_list



if __name__ == "__main__":
    all_txt = [] # 空列表，存储文件实际路径和名称以及扩展名
    path =r"E:\Codes\Python\test\tmp"# 文件夹路径
    list_dir(all_txt, path)
    print(all_txt)
    for file in all_txt:
        print(file)
    #print('文件总个数：'+ str(len(text_list)))
#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# 题目来源：https://www.liaoxuefeng.com/wiki/1016959663602400/1017623135437088#0
# 注意，isdir建议每次都使用绝对路径。 https://blog.csdn.net/weixin_42157432/article/details/104226403
import os

def digui_find(path: str, find_str: str):
    """os.path.isdir有大坑：改变path之后，os.listdir(path)函数返回的list是path下的文件，
    但os.path.isdir会以文件启动时的os.path.abspath(".")文件夹作为os.listdir(path)函数返回的文件名的文件夹
    即实际文件夹路径为 D:\python\learn\class\a_class ，但os.listdir(path) 函数判断时，使用D:\python\learn\a_class来判断。"""
    path = os.path.abspath(path)
    # print("当前路径(abspath)：" ,os.path.abspath("."),"当前实际路径(path):",path)
    all_file_and_dir = [os.path.join(path, x) for x in os.listdir(path)]
    found_file_all_path_l = [
        os.path.join(path, file)
        for file in all_file_and_dir
        if find_str in file and not os.path.isdir(file)
    ]
    # found_file_all_path_l = [os.path.join(path,file) for file in found_file_l]
    if found_file_all_path_l != []:
        print(f"{path}:")
        [print(f"    {file}") for file in found_file_all_path_l]
    all_dir = [
        os.path.join(path, a_dir) for a_dir in all_file_and_dir if os.path.isdir(a_dir)
    ]
    # print(all_dir)
    [digui_find(dir_path, find_str) for dir_path in all_dir]


digui_find(".", "enum")

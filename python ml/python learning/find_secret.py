# -*- coding: utf-8 -*-
import os
import string

def rename_files():
    # (1) get file names from folder
    file_list = os.listdir("E:\BaiduYunPan\MachineLearningJourney\python ml\python learning\prank")
    # print (file_path)
    save_path = os.getcwd()
    os.chdir("E:\BaiduYunPan\MachineLearningJourney\python ml\python learning\prank")
    # (2) changing the filename
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None, "0123456789"))
    os.chdir(save_path)

rename_files()
#!/usr/bin/python3
# coding=utf-8
import sys,os

path = "/tmp"
retval = os.getcwd()
# 查看当前的工作目录
print("当前的工作目录为：%s" % retval)
# 修改当前的工作目录
os.chdir(path)
# 查看修改后的工作目录
retval = os.getcwd()
print("目录修改成功：%s" % retval)

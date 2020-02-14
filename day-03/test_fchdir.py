#!/usr/bin/python3
# coding=utf-8

import sys,os
# 首先目录为：/etc/yum.repos.d
os.chdir('/etc/yum.repos.d/')
print("当前的工作目录为：%s" % os.getcwd())
fd = os.open('/tmp/',os.O_RDONLY)
# 通过文件描述符来改变工作目录
os.fchdir(fd)
print("当前的工作目录为：%s" % os.getcwd())
os.close(fd)

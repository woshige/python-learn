#!/usr/bin/python3
# coding=utf-8
import os,sys

# 切换到 /var/www/html目录
os.chdir("/var/www/html")
print("当前的工作目录为；%s" % os.getcwd())
# 打开 /tmp
fd = os.open("/tmp",os.O_RDONLY)
os.fchdir(fd)
# 打开当前的工作目录
print("当前的工作目录：%s" % os.getcwd())
os.close(fd)

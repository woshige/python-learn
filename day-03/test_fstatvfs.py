#!/usr/bin/python3
# coding=utf-8

import os,sys
# 打开文件
fd = os.open('/tmp/file',os.O_RDWR|os.O_CREAT)
# 获取文件所在的文件系统的详细信息
info = os.fstatvfs(fd)
print(info)
# 获取文件名的最大长度
print("文件名的最大长度为：%d" % info.f_namemax)
# 获取可用的块数
print("可用块数：%d" % info.f_bfree)
# 关闭文件
os.close(fd)

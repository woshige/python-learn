#!/usr/bin/python3
# coding=utf-8
import os,sys

fd = os.open('/tmp/foo.txt',os.O_RDWR|os.O_CREAT)
# 获取文件的元信息
info = os.fstat(fd)
print("文件信息：",info)
# 获取文件的uid
print("文件uid：%d" % info.st_uid)
# 获取文件gid
print("文件gid：%d" % info.st_gid)
# 关闭文件
os.close(fd)

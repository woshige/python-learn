#!/usr/bin/python3
# coding=utf-8
import os,sys

fd = os.open('/tmp/foo.txt',os.O_RDWR|os.O_CREAT)
print("%s" % os.pathconf_names)
# 获取最大的文件连接数
no = os.fpathconf(fd,'PC_LINK_MAX')
print("文件的最大连接数：%d" % no)
# 获取文件名的最大长度
no = os.fpathconf(fd,'PC_NAME_MAX')
print("文件名的最大长度为：%d" % no)
# 关闭文件
os.close(fd)
print("关闭文件成功")

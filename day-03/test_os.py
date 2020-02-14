#!/usr/bin/python3
# coding=utf-8

import os,sys

# 判断/tmp/yum.log的文件是不是存在
ret = os.access('/tmp/yum.log',os.F_OK)
print("F_OK的返回值为：%s" % ret)
# 判断是不是对/tmp/yum.log文件有读权限
ret = os.access('/tmp/yum.log',os.R_OK)
print("R_OK的返回值为：%s" % ret)
# 判断是不是对/tmp/yum.log文件有写权限
ret = os.access('/tmp/yum.log',os.W_OK)
print("W_OK的返回值为：%s" % ret)
# 判断是不是对/tmp/yum.log文件有执行权限
ret = os.access('/tmp/yum.log',os.X_OK)
print("X_OK的返回值为：%s" % ret)





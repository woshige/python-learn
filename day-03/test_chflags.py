#!/usr/bin/python3
# coding=utf-8
import os,stat

path = '/tmp/yum.log'
flags = stat.SF_NOUNLINK
retval = os.chflags(path,flags)
print("返回值为：%s" % retval)

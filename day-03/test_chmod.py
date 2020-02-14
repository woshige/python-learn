#!/usr/bin/python3
# coding=utf-8
import os,sys,stat

path='/tmp/yum.log'
os.chmod(path,stat.S_IXGRP)
#os.chmod(path,stat.S_IWOTH)
print("修改成功")

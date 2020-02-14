#!/usr/bin/python3
# coding=utf-8

import os,sys

# file   uid    gid
os.chown('/tmp/yum.log',1000,1000)
print("修改权限成功")

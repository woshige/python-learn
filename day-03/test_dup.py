#!/usr/bin/python3
# coding=utf-8
import os,sys

fd = os.open('/tmp/dup.log',os.O_RDWR|os.O_CREAT)
fd2 = os.dup(fd)
os.write(fd2,'hello is fd2'.encode())
os.closerange(fd,fd2)
print("关闭所有文件成功")


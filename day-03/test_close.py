#!/usr/bin/python3
# coding=utf-8
import os,sys

# 打开文件 按照读写的方式进行打开
fd = os.open('/tmp/test_for_close',os.O_RDWR|os.O_CREAT)
# 写入字符串
str = "this is a test"
str = str.encode()
os.write(fd,str)
print(fd)
os.close(fd)
print("关闭文件成功")

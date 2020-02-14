#!/usr/bin/python3
# coding=utf-8
import os

fd = os.open('/tmp/dup2.log',os.O_RDWR|os.O_CREAT)
os.write(fd,"写入字符串".encode("utf-8"))
os.fsync(fd)
# 从文件的首部开始计算pos
os.lseek(fd,1,0)
print(os.read(fd,100).decode("utf-8","ignore"))
os.close(fd)

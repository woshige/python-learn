#!/usr/bin/python3
# coding=utf-8

import os,sys

fd = os.open('/tmp/foo.txt',os.O_RDWR|os.O_CREAT)
fo = os.fdopen(fd,'w+')
# 打印当前的文件的position
print("current i/o pointer position:%d" % fo.tell())
fo.write("python is a great language.\n yeah its great!\n")
os.lseek(fd,0,0)
os.fsync(fd)
read_str = os.read(fd,100)
print("read string is :",read_str.decode("utf-8","ignore"))
# 打印当前的位置
print("current position is :%d" % fo.tell())
# 关闭文件
os.close(fd)

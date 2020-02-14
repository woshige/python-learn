#!/usr/bin/python3
# coding=utf-8
import os,sys

fd = os.open("/tmp/foo.txt",os.O_RDWR|os.O_CREAT)
# 写入字符串
os.write(fd,'this is test-This is test'.encode())
os.fsync(fd)
# 裁剪字符串，使得其不能超过文件的大小
os.ftruncate(fd,10)
os.lseek(fd,0,0)
read_str = os.read(fd,100)
print("读取的字符串为：",read_str.decode('utf-8','ignore'))
os.close(fd)
print("关闭文件成功")

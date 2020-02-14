#!/usr/bin/python3

import os, sys

# 打开文件
fd = os.open( "foo.txt", os.O_RDWR|os.O_CREAT )

# 写入字符串
os.write(fd, "This is test")

# 所有 fsync() 方法
os.fsync(fd)

# 从开始位置读取字符串
os.lseek(fd, 0, 0)
str = os.read(fd, 100)
print ("Read String is : ", str)

# 关闭文件
os.close( fd )

print ("关闭文件成功!!")

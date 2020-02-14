#!/usr/bin/python3

import os,sys

fd = os.open("/tmp/foo.txt",os.O_RDWR|os.O_CREAT)
# 写入文件
input_str = "this is runoob.com site"
os.write(fd,bytes(input_str,'UTF-8'))
ret = os.isatty(fd)
print("返回值为",ret)
os.close(fd)

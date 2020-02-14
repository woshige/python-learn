#!/usr/bin/python3
# coding=utf-8
import os

#打开了一个文件，并将其文件的描述符复制到标准输入，这样print()函数标准输出的内容就到了/tmp/dup2.log下面
file = open('/tmp/dup2.log','a')
os.dup2(file.fileno(),1)
file.close()
print('hello')
print('hello')

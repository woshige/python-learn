#!/usr/bin/python3
# coding=utf-8
import os

# 切换当前的工作目录
os.chdir('/var/www/html')
print("当前的工作目录为：%s" % os.getcwdu().decode('ascii','ignore')
# 修改目录
my_fd = os.open("/tmp",os.O_RDONLY)
os.fchdir(my_fd)
# 打印当前的目录
print("当前的工作的目录为：%s" % os.getcwdu())
# 关闭文件
os.close(my_fd)

#!/usr/bin/python
# coding=utf-8

# 改变文件的当前的位置  seek(x,0) 从起始位置开始移动x个字符   seek(x,1)表示当前位置往后移动x个字符
# seek(-x,2) 从尾部位置向前移动x个字符  打开方式中没有b的时候，只会相对于起始位置定位
f = open("tmp/file", 'wb+')
# b bytes  u/U unicode r/R 非转义字符串
f.write(b'0123456789abcdef')
# 从文件的首部开始移动  可以理解为类似光标
# 从光标最开始的位置向后移动5下
f.seek(5, 0)
# 移动光标一次
print(f.read(1))
# 移动光标一次
print(f.read(1))
# 从当前的光标开始移动2个
f.seek(2, 1)
print(f.read(1))
f.seek(-3, 2)
print(f.read(1))
# 关闭文件连接，并释放系统资源，如果再次调用，会抛出异常
f.close()
# 优雅的处理打开文件对象
with open('tmp/file') as f:
    read_data = f.read()
print(f.closed)
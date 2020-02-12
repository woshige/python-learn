#!/usr/bin/python
# coding=utf-8
import math

# rjust()函数返回一个原字符串右对齐，并使用空格符填充至width新字符串，如果指定的长度小于
# 字符串的长度，则返回原字符串 print()函数的end属性为每行的结束符号
for x in range(1, 11):
    print(repr(x).rjust(2), repr(x * x).rjust(3), end=' ')
    print(repr(x * x * x).rjust(4))
# 另一种输出平方立方表的方式  0 1 2 分别代表的是位置参数  2 2 4表示的是显示10进制的宽度
for x in range(1, 11):
    print('{0:2d} {1:2d} {2:4d}'.format(x, x * x, x * x * x))
# 在数字的左边填充数字
print("12".zfill(5))
print("-3.14".zfill(7))
print("{}网址为：{}".format('百度', 'www.baidu.com'))
print("{name}网址为：{site}".format(name='百度', site='www.baidu.com'))
print("{1},{0},{site}".format(10, 9, site='www.baidu.com'))
# 0 表示的是第0个值，10表示的是整数部分的宽度，3表示的是小数的精度
print('常量 PI的近似值为：{0:10.3f}'.format(math.pi))
table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
for name, number in table.items():
    print('{0:10} ===> {1:10d}'.format(name, number))
# input_str = input("请输入您的内容：")
# print("您输入的内容为：",input_str)
# 读和写文件
f = open("file", 'a')
f.write("hello 我喜欢Python\n")
f.close()
f = open("file", 'r')
# 从文件中读取单独的一行
print("从file中进行读取", f.readline())
print("---------")
print("从file中进行读取", f.readline())
f.close()
f = open("file", 'r')
content = f.readline()
f.close()
f1 = open("file2", 'a')
# 返回的是写入文件的字符数
num = f1.write(content)
print("所在的行数为：",num)
f.close()
# 将所有的行进行读取
f = open("file")
# 进行遍历，readlines()返回的是一个列表的内容
context = f.readlines()
# 返回的文件对象所处的位置，它是从文件开头开始算起的字节数
pos = f.tell()
print("文件对象所在的位置为：",pos)
print(context)
for c in context:
    print(c)
f.close()
# 也可以对一个文件对象迭代
print("利用对文件对象进行迭代")
f = open("file")
for i in f:
    print(i)
f.close()
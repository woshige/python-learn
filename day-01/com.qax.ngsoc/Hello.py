#!/usr/bin/python
# coding=utf-8
# 这里的coding指定为utf-8的原因是在python默认的编码为ASCII格式，所以打印中文会出错
# python3的环境为
print("hello")
print("你好世界")
counter = 100
miles = 1000.0
name = "john"
print(miles)
print(name)
print(counter)
# python 数字
var1 = 1
var2 = 10
var3 = 100
# 删除变量
del [var1]
print(var2)
del var3, var2
var4 = 3.4j
print(var4)
str = 'hello world'
print(str)
print(str[0])
print(str[2:5])  # 输出从第三个到第六个字符串
print(str[2:])  # 输出从第二个字符串到最尾部的字符串
print(str * 2)  # 输出字符串两次
print(str + "TEST")  # 字符串的拼接
list = ['linux', 'java', 'python', 'john', 'slc']
tinylist = ['123', '111']
list[0] = tinylist
print(list)
print(list[0])
print(list[1:3])
print(list[2:])
print(list * 2)
print(list + tinylist)
print(list[1:4:2])  # 下标为1到4按照步长为2进行访问
tuple = ('hello', list, tinylist)
print(tuple)
print(tuple)
tinydict = {'name': 'slc', 'age': '21'}
print(tinydict)
print(tinydict['name'])
print(tinydict['age'])
dick = {}
dick[0] = 'slc'
dick[2] = 'linux'
dick[3] = tinydict
print(dick)
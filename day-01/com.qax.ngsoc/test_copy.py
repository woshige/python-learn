#!/usr/bin/python
# coding=utf-8
import copy

# 字典的浅拷贝和深拷贝  拷贝：就是从另外的内存上开辟一个空间，复制一个数据结构
a = {1: [1, 2, 3, 4], 2: 10}
b = a
c = a.copy()
d = copy.deepcopy(a)
a[1].append(5)
a[2] = 5
print(a)  # {1: [1, 2, 3, 4, 5], 2: 5}
print(b)  # {1: [1, 2, 3, 4, 5], 2: 5} 因为a和b
print(c)  # {1: [1, 2, 3, 4, 5], 2: 10}  一级的对象进行了复制，但是二级的对象使用的还是引用
print(d)  # {1: [1, 2, 3, 4], 2: 10} 完完全全使用了深拷贝
myDict = {}
mySeq = ('google', 'runoob', 'taobal')
myDict = myDict.fromkeys(mySeq)
print(myDict)  # {'runoob': None, 'taobal': None, 'google': None}
myDict = myDict.fromkeys(mySeq, 10)
print(myDict)  # {'taobal': 10, 'runoob': 10, 'google': 10}
print(myDict.__contains__("slc"))

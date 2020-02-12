#!/usr/bin/python
# coding=utf-8


# 列表的访问
myList = ['physics', 'chemistry', 1997, 2000]
myList2 = [1, 2, 3, 4, 5, 6, 7]
print("myList[0]:", myList[0])
print("myList2[1:5]", myList2[1:5])
# 更新列表
myList.append("slc")
print(myList)
del myList[1]
print("after del myList[0]")
print(myList)
print(max(myList2))
# 查找对应元素的索引
print("'slc' 的索引为", myList.index('slc'))
# 指定的索引插入数值
print(myList.insert(0, "first"))
print(myList)
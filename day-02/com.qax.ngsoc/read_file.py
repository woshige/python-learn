#!/usr/bin/python
# coding=utf-8

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
# 改变文件的当前的位置  seek(x,0) 从起始位置开始移动x个字符   seek(x,1)表示当前位置往后移动x个字符
# seek(-x,2) 从尾部位置向前移动x个字符
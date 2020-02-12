#!/usr/bin/python
# coding=utf-8
nums = [12, 37, 5, 42, 8, 3]
even = []
odd = []
a = 1
while a < 10:
    print(a)
    a += 2
while len(nums) > 0:
    num = nums.pop()
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)
print("偶数集合为：" + str(even))
print("奇数集合为：" + str(odd))
# 非偶数的时候跳过
i = 1
while i < 10:
    i += 1
    if i % 2 != 0:
        continue
    else:
        print(i)
# 大于10跳出循环
i = 1
while 1:
    print(i)
    i += 1
    if i > 10:
        break
# while 和 else使用  当while执行完毕的之后执行else
num = 1
while num < 5:
    print(num, "is less than 5")
    num += 1
else:
    print(num, "is not less than 5")
# for循环  遍历字符串和列表
myList = ['banana', 'apple', 'mango']
myStr = 'Python'
for s in myStr:
    print("当前的字母为：" + str(s))

for e in myList:
    print("当前的元素为：" + e)
# 通过range函数产生的序列进行遍历
for index in range(len(myList)):
    print("使用序列进行遍历，当前的元素为：" + myList[index])
# 使用for循环来得到10到20之间的质数  for和else使用的时候，for循环跳出，执行else
for i in range(10, 20):
    for num in range(2, i):
        if i % num == 0:
            j = num / i
            print('%d 等于 %d * %d' % (i, num, j))
            break
    else:
        print("%d 是一个质数" % i)
# 使用enumerate函数进行遍历
for i, j in enumerate(myList):
    print("index: %s,items: %s" % (i, j))
# pass表示占位符  一般用来在def的函数中进行使用，如果定义了一个空的函数，程序会报错
for letter in 'Python':
    if letter == 'h':
        pass
        print("this is a pass block")
    print("当前的字母为",letter)

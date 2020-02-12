#!/usr/bin/python
# coding=utf-8

# 函数定义
def print_input_str(input_str):
    """ 打印传入的字符串到标准的显示设备上 """
    input_str = "input_str已经被修改"
    print(input_str)
    return


def chang_field(filed):
    filed.append([1, 2, 3, 4])
    print("函数内的值为：", filed)
    return


def my_function(parameter1, parameter2):
    print("输入的两个参数分别为：", parameter1, parameter2)
    return


def my_function3(parameter1, *parameters):
    print("输入的第一个参数为：", parameter1)
    for par in parameters:
        print(par)


def my_function2(parameter1=10):
    print("传入的参数值的值为：", parameter1)
    return


# 函数调用
print_input_str("我要调用用户自定义函数")
print_input_str("再次调用")
s = "slc"
# 当传入的是不可变的对象的时候，在函数之内进行修改不影响的
print_input_str(s)
print(s)

# 传入的值为可变的对象时
myList = [1, 2, 3, 4]
chang_field(myList)
print("传入之后的myList的值为：", myList)
my_function(parameter2='slc', parameter1='age')
my_function2()
my_function3(10, 20, 30)
age=10
res = lambda arg1, arg2: arg1 + arg2 + age
print("两数相加的结果为：", res(10,20))

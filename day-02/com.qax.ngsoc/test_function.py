#!/usr/bin/python
# -*-coding:utf-8-*-

# ����Ĳ���������
def my_function(num1: int, num2: int = 100) -> int:
    return num1 + num2


if __name__ == "__main__":
    print(my_function.__annotations__)
    print(my_function(10))

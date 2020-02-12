#!/usr/bin/python
# coding=utf-8
# 用来限制调用者执行方法的限制
"""
this is a doc about test_module.py
"""
def message(mes):
    """
    这是message方法
    :param mes:
    :return:
    """
    if __name__ == '__main__':
        print("我在执行自己的函数，我的密码是XXX")
        print('%s' % __name__)
    else:
        print("我在被别人调用")
        print("%s" % __name__)


message("message")

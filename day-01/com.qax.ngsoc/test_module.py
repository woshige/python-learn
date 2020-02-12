#!/usr/bin/python
# coding=utf-8
"""
this is a test_module.py doc
"""
import sys
import install_all
from util import ngsoc_util

print('命令行参数如下：')
for i in sys.argv:
    print(i)
print('\n\nPython的路径为：',sys.path,'\n')
install_all.install("/usr/bin")
ngsoc_util.message("import")
print(__name__)
ngsoc_util.message("path")
print("---------------")
print(dir(sys))
print(ngsoc_util.__doc__)
#!/usr/bin/python
# -*-coding:utf-8-*-
import pickle
import pprint

data1 = {'a': [1, 2.0, 3, 4 + 6j],
         'b': ('string', u'Unicode string'),
         'c': None}
selfref_list = [1, 2, 3]
selfref_list.append(selfref_list)
with open('data.pkl', 'wb') as output:
    # 使用协议0
    pickle.dump(data1, output)
    # 使用协议1
    pickle.dump(selfref_list, output, -1)
print(output.closed)
with open('data.pkl','rb') as file_input:
    data1 = pickle.load(file_input)
    pprint.pprint(data1)
    data2 = pickle.load(file_input)
    pprint.pprint(data2)
    print(file_input.isatty())
print(file_input.closed)
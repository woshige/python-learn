#!/usr/bin/python
# coding=utf-8
import calendar
import time

# 时间戳单位最适于做日期运算。但是1970年之前的日期就无法以此表示了。
# 太遥远的日期也不行，UNIX和Windows只支持到2038年。
ticks = time.time()
print("当前的时间戳为：", ticks)
local_time = time.localtime(time.time())
print(local_time)
print("本地时间为：", time.asctime(time.localtime(time.time())))
print(time.strftime("%Y-%m-%d  %H-%M-%S"), time.localtime(time.time()))
# 获取日历：theyear为年份  w 为 日期之间的宽度间距 l为行之间的间距 c 为每个月份之间的间隔
print(calendar.calendar(theyear=2020))
# 设置每周的第一天为6
calendar.setfirstweekday(6)
# 获取每周的第一天
print(calendar.firstweekday())
# 判断是不是闰年
print(calendar.isleap(2020))
# 获取某个月的日历
print(calendar.month(2020, 2))

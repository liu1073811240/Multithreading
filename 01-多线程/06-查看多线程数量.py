# -- coding: utf-8 --
# @Time : 2022/7/27 14:13
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : 06-查看多线程数量.py
# @Software: PyCharm

import threading
import time

print(threading.enumerate())

def task_l():
    for i in range(5):
        print('1111')
        time.sleep(1)

t = threading.Thread(target=task_l)
print(threading.enumerate())
t.start()  # 当调用start方法之后，才会真正创建一个新的子线程

print(threading.enumerate())
time.sleep(6)
print(threading.enumerate())
# while True:
#     print(threading.enumerate())

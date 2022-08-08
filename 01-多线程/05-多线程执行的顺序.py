# -- coding: utf-8 --
# @Time : 2022/7/27 13:59
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : 05-多线程执行的顺序.py
# @Software: PyCharm

import threading
from time import sleep

def test1():
    '''
    这是一个单独的任务
    :return:
    '''
    for i in range(10):
        print("任务1...%d" % i)
        sleep(0.1)

def test2():
    '''
    这是另外一个单独的任务
    :return:
    '''
    for i in range(5):
        print("任务2...%d" % i)
        sleep(0.2)

t1 = threading.Thread(target=test1)
t2 = threading.Thread(target=test2)

t1.start()
t2.start()


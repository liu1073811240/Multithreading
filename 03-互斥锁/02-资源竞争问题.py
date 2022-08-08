# -- coding: utf-8 --
# @Time : 2022/7/29 15:43
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : 02-资源竞争问题.py
# @Software: PyCharm


import threading
import time

# 1. 定义一个全局变量
g_num = 0


# 2. 定义2个函数，用它们来充当线程要执行的代码
def task1(num):
    global g_num
    for i in range(num):
        g_num += 1
    print("在task1中, g_num=%d" % g_num)


def task2(num):
    global g_num
    for i in range(num):
        g_num += 1
    print("在task1中, g_num=%d" % g_num)


# 3. 创建线程对象
t1 = threading.Thread(target=task1, args=(1000000, ))
t2 = threading.Thread(target=task2, args=(1000000, ))

# 4. 调用start创建线程，让线程开始运行。
t1.start()
t2.start()

'''

# 程序有时并行、有时串行。
# g_num +=1应该是一个整体的功能即一气呵成,但是操作系统在执行这个本应该一次
# 性全部执行的代码时。刚执行了一部分，反而去执行其他线程的代码，导致了这样的问题产生

'''

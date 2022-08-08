# -- coding: utf-8 --
# @Time : 2022/7/27 10:35
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : 03-多线程_thread.py
# @Software: PyCharm

'''
多个线程执行不同的代码

'''

# 1. 导入threading模块
import threading
import time

def task_l1():
    while True:
        print("111111")
        time.sleep(1)

def task_l2():
    while True:
        print("222222")
        time.sleep(0.2)

def task_l3():
    while True:
        print("333333")
        time.sleep(1)

# 2. 使用threading模块中的Thread创建一个对象
t1 = threading.Thread(target=task_l1)   # 子线程1
t2 = threading.Thread(target=task_l2)   # 子线程2
t3 = threading.Thread(target=task_l3)  # 子线程3


# 3. 调用这个实例对象的start方法让这个线程开始运行
t1.start()
t2.start()
t3.start()

while True:  # 主线程执行
    print("---主主主---")
    time.sleep(1)

# 操作系统来决定 主线程、子线程谁先执行打印。

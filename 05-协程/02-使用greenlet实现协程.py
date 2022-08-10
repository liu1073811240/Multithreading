# -- coding: utf-8 --
# @Time : 2022/8/10 10:00
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : 02-使用greenlet实现协程.py
# @Software: PyCharm

from greenlet import greenlet
import time


def test1():
    while True:
        print("---A---")
        gr2.switch()
        time.sleep(0.5)


def test2():
    while True:
        print("---B---")
        gr1.switch()
        time.sleep(0.5)


gr1 = greenlet(test1)
gr2 = greenlet(test2)

# 切换到gr1中运行
gr1.switch()
# gr2.switch()

# 协程与进程、协程的不同
# 1. 进程、线程创建完之后，到底是哪个进程、线程执行不确定 ，这让操作系统来进行计算（调度算法，例如优先级调度）
# 2. 协程是可以人为来控制的。



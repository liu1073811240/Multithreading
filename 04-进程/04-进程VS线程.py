# -- coding: utf-8 --
# @Time : 2022/8/1 16:13
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : 04-进程VS线程.py
# @Software: PyCharm

import multiprocessing
import time

num = 100

def task1():
    global num
    num = 200  # 要修改全局变量的值
    print("----in task1, num is %d " % num)


def task2():
    print("----in task2, num is %d" % num)


if __name__ == '__main__':
    p1 = multiprocessing.Process(target=task1)
    p2 = multiprocessing.Process(target=task2)

    # 先让p1标记的进程执行
    p1.start()

    # 让主进程延时1秒钟，保证在这个1秒钟内，p1标记的进程执行完毕代码。
    time.sleep(1)

    # 让p2标记的进程开始运行，看看获取的值是否是200
    p2.start()


'''
进程之间不共享全局变量
1. 当创建一个子进程的时候，会复制父进程的很多东西（全局变量等）
2. 子进程和主进程是单独的2个进程，不是一个。当一个进程结束的时候，不会对其它的进程产生影响。

线程之间共享全局变量。所有的线程都在一个进程汇总，这个进程是主进程。


'''



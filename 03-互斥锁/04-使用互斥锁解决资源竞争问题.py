# -- coding: utf-8 --
# @Time : 2022/8/1 11:31
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : 04-使用互斥锁解决资源竞争问题.py
# @Software: PyCharm


import threading
import time

# 5. 定义一个全局的变量，用来存储互斥锁
mutex = threading.Lock()


# 1. 定义一个全局变量
g_num = 0

# 2. 定义2个函数，用它们来充当线程要执行的代码
def task1(num):
    global g_num
    for i in range(num):
        # 上锁
        mutex.acquire()
        g_num += 1
        # 解锁
        mutex.release()
    print("在task1中, g_num=%d" % g_num)


def task2(num):
    global g_num
    for i in range(num):
        # 上锁
        mutex.acquire()
        g_num += 1
        # 解锁
        mutex.release()
    print("在task2中, g_num=%d" % g_num)


# 3. 创建线程对象
t1 = threading.Thread(target=task1, args=(1000000, ))
t2 = threading.Thread(target=task2, args=(1000000, ))

# 4. 调用start创建线程，让线程开始运行。
t1.start()
t2.start()

'''
注意点1： 当线程task1、task2执行的时候，双方要抢着给mutex这个互斥锁上锁。
        不管是哪个线程先抢到，都会保证一件事情：其它的线程会卡在上锁的那个位置。
    例如：task1先对mutex上锁，会导致在调用release解锁之前，task2线程会堵塞在mutex.acquire上锁的那个位置，一直到task1线程
        调用了mutex.release()释放锁。当task1调用了release释放锁之后，接下来task1和task2线程依然会抢着给mutex上锁，不确定
        会让哪个线程上锁，这是操作系统做的事情，这里程序不能控制。

注意点2：
    如果在task1与task2这两个线程都抢着上锁的时候，恰巧task1线程抢到了999999次，当下一次的时候task2抢到了500000次，在下一次的时候
    task1抢到了，此时task1总共执行的100万次已经完成，而此时打印出来的g_num的值是150万，而不是100万。

'''


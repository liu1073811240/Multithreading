# -- coding: utf-8 --
# @Time : 2022/8/8 9:42
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : 08-进程池通信-Queue.py
# @Software: PyCharm

# 修改import中的Queue为Manager
from multiprocessing import Manager, Pool
import os, time, random


def reader(q):
    print("reader启动(%s), 父进程为(%s)" % (os.getpid(), os.getppid()))
    for i in range(q.qsize()):
        print("reader从Queue获取到消息：%s" % q.get(True))


def writer(q):
    print("writer启动(%s), 父进程为(%s)" % (os.getpid(), os.getppid()))
    for i in "itcast":
        q.put(i)


if __name__ == '__main__':
    print("(%s) start" % os.getpid())

    q = Manager().Queue()  # 使用Manager中的Queue
    po = Pool()
    po.apply_async(writer, (q, ))

    time.sleep(1)  # 先让上面的任务向Queue存入数据，然后再让下面的 任务开始从中获取数据。

    po.apply_async(reader, (q, ))
    po.close()
    po.join()
    print("(%s) End" % os.getpid())

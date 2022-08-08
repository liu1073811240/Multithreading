# -- coding: utf-8 --
# @Time : 2022/8/5 9:42
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : 07-使用进程池.py
# @Software: PyCharm

from multiprocessing import Pool
import os
import random
import time


def work(num):
    for i in range(5):
        print('===pid=%d==num%d' % (os.getpid(), num))
        time.sleep(1)


if __name__ == '__main__':

    # 3表示进程池中最多有三个进程一起执行
    pool = Pool(3)

    for i in range(10):
        print('----%d----' % i)
        #  向进程中添加 任务
        # 注意： 如果添加的任务数量超过了进程池中进程的个数的话，那么就不会接着往进程池中添加，
        # 如果还没有执行的话，他就会等待前面的进程结束，然后再往进程池中添加新进程。
        pool.apply_async(work, (i, ))

    pool.close()  # 关闭进程池
    pool.join()  # 主进程在这里等待，只有子进程全部结束之后，才会开启主线程。


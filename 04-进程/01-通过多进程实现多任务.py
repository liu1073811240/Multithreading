# -- coding: utf-8 --
# @Time : 2022/8/1 15:00
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : 01-通过多进程实现多任务.py
# @Software: PyCharm

# 1. 导入模块
import multiprocessing
import time

# 2. 定义一个函数，表示要执行的代码。
def task1():
    while True:
        print("我是子进程...")
        time.sleep(1)

if __name__ == '__main__':

    # 3. 创建一个进程对象
    p = multiprocessing.Process(target=task1)

    # 4. 调用它的start方法才会真正的创建进程
    p.start()

    # 5. 主进程继续向下运行
    while True:
        print("我是主进程...")
        time.sleep(1)


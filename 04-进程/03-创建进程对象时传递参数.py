# -- coding: utf-8 --
# @Time : 2022/8/1 15:50
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : 03-创建进程对象时传递参数.py
# @Software: PyCharm

import multiprocessing

def task(name, age, **kwargs):
    print("name", name)
    print("age", age)
    print(kwargs)


if __name__ == '__main__':
    # 线程共享全局变量，进程不共享全局变量。

    p = multiprocessing.Process(target=task, args=("xiaohong", 18), kwargs={"mm": 10})
    p.start()


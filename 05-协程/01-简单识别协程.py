# -- coding: utf-8 --
# @Time : 2022/8/9 11:34
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : 01-简单识别协程.py
# @Software: PyCharm

import time

def work1():
    while True:
        print("--work1--")
        yield
        time.sleep(2)

def work2():
    while True:
        print("--work2--")
        yield
        time.sleep(3)

def main():
    w1 = work1()
    w2 = work2()
    while True:
        next(w1)
        next(w2)


if __name__ == '__main__':
    main()

# 通过协程能够实现多任务，但是它的这种方案一定是假的多任务。
# 又因为只要运行时切换任务足够快，用户看不出区别，所以表面上这就是多任务。


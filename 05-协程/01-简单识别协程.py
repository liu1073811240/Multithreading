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
        time.sleep(0.5)

def work2():
    while True:
        print("--work2--")
        yield
        time.sleep(0.5)

def main():
    w1 = work1()
    w2 = work2()
    print('******')
    while True:
        next(w1)
        next(w2)

if __name__ == '__main__':
    main()


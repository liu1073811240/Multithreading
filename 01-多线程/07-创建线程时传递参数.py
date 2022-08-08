# -- coding: utf-8 --
# @Time : 2022/7/27 14:31
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : 07-创建线程时传递参数.py
# @Software: PyCharm
import threading
import time


def print_lines(num):
    for i in range(num):
        print("1111")
        time.sleep(0.1)

def print_lines2(num1, num2):
    for i in range(num1):
        print('222')

        time.sleep(0.1)

    for i in range(num2):
        print('3333')
        time.sleep(0.1)


def work2(num1, num2, num3, n):
    print("----in work1--num1=%d, num2=%d, num3=%d, n=%d ---" % (num1, num2, num3, n))


t1 = threading.Thread(target=print_lines, args=(5,))
t2 = threading.Thread(target=print_lines2, args=(3, 4))
t3 = threading.Thread(target=work2, args=(11, 22, 33), kwargs={"n": 44})

t1.start()
t2.start()
t3.start()

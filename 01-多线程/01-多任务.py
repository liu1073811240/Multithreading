# -- coding: utf-8 --
# @Time : 2022/7/27 9:11
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : 01-多任务.py
# @Software: PyCharm

from time import sleep
import threading

def sing():
    for i in range(3):
        print("正在唱歌...%d" % i)
        sleep(1)


def dance():
    for i in range(3):
        print("正在跳舞...%d" % i)
        sleep(1)


if __name__ == '__main__':

    # 多线程程序
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)
    t1.start()
    t2.start()

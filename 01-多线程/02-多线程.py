# -- coding: utf-8 --
# @Time : 2022/7/27 10:31
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : 02-多线程.py
# @Software: PyCharm

import threading
import time


def say_sorry():
    print("亲爱的，我错了，我能吃饭了吗？")
    time.sleep(1)


for i in range(5):
    t = threading.Thread(target=say_sorry)
    t.start()  # 启动线程， 即让线程开始执行

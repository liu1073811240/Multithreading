# -- coding: utf-8 --
# @Time : 2022/7/27 16:39
# @Author : Liu Hui
# @Email : 1073811240@qq.com
# @File : 08-自定义类创建线程.py
# @Software: PyCharm

import threading
import time

class Task(threading.Thread):
    def run(self):
        while True:
            print(self.name)
            print("1111")
            time.sleep(1)

t = Task()
t.start()

while True:
    print("main")
    time.sleep(1)
